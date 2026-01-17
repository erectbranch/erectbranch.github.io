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
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from xml.sax.saxutils import escape as xml_escape

import markdown
import requests
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
CONFIG_PATH = Path(__file__).resolve().parent / "static-mirror.yaml"

MD_LINK_RE = re.compile(
    r'(?<!!)\[([^\]]+)\]\(([^)#\s]+)(?:\s+"[^"]*")?\)'
)
HTML_FIRST_P_RE = re.compile(r"<p[^>]*>(.*?)</p>", re.S)
HTML_TAGS_RE = re.compile(r"<[^>]+>")

SESSION = requests.Session()
SESSION.headers["User-Agent"] = "docsify-static-mirror/1.0 (+https://erectbranch.github.io)"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


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
<html lang="en">
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


def render_html_page(label, target, conf, md_engine):
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

    md_engine.reset()
    html = md_engine.convert(md_text)
    title, description = extract_title_desc(html, label)
    spa_url = f"/#/{clean_path}"
    canonical = f"{conf['base_url'].rstrip('/')}/{clean_path}/"

    import json
    page = PAGE_TEMPLATE.format(
        title=xml_escape(title),
        description=xml_escape(description),
        canonical=xml_escape(canonical),
        spa_url=xml_escape(spa_url),
        spa_url_json=json.dumps(spa_url),
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


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dry-run", action="store_true", help="List routes without writing files")
    p.add_argument("--only", help="Process only sidebar matching this substring (debug)")
    args = p.parse_args()

    conf = load_config()
    skip_dirs = set(conf.get("skip_sidebars") or [])
    skip_kw = list(conf.get("skip_label_keywords") or [])

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
            clean, err = render_html_page(label, target, conf, md_engine)
            if err:
                failures.append((clean, target, err))
                print(f"  FAIL  {target}: {err}", file=sys.stderr)
            else:
                successes.append(clean)
                print(f"  OK    {clean}")

    if not args.dry_run:
        emit_sitemap(sorted(successes), conf)
        print(f"\nGenerated {len(successes)} pages, {len(failures)} failures.")
        if failures:
            print("Failures:")
            for c, t, e in failures:
                print(f"  - {c or t}: {e}")


if __name__ == "__main__":
    main()
