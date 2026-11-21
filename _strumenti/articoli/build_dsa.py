#!/usr/bin/env python3
"""Articolo: Informatica e DSA (stile professionale, riscritto il 21/11/2026)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

TITLE = "Informatica e DSA: strategie e strumenti compensativi per l'apprendimento della programmazione"
SEO_TITLE = "Informatica e DSA: strategie e strumenti compensativi — AlessandroSimone.it"
DESC = "DSA e programmazione: criticità, strumenti compensativi, strategie di studio, un esempio guidato in Python e indicazioni per il PDP in ambito informatico."
URL = "https://alessandrosimone.it/articolo-informatica-dsa.html"
IMG = "https://alessandrosimone.it/articolo-informatica-dsa.jpg"

# ------------------------------------------------------------------ FIGURE
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

SCHEDA = '''# Scrivere sullo schermo
print("Ciao")

# Chiedere un dato
nome = input("Nome? ")
voto = int(input("Voto? "))

# Decidere
if voto >= 6:
    print("Bene")
else:
    print("Ripassa")

# Ripetere un numero stabilito di volte
for i in range(5):
    print(i)

# Ripetere finché una condizione è vera
while voto < 6:
    voto = voto + 1

# Definire una funzione
def saluta(nome):
    print("Ciao", nome)'''

FIG_SCHEDA = f'''
    <figure class="dsa-figure" aria-labelledby="cap-sch">
      {code(SCHEDA, label="Esempio di scheda personale della sintassi Python", numbers=False)}
      <figcaption id="cap-sch">Un esempio di scheda personale della sintassi Python. Le righe che introducono un blocco (if, else, for, while, def) terminano con i due punti e la riga successiva è rientrata di quattro spazi.</figcaption>
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
        <div><div class="panel-title">Codice compatto</div>{code(FITTO, numbers=False)}</div>
        <div><div class="panel-title">Codice leggibile</div>{code(ARIOSO, numbers=False)}</div>
      </div>
      <figcaption id="cap-ari">I due programmi calcolano la stessa media. Il secondo usa nomi espliciti, righe vuote e un commento: si legge molto meglio.</figcaption>
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
    faq("La dislessia è compatibile con la professione di programmatore?", "Sì. La programmazione richiede soprattutto capacità di ragionamento e di risoluzione dei problemi. Con strumenti adeguati la lettura del codice risulta molto meno onerosa e, nella pratica professionale, editor e documentazione costituiscono un supporto per chiunque."),
    faq("Nelle verifiche di informatica è possibile utilizzare il computer?", "Dipende da quanto previsto nel PDP. Nelle prove di programmazione l'uso del computer in luogo della scrittura a mano rappresenta uno strumento compensativo particolarmente efficace, specie in presenza di disgrafia; la decisione va condivisa con il consiglio di classe e la famiglia."),
    faq("Quale linguaggio è più indicato per iniziare?", 'Python è spesso una scelta appropriata: impiega pochi simboli e una sintassi vicina al linguaggio naturale. È possibile iniziare con il <a href="corso-python.html">corso gratuito di Python</a>. Per i primissimi passi sono disponibili anche linguaggi a blocchi come Scratch, che sostituiscono la scrittura con il trascinamento di blocchi.'),
    faq("La discalculia costituisce un ostacolo in informatica?", 'Non necessariamente: programmare non significa eseguire calcoli mentali, che sono demandati al calcolatore. Per argomenti come il <a href="articolo-sistema-binario.html">sistema binario</a> risultano utili tabelle e schemi, che possono essere previsti nel PDP.'),
])

# ------------------------------------------------------------------ CORPO
BODY = f'''
    <p>Un DSA (Disturbo Specifico dell'Apprendimento) non preclude l'apprendimento della programmazione: in informatica contano soprattutto la logica, la capacità di scomporre i problemi e di costruire soluzioni. Le difficoltà riguardano piuttosto la lettura di un codice denso di simboli, la discriminazione di caratteri simili e la correttezza formale della scrittura.</p>
    <p>Avendo insegnato informatica per anni, e lavorando oggi come docente per l'inclusività (<a href="/#chi-sono">chi sono</a>), propongo in questo contributo un'analisi delle criticità più frequenti, una rassegna degli strumenti compensativi, alcune strategie di studio, un esempio guidato e indicazioni per la predisposizione del PDP in ambito informatico.</p>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title">Indice</h2>
      <ol>
        <li><a href="#cosa-sono">I DSA: inquadramento</a></li>
        <li><a href="#difficolta">Le criticità della programmazione</a></li>
        <li><a href="#buona-notizia">I punti di forza</a></li>
        <li><a href="#strumenti">Gli strumenti compensativi</a></li>
        <li><a href="#strategie">Strategie di studio</a></li>
        <li><a href="#esempio">Un esempio guidato</a></li>
        <li><a href="#pdp">Il PDP in ambito informatico</a></li>
        <li><a href="#sintesi">Considerazioni conclusive</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <h2 id="cosa-sono">I DSA: inquadramento</h2>
    <p>I <strong>DSA</strong> sono disturbi del neurosviluppo che rendono più onerose specifiche abilità strumentali, indipendentemente dal livello intellettivo e dall'impegno. La <strong>L. 170/2010</strong> ne riconosce quattro:</p>
    <ul>
      <li><strong>dislessia</strong>: difficoltà nella lettura, che risulta più lenta, faticosa e meno accurata;</li>
      <li><strong>disortografia</strong>: difficoltà nella correttezza ortografica della scrittura;</li>
      <li><strong>disgrafia</strong>: difficoltà nella grafia, che può risultare lenta o poco leggibile;</li>
      <li><strong>discalculia</strong>: difficoltà nell'elaborazione numerica e nel calcolo.</li>
    </ul>
    <p>I disturbi si presentano spesso in associazione e con profili individuali molto diversi: gli strumenti vanno dunque calibrati sul singolo studente. Le distinzioni tra DSA, disabilità e altri BES (Bisogni Educativi Speciali) sono illustrate in <a href="articolo-bes-dsa-disabilita.html">Disabilità (L. 104/92), DSA e altri BES</a>.</p>
    <p>Tre nozioni ricorrono nel seguito: il <strong>PDP</strong> (Piano Didattico Personalizzato), documento con cui il consiglio di classe, con la famiglia, formalizza le misure per lo studente; gli <strong>strumenti compensativi</strong>, che sollevano da una prestazione resa difficoltosa dal disturbo senza facilitare il compito sul piano cognitivo; le <strong>misure dispensative</strong>, che esonerano da prestazioni particolarmente onerose e non formative o ne consentono lo svolgimento in forma adattata.</p>

    <h2 id="difficolta">Le criticità della programmazione</h2>
    <p>Il codice è un testo peculiare: denso, ricco di simboli e intollerante agli errori formali. Le criticità più frequenti sono:</p>
    <ul>
      <li><strong>la lettura di righe lunghe e dense di simboli</strong> (parentesi, due punti, virgolette), con rallentamento e perdita del punto di lettura in presenza di dislessia;</li>
      <li><strong>la discriminazione di caratteri simili</strong>: <code>l</code> (elle minuscola), <code>1</code> (uno) e <code>I</code> (i maiuscola); <code>O</code> (o maiuscola) e <code>0</code> (zero); <code>=</code> e <code>==</code>;</li>
      <li><strong>la correttezza formale dei comandi</strong>: scrivere <code>pirnt</code> anziché <code>print</code> impedisce l'esecuzione, evenienza più frequente in presenza di disortografia;</li>
      <li><strong>il carico sulla memoria di lavoro</strong>, dovuto alla gestione contestuale di nomi di variabili, sequenze di istruzioni e regole sintattiche;</li>
      <li><strong>la scrittura del codice a mano</strong> nelle prove cartacee, lenta e difficilmente rileggibile in presenza di disgrafia;</li>
      <li><strong>numeri e conversioni</strong>: l'indicizzazione da zero delle <a href="articolo-liste-python.html">liste</a> o il <a href="articolo-sistema-binario.html">sistema binario</a>, particolarmente critici in presenza di discalculia.</li>
    </ul>
    <p>Anche la scelta del carattere tipografico incide: nei caratteri di uso comune la i maiuscola e la elle minuscola risultano quasi indistinguibili e la sequenza «rn» può essere letta come «m», mentre i caratteri progettati per il codice attribuiscono a ogni simbolo una forma distinta.</p>

    <h2 id="buona-notizia">I punti di forza</h2>
    <p>La programmazione presenta, al tempo stesso, caratteristiche favorevoli:</p>
    <ul>
      <li><strong>la centralità del ragionamento</strong>: un programma è una sequenza di passaggi logici, indipendente dalla velocità di lettura;</li>
      <li><strong>il riscontro immediato</strong>: si scrive, si esegue e si osserva il risultato, apprendendo per sperimentazione;</li>
      <li><strong>la non necessità della memorizzazione integrale</strong>: gli editor completano i comandi e la consultazione della documentazione è prassi anche tra i professionisti;</li>
      <li><strong>il ruolo delle rappresentazioni visive</strong>: diagrammi, schemi e colori fanno parte del lavoro ordinario.</li>
    </ul>
    <p>Un DSA non preclude dunque la professione di programmatore, che consiste anzitutto nella risoluzione di problemi, come illustrato in <a href="articolo-programmatore.html">cosa fa un programmatore</a>.</p>

    <h2 id="strumenti">Gli strumenti compensativi</h2>
    <p>Gli strumenti seguenti risultano particolarmente efficaci; non sono tutti necessari e vanno selezionati in base al profilo dello studente. Le funzioni di accessibilità già disponibili nei sistemi operativi e le modalità per ottenere ulteriori ausili sono descritte in <a href="articolo-tecnologie-assistive.html">Le tecnologie assistive a scuola</a>.</p>

    <h3>Un editor di codice</h3>
    <p>Un editor di codice offre funzioni assenti in un semplice editor di testo:</p>
    <ul>
      <li>evidenzia la sintassi con colori diversi per comandi, stringhe e numeri;</li>
      <li>completa automaticamente i comandi durante la digitazione;</li>
      <li>segnala molti errori prima dell'esecuzione;</li>
      <li>colora le parentesi a coppie, rendendo evidente la corrispondenza;</li>
      <li>gestisce automaticamente l'indentazione.</li>
    </ul>
    <p>Per iniziare con Python è indicato <strong>Thonny</strong>, ambiente semplice e pensato per la didattica: il menu Visualizza → Variabili mostra il valore delle variabili, il pulsante Debug consente l'esecuzione passo passo e la combinazione Ctrl + Spazio attiva i suggerimenti, che possono essere resi permanenti da Strumenti → Opzioni → Editor.</p>
    <p>A un livello più avanzato si colloca <strong>Visual Studio Code</strong>, che propone i suggerimenti in automatico. Entrambi sono indicati nella sezione <a href="lezioni.html#software">Software utilizzati</a>; per sperimentare senza installazioni è disponibile l'editor «Provalo tu» delle <a href="lezioni.html">lezioni gratuite</a>.</p>
{FIG_COLORI}

    <h3>Carattere tipografico e spaziatura</h3>
    <p>Per il codice è opportuno un <strong>carattere monospaziato</strong>, in cui ogni simbolo abbia una forma distinta, come <strong>JetBrains Mono</strong> o <strong>Fira Code</strong>, entrambi gratuiti. Giovano inoltre un corpo del testo maggiore e un'interlinea più ampia.</p>
    <details class="dsa-faq vscode-box">
      <summary>Impostazioni consigliate per Visual Studio Code<span aria-hidden="true">+</span></summary>
    <p>Le impostazioni si aprono con <strong>Ctrl + ,</strong> (sul Mac <strong>Cmd + ,</strong>). In alternativa è possibile incollarle nel file <code>settings.json</code>:</p>
    <ol>
      <li>premere <strong>Ctrl + Maiusc + P</strong>;</li>
      <li>digitare <strong>Apri impostazioni utente (JSON)</strong>, oppure <strong>Open User Settings (JSON)</strong> se l'interfaccia è in inglese, e premere Invio;</li>
      <li>se il file è vuoto, incollare l'intero blocco; se contiene già altre impostazioni, copiare soltanto le righe comprese tra le parentesi graffe <code>{{ }}</code>, inserirle prima della graffa di chiusura <code>}}</code> e aggiungere una virgola al termine dell'ultima riga preesistente.</li>
    </ol>
    {code(VSCODE, 'json', 'Impostazioni di Visual Studio Code per un codice più leggibile')}
    <ul>
      <li><code>fontFamily</code>: il carattere da utilizzare, da installare preventivamente;</li>
      <li><code>fontSize</code>: il corpo del testo, qui maggiorato;</li>
      <li><code>lineHeight</code>: l'interlinea; il valore <code>1.8</code> corrisponde a 1,8 volte il corpo del testo;</li>
      <li><code>fontLigatures</code>: con <code>false</code> i simboli restano distinti, sicché <code>&gt;=</code> non viene reso come un unico segno ≥ (le legature sono già disattivate per impostazione predefinita; la riga ne previene l'attivazione accidentale);</li>
      <li><code>renderWhitespace</code>: visualizza gli spazi di indentazione come puntini, utile in Python;</li>
      <li><code>bracketPairColorization</code>: colora le parentesi a coppie, opzione già attiva nelle versioni recenti.</li>
    </ul>
    </details>
    <p>Anche il tema cromatico incide sulla leggibilità: alcuni studenti leggono meglio su sfondo scuro, altri su sfondo chiaro o color crema. Questa pagina, ad esempio, consente di attivare il carattere Atkinson Hyperlegible e lo sfondo crema dalla barra di lettura in alto.</p>

    <h3>Diagrammi di flusso e mappe</h3>
    <p>Prima della codifica è utile rappresentare graficamente il ragionamento. Il <a href="articolo-diagramma-di-flusso.html">diagramma di flusso</a> traduce il problema in forme e frecce, più agevoli da seguire di un testo; a diagramma completato, la scrittura del codice si configura quasi come una traduzione, come mostra l'<a href="#esempio">esempio guidato</a>. Per approfondire si vedano <a href="articolo-come-costruire-algoritmo.html">come si costruisce un algoritmo</a> e <a href="articolo-strutture-programmazione.html">le tre strutture di base</a> della programmazione.</p>
    <p>Per lo studio della teoria risultano efficaci le <strong>mappe concettuali</strong>, con l'argomento al centro e i concetti collegati disposti intorno.</p>

    <h3>La sintesi vocale</h3>
    <p>La sintesi vocale è utile per l'ascolto della teoria e delle consegne e per la lettura dei messaggi di errore, spesso estesi e in lingua inglese. Sul computer, ad esempio, Microsoft Edge dispone della funzione «Leggi ad alta voce»; su smartphone e tablet la funzione si attiva dalle impostazioni di accessibilità. Anche questo articolo può essere ascoltato con il pulsante «Ascolta l'articolo».</p>

    <h3>Una scheda personale della sintassi</h3>
    <p>La memorizzazione integrale delle regole sintattiche è onerosa e poco utile: conta piuttosto comprendere quando impiegare ciascuna istruzione. Una <strong>scheda personale</strong> raccoglie gli schemi d'uso più frequenti.</p>
{FIG_SCHEDA}
    <p>Ciascuno schema è approfondito in una guida dedicata, ad esempio <a href="articolo-cicli-for-python.html">il ciclo for in Python</a> e <a href="articolo-funzioni-python.html">le funzioni in Python</a>. Se prevista nel PDP, la scheda può essere utilizzata anche durante le verifiche.</p>

    <h3>L'intelligenza artificiale come tutor</h3>
    <p>Strumenti come ChatGPT possono spiegare un errore con un linguaggio semplice, riformulare una spiegazione complessa o proporre domande di ripasso. Una richiesta efficace può essere: «Ho un DSA. Spiegami questo messaggio di errore di Python con frasi brevi e un esempio: [messaggio di errore]».</p>
    <p>L'intelligenza artificiale va impiegata per comprendere, non per sostituirsi allo studente nello svolgimento, e le sue risposte richiedono sempre una verifica. Un approfondimento è in <a href="articolo-chatgpt-studiare.html">come usare ChatGPT per studiare meglio</a>.</p>

    <h2 id="strategie">Strategie di studio</h2>
    <p>Oltre agli strumenti, incide in modo determinante il metodo di studio:</p>
    <ol>
      <li><strong>procedere per incrementi</strong>: scrivere poche righe, eseguirle e verificarle prima di proseguire, così da circoscrivere gli eventuali errori;</li>
      <li><strong>partire dall'esempio</strong>: modificare un programma funzionante (un valore, un testo, una condizione) e osservarne gli effetti;</li>
      <li><strong>adottare nomi espliciti</strong>: <code>media_voti</code> è più leggibile e memorizzabile di <code>mv</code>;</li>
      <li><strong>utilizzare i commenti</strong>, introdotti da <code>#</code>, come promemoria della funzione del codice;</li>
      <li><strong>leggere con metodo i messaggi di errore</strong>, individuando dapprima il numero di riga e poi l'ultima riga, che indica il tipo di errore;</li>
      <li><strong>prevedere pause brevi e frequenti</strong>, ad esempio dopo 20-25 minuti di lavoro;</li>
      <li><strong>verbalizzare il programma</strong>, spiegandolo riga per riga, per verificarne l'effettiva comprensione.</li>
    </ol>
{FIG_ARIOSO}
    <p>Per la lettura dei messaggi di errore, si consideri il seguente esempio:</p>
    {ERRORE}
    <ul>
      <li><strong>line 3</strong> indica dove intervenire: l'errore si trova alla riga 3 e il simbolo <code>^</code> ne segnala il punto preciso; al posto di <code>voti.py</code> può comparire il percorso completo del file, che non è necessario leggere integralmente;</li>
      <li><strong>SyntaxError: expected ':'</strong> indica che cosa è accaduto: un errore di sintassi, poiché Python attendeva i due punti;</li>
      <li>la correzione consiste nell'aggiungere i due punti al termine della condizione: <code>if voto &gt;= 6:</code>.</li>
    </ul>
    <p>Un metodo sistematico per l'individuazione degli errori è illustrato in <a href="articolo-debug.html">come trovare e correggere i bug</a>.</p>

    <h2 id="esempio">Un esempio guidato</h2>
    <p>L'esercizio proposto consiste in un programma che richiede un voto e indica se è sufficiente.</p>
    <h3>1. Analisi del problema</h3>
    <p>Il dato in ingresso è un voto; in uscita si attende la scritta «Sufficiente» oppure «Insufficiente».</p>
    <h3>2. Diagramma di flusso</h3>
    <p>Prima della codifica si rappresenta la sequenza dei passaggi.</p>
{FIG_FLUSSO}
    <h3>3. Prima porzione di codice</h3>
    <p>Ci si limita alla lettura del voto, convertito in numero intero con <code>int()</code>. Se il programma stampa il valore inserito, questa parte è corretta.</p>
    {code(PASSO3, label='Passo 3: leggere il voto')}
    <h3>4. La struttura condizionale</h3>
    <p>Il rombo del diagramma si traduce con <code>if</code> ed <code>else</code>, accompagnati da due commenti. Il simbolo ≥ del diagramma si scrive in Python con due caratteri: <code>&gt;=</code>.</p>
    {code(PASSO4, label='Passo 4: il programma completo')}
    <h3>5. Prova con casi diversi</h3>
    <p>Si inseriscono i valori 8, 6 e 4. Il valore 6 è il più significativo, in quanto costituisce il confine tra sufficienza e insufficienza; se tutti i casi producono il risultato atteso, il programma è corretto.</p>
    <p>L'istruzione <code>if</code>/<code>else</code> è approfondita in <a href="articolo-if-else-python.html">if, elif ed else in Python</a>; <code>input()</code> e le variabili in <a href="articolo-variabili-python.html">le variabili in Python</a>. Per esercitarsi è disponibile l'<a href="esercizio-media-voti-python.html">esercizio sulla media dei voti</a>, con editor integrato.</p>

    <h2 id="pdp">Il PDP in ambito informatico</h2>
    <p>Per gli studenti con DSA il <strong>PDP</strong> è obbligatorio a seguito della presentazione della diagnosi. È redatto dal consiglio di classe con la famiglia entro il primo trimestre dell'anno scolastico o, se la diagnosi è successiva, nel più breve tempo possibile, e contiene strumenti compensativi, misure dispensative e criteri di verifica e valutazione. Il quadro completo è in <a href="articolo-pdp-passo-dopo-passo.html">Il Piano Didattico Personalizzato (PDP)</a>.</p>
    <p>Le misure seguenti, riferite all'informatica, sono esemplificative e vanno calibrate sul singolo studente.</p>
    <h3>Strumenti compensativi</h3>
    <ul>
      <li>svolgimento delle prove di programmazione al computer, con un editor, anziché per iscritto;</li>
      <li>evidenziazione della sintassi e completamento automatico attivi durante le prove;</li>
      <li>scheda personale della sintassi o formulario;</li>
      <li>diagrammi di flusso e mappe durante verifiche e interrogazioni;</li>
      <li>sintesi vocale per la lettura di testi e consegne.</li>
    </ul>
    <h3>Misure dispensative</h3>
    <ul>
      <li>tempi più lunghi o riduzione quantitativa delle consegne, a parità di obiettivi;</li>
      <li>dispensa dalla copiatura di codice esteso dalla lavagna, con fornitura degli esempi in formato digitale;</li>
      <li>dispensa dalla lettura ad alta voce in classe.</li>
    </ul>
    <h3>Verifica e valutazione</h3>
    <ul>
      <li>valutazione centrata sul ragionamento più che sulla forma: un errore di digitazione non dovrebbe pesare quanto un errore logico;</li>
      <li>verifiche programmate e consegne brevi, con una richiesta per volta;</li>
      <li>possibilità di integrare la prova scritta con una prova orale.</li>
    </ul>
    <p>All'<strong>esame di maturità</strong> la commissione definisce le modalità di svolgimento delle prove sulla base del PDP (art. 20 del D.Lgs. 62/2017). Negli scritti possono essere concessi tempi più lunghi e possono essere utilizzati gli strumenti compensativi del PDP già impiegati nelle verifiche durante l'anno, o altri ritenuti funzionali dalla commissione, purché non ne risulti alterato l'oggetto della prova: di qui l'importanza di un uso regolare e non occasionale.</p>
    <p>Alcuni accorgimenti didattici giovano agli studenti con DSA e, in generale, all'intera classe: la condivisione degli esempi in formato digitale, consegne brevi con una richiesta per riga, la presentazione del diagramma prima del codice e la sperimentazione immediata al computer.</p>
    <p class="norme rt-skip">Riferimenti normativi: L. 170/2010; D.M. 5669/2011 e Linee guida allegate; D.Lgs. 62/2017, art. 20 (esame di maturità per gli studenti con DSA).</p>

    <h2 id="sintesi">Considerazioni conclusive</h2>
    <ul>
      <li>Un DSA non preclude l'apprendimento della programmazione, fondata soprattutto sul ragionamento.</li>
      <li>Le criticità riguardano la lettura del codice, la discriminazione di caratteri simili, la correttezza formale e la scrittura a mano.</li>
      <li>Editor di codice, carattere tipografico adeguato, diagrammi, sintesi vocale, scheda della sintassi e uso consapevole dell'intelligenza artificiale riducono in misura significativa il carico.</li>
      <li>Procedere per incrementi, partire dagli esempi e leggere con metodo i messaggi di errore sono strategie decisive.</li>
      <li>Le misure vanno formalizzate nel PDP e impiegate con regolarità, anche in vista dell'esame di maturità.</li>
    </ul>
    <p>La chiave non consiste nel contrastare le difficoltà, ma nell'aggirarle con gli strumenti appropriati. Qualora le difficoltà persistano, il PDP può essere rivisto; in assenza di diagnosi, in caso di sospetto DSA, è opportuno che la famiglia si rivolga alla scuola e al medico per una valutazione specialistica.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Programmare un passo alla volta</h2>
      <p>Le lezioni gratuite del sito propongono esempi brevi e modificabili, con l'editor «Provalo tu» integrato nel browser.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai un DSA e vuoi farmi una domanda, o raccontarmi come studi informatica? <a href="contatti.html">Scrivimi</a>: leggo tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
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
    keywords="informatica DSA, DSA programmazione, L. 170/2010, strumenti compensativi informatica, dislessia programmazione, PDP informatica, studiare informatica con DSA, misure dispensative informatica",
    og_alt="Il titolo «Informatica e DSA», un pezzo di puzzle con le parentesi graffe del codice e un breve programma Python che scrive «Ce la fai!».",
    date_iso="2026-11-08", date_it="8 novembre 2026", modified_iso="2026-11-21",
    ld_keywords="DSA, dislessia, strumenti compensativi, misure dispensative, PDP, programmazione, informatica",
    hero_src="articolo-informatica-dsa.jpg",
    no_rt_note=True, no_tool_icons=True,   # stile professionale (dal 21/11/2026)
    hero_alt="Copertina dell'articolo: il titolo «Informatica e DSA», un pezzo di puzzle con dentro le parentesi graffe del codice e un breve programma Python che scrive «Ce la fai!».",
)
if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, 'articolo-informatica-dsa.html'), 'w', encoding='utf-8').write(page(META))
    print('DSA: parole', words, '| minuti', MIN)
