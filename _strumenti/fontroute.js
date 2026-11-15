// Serve i caratteri di Google Fonts dalle copie locali (@fontsource) durante le prove nel browser.
const fs=require('fs'),path=require('path'); const F=path.join(__dirname,'node_modules/@fontsource');
const map={'Atkinson Hyperlegible':['atkinson-hyperlegible',[400,700]],'Inter':['inter',[400,500,600,700]],'JetBrains Mono':['jetbrains-mono',[400,600]],'Poppins':['poppins',[700,800]]};
let css='';for(const [fam,[dir,ws]] of Object.entries(map)) for(const w of ws) css+=`@font-face{font-family:'${fam}';font-weight:${w};font-style:normal;font-display:swap;src:url(https://localfont/${dir}/files/${dir}-latin-${w}-normal.woff2) format('woff2')}\n`;
module.exports=async function(ctx){
  await ctx.route(/fonts\.googleapis\.com/,r=>r.fulfill({contentType:'text/css',body:css}));
  await ctx.route(/localfont\//,r=>{const p=path.join(F,r.request().url().split('localfont/')[1]);r.fulfill({contentType:'font/woff2',body:fs.readFileSync(p)});});
  await ctx.route(/^https?:\/\/(?!localhost|localfont)/,r=>r.fulfill({body:''}));
};
