document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.href;

    if (path.includes('showcase')) {
      // document.body.classList.add('close');
      var editCSS = document.createElement('style')
      editCSS.innerHTML = ".content {left: 250px;} .markdown-section {padding-top: 0rem !important; height: 100%;} .app-name {display: none;} .search {display: none;} nav {display: none;}";
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