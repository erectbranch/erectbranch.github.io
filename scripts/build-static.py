#!/usr/bin/env python3
"""Generate static HTML mirror of docsify notes for SEO indexing.

Scans docs/notes/*/_sidebar.md, resolves each linked route to either an
external GitHub raw URL or a local markdown file, renders to HTML, and
writes docs/<clean_path>/index.html for each. Also regenerates
docs/sitemap.xml listing every produced URL plus the homepage.

The generated HTML is a flat content view (no docsify chrome) with
- <link rel="canonical"> pointing to the static URL (the indexable one)
- a small JS redirect that bounces human visitors to the docsify SPA hash URL
- robots/og tags for SEO

Bots see the full content and index it under the static URL. Humans get
redirected to the interactive SPA experience automatically.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from xml.sax.saxutils import escape as xml_escape

import markdown
import requests
import yaml
from latex2mathml.converter import convert as latex2mathml_convert

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
CONFIG_PATH = Path(__file__).resolve().parent / "static-mirror.yaml"
POSTS_JSON_PATH = DOCS_DIR / "metadata" / "posts.json"

MD_LINK_RE = re.compile(
    r'(?<!!)\[([^\]]+)\]\(([^)#\s]+)(?:\s+"[^"]*")?\)'
)
HTML_FIRST_P_RE = re.compile(r"<p[^>]*>(.*?)</p>", re.S)
HTML_TAGS_RE = re.compile(r"<[^>]+>")

SESSION = requests.Session()
SESSION.headers["User-Agent"] = "docsify-static-mirror/1.0 (+https://erectbranch.github.io)"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def load_posts_lookup() -> dict:
    """Build clean_path → posts.json entry lookup.

    SPA-side metadata (docs/metadata/posts.json) drives the dashboard cards
    and per-page title block. Reusing the same source here keeps SEO and SPA
    metadata in lockstep (same image, tags, date).
    """
    if not POSTS_JSON_PATH.is_file():
        return {}
    try:
        data = json.loads(POSTS_JSON_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    lookup = {}
    for entry in data:
        href = entry.get("href", "")
        if href.startswith("#/"):
            lookup[href[2:].rstrip("/")] = entry
    return lookup


INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
BLOCK_MATH_RE = re.compile(r"\$\$([^$]+?)\$\$", re.S)
INLINE_MATH_RE = re.compile(r"(?<!\$)\$([^$\n]+?)\$(?!\$)")


def _latex_to_mathml(latex: str, *, display: str) -> str:
    """Convert a LaTeX expression to MathML.

    Falls back to escaped <code> on conversion failure so unsupported syntax
    stays readable rather than crashing the build. docsify-katex renders the
    same content in the SPA, so users still see proper math in the live app.
    """
    try:
        return latex2mathml_convert(latex.strip(), display=display)
    except Exception:
        return f"<code>{xml_escape(latex.strip())}</code>"


def render_math_in_markdown(md: str) -> str:
    """Replace $...$ and $$...$$ LaTeX with semantic MathML, skipping code blocks.

    Bots index MathML as structured math; raw `$\\sum$` characters would
    otherwise leak into the body text and pollute topic classification.
    """
    fence_parts = re.split(r"(```[\s\S]*?```)", md)
    out_pieces = []
    for piece in fence_parts:
        if piece.startswith("```"):
            out_pieces.append(piece)
            continue
        # Within non-fenced text, also protect single-backtick inline code.
        inline_parts = INLINE_CODE_RE.split(piece)
        inline_codes = INLINE_CODE_RE.findall(piece)
        rebuilt = []
        for i, txt in enumerate(inline_parts):
            txt = BLOCK_MATH_RE.sub(
                lambda m: _latex_to_mathml(m.group(1), display="block"), txt
            )
            txt = INLINE_MATH_RE.sub(
                lambda m: _latex_to_mathml(m.group(1), display="inline"), txt
            )
            rebuilt.append(txt)
            if i < len(inline_codes):
                rebuilt.append(inline_codes[i])
        out_pieces.append("".join(rebuilt))
    return "".join(out_pieces)


LECTURE_PATTERNS = [
    (re.compile(r"^lec(\d+)$", re.I), lambda m: f"Lec {int(m.group(1)):02d}"),
    (re.compile(r"^ch(\d+)$", re.I), lambda m: f"Ch {int(m.group(1)):02d}"),
    (re.compile(r"^section(\d+)$", re.I), lambda m: f"Sec {int(m.group(1)):02d}"),
    (re.compile(r"^summary(\d+)$", re.I), lambda m: f"Pt {int(m.group(1)):02d}"),
    (re.compile(r"^(\d{4})$"), lambda m: m.group(0)),  # academic year
    (re.compile(r"^(\d+)_.+$"), lambda m: f"#{int(m.group(1)):02d}"),  # enroot-style "01_UBAI"
]


def extract_lecture_label(clean_path: str) -> str:
    """Compose a short, human-readable lecture/chapter marker from URL segments.

    Walks the segments after `notes/` and applies pattern table. Unmatched
    segments are skipped silently. Returns empty string when no markers found
    (e.g., course landing page).
    """
    parts = clean_path.split("/")
    try:
        idx = parts.index("notes")
    except ValueError:
        return ""
    labels = []
    for seg in parts[idx + 1:]:
        for pattern, formatter in LECTURE_PATTERNS:
            m = pattern.match(seg)
            if m:
                labels.append(formatter(m))
                break
    return " ".join(labels)


def build_seo_title(headline: str, clean_path: str, course_shorts: dict,
                    site_name: str) -> str:
    """Compose `<title>` text: `{headline} · {course_short} {lecture} — {site}`.

    Falls back gracefully when course_shorts misses an entry or no lecture
    pattern matches.
    """
    parts = clean_path.split("/")
    if parts[0] == "notes" and len(parts) >= 2:
        repo_key = parts[1]
    else:
        repo_key = parts[0]
    course_short = course_shorts.get(repo_key, "")
    lecture_label = extract_lecture_label(clean_path)

    suffix_parts = []
    if course_short and lecture_label:
        suffix_parts.append(f"{course_short} {lecture_label}")
    elif lecture_label:
        suffix_parts.append(lecture_label)
    elif course_short:
        suffix_parts.append(course_short)

    if suffix_parts:
        body = f"{headline} · {' · '.join(suffix_parts)}"
    else:
        body = headline
    return f"{body} — {site_name}"


def normalize_pub_date(raw: str) -> str:
    """Convert posts.json 'YYYY.MM.DD' → ISO 'YYYY-MM-DD' (schema.org datePublished)."""
    if not raw:
        return ""
    m = re.match(r"(\d{4})[.\-/](\d{1,2})[.\-/](\d{1,2})", raw.strip())
    if not m:
        return ""
    y, mo, d = m.groups()
    return f"{y}-{int(mo):02d}-{int(d):02d}"


def build_breadcrumbs(clean_path: str, headline: str, course_names: dict, base_url: str):
    """Return list of (name, url) for BreadcrumbList JSON-LD."""
    crumbs = [("Branch Log", f"{base_url}/")]
    parts = clean_path.split("/")
    if parts[0] == "notes" and len(parts) >= 2:
        repo_key = parts[1]
        course_path = f"/notes/{repo_key}/"
    else:
        repo_key = parts[0]
        course_path = f"/{repo_key}/notes/"
    course_name = course_names.get(repo_key, repo_key)
    course_url = f"{base_url}{course_path}"
    page_url = f"{base_url}/{clean_path}/"
    # Skip intermediate crumb when we're already on the course landing page.
    if course_url.rstrip("/") != page_url.rstrip("/"):
        crumbs.append((course_name, course_url))
    crumbs.append((headline, page_url))
    return crumbs


def build_json_ld(*, headline, description, canonical, image, pub_date,
                  tags, breadcrumbs, site, lang):
    blog = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": headline,
        "url": canonical,
        "mainEntityOfPage": canonical,
        "inLanguage": "ko-KR" if lang == "ko" else "en",
        "author": {
            "@type": "Person",
            "name": site["author"],
            "url": site["author_url"],
        },
        "publisher": {
            "@type": "Organization",
            "name": site["name"],
            "url": canonical.split("/", 3)[0] + "//" + canonical.split("/")[2] + "/",
        },
    }
    if description:
        blog["description"] = description
    if image:
        blog["image"] = image
    if pub_date:
        blog["datePublished"] = pub_date
        blog["dateModified"] = pub_date
    if tags:
        blog["keywords"] = ", ".join(tags) if isinstance(tags, list) else str(tags)

    crumb_list = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(breadcrumbs)
        ],
    }
    return (
        json.dumps(blog, ensure_ascii=False, indent=2),
        json.dumps(crumb_list, ensure_ascii=False, indent=2),
    )


def discover_sidebars(skip: set[str]) -> list[Path]:
    return sorted(
        p for p in (DOCS_DIR / "notes").glob("*/_sidebar.md")
        if p.parent.name not in skip
    )


def parse_sidebar_routes(sidebar: Path, skip_kw: list[str]):
    text = sidebar.read_text(encoding="utf-8")
    for label, target in MD_LINK_RE.findall(text):
        t = target.strip()
        if (
            t in ("dashboard", "dashboard.md", "tags.md", "wip.md")
            or t.endswith("_sidebar.md")
            or t.endswith("nav.md")
            or t.startswith(("http://", "https://", "#", "mailto:"))
        ):
            continue
        lab = label.strip()
        if any(k.lower() in lab.lower() for k in skip_kw):
            continue
        yield lab, t


def normalize_route(target: str):
    """Return (clean_path, source_kind, source_arg).

    clean_path: route path under docs/, no leading or trailing slash
                (e.g., "MIT-Efficient-AI/notes/2022/lec03")
    source_kind: "external" or "local"
    source_arg: external → (repo, sub_path); local → Path
    """
    t = target.rstrip("/")
    if t.endswith("/README.md"):
        t = t[: -len("/README.md")]
    elif t.endswith("/README"):
        t = t[: -len("/README")]
    elif t.endswith(".md"):
        t = t[:-3]

    parts = t.split("/")
    if not parts or not parts[0]:
        return None, None, None

    if parts[0] == "notes":
        return t, "local", DOCS_DIR / Path(*parts)

    # External: alias docsify rewrites `<repo>/notes/<rest>` → raw github URL.
    if len(parts) >= 2 and parts[1] == "notes":
        repo, rest = parts[0], parts[2:]
    else:
        repo, rest = parts[0], parts[1:]
    sub = "/".join(rest)
    return t, "external", (repo, sub)


def fetch_external(repo: str, sub: str, conf):
    user = conf["github_user"]
    branch = conf["default_branch"]
    if sub:
        url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{sub}/README.md"
        base = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{sub}/"
    else:
        url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/README.md"
        base = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/"
    try:
        r = SESSION.get(url, timeout=20)
    except requests.RequestException as e:
        return None, None, f"network: {e}"
    if r.status_code != 200:
        return None, None, f"HTTP {r.status_code}"
    return r.text, base, None


def read_local(local: Path):
    # Sidebar links may resolve to either <path>.md or <path>/README.md
    candidates = [local.with_suffix(".md"), local / "README.md"]
    for candidate in candidates:
        if candidate.is_file():
            base = "/" + str(candidate.parent.relative_to(DOCS_DIR)).replace("\\", "/") + "/"
            return candidate.read_text(encoding="utf-8"), base, None
    return None, None, f"not found: {local}"


def rewrite_relative_assets(md: str, base: str) -> str:
    """Rewrite relative image/link targets to absolute URLs so SEO snippets aren't broken."""

    def absolutize(p: str) -> str:
        if p.startswith(("http://", "https://", "/", "#", "data:", "mailto:")):
            return p
        return urljoin(base, p)

    md = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)([^)]*)\)",
        lambda m: f"![{m.group(1)}]({absolutize(m.group(2))}{m.group(3)})",
        md,
    )
    md = re.sub(
        r'src="([^"]+)"',
        lambda m: f'src="{absolutize(m.group(1))}"',
        md,
    )
    return md


def extract_title_desc(html: str, fallback_label: str):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    title = HTML_TAGS_RE.sub("", h1.group(1)).strip() if h1 else fallback_label

    desc = ""
    for m in HTML_FIRST_P_RE.finditer(html):
        candidate = HTML_TAGS_RE.sub("", m.group(1)).strip()
        if candidate:
            desc = re.sub(r"\s+", " ", candidate)[:160]
            break
    return title, desc


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Branch Log</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:title" content="{title} — Branch Log">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Branch Log">
{og_image_tag}
<script type="application/ld+json">
{json_ld_blog}
</script>
<script type="application/ld+json">
{json_ld_breadcrumb}
</script>
<style>
  body{{font-family:-apple-system,BlinkMacSystemFont,'Source Sans Pro',sans-serif;max-width:780px;margin:2rem auto;padding:0 1rem;line-height:1.6;color:#222;visibility:hidden}}
  article img{{max-width:100%;height:auto}}
  pre{{overflow:auto;background:#f6f8fa;padding:.75rem;border-radius:4px}}
  code{{font-size:.9em}}
  a{{color:#0374B5}}
  .static-banner{{background:#f6f8fa;border:1px solid #d0d7de;padding:.5rem .75rem;border-radius:4px;font-size:.9em;margin-bottom:1.5rem}}
</style>
<script>
  // Redirect human visitors to the docsify SPA. Bots will index the rendered content above.
  (function(){{
    if (location.hash) return;
    location.replace({spa_url_json});
  }})();
</script>
<noscript><style>body{{visibility:visible}}</style></noscript>
</head>
<body>
<div class="static-banner">
  <a href="/">Branch Log</a> · <a href="{spa_url}">Open in interactive viewer →</a>
</div>
<article>
{content}
</article>
</body>
</html>
"""


def render_html_page(label, target, conf, md_engine, posts_lookup, course_names):
    clean_path, kind, arg = normalize_route(target)
    if clean_path is None:
        return None, f"unparseable target: {target}"

    if kind == "external":
        repo, sub = arg
        md_text, base, err = fetch_external(repo, sub, conf)
    else:
        md_text, base, err = read_local(arg)
    if err:
        return clean_path, err

    md_text = rewrite_relative_assets(md_text, base)
    # docsify-katex compatibility: ```math fences → $$ $$
    md_text = re.sub(r"```math([\s\S]*?)```", r"$$\1$$", md_text)
    # Convert LaTeX math to MathML so bots index semantic structure instead
    # of seeing raw `$\sum$` noise. docsify-katex still handles SPA rendering.
    md_text = render_math_in_markdown(md_text)

    md_engine.reset()
    html = md_engine.convert(md_text)
    h1_title, description = extract_title_desc(html, label)

    # SPA-side metadata (posts.json) takes precedence — keeps SEO in sync with dashboard.
    post = posts_lookup.get(clean_path, {})
    headline = post.get("title") or h1_title
    image = post.get("image") or ""
    tags = post.get("tag") or []
    pub_date = normalize_pub_date(post.get("time") or "")

    base_url = conf["base_url"].rstrip("/")
    spa_url = f"/#/{clean_path}"
    canonical = f"{base_url}/{clean_path}/"
    lang = "ko" if re.search(r"[ㄱ-힝]", headline + " " + description) else "en"

    breadcrumbs = build_breadcrumbs(clean_path, headline, course_names, base_url)
    json_ld_blog, json_ld_crumb = build_json_ld(
        headline=headline,
        description=description,
        canonical=canonical,
        image=image,
        pub_date=pub_date,
        tags=tags,
        breadcrumbs=breadcrumbs,
        site=conf["site"],
        lang=lang,
    )

    og_image_tag = (
        f'<meta property="og:image" content="{xml_escape(image)}">' if image else ""
    )

    page = PAGE_TEMPLATE.format(
        lang=lang,
        title=xml_escape(headline),
        description=xml_escape(description),
        canonical=xml_escape(canonical),
        spa_url=xml_escape(spa_url),
        spa_url_json=json.dumps(spa_url),
        og_image_tag=og_image_tag,
        json_ld_blog=json_ld_blog,
        json_ld_breadcrumb=json_ld_crumb,
        content=html,
    )

    out_path = DOCS_DIR / clean_path / "index.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page, encoding="utf-8")
    return clean_path, None


def emit_sitemap(clean_paths: list[str], conf):
    lastmod = conf.get("lastmod") or datetime.now(timezone.utc).date().isoformat()
    base = conf["base_url"].rstrip("/")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        "  <url>",
        f"    <loc>{base}/</loc>",
        f"    <lastmod>{lastmod}</lastmod>",
        "    <changefreq>weekly</changefreq>",
        "    <priority>1.0</priority>",
        "  </url>",
    ]
    for cp in clean_paths:
        lines += [
            "  <url>",
            f"    <loc>{base}/{cp}/</loc>",
            f"    <lastmod>{lastmod}</lastmod>",
            "    <changefreq>monthly</changefreq>",
            "    <priority>0.8</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    (DOCS_DIR / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _rfc822(time_str: str) -> str:
    parts = re.split(r"[.\-/]", (time_str or "").strip())
    try:
        dt = datetime(int(parts[0]), int(parts[1]), int(parts[2]), tzinfo=timezone.utc)
    except (ValueError, IndexError):
        dt = datetime.now(timezone.utc)
    return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")


def emit_rss(successes: list[str], posts_lookup: dict, conf):
    base = conf["base_url"].rstrip("/")
    site = conf.get("site") or {}
    site_name = site.get("name", "Branch Log")
    site_desc = site.get("description", "")
    max_items = (conf.get("rss") or {}).get("max_items", 30)

    # Intersect with successes so the feed never links to a page we failed to render.
    success_set = set(successes)
    items = [
        (post.get("time", ""), cp, post)
        for cp, post in posts_lookup.items()
        if cp in success_set and post.get("time")
    ]
    items.sort(reverse=True)
    items = items[:max_items]

    build_date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "  <channel>",
        f"    <title>{xml_escape(site_name)}</title>",
        f"    <link>{base}/</link>",
        f"    <description>{xml_escape(site_desc)}</description>",
        "    <language>ko</language>",
        f'    <atom:link href="{base}/rss.xml" rel="self" type="application/rss+xml" />',
        f"    <lastBuildDate>{build_date}</lastBuildDate>",
    ]
    for time_str, cp, post in items:
        url = f"{base}/{cp}/"
        title = post.get("title") or cp
        tags = post.get("tag") or []
        if isinstance(tags, str):
            tags = [tags]
        description = " · ".join(tags) if tags else title
        lines += [
            "    <item>",
            f"      <title>{xml_escape(title)}</title>",
            f"      <link>{xml_escape(url)}</link>",
            f'      <guid isPermaLink="true">{xml_escape(url)}</guid>',
            f"      <pubDate>{_rfc822(time_str)}</pubDate>",
            f"      <description>{xml_escape(description)}</description>",
        ]
        for t in tags:
            lines.append(f"      <category>{xml_escape(t)}</category>")
        lines.append("    </item>")

    lines += ["  </channel>", "</rss>"]
    (DOCS_DIR / "rss.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dry-run", action="store_true", help="List routes without writing files")
    p.add_argument("--only", help="Process only sidebar matching this substring (debug)")
    args = p.parse_args()

    conf = load_config()
    skip_dirs = set(conf.get("skip_sidebars") or [])
    skip_kw = list(conf.get("skip_label_keywords") or [])
    posts_lookup = load_posts_lookup()
    course_names = conf.get("course_names") or {}

    md_engine = markdown.Markdown(
        extensions=["fenced_code", "tables", "toc", "sane_lists", "attr_list"],
    )

    successes, failures, seen = [], [], set()
    for sidebar in discover_sidebars(skip_dirs):
        if args.only and args.only not in str(sidebar):
            continue
        print(f"\n== {sidebar.relative_to(REPO_ROOT)} ==")
        for label, target in parse_sidebar_routes(sidebar, skip_kw):
            if target in seen:
                continue
            seen.add(target)
            if args.dry_run:
                clean, kind, _ = normalize_route(target)
                print(f"  [{kind:8}] {clean}  ←  {target}")
                continue
            clean, err = render_html_page(
                label, target, conf, md_engine, posts_lookup, course_names
            )
            if err:
                failures.append((clean, target, err))
                print(f"  FAIL  {target}: {err}", file=sys.stderr)
            else:
                successes.append(clean)
                print(f"  OK    {clean}")

    if not args.dry_run:
        emit_sitemap(sorted(successes), conf)
        emit_rss(successes, posts_lookup, conf)
        print(f"\nGenerated {len(successes)} pages, {len(failures)} failures.")
        if failures:
            print("Failures:")
            for c, t, e in failures:
                print(f"  - {c or t}: {e}")


if __name__ == "__main__":
    main()
