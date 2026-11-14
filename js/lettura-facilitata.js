/* Strumenti di lettura: carattere, sfondo, dimensione e sintesi vocale */
(function () {
  var art = document.querySelector('.article-dsa');
  if (!art) return;
  var KEY = 'as-dsa-lettura', MIN = 0.9, MAX = 1.5;
  var st = { font: true, bg: true, scale: 1 };
  try { var sv = JSON.parse(localStorage.getItem(KEY) || 'null'); if (sv) { for (var k in st) if (k in sv) st[k] = sv[k]; } } catch (e) {}
  function save() { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {} }
  var $ = function (id) { return document.getElementById(id); };
  function apply() {
    art.classList.toggle('dsa-font', !!st.font);
    art.classList.toggle('dsa-bg', !!st.bg);
    art.style.setProperty('--rt-scale', st.scale);
    art.classList.toggle('rt-big', st.scale > 1.05);
    $('rt-font').setAttribute('aria-pressed', st.font ? 'true' : 'false');
    $('rt-bg').setAttribute('aria-pressed', st.bg ? 'true' : 'false');
    $('rt-bigger').setAttribute('aria-disabled', st.scale >= MAX ? 'true' : 'false');
    $('rt-smaller').setAttribute('aria-disabled', st.scale <= MIN ? 'true' : 'false');
  }
  apply();
  $('rt-font').addEventListener('click', function () { st.font = !st.font; apply(); save(); });
  $('rt-bg').addEventListener('click', function () { st.bg = !st.bg; apply(); save(); });
  $('rt-bigger').addEventListener('click', function () { st.scale = Math.min(MAX, Math.round((st.scale + 0.1) * 10) / 10); apply(); save(); });
  $('rt-smaller').addEventListener('click', function () { st.scale = Math.max(MIN, Math.round((st.scale - 0.1) * 10) / 10); apply(); save(); });

  /* ---- Sintesi vocale ---- */
  var synth = window.speechSynthesis;
  var bListen = $('rt-listen'), player = $('rt-player'), bPause = $('rp-pause'), bStop = $('rp-stop');
  if (!synth || typeof SpeechSynthesisUtterance === 'undefined') { bListen.hidden = true; return; }
  try { synth.cancel(); } catch (e) {}
  var queue = [], idx = 0, current = null, playing = false, gen = 0, voice = null, fails = 0;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var EMOJI = /\p{Extended_Pictographic}|[\u{FE0F}\u{200D}\u{20E3}]/gu;

  function clean(t) { return t.replace(EMOJI, '').replace(/\s*→\s*/g, ', ').replace(/\s+/g, ' ').trim(); }
  /* frasi brevi: alcune voci online si interrompono sui testi lunghi */
  function push(el, t) {
    var parts = [], buf = '';
    (t.match(/[^.!?;:]+[.!?;:]*\s*/g) || [t]).forEach(function (p) {
      if (p.length <= 160) parts.push(p); else parts.push.apply(parts, p.match(/[^,]+,?\s*/g) || [p]);
    });
    parts.forEach(function (p) {
      if (buf && (buf + p).length > 160) { queue.push({ el: el, text: buf.trim() }); buf = ''; }
      buf += p;
    });
    if (buf.trim()) queue.push({ el: el, text: buf.trim() });
  }
  function build() {
    queue = [];
    art.querySelectorAll('h1, .article-body h2, .article-body h3, .article-body p, .article-body li, .article-body figcaption, .article-body .step-card > div, .article-body .prompt-box, .article-body .dsa-faq summary, .article-body pre[aria-label], .article-body .pc-title, .article-body .sigla, .article-body .cmp-table tbody tr, .article-body .cmp-card').forEach(function (el) {
      var isPre = el.matches('pre');
      if (el.closest('.rt-skip, .reading-tools, .syntax-card')) return;
      if (!isPre && el.closest('pre')) return;
      if (el.matches('li') && el.closest('.toc')) return;
      if (el.matches('.cmp-table tr, .cmp-card') && !el.getClientRects().length) return;  /* solo la versione visibile */
      var t;
      if (isPre) {
        t = 'Riquadro di codice: ' + el.getAttribute('aria-label') + '.';
      } else if (el.matches('.sigla')) {
        t = clean(el.querySelector('b').textContent) + ': ' + clean(el.querySelector('span').textContent);
      } else if (el.matches('.cmp-table tr')) {
        var hs = el.closest('table').tHead.rows[0].cells;
        t = Array.prototype.map.call(el.cells, function (c, i) { return i ? clean(hs[i].textContent) + ': ' + clean(c.textContent) : clean(c.textContent).replace(/\?$/, ''); }).join('. ') + '.';
      } else if (el.matches('.cmp-card')) {
        t = clean(el.querySelector('.cc-title').textContent) + '. ' + Array.prototype.map.call(el.querySelectorAll('dt'), function (dt) { return clean(dt.textContent).replace(/\?$/, '') + ': ' + clean(dt.nextElementSibling.textContent); }).join('. ') + '.';
      } else {
        t = clean(el.innerText || el.textContent);
        if (el.matches('.pc-title')) t = 'Percorso: ' + t + '.';
        if (el.matches('.path-col li')) t = 'Passo ' + (Array.prototype.indexOf.call(el.parentNode.children, el) + 1) + '. ' + t + '.';
        if (el.matches('summary')) t = t.replace(/\s*\+$/, '');
        if (el.matches('.steps-list > li')) t = 'Strategia ' + (Array.prototype.indexOf.call(el.parentNode.children, el) + 1) + '. ' + t;
        if (el.matches('.step-card > div')) t = 'Passo ' + el.parentNode.querySelector('.step-n').textContent + '. ' + t;
      }
      if (t) push(el, t);
    });
  }
  function itVoice() {
    var v = synth.getVoices().filter(function (x) { return /^it/i.test(x.lang); });
    return v.filter(function (x) { return /Google|Natural|Online|Neural/i.test(x.name); })[0] || v[0] || null;
  }
  /* la voce si sceglie prima di iniziare e non cambia durante la lettura */
  function pickVoice() { if (!playing) voice = itVoice() || voice; }
  pickVoice();
  if (synth.addEventListener) synth.addEventListener('voiceschanged', pickVoice);
  function mark(el) {
    if (current && current !== el) current.classList.remove('rt-reading');
    current = el;
    if (!el) return;
    var d = el.closest('details'); if (d && !d.open) d.open = true;
    el.classList.add('rt-reading');
    var r = el.getBoundingClientRect();
    if (r.top < 90 || r.bottom > window.innerHeight - 110) el.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' });
  }
  /* il lettore audio non deve finire sotto il banner dei cookie */
  function placePlayer() {
    var cb = document.getElementById('as-cookie-banner');
    var off = (cb && cb.parentNode && cb.style.opacity !== '0') ? cb.offsetHeight : 0;
    player.style.bottom = (16 + off) + 'px';
  }
  if (window.MutationObserver) new MutationObserver(placePlayer).observe(document.body, { childList: true });
  window.addEventListener('resize', placePlayer);
  function ui() {
    placePlayer();
    player.hidden = !(playing || idx > 0);
    player.querySelector('.rp-state').textContent = playing ? 'In ascolto' : 'In pausa';
    bPause.innerHTML = playing ? '<span aria-hidden="true">⏸</span> Pausa' : '<span aria-hidden="true">▶</span> Riprendi';
    bListen.innerHTML = playing ? '<span aria-hidden="true">⏸</span> Metti in pausa'
      : (idx > 0 ? '<span aria-hidden="true">▶</span> Riprendi l\'ascolto' : '<span aria-hidden="true">🔊</span> Ascolta l\'articolo');
  }
  function speakNext() {
    if (!playing) return;
    if (idx >= queue.length) { stop(); return; }
    var item = queue[idx], my = gen, done = false;
    mark(item.el);
    var u = new SpeechSynthesisUtterance(item.text);
    u.lang = 'it-IT'; u.rate = 0.95;
    if (voice) u.voice = voice;
    function next(ok) {
      if (done || my !== gen || !playing) return;
      done = true;
      fails = ok ? 0 : fails + 1;
      if (fails >= 3) { stop(); bListen.innerHTML = '<span aria-hidden="true">🔊</span> Sintesi vocale non disponibile'; return; }
      idx++; speakNext();
    }
    u.onend = function () { next(true); };
    u.onerror = function (e) { if (e.error === 'interrupted' || e.error === 'canceled') return; next(false); };
    synth.speak(u);
  }
  function play() { if (!queue.length || idx >= queue.length) { build(); idx = 0; } voice = voice || itVoice(); fails = 0; gen++; playing = true; ui(); speakNext(); }
  function pause() { gen++; playing = false; try { synth.cancel(); } catch (e) {} ui(); }
  function stop() {
    gen++; playing = false; try { synth.cancel(); } catch (e) {}
    idx = 0; mark(null);
    if (player.contains(document.activeElement)) bListen.focus();
    ui();
  }
  bListen.addEventListener('click', function () { playing ? pause() : play(); });
  bPause.addEventListener('click', function () { playing ? pause() : play(); });
  bStop.addEventListener('click', stop);
  window.addEventListener('pagehide', function () { if (playing) pause(); else { try { synth.cancel(); } catch (e) {} } });
  document.addEventListener('click', function (e) { if (e.target && /^as-(accept|reject)$/.test(e.target.id)) setTimeout(placePlayer, 350); });
})();
