// Dark mode toggle. Persists in localStorage and swaps the themeable
// stylesheets. The initial state is applied by an inline bootstrap script in
// index.html to avoid a flash of light content.
//
// Click handling uses event delegation because docsify re-renders nav.md on
// every route change, replacing the toggle element. The icon (half-stroke
// circle) is intentionally identical in both modes, so no icon class swap is
// needed.
(function () {
  var STORAGE_KEY = 'theme';
  var DEFAULT_THEME = 'light';

  function currentTheme() {
    return document.documentElement.getAttribute('data-theme') || DEFAULT_THEME;
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    try { localStorage.setItem(STORAGE_KEY, theme); } catch (e) {}

    var light = document.getElementById('theme-light');
    var dark = document.getElementById('theme-dark');
    if (light && dark) {
      light.disabled = (theme === 'dark');
      dark.disabled = (theme === 'light');
    }
  }

  function toggle(e) {
    if (e) e.preventDefault();
    applyTheme(currentTheme() === 'dark' ? 'light' : 'dark');
  }

  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('#theme-toggle');
    if (t) toggle(e);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var a = document.activeElement;
    if (a && a.id === 'theme-toggle') toggle(e);
  });
})();
