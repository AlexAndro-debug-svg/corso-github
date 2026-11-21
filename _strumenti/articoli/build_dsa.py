#!/usr/bin/env python3
"""Articolo: Informatica e DSA."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

TITLE = "Informatica e DSA: strategie e strumenti compensativi per studiare programmazione"
SEO_TITLE = "Informatica e DSA: strumenti compensativi per programmare — AlessandroSimone.it"
DESC = "Hai un DSA, come la dislessia, e studi informatica? Strategie pratiche, strumenti compensativi e idee per il PDP: impara a programmare con meno fatica."
URL = "https://alessandrosimone.it/articolo-informatica-dsa.html"
IMG = "https://alessandrosimone.it/articolo-informatica-dsa.jpg"

# ------------------------------------------------------------------ FIGURE
FIG_CARATTERI = '''
    <figure class="dsa-figure" aria-labelledby="cap-car">
      <div class="glyph-compare" role="img" aria-label="Confronto tra due tipi di carattere. In un tipo di carattere comune la i maiuscola e la elle minuscola sono quasi uguali, la o maiuscola si confonde con lo zero e le lettere r e n vicine sembrano una emme. In un tipo di carattere pensato per il codice ogni simbolo ha una forma diversa.">
        <div class="gc-row">
          <div class="gc-title">❌ Carattere comune</div>
          <div class="gc-cells gc-common">
            <div><span>I l 1</span><small>i maiuscola · elle · uno</small></div>
            <div><span>O 0</span><small>o maiuscola · zero</small></div>
            <div><span>rn m</span><small>r + n · emme</small></div>
          </div>
        </div>
        <div class="gc-row">
          <div class="gc-title">✅ Carattere per il codice</div>
          <div class="gc-cells gc-code">
            <div><span>I l 1</span><small>i maiuscola · elle · uno</small></div>
            <div><span>O 0</span><small>o maiuscola · zero</small></div>
            <div><span>rn m</span><small>r + n · emme</small></div>
          </div>
        </div>
      </div>
      <figcaption id="cap-car">Sopra, un tipo di carattere comune: la i maiuscola e la elle minuscola sono quasi identiche, e «rn» sembra una «m». Sotto, un tipo di carattere pensato per il codice: ogni simbolo ha una forma diversa.</figcaption>
    </figure>'''

SALUTO = '''# Saluto e conto fino a 3
nome = input("Come ti chiami? ")
print("Ciao", nome)
for numero in range(1, 4):
    print(numero)'''

FIG_COLORI = f'''
    <figure class="dsa-figure" aria-labelledby="cap-col">
      <div class="two-col">
        <div><div class="panel-title">Senza colori</div>{plain(SALUTO)}</div>
        <div><div class="panel-title">Con i colori dell'editor</div>{code(SALUTO, numbers=False)}</div>
      </div>
      <figcaption id="cap-col">Lo stesso codice senza colori e con i colori di un editor. I colori aiutano a distinguere a colpo d'occhio comandi, testi e numeri.</figcaption>
    </figure>'''

FIG_FLUSSO = '''
    <figure class="dsa-figure" aria-labelledby="cap-flu">
      <svg viewBox="0 0 460 560" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="flu-t flu-d" class="dsa-svg" style="max-width:440px">
        <title id="flu-t">Diagramma di flusso: il voto è sufficiente?</title>
        <desc id="flu-d">Inizio. Leggi il voto. Il voto è maggiore o uguale a 6? Se sì, scrivi Sufficiente. Se no, scrivi Insufficiente. Fine.</desc>
        <defs><marker id="fa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#4f46e5"/></marker></defs>
        <g font-family="Atkinson Hyperlegible, Verdana, Arial, sans-serif" font-size="22" font-weight="700" text-anchor="middle">
          <ellipse cx="230" cy="40" rx="80" ry="28" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5"/>
          <text x="230" y="46" fill="#14532d">Inizio</text>
          <line x1="230" y1="68" x2="230" y2="102" stroke="#4f46e5" stroke-width="2.5" marker-end="url(#fa)"/>
          <polygon points="135,106 345,106 325,162 115,162" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
          <text x="230" y="140" fill="#0c4a6e">Leggi il voto</text>
          <line x1="230" y1="162" x2="230" y2="196" stroke="#4f46e5" stroke-width="2.5" marker-end="url(#fa)"/>
          <polygon points="230,200 340,265 230,330 120,265" fill="#eef2ff" stroke="#4f46e5" stroke-width="2.5"/>
          <text x="230" y="262" fill="#1e1b4b">voto ≥ 6?</text>
          <text x="230" y="284" fill="#1e1b4b" font-size="17" font-weight="400">(è sufficiente?)</text>
          <polyline points="120,265 70,265 70,372" fill="none" stroke="#4f46e5" stroke-width="2.5" marker-end="url(#fa)"/>
          <text x="92" y="254" fill="#15803d">sì</text>
          <polyline points="340,265 390,265 390,372" fill="none" stroke="#4f46e5" stroke-width="2.5" marker-end="url(#fa)"/>
          <text x="370" y="254" fill="#b91c1c">no</text>
          <polygon points="18,376 186,376 166,436 0,436" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5" transform="translate(4,0)"/>
          <text x="95" y="401" fill="#0c4a6e" font-size="20">Scrivi</text>
          <text x="95" y="425" fill="#0c4a6e" font-size="20">Sufficiente</text>
          <polygon points="294,376 456,376 436,436 274,436" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
          <text x="365" y="401" fill="#0c4a6e" font-size="20">Scrivi</text>
          <text x="365" y="425" fill="#0c4a6e" font-size="20">Insufficiente</text>
          <polyline points="95,436 95,470 230,470 230,492" fill="none" stroke="#4f46e5" stroke-width="2.5" marker-end="url(#fa)"/>
          <polyline points="365,436 365,470 230,470" fill="none" stroke="#4f46e5" stroke-width="2.5"/>
          <ellipse cx="230" cy="522" rx="80" ry="28" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
          <text x="230" y="528" fill="#7f1d1d">Fine</text>
        </g>
      </svg>
      <figcaption id="cap-flu">Il diagramma di flusso dell'esercizio: ovali per inizio e fine, parallelogrammi per leggere e scrivere i dati, rombo per la decisione.</figcaption>
    </figure>'''

FIG_SCHEDA = f'''
    <figure class="dsa-figure" aria-labelledby="cap-sch">
      <div class="syntax-card">
        <div class="sc-head">🗂️ La mia scheda della sintassi Python</div>
        <div class="sc-grid">
          <div class="sc-item"><div class="sc-t">🖨️ Scrivere sullo schermo</div>{mini('print("Ciao")')}</div>
          <div class="sc-item"><div class="sc-t">⌨️ Chiedere un dato</div>{mini('nome = input("Nome? ")' + chr(10) + 'voto = int(input("Voto? "))')}</div>
          <div class="sc-item"><div class="sc-t">🔀 Decidere</div>{mini('if voto >= 6:' + chr(10) + '    print("Bene")' + chr(10) + 'else:' + chr(10) + '    print("Ripassa")')}</div>
          <div class="sc-item"><div class="sc-t">🔁 Ripetere un certo numero di volte</div>{mini('for i in range(5):' + chr(10) + '    print(i)')}</div>
          <div class="sc-item"><div class="sc-t">🔄 Ripetere finché…</div>{mini('while voto < 6:' + chr(10) + '    voto = voto + 1')}</div>
          <div class="sc-item"><div class="sc-t">🧱 Creare una funzione</div>{mini('def saluta(nome):' + chr(10) + '    print("Ciao", nome)')}</div>
        </div>
        <div class="sc-foot">⚠️ Ricorda: le righe che iniziano con <strong>if</strong>, <strong>else</strong>, <strong>for</strong>, <strong>while</strong> e <strong>def</strong> finiscono con i due punti (<strong>:</strong>). La riga sotto va spostata a destra di 4 spazi: l'editor lo fa da solo quando premi Invio.</div>
      </div>
      <figcaption id="cap-sch">Un esempio di scheda della sintassi Python. Puoi crearne una tua, con i colori e gli esempi che ti aiutano di più.</figcaption>
    </figure>'''

FITTO = '''a=[6,7,5,8]
s=0
for x in a:s=s+x
print("Media:",s/len(a))'''

ARIOSO = '''# Calcolo la media dei voti
voti = [6, 7, 5, 8]
somma = 0

for voto in voti:
    somma = somma + voto

media = somma / len(voti)
print("Media:", media)'''

FIG_ARIOSO = f'''
    <figure class="dsa-figure" aria-labelledby="cap-ari">
      <div class="two-col">
        <div><div class="panel-title">❌ Codice fitto</div>{code(FITTO, numbers=False)}</div>
        <div><div class="panel-title">✅ Codice arioso</div>{code(ARIOSO, numbers=False)}</div>
      </div>
      <figcaption id="cap-ari">I due programmi calcolano la stessa media. Il secondo, «Codice arioso», usa nomi chiari, righe vuote e un commento: si legge molto meglio.</figcaption>
    </figure>'''

MAP_NODES = [
    (110, 70, "🖥️", "Editor", "con i colori", "#eef2ff", "#4f46e5"),
    (360, 40, "🔤", "Carattere", "leggibile", "#f0fdfa", "#0d9488"),
    (610, 70, "📐", "Diagrammi", "e mappe", "#fff7ed", "#ea580c"),
    (640, 230, "🔊", "Sintesi", "vocale", "#fdf2f8", "#db2777"),
    (560, 375, "🗂️", "Scheda della", "sintassi", "#ecfeff", "#0891b2"),
    (160, 375, "🤖", "AI come", "tutor", "#f5f3ff", "#7c3aed"),
    (80, 230, "📝", "PDP", "su misura", "#fefce8", "#ca8a04"),
]
def mindmap():
    parts = []
    for x, y, ico, a, b, fill, stroke in MAP_NODES:
        parts.append(f'<line x1="360" y1="215" x2="{x}" y2="{y}" stroke="{stroke}" stroke-width="3" stroke-linecap="round" opacity=".55"/>')
    parts.append('<circle cx="360" cy="215" r="82" fill="#4f46e5"/>')
    parts.append('<text x="360" y="200" fill="#fff" font-size="21">Informatica</text>')
    parts.append('<text x="360" y="226" fill="#fff" font-size="21">con un DSA</text>')
    parts.append('<text x="360" y="252" fill="#e0e7ff" font-size="15" font-weight="400">i tuoi strumenti</text>')
    for x, y, ico, a, b, fill, stroke in MAP_NODES:
        parts.append(f'<rect x="{x-78}" y="{y-34}" width="156" height="68" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
        parts.append(f'<text x="{x}" y="{y-6}" fill="#1f2937" font-size="18">{ico} {a}</text>')
        parts.append(f'<text x="{x}" y="{y+18}" fill="#1f2937" font-size="18">{b}</text>')
    return '\n          '.join(parts)

FIG_MAPPA = f'''
    <figure class="dsa-figure" aria-labelledby="cap-map">
      <svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="map-t map-d" class="dsa-svg map-svg">
        <title id="map-t">Mappa: gli strumenti per studiare informatica con un DSA</title>
        <desc id="map-d">Al centro: informatica con un DSA. Intorno sette strumenti: editor con i colori, carattere leggibile, diagrammi e mappe, sintesi vocale, scheda della sintassi, intelligenza artificiale come tutor, PDP su misura.</desc>
        <g font-family="Atkinson Hyperlegible, Verdana, Arial, sans-serif" font-weight="700" text-anchor="middle">
          {mindmap()}
        </g>
      </svg>
      <ul class="icon-list map-list rt-skip">
        <li><span class="t-ico">🖥️</span><span><strong>Editor con i colori</strong></span></li>
        <li><span class="t-ico">🔤</span><span><strong>Carattere leggibile</strong></span></li>
        <li><span class="t-ico">📐</span><span><strong>Diagrammi e mappe</strong></span></li>
        <li><span class="t-ico">🔊</span><span><strong>Sintesi vocale</strong></span></li>
        <li><span class="t-ico">🗂️</span><span><strong>Scheda della sintassi</strong></span></li>
        <li><span class="t-ico">🤖</span><span><strong>AI come tutor</strong></span></li>
        <li><span class="t-ico">📝</span><span><strong>PDP su misura</strong></span></li>
      </ul>
      <figcaption id="cap-map">Il riepilogo: tutti gli strumenti di questo articolo a colpo d'occhio. Puoi stamparlo o fotografarlo per ripassare.</figcaption>
    </figure>'''

ERRORE = '''<pre class="code-dsa no-ln error-box" role="figure" aria-label="Esempio di messaggio di errore di Python"><code><span class="l">  File "voti.py", <mark class="em-line">line 3</mark></span>
<span class="l">    if voto &gt;= 6</span>
<span class="l">                ^</span>
<span class="l"><mark class="em-err">SyntaxError: expected ':'</mark></span></code></pre>'''

VSCODE = '''{
  "editor.fontFamily": "JetBrains Mono",
  "editor.fontSize": 18,
  "editor.lineHeight": 1.8,
  "editor.fontLigatures": false,
  "editor.renderWhitespace": "boundary",
  "editor.bracketPairColorization.enabled": true
}'''

PASSO3 = '''voto = int(input("Scrivi il voto: "))
print(voto)'''

PASSO4 = '''# Chiedo il voto all'utente
voto = int(input("Scrivi il voto: "))

# Controllo se è sufficiente
if voto >= 6:
    print("Sufficiente")
else:
    print("Insufficiente")'''

def faq(q, a):
    return f'''    <details class="dsa-faq">
      <summary>{q}<span aria-hidden="true">+</span></summary>
      <p>{a}</p>
    </details>'''

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Con la dislessia si può diventare programmatori?", "Sì. La programmazione richiede soprattutto ragionamento e capacità di risolvere problemi. Con gli strumenti giusti la lettura del codice diventa molto meno faticosa, e nel lavoro di tutti i giorni editor e documentazione aiutano chiunque."),
    faq("Nelle verifiche di informatica posso usare il computer?", "Dipende da cosa è scritto nel tuo PDP. Nelle verifiche di programmazione il computer, al posto di carta e penna, è uno strumento compensativo molto utile, soprattutto con la disgrafia. Chiedi ai tuoi docenti di valutarlo insieme a te e alla tua famiglia."),
    faq("Quale linguaggio è più adatto per iniziare?", 'Python è spesso una buona scelta: usa poche parentesi e pochi simboli, e si legge quasi come l\'inglese. Puoi iniziare con il <a href="corso-python.html">corso gratuito di Python</a>. Per i primissimi passi esistono anche i linguaggi a blocchi come Scratch, in cui si programma trascinando blocchi colorati invece di scrivere.'),
    faq("La discalculia è un ostacolo in informatica?", 'Non per forza. Programmare non significa fare calcoli a mente: i calcoli li fa il computer. Per argomenti come il <a href="articolo-sistema-binario.html">sistema binario</a> aiutano tabelle e schemi, che si possono prevedere nel PDP.'),
])

# ------------------------------------------------------------------ CORPO
BODY = f'''
    <div class="dsa-box tldr" id="in-breve">
      <h2 class="box-title"><span aria-hidden="true">📌</span> L'articolo in 30 secondi</h2>
      <ul>
        <li>Avere un <strong>DSA non ti impedisce di programmare</strong>: in informatica contano soprattutto la logica e il ragionamento.</li>
        <li>Le difficoltà più comuni sono <strong>leggere codice fitto</strong>, <strong>confondere caratteri simili</strong> e <strong>scrivere i comandi senza errori</strong>.</li>
        <li>Gli <strong>strumenti compensativi giusti</strong> (editor con i colori, diagrammi, sintesi vocale, schede) riducono molto la fatica.</li>
        <li>Molti strumenti si possono <strong>inserire nel PDP</strong> (il Piano Didattico Personalizzato) e usare anche nelle verifiche.</li>
      </ul>
    </div>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title"><span aria-hidden="true">🧭</span> Indice</h2>
      <ol>
        <li><a href="#cosa-sono">Cosa sono i DSA, in parole semplici</a></li>
        <li><a href="#difficolta">Perché la programmazione può sembrare difficile?</a></li>
        <li><a href="#buona-notizia">La buona notizia: l'informatica può diventare un punto di forza</a></li>
        <li><a href="#strumenti">Quali strumenti compensativi aiutano in informatica?</a></li>
        <li><a href="#strategie">Strategie di studio che funzionano</a></li>
        <li><a href="#esempio">Un esempio guidato, passo dopo passo</a></li>
        <li><a href="#pdp">Cosa si può prevedere nel PDP per l'informatica?</a></li>
        <li><a href="#sintesi">In sintesi</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <p>Se hai un DSA e studi informatica, forse ti è capitato di pensare: «Il codice è pieno di simboli, non fa per me». È un pensiero comune, ma <strong>non è vero</strong>.</p>
    <p>Programmare non vuol dire leggere veloce o scrivere senza errori di ortografia. Vuol dire <strong>ragionare</strong>, <strong>dividere un problema in pezzi</strong> e <strong>trovare una soluzione</strong>. Per tutto il resto esistono strumenti che ti aiutano.</p>
    <p>In questa guida ti spiego, un passo alla volta, quali difficoltà si incontrano più spesso, quali strumenti usare e come organizzare lo studio. Verso la fine c'è anche una parte per <strong>famiglie e docenti</strong>: spiega cosa si può prevedere nel PDP.</p>

    <h2 id="cosa-sono">Cosa sono i DSA, in parole semplici</h2>
    <p>I <strong>DSA</strong> (Disturbi Specifici dell'Apprendimento) sono disturbi del neurosviluppo, cioè legati a come si sviluppa il cervello. Rendono più faticose alcune attività, come leggere, scrivere o fare calcoli. <strong>Non dipendono dall'intelligenza</strong> né dall'impegno.</p>
    <p>In Italia sono riconosciuti dalla <strong>Legge 170 del 2010</strong>, che ne indica quattro:</p>
    <ul class="dsa-types">
      <li><span class="t-ico" aria-hidden="true">📖</span><strong>Dislessia</strong>: difficoltà nella lettura, che diventa più lenta, faticosa e meno precisa.</li>
      <li><span class="t-ico" aria-hidden="true">✏️</span><strong>Disortografia</strong>: difficoltà nello scrivere le parole in modo corretto.</li>
      <li><span class="t-ico" aria-hidden="true">🖊️</span><strong>Disgrafia</strong>: difficoltà nella scrittura a mano, che può risultare lenta o poco leggibile.</li>
      <li><span class="t-ico" aria-hidden="true">🔢</span><strong>Discalculia</strong>: difficoltà con i numeri e i calcoli.</li>
    </ul>
    <p>Spesso se ne presenta più di uno insieme, e ogni persona è diversa. Per questo gli strumenti vanno <strong>scelti su misura</strong>.</p>
    <p>Che differenza c'è tra DSA, disabilità e <strong>BES</strong> (Bisogni Educativi Speciali)? Lo spiego nella guida <a href="articolo-bes-dsa-disabilita.html">Disabilità (L. 104/92), DSA e altri BES</a></p>

    <div class="dsa-box glossary">
      <h3 class="box-title"><span aria-hidden="true">📚</span> Tre parole da conoscere</h3>
      <ul>
        <li><strong>PDP (Piano Didattico Personalizzato)</strong>: il documento in cui la scuola, insieme alla famiglia, scrive gli strumenti e le misure pensati per te.</li>
        <li><strong>Strumenti compensativi</strong>: ti aiutano a fare un compito in un altro modo, più facile per te. Per esempio la sintesi vocale, che legge al posto tuo, o le mappe.</li>
        <li><strong>Misure dispensative</strong>: ti permettono di non fare alcune attività che per te sono molto faticose e non ti aiutano a imparare, come leggere ad alta voce davanti alla classe. Oppure ti permettono di farle in modo adattato, per esempio con più tempo.</li>
      </ul>
    </div>

    <h2 id="difficolta">Perché la programmazione può sembrare difficile?</h2>
    <p>Il codice è un testo particolare: è <strong>fitto</strong>, pieno di <strong>simboli</strong> e <strong>non perdona</strong> gli errori di battitura. Ecco gli ostacoli più comuni.</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">👀</span><span><strong>Leggere righe lunghe e piene di simboli</strong>: parentesi, due punti, virgolette. Con la dislessia la lettura è più lenta ed è facile perdere il segno.</span></li>
      <li><span class="t-ico" aria-hidden="true">🔤</span><span><strong>Confondere caratteri simili</strong>:<br><code>l</code> elle minuscola, <code>1</code> uno, <code>I</code> i maiuscola;<br><code>O</code> o maiuscola e <code>0</code> zero;<br><code>=</code> uguale e <code>==</code> doppio uguale.</span></li>
      <li><span class="t-ico" aria-hidden="true">✏️</span><span><strong>Scrivere i comandi senza errori</strong>: basta scrivere <code>pirnt</code> invece di <code>print</code> e il programma non funziona. Con la disortografia capita più spesso.</span></li>
      <li><span class="t-ico" aria-hidden="true">🧠</span><span><strong>Ricordare tanti dettagli insieme</strong>: nomi delle variabili, ordine delle istruzioni, regole di scrittura. La memoria si affatica in fretta.</span></li>
      <li><span class="t-ico" aria-hidden="true">🖊️</span><span><strong>Scrivere codice a mano</strong>: nelle verifiche su carta, con la disgrafia, il codice diventa lento da scrivere e difficile da rileggere.</span></li>
      <li><span class="t-ico" aria-hidden="true">🔢</span><span><strong>Numeri e conversioni</strong>: le posizioni negli elenchi (in Python, le <a href="articolo-liste-python.html">liste</a>), che si contano partendo da zero, o il <a href="articolo-sistema-binario.html">sistema binario</a> possono creare confusione, soprattutto con la discalculia.</span></li>
    </ul>
{FIG_CARATTERI}

    <h2 id="buona-notizia">La buona notizia: l'informatica può diventare un punto di forza</h2>
    <p>Ora la parte più importante: la programmazione ha anche <strong>tanti lati che possono aiutarti</strong>.</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">🧩</span><span><strong>Conta il ragionamento</strong>: un programma è una sequenza di passi logici. Puoi essere bravissimo a ragionare anche se leggi lentamente.</span></li>
      <li><span class="t-ico" aria-hidden="true">⚡</span><span><strong>Il computer ti risponde subito</strong>: scrivi, provi e vedi il risultato. Si impara provando, non solo leggendo.</span></li>
      <li><span class="t-ico" aria-hidden="true">🔍</span><span><strong>Non devi sapere tutto a memoria</strong>: gli editor completano i comandi, e anche i programmatori esperti consultano di continuo la documentazione, cioè le guide ufficiali del linguaggio.</span></li>
      <li><span class="t-ico" aria-hidden="true">🎨</span><span><strong>Si lavora molto con le immagini</strong>: diagrammi, schemi e colori fanno parte del lavoro di tutti i giorni.</span></li>
    </ul>
    <p>Un DSA non ti impedisce di diventare programmatore, perché programmare vuol dire soprattutto <strong>risolvere problemi</strong>: lo racconto nell'articolo su <a href="articolo-programmatore.html">cosa fa un programmatore</a>.</p>

    <h2 id="strumenti">Quali strumenti compensativi aiutano in informatica?</h2>
    <p>Ecco gli strumenti che, secondo me, fanno davvero la differenza. <strong>Non servono tutti</strong>: scegli quelli che ti aiutano di più.</p>
    <p>Quali tecnologie hai già gratis nel computer e come averne altre a scuola lo spiego nella guida <a href="articolo-tecnologie-assistive.html">Le tecnologie assistive a scuola</a>.</p>

    <h3>1. Un editor di codice che lavora per te</h3>
    <p>Scrivere codice in un semplice blocco note è come scrivere un tema senza correttore. Un <strong>editor di codice</strong> ti aiuta in tanti modi:</p>
    <ul>
      <li><strong>colora le parole</strong> in base al loro ruolo (comandi, testi, numeri), così le riconosci a colpo d'occhio;</li>
      <li><strong>completa i comandi</strong> mentre scrivi: se digiti <code>pr</code>, ti propone <code>print</code> già scritto bene;</li>
      <li><strong>sottolinea molti errori</strong> ancora prima che tu esegua il programma;</li>
      <li><strong>colora le parentesi a coppie</strong>, così vedi subito quale parentesi chiude quale;</li>
      <li><strong>sistema i rientri</strong> (l'indentazione) in automatico.</li>
    </ul>
    <p>Per iniziare con Python ti consiglio <strong>Thonny</strong>: è semplice e pensato per chi impara.</p>
    <ul>
      <li>dal menu <strong>Visualizza → Variabili</strong> vedi il valore delle variabili;</li>
      <li>con il pulsante <strong>Debug</strong> esegui il programma un passo alla volta;</li>
      <li>con <strong>Ctrl + Spazio</strong> chiedi i suggerimenti mentre scrivi. Per averli sempre, attivali in <strong>Strumenti → Opzioni → Editor</strong>.</li>
    </ul>
    <p>Per andare oltre c'è <strong>Visual Studio Code</strong>, che mostra i suggerimenti in automatico. Trovi Thonny e Visual Studio Code nella sezione <a href="lezioni.html#software">Software utilizzati</a>. E se vuoi provare subito senza installare nulla, nelle <a href="lezioni.html">lezioni gratuite</a> c'è l'editor «Provalo tu».</p>
{FIG_COLORI}

    <h3>2. Un carattere leggibile e più spazio</h3>
    <p>Il carattere giusto evita tante confusioni. Per il codice scegli un <strong>carattere monospaziato</strong>, cioè con tutte le lettere della stessa larghezza. Meglio se ogni simbolo ha una forma diversa, come in <strong>JetBrains Mono</strong> o <strong>Fira Code</strong>: sono entrambi gratuiti.</p>
    <p>Poi aumenta la <strong>dimensione del testo</strong> e lo <strong>spazio tra le righe</strong>. Se usi Visual Studio Code, apri qui sotto le istruzioni passo per passo.</p>
    <details class="dsa-faq vscode-box">
      <summary>Per chi usa Visual Studio Code: le impostazioni da copiare<span aria-hidden="true">+</span></summary>
    <p>Puoi aprire le impostazioni con <strong>Ctrl + ,</strong> (la virgola; sul Mac <strong>Cmd + ,</strong>) e cercare le opzioni una per una. Oppure, più in fretta, puoi incollarle tutte insieme nel file <code>settings.json</code>:</p>
    <ol>
      <li>premi <strong>Ctrl + Maiusc + P</strong>;</li>
      <li>scrivi <strong>Apri impostazioni utente (JSON)</strong> e premi Invio. Se Visual Studio Code è in inglese, scrivi invece <strong>Open User Settings (JSON)</strong>;</li>
      <li>se il file è vuoto, incolla tutto il blocco qui sotto. Se invece contiene già altre righe, copia solo le righe tra le parentesi graffe <code>{{ }}</code> e incollale subito prima della graffa di chiusura <code>}}</code>. Poi metti una virgola alla fine dell'ultima riga che c'era già.</li>
    </ol>
    {code(VSCODE, 'json', 'Impostazioni di Visual Studio Code per un codice più leggibile')}
    <ul>
      <li><code>fontFamily</code>: il carattere da usare (va installato prima sul computer);</li>
      <li><code>fontSize</code>: la dimensione del testo, qui più grande del normale;</li>
      <li><code>lineHeight</code>: l'altezza di ogni riga. <code>1.8</code> vuol dire 1,8 volte la dimensione del testo, quindi più spazio tra una riga e l'altra;</li>
      <li><code>fontLigatures</code>: con <code>false</code> i simboli restano separati, così <code>&gt;=</code> appare proprio come lo scrivi e non come un unico segno ≥ (le legature, cioè i simboli uniti in un unico segno, di base sono già disattivate: questa riga serve solo a non attivarle per sbaglio);</li>
      <li><code>renderWhitespace</code>: mostra gli spazi dei rientri come puntini, molto utile in Python;</li>
      <li><code>bracketPairColorization</code>: colora le parentesi a coppie (nelle versioni recenti è già attivo).</li>
    </ul>
    </details>
    <p>Conta anche il <strong>tema</strong>: c'è chi legge meglio su sfondo scuro e chi su sfondo chiaro o color crema. Prova temi diversi e scegli il tuo. Questa pagina, per esempio, usa <strong>Atkinson Hyperlegible</strong>, un carattere progettato per essere facile da leggere: puoi attivarlo o disattivarlo con il pulsante <strong>🔤 Carattere leggibile</strong> in alto.</p>

    <h3>3. Diagrammi di flusso e mappe</h3>
    <p>Prima di scrivere il codice, <strong>disegna il ragionamento</strong>. Un <a href="articolo-diagramma-di-flusso.html">diagramma di flusso</a> trasforma il problema in forme e frecce, molto più facili da seguire di un testo. Con il diagramma pronto, scrivere il codice diventa quasi una traduzione: lo vedrai nell'<a href="#esempio">esempio guidato</a> più avanti.</p>
    <p>Per approfondire: <a href="articolo-come-costruire-algoritmo.html">come si costruisce un algoritmo</a> e <a href="articolo-strutture-programmazione.html">le tre strutture di base</a> della programmazione.</p>
    <p>Per ripassare la teoria aiuta una <strong>mappa concettuale</strong>: l'argomento al centro e le idee collegate intorno. Ne trovi una nella sezione <a href="#sintesi">In sintesi</a>.</p>

    <h3>4. La sintesi vocale</h3>
    <p>La sintesi vocale legge il testo al posto tuo. In informatica è utile per:</p>
    <ul>
      <li>ascoltare la <strong>teoria</strong> e le <strong>consegne</strong> degli esercizi;</li>
      <li>farti leggere i <strong>messaggi di errore</strong>, che a volte sono lunghi e in inglese.</li>
    </ul>
    <p>Sul computer, ad esempio, il browser Microsoft Edge ha la funzione «Leggi ad alta voce». Su smartphone e tablet la sintesi vocale si attiva dalle impostazioni di accessibilità. Anche questo articolo si può ascoltare: usa il pulsante <strong>🔊 Ascolta l'articolo</strong> in alto.</p>

    <h3>5. Una scheda personale della sintassi</h3>
    <p>Imparare a memoria tutte le regole di scrittura (la <strong>sintassi</strong>) è faticoso e non serve: è più importante capire <strong>quando</strong> usare un'istruzione. Preparati una <strong>scheda</strong> con gli schemi che usi di più, scritta grande e con i colori.</p>
{FIG_SCHEDA}
    <p>Ogni schema della scheda ha una guida dedicata: per esempio <a href="articolo-cicli-for-python.html">il ciclo for in Python</a> e <a href="articolo-funzioni-python.html">le funzioni in Python</a>.</p>
    <p>Se la scheda è prevista nel tuo PDP, puoi usarla anche durante le verifiche: <strong>concordalo con i tuoi docenti</strong>.</p>

    <h3>6. L'intelligenza artificiale come tutor, non come scorciatoia</h3>
    <p>Strumenti come ChatGPT possono spiegarti un errore con parole semplici, riformulare una spiegazione difficile o farti domande per ripassare. Ecco una richiesta che puoi usare:</p>
    <div class="prompt-box">💬 «Ho un DSA. Spiegami questo messaggio di errore di Python con frasi brevi e un esempio: [incolla qui l'errore]»</div>
    <p>Usa l'AI per <strong>capire</strong>, non per copiare: un esercizio fatto dall'AI non ti insegna nulla, e le risposte vanno sempre controllate. Ne parlo nella guida <a href="articolo-chatgpt-studiare.html">come usare ChatGPT per studiare meglio</a>.</p>

    <h2 id="strategie">Strategie di studio che funzionano</h2>
    <p>Gli strumenti aiutano, ma conta anche <strong>come</strong> studi. Ecco le strategie che funzionano meglio.</p>
    <ol class="steps-list">
      <li><strong>Un passo alla volta.</strong> Scrivi due o tre righe, esegui il programma e controlla che funzioni. Poi aggiungi il pezzo successivo. Così, se c'è un errore, sai subito dove cercarlo.</li>
      <li><strong>Prima l'esempio, poi la regola.</strong> Parti da un programma che funziona e modificalo: cambia un numero, un testo, una condizione. Capire cosa succede è il modo più naturale per imparare.</li>
      <li><strong>Dai nomi chiari alle variabili.</strong> <code>media_voti</code> si legge e si ricorda meglio di <code>mv</code>.</li>
      <li><strong>Usa i commenti come promemoria.</strong> Una riga che inizia con <code>#</code> spiega a cosa serve il codice, e aiuta anche te quando lo rileggi dopo una settimana.</li>
      <li><strong>Leggi il messaggio di errore con calma.</strong> Non devi capirlo tutto: guarda prima il <strong>numero dopo la parola line</strong>, poi l'<strong>ultima riga del messaggio</strong>, che dice il tipo di errore.</li>
      <li><strong>Fai pause brevi e frequenti.</strong> Meglio 20-25 minuti di concentrazione e poi una pausa, piuttosto che due ore di fila con la testa che si annebbia.</li>
      <li><strong>Spiega a voce quello che hai fatto.</strong> Raccontare il programma riga per riga, anche solo a te stesso, ti fa scoprire se l'hai capito davvero.</li>
    </ol>
{FIG_ARIOSO}
    <p>Vediamo meglio la strategia numero 5, «Leggi il messaggio di errore con calma». Ecco un messaggio di errore tipico di Python:</p>
    {ERRORE}
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">📍</span><span><strong>line 3</strong> ti dice <strong>dove</strong> guardare: l'errore è alla riga 3. Il simbolo <code>^</code> indica il punto preciso. Sul tuo computer, al posto di <code>voti.py</code>, vedrai il percorso completo del file: non serve leggerlo tutto, cerca solo la parola <strong>line</strong> e il numero che la segue.</span></li>
      <li><span class="t-ico" aria-hidden="true">🏷️</span><span><strong>SyntaxError: expected ':'</strong> ti dice <strong>cosa</strong> è successo: un errore di scrittura, perché Python si aspettava i due punti.</span></li>
      <li><span class="t-ico" aria-hidden="true">🔧</span><span><strong>La soluzione</strong> è aggiungere i due punti alla fine della condizione. La riga corretta è <code>if voto &gt;= 6:</code></span></li>
    </ul>
    <p>Per scovare gli errori esiste un metodo preciso: lo spiego passo dopo passo nella guida su <a href="articolo-debug.html">come trovare e correggere i bug</a>.</p>

    <h2 id="esempio">Un esempio guidato, passo dopo passo</h2>
    <p>Mettiamo insieme tutto con un esercizio classico: <strong>un programma che chiede un voto e dice se è sufficiente</strong>.</p>
    <div class="step-card"><span class="step-n">1</span><div><strong>Capisco il problema.</strong> Cosa entra? Un voto. Cosa esce? La scritta «Sufficiente» oppure «Insufficiente».</div></div>
    <div class="step-card"><span class="step-n">2</span><div><strong>Disegno il diagramma di flusso.</strong> Prima di scrivere codice, metto in fila i passi.</div></div>
{FIG_FLUSSO}
    <div class="step-card"><span class="step-n">3</span><div><strong>Scrivo poche righe e provo.</strong> Per ora mi occupo solo di leggere il voto. Uso <code>int()</code> per trasformare in numero quello che scrivo con la tastiera. Se il programma stampa il numero che ho scritto, questa parte funziona.</div></div>
    {code(PASSO3, label='Passo 3: leggere il voto')}
    <div class="step-card"><span class="step-n">4</span><div><strong>Aggiungo la decisione.</strong> Traduco il rombo del diagramma con <code>if</code> ed <code>else</code> e inserisco due commenti come promemoria. Attenzione: il simbolo <strong>≥</strong> del diagramma in Python si scrive con due caratteri, <code>&gt;=</code>.</div></div>
    {code(PASSO4, label='Passo 4: il programma completo')}
    <div class="step-card"><span class="step-n">5</span><div><strong>Provo casi diversi.</strong> Inserisco 8, poi 6, poi 4. Il 6 è il caso più importante: è il confine tra sufficiente e insufficiente. Se tutti e tre danno il risultato giusto, il programma è pronto.</div></div>
    <p>L'istruzione <code>if</code>/<code>else</code> è spiegata in dettaglio nell'articolo su <a href="articolo-if-else-python.html">if, elif ed else in Python</a>. <code>input()</code> e le variabili, invece, li trovi nell'articolo sulle <a href="articolo-variabili-python.html">variabili in Python</a>.</p>
    <p>Per esercitarti con un programma simile, prova l'<a href="esercizio-media-voti-python.html">esercizio sulla media dei voti</a>. Ha l'editor integrato: puoi scrivere e provare il codice direttamente nella pagina.</p>

    <h2 id="pdp">Cosa si può prevedere nel PDP per l'informatica?</h2>
    <p>Questa parte è dedicata soprattutto a <strong>famiglie e docenti</strong>, ma è utile anche a te: sapere cosa si può chiedere ti aiuta a parlarne con la scuola.</p>
    <p>Per gli studenti con DSA la scuola prepara il <strong>PDP</strong>, il Piano Didattico Personalizzato. Il punto di partenza è la <strong>diagnosi</strong>, che la famiglia consegna alla scuola.</p>
    <p>Il PDP viene scritto dal consiglio di classe insieme alla famiglia. Va preparato <strong>entro i primi tre mesi</strong> dell'anno scolastico, oppure appena possibile se la diagnosi arriva durante l'anno. Nel PDP ci sono gli strumenti compensativi, le misure dispensative e il modo di fare verifiche e valutazioni.</p>
    <p>Come si costruisce il PDP, un passo alla volta, lo spiego nella guida <a href="articolo-pdp-passo-dopo-passo.html">Il Piano Didattico Personalizzato (PDP)</a>.</p>
    <p>Ecco alcuni esempi pensati per l'informatica. Sono <strong>idee da valutare insieme</strong>, non una lista da copiare: ogni PDP è personale.</p>
    <div class="pdp-grid">
      <div class="dsa-box pdp-col">
        <h3><span aria-hidden="true">✅</span> Strumenti compensativi</h3>
        <ul>
          <li>verifiche di programmazione <strong>al computer</strong>, con un editor, invece che scritte a mano;</li>
          <li><strong>colori della sintassi</strong> e <strong>completamento automatico</strong> attivi durante le prove;</li>
          <li><strong>scheda personale della sintassi</strong> o formulario;</li>
          <li><strong>diagrammi di flusso e mappe</strong> durante verifiche e interrogazioni;</li>
          <li><strong>sintesi vocale</strong> per leggere testi e consegne.</li>
        </ul>
      </div>
      <div class="dsa-box pdp-col">
        <h3><span aria-hidden="true">⏱️</span> Misure dispensative</h3>
        <ul>
          <li><strong>tempi più lunghi</strong> oppure <strong>meno esercizi</strong>, con gli stessi obiettivi della classe;</li>
          <li>dispensa dal <strong>copiare codice lungo</strong> dalla lavagna, ricevendo gli esempi in formato digitale;</li>
          <li>dispensa dalla <strong>lettura ad alta voce</strong> davanti alla classe.</li>
        </ul>
      </div>
    </div>
    <div class="dsa-box pdp-col pdp-wide">
      <h3><span aria-hidden="true">📝</span> Verifica e valutazione</h3>
      <ul>
        <li>valutare <strong>il ragionamento più della forma</strong>: un piccolo errore di battitura non dovrebbe pesare come un errore di logica;</li>
        <li><strong>verifiche programmate</strong> e consegne brevi, con una richiesta per volta;</li>
        <li>possibilità di <strong>integrare lo scritto con l'orale</strong>.</li>
      </ul>
    </div>
    <p>All'<strong>esame di maturità</strong> (l'esame di Stato) la commissione decide come svolgerai le prove sulla base del tuo PDP. Negli scritti puoi avere <strong>tempi più lunghi</strong>. Puoi anche usare gli strumenti compensativi del PDP che hai <strong>già usato nelle verifiche durante l'anno</strong>, o altri che la commissione ritiene utili, purché non cambino quello che la prova deve verificare. Per questo conviene usarli con regolarità, non solo all'ultimo momento.</p>
    <div class="dsa-box tip">
      <h3 class="box-title"><span aria-hidden="true">👩‍🏫</span> Un consiglio per i docenti</h3>
      <p>Alcuni piccoli accorgimenti aiutano gli studenti con DSA e, in realtà, <strong>tutta la classe</strong>:</p>
      <ul>
        <li>condividere gli esempi in formato digitale;</li>
        <li>scrivere consegne brevi, con una richiesta per riga;</li>
        <li>mostrare il diagramma prima del codice;</li>
        <li>far provare subito il codice al computer.</li>
      </ul>
    </div>
    <p class="norme rt-skip">Riferimenti normativi: Legge 8 ottobre 2010, n. 170; DM 12 luglio 2011, n. 5669 e Linee guida allegate; D.Lgs. 13 aprile 2017, n. 62, art. 20 (esame di Stato per gli studenti con DSA).</p>

    <h2 id="sintesi">In sintesi</h2>
{FIG_MAPPA}
    <p>Con un DSA puoi imparare a programmare, e anche bene. Il segreto è non combattere contro le difficoltà, ma <strong>aggirarle con gli strumenti giusti</strong>, come quelli della mappa qui sopra.</p>
    <p>Lavora <strong>un passo alla volta</strong>, prova spesso e ricorda che sbagliare fa parte del gioco: anche i programmatori esperti passano tanto tempo a correggere errori. Se le difficoltà sono tante, parlane con i tuoi docenti e con la tua famiglia: il PDP si può rivedere e migliorare. Se invece non hai una diagnosi ma pensi di avere un DSA, insieme alla tua famiglia potete chiedere alla scuola e al medico come fare una valutazione specialistica.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Prova subito, un passo alla volta</h2>
      <p>Nelle lezioni gratuite trovi esempi da modificare e l'editor «Provalo tu» per vedere subito il risultato, senza installare nulla.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai un DSA e vuoi farmi una domanda o raccontarmi la tua esperienza? <a href="contatti.html">Scrivimi</a>: leggo tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📖</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-diagramma-di-flusso.html"><span aria-hidden="true">📐</span><strong>Cos'è un diagramma di flusso e come si legge</strong></a>
        <a href="articolo-adhd-programmazione.html"><span aria-hidden="true">⏲️</span><strong>ADHD e programmazione: strategie didattiche per l'apprendimento dell'informatica</strong></a>
        <a href="articolo-pdp-passo-dopo-passo.html"><span aria-hidden="true">📝</span><strong>Il Piano Didattico Personalizzato (PDP): destinatari, elaborazione e contenuti</strong></a>
      </div>
    </div>
'''

words, MIN = minutes(BODY)
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="informatica DSA, DSA programmazione, strumenti compensativi informatica, dislessia programmazione, PDP informatica, studiare informatica con DSA, misure dispensative informatica",
    og_alt="Il titolo «Informatica e DSA», un pezzo di puzzle con le parentesi graffe del codice e un breve programma Python che scrive «Ce la fai!».",
    date_iso="2026-11-08", date_it="8 novembre 2026", modified_iso="2026-11-19",
    ld_keywords="DSA, dislessia, strumenti compensativi, misure dispensative, PDP, programmazione, informatica",
    hero_src="articolo-informatica-dsa.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Informatica e DSA», un pezzo di puzzle con dentro le parentesi graffe del codice e un breve programma Python che scrive «Ce la fai!».",
)
if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, 'articolo-informatica-dsa.html'), 'w', encoding='utf-8').write(page(META))
    print('DSA: parole', words, '| minuti', MIN)
