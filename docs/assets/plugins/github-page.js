function githubPagePlugin(hook, vm) {
    hook.beforeEach((markdown) => {
        if (/githubusercontent\.com/.test(vm.route.file)) {
          url_pwd = vm.route.file.split('/').slice(0, -1).join('/');   // raw.githubusercontent.com/username/repo/branch/

          // change github links to raw links (1: [desc](file))
          markdown = markdown.replace(/]\((?!.*github\.com)([^)]+)\)/g, (match, p1) => {
            return `](${url_pwd}/${p1})`;
          });

          // change github links to raw links (2: src="file")
          markdown = markdown.replace(/src="(?!.*github\.com)([^"]+)"/g, (match, p1) => {
            return `src="${url_pwd}/${p1}"`;
          });
          
          // change github links to raw links (3: [desc](github file url))
          markdown = markdown.replace(/]\(https:\/\/github\.com\/[^)]+\/blob\/[^)]+\)/g, (match) => {
            return match.replace(/github\.com/, 'raw.githubusercontent.com').replace(/\/blob\//, '/');
          });

          // change github redirect links to local links (root: /docs)
          markdown = markdown.replace(/]\(https:\/\/github\.com\/[^)]+\/tree\/[^)]+\)/g, (match) => {
            return match.replace(/https:\/\/github\.com\/[^\/]+/, '').replace(/\/tree\/master\//, '/notes/').replace(/\/tree\/main\//, '/');
          });

          // preprocess math block
          markdown = markdown.replace(/```math([\s\S]*?)```/g, (match, p1) => {
            return `$$ ${p1} $$`;
          });
        }
        return markdown;  
    });

    hook.beforeEach((html) => {
      if (/githubusercontent\.com/.test(vm.route.file)) {
        editURL = vm.route.file.replace(/raw.githubusercontent\.com/, 'github.com').replace(/\/master\//, '/tree/master/').replace(/\/main\//, '/tree/main/');
        editURL = '[📝 EDIT DOCUMENT](' + editURL + ')\n';

        return (editURL + html);
      }
      return html;
  });
}

window.$docsify.plugins = [].concat(githubPagePlugin, window.$docsify.plugins)