// Prova degli strumenti di lettura facilitata di un articolo (sintesi vocale simulata, A+/A-, memoria delle scelte).
// Serve il sito in locale, es.: (cd <radice> && python3 -m http.server 8767 &)
// Uso: node _strumenti/test_lettura.js http://localhost:8767 articolo-XXX.html
const { chromium } = require('playwright'); const fr = require('./fontroute');
const [, , base, page] = process.argv;
const stub = () => { window.__spoken = []; let cur = null, t = null; const fire = (u, ev, x) => { const f = u['on' + ev]; if (f) f(Object.assign({ utterance: u }, x || {})); };
  window.SpeechSynthesisUtterance = function (text) { this.text = text; };
  Object.defineProperty(window, 'speechSynthesis', { value: { speak(u) { window.__spoken.push(u.text); cur = u; t = setTimeout(() => { cur = null; fire(u, 'end'); }, 5); },
    cancel() { if (cur) { clearTimeout(t); const u = cur; cur = null; fire(u, 'error', { error: 'interrupted' }); } }, getVoices() { return [{ lang: 'it-IT', name: 'Google italiano' }]; }, addEventListener() {} }, configurable: true }); };
(async () => {
  const exe = require('fs').existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {};
  const b = await chromium.launch(exe);
  for (const [w, tag] of [[1280, 'computer'], [390, 'telefono']]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 } }); await fr(ctx); await ctx.addInitScript(stub);
    const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto(`${base}/${page}`); const rej = await p.$('#as-reject'); if (rej) await rej.click(); await p.waitForTimeout(300);
    await p.click('#rt-listen'); await p.waitForFunction(() => document.getElementById('rt-player').hidden, null, { timeout: 90000 });
    const all = await p.evaluate(() => window.__spoken);
    const ov = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth);
    console.log(`[${tag}] frasi lette: ${all.length} | errori JS: ${errs.length} | frase più lunga: ${Math.max(...all.map(x => x.length))} | emoji o frecce lette: ${all.some(x => /→|↓|[\u{1F300}-\u{1FAFF}]/u.test(x))} | scorrimento orizzontale: ${ov}`);
    console.log('  prime frasi:', all.slice(0, 3).map(x => x.slice(0, 70)));
    if (tag === 'computer') {
      await p.click('#rt-bigger'); await p.click('#rt-bigger'); await p.click('#rt-font'); await p.reload();
      const mem = await p.evaluate(() => ({ scala: document.querySelector('.article-dsa').style.getPropertyValue('--rt-scale'), carattere: document.querySelector('.article-dsa').classList.contains('dsa-font'), tabellaASchede: document.querySelector('.article-dsa').classList.contains('rt-big') }));
      console.log('  dopo A+ A+ e carattere spento, ricaricando:', JSON.stringify(mem));
      await p.evaluate(() => localStorage.removeItem('as-dsa-lettura'));
    }
    await ctx.close();
  }
  await b.close();
})();
