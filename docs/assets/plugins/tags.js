function tagPlugin(hook, vm) {
    let jsonVariable;
    const dashboardConfig = vm.config.dashboard || {};
    const metadataUrl = dashboardConfig.metadataUrl || "metadata/posts";

    // TODO
    // const tagConfig = vm.config.tag || {};
    // const tagBaseUrl = tagConfig.baseUrl || "tags"; // url: #/{tagBaseUrl}?tag=tagName

    const getJson = (fileName) => {
        let xhttp = new XMLHttpRequest();
        xhttp.open("GET", `${fileName}.json`, false);
        xhttp.send(null);
        return JSON.parse(xhttp.response);
    };

    function filterByTag(tag) {
        return jsonVariable.filter(item => {
            if (!item || !item.tag) return false;
            return item.tag.includes(tag);
        });
    }

    function getTagList() {
        const tagList = [];
        jsonVariable.forEach(item => {
            if (typeof item.tag === 'object' && item.tag.length > 0) {
                item.tag.forEach(tag => {
                    if (!tagList.includes(tag)) {
                        tagList.push(tag);
                    }
                });
            } else if (typeof item.tag === 'string' && item.tag.length > 0) {
                if (!tagList.includes(item.tag)) {
                    tagList.push(item.tag);
                }
            }
        });
        return tagList;
    }

    hook.init(() => {
        try {
            jsonVariable = getJson(metadataUrl);
        } catch (e) {
            console.error(`Failed to fetch ${metadataUrl}.json.`, e);
        }
        tagList = getTagList();
    });

    function renderTagPage() {
        const path = window.location.href;
        hasTags = path.includes('tags');
        tagPageDiv = document.getElementsByClassName('markdown-section')[0]

        if (!hasTags) {
            return;
        }
        
        var tagName = path.split('?tag=')[1];

        if (tagName.includes('%20')) {
            tagName = tagName.replace(/%20/g, ' ');
        }

        // Get the filtered items based on the tag name
        const filteredItems = filterByTag(tagName);

        if (filteredItems && filteredItems.length > 0) {
            let tagBoardContent = `<h1>${tagName}</h1>\n<hr>`;
            tagBoardContent += `\n<div class="toc-page-div">\n`;
            for (let i = 0; i < filteredItems.length; i++) {
                var { time, title, tag, image, href } = filteredItems[i];

                if (Array.isArray(tag)) {
                    tag = tag.join(' ⋅ ');
                }
                
                tagBoardContent += `    <a class="toc-page-display-a" href="${href}" target="_blank">
        <div class="toc-page-display-div">
            <div class="toc-page-display-title-img">
                <center>
                    <img class="ignore-view-full-image-img" src="${image}">
                </center>
            </div>
            <div class="toc-page-display-title-div">
                ${title}
            </div>
            <div class="toc-page-display-date-div">
                ${time} ⋅ ${tag}
            </div>
        </div>
    </a>`
            }
            tagBoardContent += `\n</div>\n`;

            tagPageDiv.innerHTML = tagBoardContent + tagPageDiv.innerHTML;
        } else {
            tagBoardContent = `<h1>Tags</h1>\n<hr>`;
            tagBoardContent += `\n${tagList.map(tag => `<a href="#/tags?tag=${tag}" target="_blank">${tag}</a>`).join(' | ')}\n`;
            tagPageDiv.innerHTML = tagBoardContent + tagPageDiv.innerHTML;
        }

        window.addEventListener('hashchange', () => {
            location.reload();
        });
    };

    hook.doneEach(() => {        
        renderTagPage();

        const tagElement = document.getElementsByClassName("tag-list")[0];
        tagElement.innerHTML = `${tagList.map(tag => `<a class="tag-element" href="#/tags?tag=${tag}" target="_blank">${tag}</a>`).join('\n')}`;
    });

};

window.$docsify = window.$docsify || {};
window.$docsify.plugins = [].concat(tagPlugin, window.$docsify.plugins)