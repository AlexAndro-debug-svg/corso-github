(function(){
'use strict';

/* ── Indice di ricerca ─────────────────────────────────────────────── */
var INDEX = [
  /* Pagine principali */
  {t:'Home',              d:'Pagina principale del sito',                                     u:'index.html',           cat:'Sito'},
  {t:'Chi sono',          d:'Chi è Alessandro Simone, docente di informatica a Roma',         u:'chi-sono.html',        cat:'Sito'},
  {t:'Ripetizioni di Informatica', d:'Lezioni private in presenza a Roma, individuali o in gruppo', u:'ripetizioni.html', cat:'Sito'},
  {t:'Corsi di Informatica', d:'Tutti i corsi gratuiti in italiano disponibili sul sito',     u:'corsi.html',           cat:'Sito'},
  {t:'Blog & Guide',      d:'Articoli e guide di informatica e programmazione',               u:'blog.html',            cat:'Sito'},
  {t:'Contatti & FAQ',    d:'Come contattare Alessandro Simone e domande frequenti',          u:'contatti.html',        cat:'Sito'},
  {t:'Area Riservata Studenti', d:'Materiale didattico per gli studenti di Alessandro',       u:'esercizi.html',        cat:'Sito'},
  {t:'Prenota una lezione', d:'Prenota la tua prima lezione di ripetizione',                  u:'prenota.html',         cat:'Sito'},

  /* Corsi */
  {t:'Corso HTML',        d:'Corso HTML completo in italiano — struttura, tag, form, tabelle',         u:'corso-html.html',        cat:'Corso', tag:'web markup linguaggio'},
  {t:'Corso CSS',         d:'Corso CSS completo — selettori, flex, grid, animazioni, responsive',      u:'corso-css.html',         cat:'Corso', tag:'web stile design layout'},
  {t:'Corso JavaScript',  d:'Corso JavaScript — variabili, funzioni, DOM, async, API',                u:'corso-javascript.html',  cat:'Corso', tag:'web frontend scripting js'},
  {t:'Corso SQL',         d:'Corso SQL — SELECT, WHERE, JOIN, GROUP BY, subquery',                     u:'corso-sql.html',         cat:'Corso', tag:'database query'},
  {t:'Corso MySQL',       d:'Corso MySQL — database relazionali, trigger, stored procedure',           u:'corso-mysql.html',       cat:'Corso', tag:'database'},
  {t:'Corso Python',      d:'Corso Python — variabili, liste, funzioni, OOP, file',                   u:'corso-python.html',      cat:'Corso', tag:'programmazione scripting'},
  {t:'Corso Java',        d:'Corso Java — OOP, classi, interfacce, eccezioni, generics',              u:'corso-java.html',        cat:'Corso', tag:'programmazione OOP'},
  {t:'Corso PHP',         d:'Corso PHP — sintassi, form, sessioni, MySQL, MVC',                       u:'corso-php.html',         cat:'Corso', tag:'web backend programmazione'},
  {t:'Corso C',           d:'Corso C — puntatori, array, struct, memoria, I/O',                       u:'corso-c.html',           cat:'Corso', tag:'programmazione sistemi'},
  {t:'Corso C++',         d:'Corso C++ — OOP, template, STL, RAII, polimorfismo',                     u:'corso-cpp.html',         cat:'Corso', tag:'programmazione OOP sistemi'},
  {t:'Corso C#',          d:'Corso C# — .NET, LINQ, async/await, WPF, Unity',                         u:'corso-csharp.html',      cat:'Corso', tag:'programmazione .NET'},
  {t:'Corso React',       d:'Corso React — componenti, hook, props, state, JSX, router',               u:'corso-react.html',       cat:'Corso', tag:'web frontend libreria'},
  {t:'Corso TypeScript',  d:'Corso TypeScript — tipi, generics, decorators, interfacce',               u:'corso-typescript.html',  cat:'Corso', tag:'web frontend javascript tipizzato'},
  {t:'Corso Node.js',     d:'Corso Node.js — backend, Express, NPM, API REST, autenticazione',        u:'corso-nodejs.html',      cat:'Corso', tag:'backend javascript server'},
  {t:'Corso Git e GitHub',d:'Corso Git — versionamento, branch, merge, pull request, GitHub',         u:'corso-git.html',         cat:'Corso', tag:'strumenti versioning'},
  {t:'Corso Data Science',d:'Corso Data Science — Pandas, statistica, regressione, Python',           u:'corso-datascience.html', cat:'Corso', tag:'dati analisi python'},
  {t:'Corso Bootstrap',   d:'Corso Bootstrap 5 — griglia, componenti, form, modal, navbar',           u:'corso-bootstrap.html',   cat:'Corso', tag:'web css framework frontend'},
  {t:'Corso Go',          d:'Corso Go (Golang) — goroutine, canali, slice, map, interfacce',          u:'corso-go.html',          cat:'Corso', tag:'programmazione backend golang'},
  {t:'Corso Kotlin',      d:'Corso Kotlin — sintassi, OOP, extension, coroutines, Android',           u:'corso-kotlin.html',      cat:'Corso', tag:'programmazione mobile Android'},
  {t:'Corso jQuery',      d:'Corso jQuery — selettori, eventi, animazioni, AJAX, plugin',             u:'corso-jquery.html',      cat:'Corso', tag:'web frontend javascript'},
  {t:'Corso Django',      d:'Corso Django — models, views, template, ORM, admin, deploy',             u:'corso-django.html',      cat:'Corso', tag:'web backend python framework'},
  {t:'Corso Vue.js',      d:'Corso Vue.js — direttive, componenti, props, Composition API, Pinia',    u:'corso-vue.html',         cat:'Corso', tag:'web frontend framework'},
  {t:'Corso Angular',     d:'Corso Angular — componenti, direttive, servizi, RxJS, Signals',          u:'corso-angular.html',     cat:'Corso', tag:'web frontend framework TypeScript'},
  {t:'Corso MongoDB',     d:'Corso MongoDB — NoSQL, documenti, Atlas, aggregazioni, Node.js',         u:'corso-mongodb.html',     cat:'Corso', tag:'database NoSQL'},
  {t:'Corso PostgreSQL',  d:'Corso PostgreSQL — SQL avanzato, JOIN, transazioni, pgAdmin',            u:'corso-postgresql.html',  cat:'Corso', tag:'database SQL'},
  {t:'Corso NumPy',       d:'Corso NumPy — array, broadcasting, random, ufunc, linear algebra',      u:'corso-numpy.html',       cat:'Corso', tag:'python dati scientifico'},
  {t:'Corso Sass / SCSS', d:'Corso Sass — variabili, mixin, nesting, extend, funzioni',               u:'corso-sass.html',        cat:'Corso', tag:'web css preprocessore'},
  {t:'Corso Pandas',      d:'Corso Pandas — DataFrame, pulizia dati, groupby, merge, visualizzazione',u:'corso-pandas.html',      cat:'Corso', tag:'python dati analisi'},
  {t:'Corso SciPy',       d:'Corso SciPy — ottimizzazione, statistica, grafi, interpolazione',       u:'corso-scipy.html',       cat:'Corso', tag:'python scientifico matematica'},
  {t:'Corso DSA',         d:'Corso Strutture Dati e Algoritmi — liste, alberi, grafi, Big O, sorting',u:'corso-dsa.html',         cat:'Corso', tag:'algoritmi programmazione'},
  {t:'Corso Rust',        d:'Corso Rust — ownership, borrowing, lifetimes, struct, enum, wasm',       u:'corso-rust.html',        cat:'Corso', tag:'programmazione sistemi'},
  {t:'Corso Swift',       d:'Corso Swift — Optional, closures, struct, protocolli, SwiftUI',          u:'corso-swift.html',       cat:'Corso', tag:'programmazione mobile iOS Apple'},
  {t:'Corso Bash',        d:'Corso Bash — shell, scripting, automazione, pipe, cron',                 u:'corso-bash.html',        cat:'Corso', tag:'linux shell sistemi automazione'},
  {t:'Corso XML',         d:'Corso XML — sintassi, namespace, XPath, XSLT, DTD, XSD',                u:'corso-xml.html',         cat:'Corso', tag:'dati markup linguaggio'},
  {t:'Corso AWS',         d:'Corso AWS — cloud computing, EC2, S3, Lambda, IAM, sicurezza',          u:'corso-aws.html',         cat:'Corso', tag:'cloud Amazon'},
  {t:'Corso Programmazione', d:'Corso Introduzione alla Programmazione — variabili, cicli, funzioni, logica',u:'corso-programming.html', cat:'Corso', tag:'programmazione base'},
  {t:'Corso Excel',       d:'Corso Excel — formule, funzioni, grafici, tabelle pivot, VLOOKUP',       u:'corso-excel.html',       cat:'Corso', tag:'office fogli calcolo'},
  {t:'Corso AI e Machine Learning', d:'Corso AI — reti neurali, training, TensorFlow.js, classificatori',u:'corso-ai.html',      cat:'Corso', tag:'intelligenza artificiale ML'},
  {t:'Corso AngularJS',   d:'Corso AngularJS — direttive, controller, servizi, routing, $scope',      u:'corso-angularjs.html',   cat:'Corso', tag:'web frontend framework JavaScript'},
  {t:'Corso W3.CSS',      d:'Corso W3.CSS — framework CSS lightweight, layout, componenti',           u:'corso-w3css.html',       cat:'Corso', tag:'web css framework'},
  {t:'Corso Cybersecurity', d:'Corso Cybersecurity — sicurezza informatica, crittografia, attacchi, difese',u:'corso-cybersecurity.html', cat:'Corso', tag:'sicurezza hacking rete'},
  {t:'Corso Cisco Packet Tracer', d:'Corso Packet Tracer — reti, router, switch, protocolli, VLAN',   u:'corso-packet-tracer.html',cat:'Corso', tag:'reti Cisco networking'},

  /* Articoli */
  {t:'Algoritmi e diagrammi di flusso', d:'Cos\'è un algoritmo e come si rappresenta con un flowchart', u:'articolo-algoritmi-flowchart.html', cat:'Articolo', tag:'programmazione logica'},
  {t:'Come usare ChatGPT per studiare', d:'Guida su come usare ChatGPT per studiare senza barare',    u:'articolo-chatgpt-studiare.html',    cat:'Articolo', tag:'AI intelligenza artificiale studio'},
  {t:'Il ciclo for in Python',          d:'Come funziona il ciclo for in Python con esempi pratici',  u:'articolo-ciclo-for.html',           cat:'Articolo', tag:'python programmazione'},
  {t:'Le condizioni if in Python',      d:'Le istruzioni if, elif ed else in Python con esempi',      u:'articolo-condizioni-if.html',       cat:'Articolo', tag:'python programmazione'},
  {t:'La crittografia spiegata semplice', d:'Cos\'è la crittografia e a cosa serve nella sicurezza', u:'articolo-crittografia.html',        cat:'Articolo', tag:'sicurezza cybersecurity'},
  {t:'Debug: trovare e correggere i bug', d:'Come trovare e correggere gli errori nel codice',        u:'articolo-debug.html',               cat:'Articolo', tag:'programmazione errori'},
  {t:'Le funzioni in Python',           d:'Come definire e usare le funzioni in Python',              u:'articolo-funzioni-python.html',     cat:'Articolo', tag:'python programmazione'},
  {t:'HTML, CSS e JavaScript: differenze', d:'A cosa servono HTML, CSS e JavaScript e come si usano insieme', u:'articolo-html-css-js.html', cat:'Articolo', tag:'web html css javascript'},
  {t:'Gli indirizzi IP spiegati',       d:'Cosa sono gli indirizzi IPv4, le classi e le subnet',      u:'articolo-indirizzi-ip.html',        cat:'Articolo', tag:'reti networking'},
  {t:'Le JOIN in SQL',                  d:'INNER JOIN, LEFT JOIN, RIGHT JOIN in SQL con esempi',       u:'articolo-join-sql.html',            cat:'Articolo', tag:'database SQL'},
  {t:'Le liste in Python',              d:'Guida completa alle liste in Python per principianti',      u:'articolo-liste-python.html',        cat:'Articolo', tag:'python programmazione'},
  {t:'Il modello Entità-Relazione (E-R)', d:'Come si crea uno schema E-R per un database',            u:'articolo-modello-er.html',          cat:'Articolo', tag:'database progettazione'},
  {t:'Il modello OSI: i 7 livelli',     d:'I 7 livelli del modello OSI spiegati con esempi',          u:'articolo-modello-osi.html',         cat:'Articolo', tag:'reti networking'},
  {t:'Cosa fa un programmatore',        d:'Sbocchi lavorativi e percorsi dopo l\'ITIS informatica',   u:'articolo-programmatore.html',       cat:'Articolo', tag:'carriera lavoro'},
  {t:'La ricorsione in Python',         d:'La ricorsione spiegata senza paura con esempi Python',     u:'articolo-ricorsione.html',          cat:'Articolo', tag:'python programmazione algoritmi'},
  {t:'Il sistema binario',              d:'Il sistema binario spiegato semplice con conversioni',      u:'articolo-sistema-binario.html',     cat:'Articolo', tag:'basi informatica'},
  {t:'I sistemi operativi',             d:'Cos\'è un sistema operativo e come funziona',               u:'articolo-sistema-operativo.html',   cat:'Articolo', tag:'SO informatica base'},
  {t:'SQL per principianti: SELECT',    d:'SELECT, WHERE e ORDER BY spiegati con esempi pratici',     u:'articolo-sql-select.html',          cat:'Articolo', tag:'database SQL'},
  {t:'Il protocollo TCP/IP',            d:'Come funziona Internet: il protocollo TCP/IP spiegato',    u:'articolo-tcp-ip.html',              cat:'Articolo', tag:'reti networking internet'},
  {t:'Variabili in Python',             d:'Variabili e tipi di dato in Python: la guida base',        u:'articolo-variabili-python.html',    cat:'Articolo', tag:'python programmazione'},
];

/* ── Utilità ──────────────────────────────────────────────────────── */
function normalize(s){ return (s||'').toLowerCase().replace(/[àáâ]/g,'a').replace(/[èéê]/g,'e').replace(/[ìíî]/g,'i').replace(/[òóô]/g,'o').replace(/[ùúû]/g,'u'); }

function score(item, q){
  var words = q.trim().split(/\s+/).filter(Boolean);
  if(!words.length) return 0;
  var text = normalize(item.t+' '+item.d+' '+(item.tag||'')+' '+item.cat);
  var pts = 0;
  words.forEach(function(w){
    if(normalize(item.t).indexOf(w)===0) pts+=10;
    else if(normalize(item.t).indexOf(w)>-1) pts+=6;
    if(normalize(item.d).indexOf(w)>-1) pts+=3;
    if(normalize(item.tag||'').indexOf(w)>-1) pts+=2;
    if(normalize(item.cat).indexOf(w)>-1) pts+=1;
  });
  // tutti i termini devono dare almeno un hit
  var hits = words.filter(function(w){ return text.indexOf(w)>-1; });
  return hits.length===words.length ? pts : 0;
}

function catIcon(cat){
  return cat==='Corso' ? '📚' : cat==='Articolo' ? '📝' : '🏠';
}

/* ── CSS ──────────────────────────────────────────────────────────── */
var css = `
#srch-btn{
  display:inline-flex;align-items:center;gap:.35rem;
  background:none;border:1.5px solid #e2e8f0;border-radius:8px;
  padding:.38rem .85rem;font-size:.9rem;font-weight:500;color:#64748b;
  cursor:pointer;transition:border-color .2s,color .2s,background .2s;
  white-space:nowrap;
}
#srch-btn:hover{border-color:#4f46e5;color:#4f46e5;background:#eef2ff;}
#srch-btn svg{flex-shrink:0;}
@media(max-width:860px){
  #srch-btn .srch-label{display:none;}
  #srch-btn{border:none;padding:.4rem;background:none;}
  #srch-btn:hover{background:#eef2ff;}
}
#srch-overlay{
  display:none;position:fixed;inset:0;z-index:9999;
  background:rgba(15,23,42,.55);backdrop-filter:blur(4px);
  align-items:flex-start;justify-content:center;padding:5.5rem 1rem 1rem;
}
#srch-overlay.open{display:flex;}
#srch-box{
  background:#fff;border-radius:16px;width:100%;max-width:640px;
  box-shadow:0 24px 64px rgba(15,23,42,.22);overflow:hidden;
}
#srch-input-wrap{
  display:flex;align-items:center;gap:.7rem;
  padding:.9rem 1.1rem;border-bottom:1.5px solid #e2e8f0;
}
#srch-input-wrap svg{color:#94a3b8;flex-shrink:0;}
#srch-input{
  flex:1;border:none;outline:none;font-size:1.08rem;
  font-family:inherit;color:#1e293b;background:transparent;
}
#srch-input::placeholder{color:#94a3b8;}
#srch-close{
  background:none;border:none;cursor:pointer;color:#94a3b8;
  font-size:1.3rem;line-height:1;padding:.1rem .2rem;border-radius:6px;
}
#srch-close:hover{color:#1e293b;background:#f1f5f9;}
#srch-results{max-height:62vh;overflow-y:auto;}
.srch-hint{
  padding:2.5rem 1.5rem;text-align:center;
  color:#94a3b8;font-size:.95rem;
}
.srch-no{padding:2rem 1.5rem;text-align:center;color:#94a3b8;}
.srch-group{padding:.55rem 1.2rem .2rem;font-size:.72rem;font-weight:700;
  letter-spacing:1.2px;text-transform:uppercase;color:#94a3b8;}
.srch-item{
  display:flex;align-items:center;gap:.9rem;
  padding:.7rem 1.2rem;cursor:pointer;transition:background .15s;
  text-decoration:none;color:inherit;border-radius:0;
}
.srch-item:hover,.srch-item.active{background:#eef2ff;}
.srch-item-ico{font-size:1.15rem;flex-shrink:0;width:1.6rem;text-align:center;}
.srch-item-body{flex:1;min-width:0;}
.srch-item-title{font-weight:600;font-size:.97rem;color:#1e293b;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.srch-item-desc{font-size:.82rem;color:#64748b;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.srch-item-badge{
  font-size:.72rem;font-weight:700;padding:.2rem .55rem;border-radius:99px;
  white-space:nowrap;flex-shrink:0;
}
.srch-badge-Corso{background:#eef2ff;color:#4f46e5;}
.srch-badge-Articolo{background:#f0fdfa;color:#0d9488;}
.srch-badge-Sito{background:#fff7ed;color:#d97706;}
#srch-footer{
  padding:.65rem 1.2rem;border-top:1px solid #e2e8f0;
  display:flex;gap:1.2rem;align-items:center;
  font-size:.78rem;color:#94a3b8;flex-wrap:wrap;
}
.srch-key{
  display:inline-flex;align-items:center;justify-content:center;
  background:#f1f5f9;border:1px solid #e2e8f0;border-radius:5px;
  padding:.05rem .45rem;font-size:.78rem;font-weight:600;color:#475569;min-width:1.4rem;
}
`;

/* ── HTML overlay ─────────────────────────────────────────────────── */
var overlayHTML = '<div id="srch-overlay" role="dialog" aria-modal="true" aria-label="Cerca nel sito">'
  +'<div id="srch-box">'
  +'<div id="srch-input-wrap">'
  +'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'
  +'<input id="srch-input" type="search" placeholder="Cerca corsi, articoli, pagine…" autocomplete="off" spellcheck="false">'
  +'<button id="srch-close" aria-label="Chiudi">✕</button>'
  +'</div>'
  +'<div id="srch-results"><p class="srch-hint">Digita per cercare nel sito…</p></div>'
  +'<div id="srch-footer">'
  +'<span><span class="srch-key">↑</span><span class="srch-key">↓</span> naviga</span>'
  +'<span><span class="srch-key">↵</span> apri</span>'
  +'<span><span class="srch-key">Esc</span> chiudi</span>'
  +'</div>'
  +'</div></div>';

/* ── Bottone navbar ────────────────────────────────────────────────── */
var btnHTML = '<button id="srch-btn" aria-label="Cerca nel sito">'
  +'<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'
  +'<span class="srch-label">Cerca</span></button>';

/* ── Init ─────────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', function(){
  // Inietta CSS
  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  // Inietta overlay
  var tmp = document.createElement('div');
  tmp.innerHTML = overlayHTML;
  document.body.appendChild(tmp.firstElementChild);

  // Inietta bottone nella navbar prima del nav-toggle
  var navInner = document.querySelector('.nav-inner');
  var navToggle = navInner && navInner.querySelector('.nav-toggle');
  if(navInner){
    var btnWrap = document.createElement('div');
    btnWrap.innerHTML = btnHTML;
    var btn = btnWrap.firstElementChild;
    if(navToggle) navInner.insertBefore(btn, navToggle);
    else navInner.appendChild(btn);
  }

  var overlay  = document.getElementById('srch-overlay');
  var input    = document.getElementById('srch-input');
  var results  = document.getElementById('srch-results');
  var closeBtn = document.getElementById('srch-close');
  var searchBtn= document.getElementById('srch-btn');

  var activeIdx = -1;

  function open(){
    overlay.classList.add('open');
    input.value='';
    results.innerHTML='<p class="srch-hint">Digita per cercare nel sito…</p>';
    activeIdx=-1;
    setTimeout(function(){ input.focus(); },50);
    document.body.style.overflow='hidden';
  }
  function close(){
    overlay.classList.remove('open');
    document.body.style.overflow='';
    activeIdx=-1;
  }

  searchBtn && searchBtn.addEventListener('click', open);
  closeBtn.addEventListener('click', close);
  overlay.addEventListener('click', function(e){ if(e.target===overlay) close(); });

  // Ctrl+K / Cmd+K
  document.addEventListener('keydown', function(e){
    if((e.ctrlKey||e.metaKey) && e.key==='k'){ e.preventDefault(); open(); return; }
    if(!overlay.classList.contains('open')) return;
    if(e.key==='Escape'){ close(); return; }
    var items = results.querySelectorAll('.srch-item');
    if(e.key==='ArrowDown'){
      e.preventDefault();
      activeIdx=Math.min(activeIdx+1,items.length-1);
      setActive(items);
    } else if(e.key==='ArrowUp'){
      e.preventDefault();
      activeIdx=Math.max(activeIdx-1,0);
      setActive(items);
    } else if(e.key==='Enter'){
      if(activeIdx>=0 && items[activeIdx]) items[activeIdx].click();
    }
  });

  function setActive(items){
    items.forEach(function(el,i){ el.classList.toggle('active',i===activeIdx); });
    if(items[activeIdx]) items[activeIdx].scrollIntoView({block:'nearest'});
  }

  /* ── Logica di ricerca ─────────────────────────────────────────── */
  // Determina il prefisso relativo al file corrente
  // Tutti i file HTML sono nella root; js/search.js è in /js/
  // Le pagine sono nella stessa directory → nessun prefisso
  var base = '';
  // Se la pagina è in una sottocartella, aggiusta il base
  var path = window.location.pathname;
  var depth = path.replace(/\/[^/]*$/, '').split('/').filter(Boolean).length;
  // Su GitHub Pages il sito è in /corso-github/, tutti i .html sono lì
  // quindi nessun aggiustamento necessario

  input.addEventListener('input', function(){
    var q = normalize(input.value);
    activeIdx = -1;
    if(!q){
      results.innerHTML='<p class="srch-hint">Digita per cercare nel sito…</p>';
      return;
    }
    var scored = INDEX.map(function(item){ return {item:item, s:score(item,q)}; })
      .filter(function(x){ return x.s>0; })
      .sort(function(a,b){ return b.s-a.s; });

    if(!scored.length){
      results.innerHTML='<p class="srch-no">Nessun risultato per "<strong>'+escHtml(input.value)+'</strong>"</p>';
      return;
    }

    // Raggruppa per categoria
    var groups = {};
    var order = ['Sito','Corso','Articolo'];
    scored.forEach(function(x){
      var c = x.item.cat;
      if(!groups[c]) groups[c]=[];
      groups[c].push(x.item);
    });

    var html='';
    order.forEach(function(cat){
      if(!groups[cat]) return;
      html+='<div class="srch-group">'+catIcon(cat)+' '+cat+'</div>';
      groups[cat].slice(0,12).forEach(function(item){
        var url = base + item.u;
        html+='<a class="srch-item" href="'+url+'">'
          +'<span class="srch-item-ico">'+catIcon(item.cat)+'</span>'
          +'<span class="srch-item-body">'
          +'<span class="srch-item-title">'+escHtml(item.t)+'</span>'
          +'<span class="srch-item-desc">'+escHtml(item.d)+'</span>'
          +'</span>'
          +'<span class="srch-item-badge srch-badge-'+item.cat+'">'+item.cat+'</span>'
          +'</a>';
      });
    });
    results.innerHTML = html;

    // Click su risultato → chiudi overlay
    results.querySelectorAll('.srch-item').forEach(function(el){
      el.addEventListener('click', function(){ close(); });
    });
  });

  function escHtml(s){
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }
});

})();
