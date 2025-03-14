// 문자열 규칙: [\>\>|TITLE|{제목}|TIME|{YYYY.MM.DD}|TAB|{카테고리}|IMAGE|{이미지 url}\<\<](페이지 url)
window.$docsify = window.$docsify || {};
window.$docsify.plugins = (window.$docsify.plugins || []).concat((hook) => {
    const cardRegEx = /\[>>\|TIME\|{(.+?)}\|TITLE\|{(.+?)}\|TAB\|{(.+?)}\|IMAGE\|{(.+?)}<<\]\((.+?)\)/gm;

    hook.beforeEach(content => {
        return content.replace(cardRegEx, (string, time, title, category, imageUrl, pageUrl) => {
            return string.replace(
                string, 
                `<a class="toc-page-display-a" href="${pageUrl}" target="_blank">
                    <div class="toc-page-display-div">
                        <div class="toc-page-display-title-img">
                            <center>
                                <img class="ignore-view-full-image-img" src="${imageUrl}">
                            </center>
                        </div>
                        <div class="toc-page-display-title-div">
                            ${title}
                        </div>
                        <div class="toc-page-display-date-div">
                            ${time} ⋅ ${category}
                        </div>
                    </div>
                </a>`
            );
        });
    });
});