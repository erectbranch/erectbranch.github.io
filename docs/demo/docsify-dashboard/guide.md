<div align="center">

# docsify-dashboard

[![GitHub Release](https://img.shields.io/github/v/release/erectbranch/docsify-dashboard?logo=github&color=orange&style=flat-square)](https://github.com/erectbranch/docsify-dashboard/releases)
[![NPM Release](https://img.shields.io/npm/v/docsify-dashboard.svg?logo=npm&style=flat-square)](https://www.npmjs.com/package/docsify-dashboard)
[![License: MIT](https://img.shields.io/badge/License-GPLv3-yellow.svg?style=flat-square)](https://github.com/erectbranch/docsify-dashboard/blob/master/LICENSE)

A plugin for [Docsify](https://docsify.js.org/#/) that creates a dashboard from a metadata.

</div>

## 1. Demo

<details>
<summary>Metadata (open/close) </summary>

```json
[
    {
      "time": "2025.04.23",
      "title": "A magical documentation site generator: Docsify",
      "subtitle": "Smartly loads and parses your Markdown files and displays them as a website",
      "tag": "docsify",
      "image": "images/docsify.jpeg",
      "href": "https://docsify.js.org/#/"
    },
    {
      "time": "2025.04.07",
      "title": "Making your gallery more interactive",
      "subtitle": "Introducing new docsify plugin that creates a slider for images",
      "tag": ["docsify", "plugin"],
      "image": "https://raw.githubusercontent.com/erectbranch/docsify-image-slider/master/demo.gif",
      "href": "#/demo/docsify-image-slider/guide"
    },
    {
      "time": "2025.04.01",
      "title": "Update your docsify documents with a dashboard",
      "subtitle": "How to create a dashboard with docsify-dashboard plugin, and how to customize the dashboard theme",
      "tag": ["docsify", "plugin"],
      "image": "https://raw.githubusercontent.com/erectbranch/docsify-dashboard/master/demo.png",
      "href": "#/demo/docsify-dashboard/guide"
    }
]
```

</details>

### Dashboard

<!-- tabs:start -->

#### **1**

<div class="toc-page-div">
    <a class="toc-page-display-a" id="default" href="https://docsify.js.org/#/" target="_blank">
        <div class="toc-page-display-div" id="default">
            <div class="toc-page-display-title-img" id="default">
                <center>
                    <img class="ignore-view-full-image-img" src="images/docsify.jpeg" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="default">
                A magical documentation site generator: Docsify
            </div>
            <div class="toc-page-display-subtitle-div" id="default">
                Smartly loads and parses your Markdown files and displays them as a website
            </div>
            <div class="toc-page-display-date-div" id="default">
                2025.04.23 &nbsp;&nbsp; docsify
            </div>
        </div>
    </a>
    <a class="toc-page-display-a" id="default" href="#/demo/docsify-image-slider/guide" target="_blank">
        <div class="toc-page-display-div" id="default">
            <div class="toc-page-display-title-img" id="default">
                <center>
                    <img class="ignore-view-full-image-img" src="https://raw.githubusercontent.com/erectbranch/docsify-image-slider/master/demo.gif" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="default">
                Making your gallery more interactive
            </div>
            <div class="toc-page-display-subtitle-div" id="default">
                Introducing new docsify plugin that creates a slider for images
            </div>
            <div class="toc-page-display-date-div" id="default">
                2025.04.07 &nbsp;&nbsp; docsify ⋅ plugin
            </div>
        </div>
    </a>
</div>

#### **2**

<div class="toc-page-div">
    <a class="toc-page-display-a" id="list" href="#/demo/docsify-dashboard/guide" target="_blank">
        <div class="toc-page-display-div" id="list">
            <div class="toc-page-display-title-img" id="list">
                <center>
                    <img class="ignore-view-full-image-img" src="https://raw.githubusercontent.com/erectbranch/docsify-dashboard/master/demo.png" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="list">
                Update your docsify documents with a dashboard
            </div>
            <div class="toc-page-display-subtitle-div" id="list">
                How to create a dashboard with docsify-dashboard plugin, and how to customize the dashboard theme
            </div>
            <div class="toc-page-display-date-div" id="list">
                2025.04.01 &nbsp;&nbsp; docsify ⋅ plugin
            </div>
        </div>
    </a>
</div>

<!-- tabs:end -->

### Tag-dashboard

<div class="tag-container">
    <div class="tag-list">
        <a class="tag-element" href="#/demo/docsify-dashboard/tag-demo?tag=docsify" target="_blank" style="font-size: 21px;">docsify</a>
        <a class="tag-element" href="#/demo/docsify-dashboard/tag-demo?tag=plugin" target="_blank" style="font-size: 21px;">plugin</a>
    </div>
</div>


## 2. Import

To use the dashboard, you need to include the plugin in your Docsify `index.html` file:

**Add stylesheet**

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify-dashboard@3.0.0/dist/dashboard.min.css">
```

**Add script**

> [!WARNING]
> This plugin requires [docsify-tabs](https://jhildenbiddle.github.io/docsify-tabs/#/) plugin. Make sure to import docsify-tabs after the docsify-dashboard.

```html
<script src="//cdn.jsdelivr.net/npm/docsify-dashboard@3.0.0/dist/docsify-dashboard.min.js"></script>

<!-- The docsify-tabs plugin (must be included after the docsify-dashboard plugin) -->
<script src="https://cdn.jsdelivr.net/npm/docsify-tabs@1/dist/docsify-tabs.min.js"></script>
```

## 3. Structure

The following directory structure is used:

- `tags.md`: Empty file for rendering a dashboard by tags in the URL. (e.g., `#/tags?tag=plugin`)

- `posts.json`: Metadata file containing the posts information.

```bash
.
└── docs
    ├── index.html
    └── tags.md
    └── metadata
        └── posts.json
```

The metadata should be structured as follows:

> [!NOTE]
> "*subtitle*", "*category*" is optional

```json
[
    {
        "time": "YYYY.MM.DD",
        "title": "...",
        "subtitle": "...",
        "tag": "...",
        "image": "...",
        "href": "#/...",
        "category": "..."
    },
    {
        "time": "YYYY.MM.DD",
        "title": "...",
        "tag": "...",
        "image": "...",
        "href": "#/..."
    },
    ...
]
```


## 4. Usage

### Dashboard

You can create a dashboard by adding the following code to your markdown file:

> \<\!-- tabs:start --\>
>
> \<\!-- dashboard --\>
>
> \<\!-- tabs:end --\>

To display posts from a specific category only, you can use the following code:

> \<\!-- dashboard:categoryName --\>

### Tag-dashboard

You can display a tag list by adding the following code to your markdown file:

- **In sidebar file**: display all tags in the metadata.

- **In markdown file**: only display the current page's tags.

> \<\!-- tag-list --\>

It will redirect to the tag-dashboard containing all posts that have the same tag.

### Example

#### Footer with Page Tags
    
Add a page footer to display the tag list on each page.

```javascript
window.$docsify = {
  plugins: [
    function pageFooter(hook, vm) {
      var footer = [
        '<!-- tag-list -->',
        '<hr/>',
      ].join('');

      hook.afterEach(function (html) {
        return html + footer;
      });
    },
  ],
};
```

## 5. Configuration

To configure the dashboard, you can set options in your `index.html` file. The available options are:

- **Theme**: `default`, `cards`, `list`

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `numTabContent` | `Int` | 3 | Number of cards to show in a docsify-tabs slide. |
| `metadataUrl` | `String` | 'metadata/posts' | JSON URL to fetch metadata. |
| `sort` | `Boolean` | false | Sort the posts by time. (`YYYY.MM.DD`, `YYYY/MM/DD`) |
| `theme` | `String` | 'default' | Theme for the dashboard. |
| `tagboardTheme` | `String` | 'default' | Theme for the tag-dashboard. |
| `pagination` | `Boolean` | false | Enable pagination for the dashboard tabs. |

```javascript
window.$docsify = {
  dashboard: {
    numTabContent: 3,
    metadataUrl: 'metadata/posts',       // do not include '.json' extension
    sort: false,                         // sort the posts by time
    theme: 'default',                    // (1) default, (2) cards, (3) list
    tagboardTheme: 'default',            // options are same as above
    pagination: false                    // enable pagination for the dashboard tabs
  }
};
```

### Demo (Theme)

<!-- tabs:start -->

#### **default**

<div class="toc-page-div">
    <a class="toc-page-display-a" id="default" href="https://docsify.js.org/#/" target="_blank">
        <div class="toc-page-display-div" id="default">
            <div class="toc-page-display-title-img" id="default">
                <center>
                    <img class="ignore-view-full-image-img" src="images/docsify.jpeg" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="default">
                A magical documentation site generator: Docsify
            </div>
            <div class="toc-page-display-subtitle-div" id="default">
                Smartly loads and parses your Markdown files and displays them as a website
            </div>
            <div class="toc-page-display-date-div" id="default">
                2025.04.23 &nbsp;&nbsp; docsify
            </div>
        </div>
    </a>
    <a class="toc-page-display-a" id="default" href="#/demo/docsify-image-slider/guide" target="_blank">
        <div class="toc-page-display-div" id="default">
            <div class="toc-page-display-title-img" id="default">
                <center>
                    <img class="ignore-view-full-image-img" src="https://raw.githubusercontent.com/erectbranch/docsify-image-slider/master/demo.gif" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="default">
                Making your gallery more interactive
            </div>
            <div class="toc-page-display-subtitle-div" id="default">
                Introducing new docsify plugin that creates a slider for images
            </div>
            <div class="toc-page-display-date-div" id="default">
                2025.04.07 &nbsp;&nbsp; docsify ⋅ plugin
            </div>
        </div>
    </a>
</div>

#### **cards**

<div class="toc-page-div">
    <a class="toc-page-display-a" id="cards" href="https://docsify.js.org/#/" target="_blank">
        <div class="toc-page-display-div" id="cards">
            <div class="toc-page-display-title-img" id="cards">
                <center>
                    <img class="ignore-view-full-image-img" src="images/docsify.jpeg" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="cards">
                A magical documentation site generator: Docsify
            </div>
            <div class="toc-page-display-subtitle-div" id="cards">
                Smartly loads and parses your Markdown files and displays them as a website
            </div>
            <div class="toc-page-display-date-div" id="cards">
                2025.04.23 &nbsp;&nbsp; docsify
            </div>
        </div>
    </a>
    <a class="toc-page-display-a" id="cards" href="#/demo/docsify-image-slider/guide" target="_blank">
        <div class="toc-page-display-div" id="cards">
            <div class="toc-page-display-title-img" id="cards">
                <center>
                    <img class="ignore-view-full-image-img" src="https://raw.githubusercontent.com/erectbranch/docsify-image-slider/master/demo.gif" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="cards">
                Making your gallery more interactive
            </div>
            <div class="toc-page-display-subtitle-div" id="cards">
                Introducing new docsify plugin that creates a slider for images
            </div>
            <div class="toc-page-display-date-div" id="cards">
                2025.04.07 &nbsp;&nbsp; docsify ⋅ plugin
            </div>
        </div>
    </a>
</div>

#### **list**

<div class="toc-page-div">
    <a class="toc-page-display-a" id="list" href="https://docsify.js.org/#/" target="_blank">
        <div class="toc-page-display-div" id="list">
            <div class="toc-page-display-title-img" id="list">
                <center>
                    <img class="ignore-view-full-image-img" src="images/docsify.jpeg" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="list">
                A magical documentation site generator: Docsify
            </div>
            <div class="toc-page-display-subtitle-div" id="list">
                Smartly loads and parses your Markdown files and displays them as a website
            </div>
            <div class="toc-page-display-date-div" id="list">
                2025.04.23 &nbsp;&nbsp; docsify
            </div>
        </div>
    </a>
    <a class="toc-page-display-a" id="list" href="#/demo/docsify-image-slider/guide" target="_blank">
        <div class="toc-page-display-div" id="list">
            <div class="toc-page-display-title-img" id="list">
                <center>
                    <img class="ignore-view-full-image-img" src="https://raw.githubusercontent.com/erectbranch/docsify-image-slider/master/demo.gif" loading="lazy">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="list">
                Making your gallery more interactive
            </div>
            <div class="toc-page-display-subtitle-div" id="list">
                Introducing new docsify plugin that creates a slider for images
            </div>
            <div class="toc-page-display-date-div" id="list">
                2025.04.07 &nbsp;&nbsp; docsify ⋅ plugin
            </div>
        </div>
    </a>
</div>

<!-- tabs:end -->


## 6. Customization

The dashboard can be customized using CSS. You can override the following CSS variables.

### Dashboard

To change the styles, you can add the following CSS to your `index.html` file:

```html
<style>
  /* default */
  :root {
    /* card style */
    --dashboard-card-border-radius: 5px;
    --dashboard-card-margin-top: 10px; 
    --dashboard-card-bg-color: #ffffff; 
    --dashboard-card-max-width: 330px;
    --dashboard-card-min-height: 220px;
    --dashboard-card-shadow: 0 0.3em 0.3em rgba(0,0,0,0.2);

    /* card text */
    --dashboard-card-text-align: left; 
    --dashboard-card-text-color: #000000;
    --dashboard-card-title-font-size: 1.2rem; 
    --dashboard-card-title-font-weight: bolder;
    --dashboard-card-subtitle-font-size: 1rem; 
    --dashboard-card-subtitle-color: #808080; 
    --dashboard-card-date-font-size: 0.8rem; 
    --dashboard-card-date-color: #808080;

    /* card image */
    --dashboard-card-img-min-width: 100%;
    --dashboard-card-img-min-height: 160px;
    --dashboard-card-img-max-height: 160px;
    --dashboard-card-img-border: 0.1em solid #ced4da;

    /* list theme */
    --dashboard-list-theme-max-width: var(--content-max-width, 100%);
    --dashboard-list-theme-img-max-width: 200px;

    /* pagination style */
    --pagination-tab-font-size: 1.1rem;
    --pagination-tab-highlight-color: var(--theme-color, #dbe8f0);
  }
</style>
```

### Tag-dashboard

To change the tag-list styles, add the following CSS:

```html
<style>
  /* default */
  :root {
    --tags-bg-color: #fafbfbff;
    --tags-font-color: #54cca7ff;
    --tags-font-size: var(--base-font-size);
    --tags-margin-top: 5px;

    --sidebar-tags-bg-color: var(--tags-bg-color);
    --sidebar-tags-font-color: var(--tags-font-color);
    --sidebar-tags-font-size: var(--tags-font-size);
    --sidebar-tags-margin-top: var(--tags-margin-top);
  }
</style>
```

## 7. License

This project is licensed under the GNU General Public License v3.0.

- Original work © 2023–2025 李亦楊 ([@pikapikapikaori](https://github.com/pikapikapikaori))

- Modified work © 2025 Sungjae Jeon ([@erectbranch](https://github.com/erectbranch))

See [LICENSE](https://github.com/erectbranch/docsify-dashboard/blob/master/LICENSE) for more details.

## 8. Contribution

Please feel free to submit a pull request or open an issue on the GitHub repository. Your contributions are welcome and appreciated!

---