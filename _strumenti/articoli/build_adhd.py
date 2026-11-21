#!/usr/bin/env python3
"""Articolo della serie inclusione: ADHD e programmazione (stile professionale, riscritto il 21/11/2026)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-adhd-programmazione"
TITLE = "ADHD e programmazione: strategie didattiche per l'apprendimento dell'informatica"
SEO_TITLE = "ADHD e programmazione: strategie didattiche — AlessandroSimone.it"
DESC = "ADHD a scuola: inquadramento, PDP e PEI, strategie per l'apprendimento della programmazione, un esempio in Python e indicazioni per docenti e famiglie."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

MEDIA = '''
# Passo 1: chiedo tre voti
voto1 = float(input("Primo voto: "))
voto2 = float(input("Secondo voto: "))
voto3 = float(input("Terzo voto: "))

# Passo 2: calcolo la media (arrotondata a un decimale)
media = round((voto1 + voto2 + voto3) / 3, 1)

# Passo 3: stampo il risultato
print("Media:", media)

# Passo 4: aggiungo un messaggio
if media >= 6:
    print("Sufficiente")
else:
    print("Da recuperare")
'''

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Lo studente con ADHD ha diritto al PDP?",
        "L'ADHD non rientra nell'ambito della L. 170/2010: la predisposizione del PDP è rimessa alla deliberazione motivata del consiglio di classe (Nota 2563/2013). In presenza di un DSA associato il PDP è obbligatorio; nei casi più gravi può essere riconosciuta una disabilità ai sensi della L. 104/92, con conseguente redazione del PEI."),
    faq("Chi formula la diagnosi di ADHD?",
        "La diagnosi compete agli specialisti, di norma il servizio di neuropsichiatria dell'infanzia e dell'adolescenza dell'ASL (Azienda sanitaria locale) o un centro accreditato; dopo il compimento della maggiore età il riferimento sono i servizi per l'età adulta, ad esempio il Centro di salute mentale. Il primo interlocutore è il medico di medicina generale o il pediatra."),
    faq("Qual è il ruolo della scuola rispetto ai trattamenti farmacologici?",
        "Le decisioni terapeutiche competono esclusivamente agli specialisti. Qualora un farmaco debba essere assunto in orario scolastico, la famiglia presenta richiesta scritta al dirigente scolastico, corredata dalla prescrizione medica, secondo le Raccomandazioni del 25 novembre 2005 e gli eventuali protocolli regionali."),
    faq("Timer e cuffie possono essere utilizzati in classe?",
        "Sì, se previsti dal PDP. Si ricordi che nella secondaria di secondo grado l'uso dello smartphone in classe è vietato dalla Circ. MIM 3392/2025, salvo i casi previsti dal PEI o dal PDP: un timer autonomo può risultare più agevole da integrare."),
    faq("L'intelligenza artificiale può costituire un supporto?",
        "Sì, se impiegata come tutor: ad esempio per scomporre un esercizio articolato in passaggi o per chiarire un messaggio di errore, non per generare il programma. Un approfondimento è disponibile in <a href=\"articolo-chatgpt-studiare.html\">Come usare ChatGPT per studiare</a>."),
    faq("Lo studente è tenuto a informare i compagni della diagnosi?",
        "No. Si tratta di una scelta personale dello studente e della famiglia: i dati sanitari sono riservati e i docenti non possono comunicarli senza il consenso dell'interessato e della famiglia."),
    faq("Quale regime si applica all'esame di maturità?",
        "Se il consiglio di classe ha predisposto un PDP, si applica il regime degli altri BES: non sono previste misure dispensative né tempi aggiuntivi, mentre sono ammessi gli strumenti compensativi indicati nel PDP e utilizzati durante l'anno. In presenza di un DSA associato si applica il regime dei DSA, che prevede anche tempi più lunghi; in presenza di disabilità certificata, quello del PEI. I dettagli sono in <a href=\"articolo-pdp-passo-dopo-passo.html#verifiche\">Il Piano Didattico Personalizzato (PDP)</a>."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <p>L'<strong>ADHD</strong> (Attention Deficit Hyperactivity Disorder, disturbo da deficit di attenzione e iperattività) incide sulla regolazione dell'attenzione, dell'attività motoria e dell'impulsività. Non dipende dalla volontà né costituisce un problema di comportamento in senso disciplinare.</p>
    <p>La programmazione presenta caratteristiche che possono favorire gli studenti con ADHD, insieme ad altre che ne espongono le fragilità. Come docente per l'inclusività (<a href="/#chi-sono">chi sono</a>), e avendo insegnato informatica per anni, propongo in questo contributo un inquadramento normativo, alcune strategie didattiche e un esempio operativo, con indicazioni rivolte a docenti, famiglie e studenti.</p>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title">Indice</h2>
      <ol>
        <li><a href="#cos-e">Inquadramento clinico</a></li>
        <li><a href="#scuola">L'ADHD a scuola: PDP o PEI</a></li>
        <li><a href="#programmazione">Programmazione: punti di forza e criticità</a></li>
        <li><a href="#strategie">Strategie per l'apprendimento della programmazione</a></li>
        <li><a href="#esempio">Un esempio: la scomposizione in passi</a></li>
        <li><a href="#verifiche">Le prove di verifica</a></li>
        <li><a href="#docenti">Indicazioni per docenti e famiglie</a></li>
        <li><a href="#falsi-miti">Alcuni fraintendimenti ricorrenti</a></li>
        <li><a href="#sintesi">Considerazioni conclusive</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <h2 id="cos-e">Inquadramento clinico</h2>
    <p>L'ADHD è un disturbo del <strong>neurosviluppo</strong>. La letteratura clinica ne descrive tre presentazioni:</p>
    <ul>
      <li><strong>prevalentemente disattentiva</strong>: difficoltà a mantenere l'attenzione, a cogliere i dettagli, a organizzare il lavoro, con facile distraibilità;</li>
      <li><strong>prevalentemente iperattiva-impulsiva</strong>: difficoltà a rimanere fermi, tendenza a interrompere e a rispondere prima del completamento della domanda;</li>
      <li><strong>combinata</strong>, in cui coesistono entrambe le componenti, con intensità variabile.</li>
    </ul>
    <p>L'ADHD si associa frequentemente ad altre condizioni, tra cui i DSA (Disturbi Specifici dell'Apprendimento), trattati in <a href="articolo-informatica-dsa.html">Informatica e DSA</a>. La distraibilità, peraltro, è esperienza comune: la diagnosi richiede che le difficoltà siano persistenti, pervasive e funzionalmente rilevanti, e compete esclusivamente agli specialisti.</p>

    <h2 id="scuola">L'ADHD a scuola: PDP o PEI</h2>
    <p>Sul piano scolastico l'ADHD rientra tra gli <strong>altri BES</strong> (Bisogni Educativi Speciali), secondo la Direttiva ministeriale 27 dicembre 2012, che lo annovera tra i disturbi evolutivi specifici; indicazioni didattiche specifiche erano già contenute nella Nota ministeriale 4089/2010. Le distinzioni tra i diversi regimi sono illustrate in <a href="articolo-bes-dsa-disabilita.html">Disabilità 104, DSA e BES</a>.</p>
    <p>La predisposizione del <strong>PDP</strong> è rimessa al consiglio di classe, che motiva a verbale la propria decisione (Nota 2563/2013). Due situazioni modificano il quadro:</p>
    <ul>
      <li>in presenza di un <strong>DSA associato</strong>, il PDP è obbligatorio ai sensi della L. 170/2010;</li>
      <li>nei casi più gravi, anche per comorbilità, può essere riconosciuta una <strong>disabilità</strong> ai sensi della L. 104/92: in tal caso si redige il PEI (Piano Educativo Individualizzato) e alla classe è assegnato il <a href="articolo-docente-di-sostegno.html">docente di sostegno</a>.</li>
    </ul>
    <p>Per avviare il procedimento è opportuno presentare la diagnosi in segreteria, con protocollazione, e chiedere un incontro al coordinatore di classe. Nella secondaria di secondo grado lo studente può partecipare alla definizione delle misure. I due documenti sono descritti in <a href="articolo-pdp-passo-dopo-passo.html">Il Piano Didattico Personalizzato (PDP)</a> e in <a href="articolo-pei-spiegato-semplice.html">Il Piano Educativo Individualizzato (PEI)</a>.</p>

    <h2 id="programmazione">Programmazione: punti di forza e criticità</h2>
    <p>Tra le caratteristiche della programmazione favorevoli agli studenti con ADHD:</p>
    <ul>
      <li>il <strong>riscontro immediato</strong> dell'esecuzione del codice;</li>
      <li>la possibilità di procedere per <strong>incrementi successivi</strong>;</li>
      <li>la natura gratificante della risoluzione dei singoli errori;</li>
      <li>lo spazio lasciato alla <strong>creatività</strong>, potendo un problema ammettere più soluzioni.</li>
    </ul>
    <p>Tra le criticità più frequenti:</p>
    <ul>
      <li>gli <strong>errori di distrazione</strong>, come parentesi o due punti omessi;</li>
      <li>le <strong>consegne articolate</strong> in molte richieste contestuali;</li>
      <li>le fasi di ricerca degli errori, percepite come ripetitive;</li>
      <li>la difficoltà a percepire lo scorrere del tempo quando l'attività è coinvolgente.</li>
    </ul>

    <h2 id="strategie">Strategie per l'apprendimento della programmazione</h2>
    <p>Le strategie seguenti vanno sperimentate progressivamente, mantenendo quelle che si rivelano efficaci per il singolo studente.</p>
    <h3>Scomposizione del problema</h3>
    <p>Prima della codifica, il problema va scomposto in passaggi elementari, formulati in linguaggio naturale e affrontati uno alla volta. Il <a href="articolo-diagramma-di-flusso.html">diagramma di flusso</a> offre un supporto visivo efficace.</p>
    <h3>Organizzazione del lavoro per intervalli</h3>
    <p>Il lavoro può essere articolato in intervalli brevi, ad esempio di 20-25 minuti, seguiti da pause di circa 5 minuti; se necessario, si parte da intervalli di 10-15 minuti. È preferibile un timer autonomo rispetto allo smartphone. Le pause dovrebbero prevedere movimento, che favorisce la ripresa dell'attenzione.</p>
    <h3>Riduzione dei distrattori</h3>
    <p>È opportuno disattivare le notifiche e mantenere aperti soltanto l'editor e la consegna. Visual Studio Code dispone della <strong>modalità Zen</strong>, che nasconde ogni elemento diverso dal codice: si attiva da Visualizza, Aspetto, Modalità Zen, oppure con Ctrl+K seguito da Z, e si disattiva premendo due volte Esc. Poiché la modalità nasconde anche il terminale, l'output si visualizza con Ctrl+J.</p>
    <h3>Esecuzione frequente del codice</h3>
    <p>Anziché scrivere l'intero programma e verificarlo al termine, è preferibile scrivere poche istruzioni ed eseguirle subito: il riscontro è immediato e gli errori emergono quando sono ancora circoscritti.</p>
    <h3>Lista di controllo degli errori</h3>
    <p>Molti errori derivano dalla distrazione più che da lacune concettuali. Una lista di controllo consente allo studente di individuarli autonomamente; per Python, ad esempio:</p>
    <ol>
      <li>sono presenti i due punti dopo <code>if</code>, <code>elif</code>, <code>else</code>, <code>for</code>, <code>while</code> e <code>def</code>?</li>
      <li>l'indentazione all'interno di ciascun blocco è uniforme?</li>
      <li>ogni parentesi e ogni virgoletta aperta è stata chiusa?</li>
      <li>i nomi delle variabili sono scritti in modo coerente, comprese maiuscole e minuscole?</li>
      <li>è stato usato <code>==</code> per il confronto e <code>=</code> per l'assegnazione?</li>
      <li>il file è stato salvato prima dell'esecuzione?</li>
    </ol>
    <p>Ulteriori tecniche sono illustrate in <a href="articolo-debug.html">Come trovare e correggere i bug nel codice</a>.</p>
    <h3>Gestione dell'iperfocalizzazione</h3>
    <p>Molte persone con ADHD riferiscono anche la condizione opposta: un compito coinvolgente può assorbire l'attenzione al punto da far perdere la percezione del tempo, fenomeno spesso definito <strong>iperfocalizzazione</strong>. Può costituire una risorsa, ma rischia di sottrarre tempo ad altre attività: un promemoria temporale aiuta a interrompere il lavoro al momento opportuno.</p>

    <h2 id="esempio">Un esempio: la scomposizione in passi</h2>
    <p>Il compito proposto consiste nel richiedere tre voti, calcolarne la media e indicare se risulta sufficiente. Applicando la scomposizione e l'esecuzione frequente, il programma viene costruito in quattro passi, verificando il funzionamento dopo ciascuno di essi.</p>
    {code(MEDIA, label="Programma in Python diviso in quattro passi: chiede tre voti, calcola la media, la stampa e aggiunge un messaggio")}
    <p>I voti vanno inseriti con il punto come separatore decimale, ad esempio <code>6.5</code> e non <code>6,5</code>: Python non accetta la virgola. I commenti, introdotti da <code>#</code>, segnalano il punto di avanzamento e facilitano la ripresa del lavoro dopo un'interruzione.</p>
    <p>Per un ripasso delle strutture condizionali si veda <a href="articolo-if-else-python.html">if, elif e else in Python</a>.</p>

    <h2 id="verifiche">Le prove di verifica</h2>
    <p>Durante le prove alcune abitudini risultano particolarmente utili:</p>
    <ul>
      <li>leggere integralmente la consegna prima di iniziare, evidenziando le richieste;</li>
      <li>affrontare una domanda alla volta, contrassegnando quelle completate;</li>
      <li>riservare gli ultimi minuti alla lista di controllo degli errori di distrazione;</li>
      <li>chiedere chiarimenti al docente in caso di dubbio sulla consegna.</li>
    </ul>

    <h2 id="docenti">Indicazioni per docenti e famiglie</h2>
    <p>Le misure seguenti sono esemplificative e vanno calibrate sul singolo studente, anche in sede di PDP.</p>
    <h3>In classe e in laboratorio</h3>
    <ul>
      <li>consegne scritte, brevi, articolate in una richiesta alla volta;</li>
      <li>collocazione lontana da fonti di distrazione e vicina al docente;</li>
      <li>routine chiare di apertura e chiusura della lezione;</li>
      <li>pause brevi programmate o incarichi che consentano il movimento;</li>
      <li>riscontri frequenti e positivi sul lavoro svolto.</li>
    </ul>
    <h3>Nelle verifiche</h3>
    <ul>
      <li>prove suddivise in sezioni, con una consegna per volta;</li>
      <li>tempi aggiuntivi o riduzione quantitativa delle consegne a parità di obiettivi, durante l'anno scolastico;</li>
      <li>programmazione delle prove, evitandone la sovrapposizione nella stessa giornata;</li>
      <li>possibilità di compensazione orale;</li>
      <li>valutazione centrata sulla correttezza logica più che sugli errori di distrazione.</li>
    </ul>
    <p>Si tenga presente che all'esame di maturità, per gli altri BES, non sono previsti tempi aggiuntivi né misure dispensative, ma solo gli strumenti compensativi indicati nel PDP e utilizzati in corso d'anno: è opportuno non generare aspettative non corrispondenti alla disciplina dell'esame.</p>
    <p>In laboratorio risulta efficace la <strong>programmazione in coppia</strong>: uno studente scrive il codice (il «pilota»), l'altro legge, verifica e suggerisce (il «navigatore»), con scambio dei ruoli a intervalli brevi. L'abbinamento va scelto con attenzione.</p>
    <p>In ambito familiare giovano una postazione di studio stabile, orari regolari e un'agenda dei compiti condivisa, senza sostituirsi allo studente nello svolgimento. Per i casi in cui il PDP non venga predisposto o applicato si rinvia alle <a href="articolo-pdp-passo-dopo-passo.html#faq">domande frequenti sul PDP</a>.</p>

    <h2 id="falsi-miti">Alcuni fraintendimenti ricorrenti</h2>
    <p>Sgombriamo il campo da alcuni equivoci diffusi.</p>
    <p><strong>«Basterebbe un maggiore impegno».</strong> L'ADHD non dipende dalla volontà: richiede strategie e supporti adeguati, non richiami.</p>
    <p><strong>«Se si concentra sui videogiochi, non ha l'ADHD».</strong> Con l'ADHD è più difficile sostenere l'attenzione su attività poco gratificanti; i videogiochi offrono ricompense immediate e continue, che la catturano con particolare efficacia.</p>
    <p><strong>«Con la crescita l'ADHD scompare».</strong> In molte persone persiste in età adulta, pur modificandosi nelle sue manifestazioni: di qui l'utilità di strategie durature.</p>
    <p><strong>«L'ADHD preclude una carriera nella programmazione».</strong> Non vi è alcuna ragione per ritenerlo: con strategie adeguate, la programmazione può diventare un punto di forza.</p>

    <h2 id="sintesi">Considerazioni conclusive</h2>
    <ul>
      <li>L'ADHD è un disturbo del neurosviluppo che incide su attenzione, attività motoria e impulsività, indipendentemente dalla volontà.</li>
      <li>A scuola rientra tra gli altri BES: il PDP è rimesso alla deliberazione motivata del consiglio di classe ed è obbligatorio in presenza di un DSA associato.</li>
      <li>Nell'apprendimento della programmazione risultano efficaci la scomposizione dei problemi, il lavoro per intervalli, la riduzione dei distrattori e l'esecuzione frequente del codice.</li>
      <li>Una lista di controllo favorisce l'individuazione autonoma degli errori di distrazione.</li>
      <li>All'esame di maturità il regime degli altri BES non prevede tempi aggiuntivi né misure dispensative.</li>
    </ul>
    <p>L'ADHD non definisce ciò che uno studente può diventare: indica soltanto la necessità di un percorso costruito sulle sue caratteristiche.</p>
    <p class="norme rt-skip">Riferimenti normativi: Nota ministeriale 4089/2010 (alunni con ADHD); L. 170/2010 (in caso di DSA associato); Direttiva ministeriale 27 dicembre 2012 (BES e disturbi evolutivi specifici); C.M. 8/2013; Nota ministeriale 2563/2013; L. 104/92 (nei casi in cui è riconosciuta una disabilità); Circ. MIM 3392/2025 (uso del cellulare a scuola); Raccomandazioni MIUR e Ministero della Salute 25 novembre 2005 (somministrazione dei farmaci a scuola); ordinanza ministeriale annuale sull'esame di maturità. Aggiornato al 19 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Programmare un passo alla volta</h2>
      <p>Le lezioni gratuite del sito propongono esempi brevi e modificabili, con l'editor «Provalo tu» integrato nel browser.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai l'ADHD e studi informatica, o insegni a uno studente con ADHD? Hai una strategia che funziona e vuoi raccontarmela? <a href="contatti.html">Scrivimi</a>: rispondo a tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-informatica-dsa.html"><span aria-hidden="true">📖</span><strong>Informatica e DSA: strategie e strumenti compensativi</strong></a>
        <a href="articolo-pdp-passo-dopo-passo.html"><span aria-hidden="true">📝</span><strong>Il Piano Didattico Personalizzato (PDP): destinatari, elaborazione e contenuti</strong></a>
        <a href="articolo-tecnologie-assistive.html"><span aria-hidden="true">🛠️</span><strong>Le tecnologie assistive a scuola: tipologie, accesso e integrazione didattica</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="ADHD programmazione, ADHD informatica, ADHD scuola, ADHD PDP, strategie didattiche ADHD, deficit di attenzione e iperattività, BES",
    og_alt="Il titolo «ADHD e programmazione» con il sottotitolo «Strategie didattiche per l'informatica» e tre riquadri: destinatari, studenti con ADHD; strategie, scomposizione e intervalli; a scuola, PDP se deliberato.",
    date_iso="2026-11-19", modified_iso="2026-11-21", date_it="19 novembre 2026",
    ld_keywords="ADHD, disturbo da deficit di attenzione e iperattività, programmazione, informatica, BES, PDP, strategie didattiche, inclusione scolastica",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «ADHD e programmazione» con il sottotitolo «Strategie didattiche per l'informatica» e tre riquadri: destinatari, studenti con ADHD; strategie, scomposizione e intervalli; a scuola, PDP se deliberato.",
    no_rt_note=True, no_tool_icons=True,   # stile professionale (dal 21/11/2026)
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('ADHD: parole', words, '| minuti', MIN)
