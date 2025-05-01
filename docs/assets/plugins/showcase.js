document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.href;

    if (path.includes('showcase')) {
      // document.body.classList.add('close');
      var editCSS = document.createElement('style')
      editCSS.innerHTML = ".content {left: 250px;} .markdown-section {padding-top: 0rem !important; height: 100%;} .app-name {display: none;} .search {display: none;} nav {display: none;}";
      editCSS.innerHTML += " .anchor {font-family: sans-serif; font-weight: lighter;} .anchor span {color: #333333;}  .markdown-section h2 {border-bottom: 1px solid #dee2e6;}";
      document.body.appendChild(editCSS);
    }
    
    // showcase 페이지에서 다른 페이지로 이동 시 새로고침 & 반대의 경우에도 새로고침
    window.addEventListener('hashchange', () => {
      const newPath = window.location.href;
      if (path.includes('showcase') && !newPath.includes('showcase')) {
        location.reload();
      } else if (!path.includes('showcase') && newPath.includes('showcase')) {
        location.reload();
      }
    });
  }
);

function renderShowcaseTagPage() {
  const path = window.location.href;
  isShowcaseTag = path.includes('tag-demo') && path.includes('showcase');
  tagPageDiv = document.getElementsByClassName('markdown-section')[0]
  const showcaseMetadata = JSON.parse(`[
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
      "href": "#/showcase/docsify-image-slider/guide"
    },
    {
      "time": "2025.04.01",
      "title": "Update your docsify documents with a dashboard",
      "subtitle": "How to create a dashboard with docsify-dashboard plugin, and how to customize the dashboard theme",
      "tag": ["docsify", "plugin"],
      "image": "https://raw.githubusercontent.com/erectbranch/docsify-dashboard/master/demo.png",
      "href": "#/showcase/docsify-dashboard/guide"
    }
  ]`);

  if (!isShowcaseTag) {
      return;
  }

  console.log('showcaseTagPage');
  
  var tagName = path.split('?tag=')[1];
  if (tagName.includes('%20')) {
      tagName = tagName.replace(/%20/g, ' ');
  }

  function filterByTag(tag) {
    return showcaseMetadata.filter(item => {
        if (!item || !item.tag) return false;
        return item.tag.includes(tag);
    });
  }

  // if tagName in ["docsify", "plugin"]
  if (tagName === 'docsify' || tagName === 'plugin') {
    const filteredItems = filterByTag(tagName);  
    let showcaseTagBoardContent = `<h1>tag: ${tagName}</h1>\n<hr>`;
      showcaseTagBoardContent += `\n<div class="toc-page-div">\n`;
      for (let i = 0; i < filteredItems.length; i++) {
        var { time, title, subtitle, tag, image, href } = filteredItems[i];
        
        if (Array.isArray(tag)) {
          tag = tag.join(' ⋅ ');
        }

        showcaseTagBoardContent += `<a class="toc-page-display-a" id="list" href="${href}" target="_blank">
        <div class="toc-page-display-div" id="list">
            <div class="toc-page-display-title-img" id="list">
                <center>
                    <img class="ignore-view-full-image-img" src="${image}">
                </center>
            </div>
            <div class="toc-page-display-title-div" id="list">
                ${title}
            </div>
            <div class="toc-page-display-subtitle-div" id="list">
                ${subtitle}
            </div>
            <div class="toc-page-display-date-div" id="list">
                ${time} &nbsp;&nbsp; ${tag}
            </div>
        </div>
    </a>`;

      }
      showcaseTagBoardContent += `\n</div>\n`;

      tagPageDiv.innerHTML = showcaseTagBoardContent;
  } else {
    tagPageDiv.innerHTML = `<div class="tag-container">
    <div class="tag-list">
        <a class="tag-element" href="#/showcase/docsify-dashboard/tag-demo?tag=docsify" target="_blank" style="font-size: 21px;">docsify</a>
        <a class="tag-element" href="#/showcase/docsify-dashboard/tag-demo?tag=plugin" target="_blank" style="font-size: 21px;">plugin</a>
    </div>
</div>`
  }

  window.addEventListener('hashchange', () => {
      location.reload();
  });
};

function showcasePlugin(hook, vm) {
  hook.doneEach(() => {        
    renderShowcaseTagPage();
  });
}

window.$docsify.plugins = [].concat(showcasePlugin, window.$docsify.plugins)