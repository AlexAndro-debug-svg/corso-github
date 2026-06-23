(function () {
  'use strict';

  var STORAGE_KEY = 'as_cookie_consent';
  var STORAGE_VER = '1';

  function getConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var obj = JSON.parse(raw);
      return obj.v === STORAGE_VER ? obj : null;
    } catch (e) { return null; }
  }

  function saveConsent(choice) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ v: STORAGE_VER, choice: choice, ts: Date.now() }));
    } catch (e) {}
  }

  function injectStyles() {
    var css = [
      '#as-cookie-banner{position:fixed;bottom:0;left:0;right:0;z-index:99999;background:#1e293b;color:rgba(255,255,255,.9);padding:1.2rem 1.5rem;box-shadow:0 -4px 24px rgba(0,0,0,.25);font-family:"Inter",sans-serif;font-size:.88rem;line-height:1.5;}',
      '#as-cookie-inner{max-width:1120px;margin:0 auto;display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap;}',
      '#as-cookie-text{flex:1;min-width:220px;}',
      '#as-cookie-text p{margin:0;}',
      '#as-cookie-text a{color:#f59e0b;text-decoration:underline;}',
      '#as-cookie-actions{display:flex;gap:.7rem;flex-shrink:0;flex-wrap:wrap;}',
      '.as-btn-accept{background:#4f46e5;color:#fff;border:none;padding:.6rem 1.3rem;border-radius:8px;font-size:.88rem;font-weight:700;cursor:pointer;white-space:nowrap;transition:opacity .15s;}',
      '.as-btn-accept:hover{opacity:.85;}',
      '.as-btn-reject{background:transparent;color:rgba(255,255,255,.75);border:1px solid rgba(255,255,255,.3);padding:.6rem 1.3rem;border-radius:8px;font-size:.88rem;font-weight:600;cursor:pointer;white-space:nowrap;transition:opacity .15s;}',
      '.as-btn-reject:hover{opacity:.75;}',
      '@media(max-width:640px){#as-cookie-inner{flex-direction:column;align-items:stretch;}#as-cookie-actions{flex-direction:column;}#as-cookie-actions button{width:100%;text-align:center;}}'
    ].join('');
    var style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);
  }

  function showBanner() {
    injectStyles();

    var banner = document.createElement('div');
    banner.id = 'as-cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Consenso cookie');
    banner.innerHTML = [
      '<div id="as-cookie-inner">',
        '<div id="as-cookie-text">',
          '<p>🍪 Questo sito utilizza <strong>cookie tecnici essenziali</strong> per il corretto funzionamento. Non utilizziamo cookie di profilazione o tracciamento di terze parti. ',
          'Puoi leggere la nostra <a href="cookie-policy.html">Cookie Policy</a> per maggiori informazioni.</p>',
        '</div>',
        '<div id="as-cookie-actions">',
          '<button class="as-btn-accept" id="as-accept">✓ Accetta</button>',
          '<button class="as-btn-reject" id="as-reject">Solo essenziali</button>',
        '</div>',
      '</div>'
    ].join('');

    document.body.appendChild(banner);

    document.getElementById('as-accept').addEventListener('click', function () {
      saveConsent('accepted');
      hideBanner();
    });
    document.getElementById('as-reject').addEventListener('click', function () {
      saveConsent('essential');
      hideBanner();
    });
  }

  function hideBanner() {
    var b = document.getElementById('as-cookie-banner');
    if (b) {
      b.style.transition = 'transform .3s ease, opacity .3s ease';
      b.style.transform = 'translateY(100%)';
      b.style.opacity = '0';
      setTimeout(function () { if (b.parentNode) b.parentNode.removeChild(b); }, 320);
    }
  }

  function init() {
    if (getConsent()) return;
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', showBanner);
    } else {
      showBanner();
    }
  }

  init();
})();
