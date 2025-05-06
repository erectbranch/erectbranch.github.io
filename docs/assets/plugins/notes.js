function noteTitlePlugin(hook, vm) {
    let jsonVariable;
    let hasSubtitle = false

    const dashboardConfig = vm.config.dashboard || {};
    const metadataUrl = dashboardConfig.metadataUrl || "metadata/posts";

    const getJson = (fileName) => {
        let xhttp = new XMLHttpRequest();
        xhttp.open("GET", `${fileName}.json`, false);
        xhttp.send(null);
        return JSON.parse(xhttp.response);
    }

    function testJsonKey(json, key) {
        if (Object.keys(json).indexOf(key) > -1) {
            return true
        }
        return false
    }

    function filterByHref(href) {
        return jsonVariable.filter(item => {
            if (!item || !item.href) return false;
            return item.href.includes(href);
        });
    }

    function getGithubUrl(innerHTML) {
        const regex = /https:\/\/raw\.githubusercontent\.com\/(.*?)\/(.*?)\/(.*?)(?:\?|&)/;
        const match = innerHTML.match(regex);
        var githubUrl = `https://github.com/${match[1]}/${match[2]}/tree/${match[3]}`;
        return githubUrl;
    }

    function renderTitleOptions(githubUrl) {
        let titleOptions = "";
        let issueUrl = githubUrl.split('/tree/')[0] + '/issues';

        titleOptions += `<div class="title-options-wrapper">`;
        titleOptions += `<div class="title-options-left"><a href="${issueUrl}"><i class="fa-solid fa-comment"></i></a></div>`;
        titleOptions += `<div class="title-options-right"><a href="${githubUrl}"><i class="fa-solid fa-pen-to-square"></i></a> <button class="title-options-button" onclick="navigator.clipboard.writeText(window.location.href).then(() => alert('link copied'));"><a><i class="fa-solid fa-link"></i></a></button></div>`;
        titleOptions += `</div>`;
        return titleOptions;
    }

    hook.init(() => {
        try {
            jsonVariable = getJson(metadataUrl);
            if (sortPosts) {
                jsonVariable = sortJsonByTime(jsonVariable);
            }
        } catch (e) {
            console.error(`Failed to fetch ${metadataUrl}.json.`, e);
        }
    })

    function renderNoteTitle() {
        let node = document.querySelector('.markdown-section');
        const path = window.location.href;
        const pageHref = `#/${path.split('/#/')[1]}`;

        if (node.innerHTML.includes("<!-- titles -->")) {
            const filteredItems = filterByHref(pageHref)[0];
            hasSubtitle = testJsonKey(filteredItems, "subtitle")

            let githubUrl = getGithubUrl(node.innerHTML);

            if (hasSubtitle) {
                var { time, title, subtitle, tag, image, href } = filteredItems;
            } else {
                var { time, title, tag, image, href } = filteredItems;
            }

            if (Array.isArray(tag)) {
                tag = tag.map(tag => `<a class="tag-element" href="#/tags?tag=${tag}" target="_blank">${tag}</a>`).join('&nbsp;');
            } else {
                tag = `<a class="tag-element" href="#/tags?tag=${tag}" target="_blank">${tag}</a>`;
            }

            let noteTitleContent = `<div class="note-info">`;
            noteTitleContent += `<div class="note-title">${title}</div>`;
            if (hasSubtitle) {
                noteTitleContent += `<div class="note-subtitle">${subtitle}</div>`;
            }
            noteTitleContent += `<div class="note-time"><span style="font-weight: bolder;" id="title-author">Sungjae Jeon</span> ⋅ <span id="title-time">${time}</span></div>`;
            noteTitleContent += `<div class="note-tag">${tag}</div>`;
            noteTitleContent += `</div>`;
            noteTitleContent += renderTitleOptions(githubUrl);

            node.innerHTML = node.innerHTML.replace(/<!--\s*titles\s*-->/gm, noteTitleContent);
        }
    }

    hook.doneEach(() => {        
        renderNoteTitle();
    });
};

window.$docsify.plugins = [].concat(noteTitlePlugin, window.$docsify.plugins)