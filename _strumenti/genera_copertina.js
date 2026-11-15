// Genera la copertina 1200x630 (JPEG) di un articolo da un modello HTML in _strumenti/copertine/.
// Uso, dalla radice del sito: node _strumenti/genera_copertina.js _strumenti/copertine/copertina-XXX.html articolo-XXX.jpg
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), os = require('os');
const [, , tpl, out] = process.argv;
if (!tpl || !out) { console.error('Uso: node genera_copertina.js <modello.html> <uscita.jpg>'); process.exit(1); }
const F = (pkg, file) => 'file://' + path.join(__dirname, 'node_modules', '@fontsource', pkg, 'files', file);
const fonts = [
  `@font-face{font-family:Atk;src:url(${F('atkinson-hyperlegible', 'atkinson-hyperlegible-latin-400-normal.woff2')});font-weight:400}`,
  `@font-face{font-family:Atk;src:url(${F('atkinson-hyperlegible', 'atkinson-hyperlegible-latin-700-normal.woff2')});font-weight:700}`,
  `@font-face{font-family:JBM;src:url(${F('jetbrains-mono', 'jetbrains-mono-latin-600-normal.woff2')});font-weight:600}`,
].join('\n');
const html = fs.readFileSync(tpl, 'utf8').replace('/*FONTS*/', fonts);
const tmp = path.join(os.tmpdir(), `copertina-${process.pid}.html`);
fs.writeFileSync(tmp, html);
(async () => {
  const exe = fs.existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {};
  const b = await chromium.launch(exe);
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await p.goto('file://' + tmp); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const loaded = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').length);
  await p.screenshot({ path: out, type: 'jpeg', quality: 86 });
  await b.close(); fs.unlinkSync(tmp);
  console.log('copertina scritta:', out, '| caratteri caricati:', loaded);
})();
