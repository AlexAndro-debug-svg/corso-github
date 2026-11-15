// Prova nel browser di tutte le pagine (o solo di alcune): testo fuori posto, errori JS, esempi vuoti,
// codice estraneo negli esempi, e clic su OGNI pulsante «Provalo tu». Le librerie dei CDN sono servite
// dalle copie in node_modules (nell'ambiente di lavoro i CDN sono bloccati).
// Uso: (cd <radice> && python3 -m http.server 8767 &)  poi
//      node _strumenti/audit.js http://localhost:8767 <radice> /tmp/esito.json [pagina1.html,pagina2.html]
const { chromium } = require('playwright');
const fs=require('fs'), path=require('path');
const NM=path.join(__dirname,'node_modules');
const [,, base, root, outFile, onlyPages] = process.argv;
const mime=p=>p.endsWith('.css')?'text/css':p.endsWith('.wasm')?'application/wasm':'application/javascript';
function localFor(u){
  let m;
  if(m=u.match(/cdnjs\.cloudflare\.com\/ajax\/libs\/codemirror\/5\.65\.16\/(.+)$/)){
    let p=m[1].replace('codemirror.min.js','lib/codemirror.js').replace('codemirror.min.css','lib/codemirror.css').replace(/\.min\.(js|css)$/,'.$1');
    return path.join(NM,'codemirror',p);}
  if(m=u.match(/cdnjs\.cloudflare\.com\/ajax\/libs\/prism\/1\.29\.0\/(.+)$/)){
    let p=m[1]==='prism.min.js'?'prism.js':m[1]; return path.join(NM,'prismjs',p);}
  if(m=u.match(/cdnjs\.cloudflare\.com\/ajax\/libs\/sql\.js\/1\.10\.3\/(.+)$/)) return path.join(NM,'sql.js','dist',m[1].replace('.min.js','.js'));
  if(m=u.match(/ajax\.googleapis\.com\/ajax\/libs\/angularjs\/1\.8\.3\/(angular[-a-z]*)\.min\.js/)) return path.join(NM,m[1],m[1]+'.min.js');
  if(m=u.match(/cdn\.jsdelivr\.net\/npm\/bootstrap@5\.3\.3\/(.+)$/)) return path.join(NM,'bootstrap',m[1]);
  if(/code\.jquery\.com\/jquery-3\.7\.1\.min\.js/.test(u)) return path.join(NM,'jquery','dist','jquery.min.js');
  if(/unpkg\.com\/vue@3\/dist\/vue\.global\.js/.test(u)) return path.join(NM,'vue','dist','vue.global.js');
  return null;
}
(async()=>{
  const b=await chromium.launch(fs.existsSync('/opt/pw-browsers/chromium')?{executablePath:'/opt/pw-browsers/chromium'}:{});
  const ctx=await b.newContext({viewport:{width:1280,height:900}});
  const missing=new Set();
  await ctx.route(/^https?:\/\/(?!localhost)/, async r=>{
    const u=r.request().url(); const lp=localFor(u);
    if(lp && fs.existsSync(lp)) return r.fulfill({status:200,contentType:mime(lp),body:fs.readFileSync(lp),headers:{'access-control-allow-origin':'*'}});
    if(/googletagmanager|fonts\.g|pyodide|tfjs|brain\.js|youtube|picsum|placeholder|example\.com|wikipedia/.test(u)) return r.fulfill({status:200,contentType:u.includes('.css')||u.includes('fonts.googleapis')?'text/css':'application/javascript',body:''});
    missing.add(u.split('?')[0]); return r.abort();
  });
  let pages=fs.readdirSync(root).filter(f=>f.endsWith('.html')).sort().filter(f=>!fs.readFileSync(path.join(root,f),'utf8').includes('http-equiv="refresh"'));
  if(onlyPages) pages=pages.filter(p=>onlyPages.split(',').includes(p));
  const report=[];
  for(const f of pages){
    const p=await ctx.newPage(); const errs=[];
    p.on('pageerror',e=>errs.push(String(e.message).split('\n')[0].slice(0,160)));
    p.on('dialog',d=>d.dismiss().catch(()=>{}));
    try{ await p.goto(base+'/'+f,{waitUntil:'load',timeout:30000}); }catch(e){ errs.push('LOAD '+e.message.slice(0,80)); }
    await p.waitForTimeout(300);
    const info=await p.evaluate(()=>{
      const stray=[...document.body.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim()).map(n=>n.textContent.trim().slice(0,90));
      document.querySelectorAll('.example').forEach(e=>[...e.childNodes].forEach(n=>{if(n.nodeType===3&&n.textContent.trim())stray.push('[in esempio] '+n.textContent.trim().slice(0,80));}));
      const exs=[...document.querySelectorAll('.example')].filter(e=>e.querySelector('.code'));
      const empty=exs.filter(e=>{const c=e.querySelector('.codeview code');return c&&!c.textContent.trim();}).length;
      const foreign=exs.filter(e=>/js\/search\.js|cookie-consent|googletagmanager/.test(e.querySelector('.code').textContent)).length;
      return {stray, examples:exs.length, empty, foreign, buttons:exs.filter(e=>e.querySelector('.btn-try')).length};
    });
    // click every "Provalo tu"
    let opened=0, failed=[], srcBad=0;
    const n=info.buttons;
    for(let i=0;i<n;i++){
      try{
        const ok=await p.evaluate(i=>{
          const exs=[...document.querySelectorAll('.example')].filter(e=>e.querySelector('.code')&&e.querySelector('.btn-try'));
          const ex=exs[i]; ex.querySelector('.btn-try').click();
          const ov=document.querySelector('.editor-overlay.open, #editor.open, .editor-overlay[style*="flex"]');
          const cmEl=document.querySelector('.editor-overlay .CodeMirror, #editor .CodeMirror');
          const val=cmEl&&cmEl.CodeMirror?cmEl.CodeMirror.getValue():'';
          return {open:!!ov, hasVal:val.trim().length>0};
        },i);
        await p.waitForTimeout(40);
        const sd=await p.evaluate(()=>{const fr=document.querySelector('.editor-overlay iframe, #editor iframe');return fr?(fr.srcdoc||''):''});
        if(/js\/search\.js|cookie-consent/.test(sd)) srcBad++;
        if(ok.open&&ok.hasVal) opened++; else failed.push(i);
        await p.keyboard.press('Escape');
        await p.evaluate(()=>{const c=document.querySelector('#ed-close,.ed-close');if(c&&document.querySelector('.editor-overlay.open'))c.click();});
      }catch(e){ failed.push(i+':'+e.message.slice(0,40)); }
    }
    report.push({page:f,...info,opened,failed:failed.slice(0,5),failedCount:failed.length,srcBad,errors:[...new Set(errs)].slice(0,4)});
    await p.close();
  }
  fs.writeFileSync(outFile,JSON.stringify({report,missing:[...missing]},null,1));
  const bad=report.filter(r=>r.stray.length||r.empty||r.foreign||r.failedCount||r.srcBad||r.errors.length);
  console.log('pagine:',report.length,'esempi:',report.reduce((a,r)=>a+r.examples,0),'Provalo tu aperti:',report.reduce((a,r)=>a+r.opened,0),'/',report.reduce((a,r)=>a+r.buttons,0));
  for(const r of bad) console.log('✗',r.page,JSON.stringify({stray:r.stray.slice(0,2),empty:r.empty,foreign:r.foreign,failed:r.failedCount,srcBad:r.srcBad,errors:r.errors}));
  console.log('CDN non serviti:',[...missing].slice(0,10));
  await b.close();
})();
