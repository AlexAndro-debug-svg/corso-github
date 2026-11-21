#!/usr/bin/env python3
"""Articolo della serie inclusione: il PDP (stile professionale, riscritto il 21/11/2026)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-pdp-passo-dopo-passo"
TITLE = "Il Piano Didattico Personalizzato (PDP): destinatari, elaborazione e contenuti per DSA e altri BES"
SEO_TITLE = "Il PDP per DSA e altri BES: elaborazione e contenuti — AlessandroSimone.it"
DESC = "Destinatari, tempi, contenuti minimi e valutazione del PDP per DSA e altri BES; dispensa ed esonero dalle lingue straniere; il PDP all'esame di maturità."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Il PDP è dovuto anche se il rendimento scolastico è buono?",
        "Sì. Una volta acquisita la diagnosi di DSA, la predisposizione del PDP è obbligatoria. Il documento può tuttavia essere essenziale e prevedere poche misure: la sua funzione è descrivere ciò che serve a quello specifico studente, non di più."),
    faq("Una diagnosi rilasciata da uno specialista privato è valida?",
        "La diagnosi deve essere rilasciata dal Servizio sanitario nazionale o, ove la Regione lo preveda, da strutture e professionisti accreditati (art. 3 della L. 170/2010; Accordo Stato-Regioni 25 luglio 2012). Poiché la disciplina varia da regione a regione, è opportuno verificarne la validità con l'ASL o con la scuola. Nelle more del rilascio di una certificazione valida, il consiglio di classe può comunque adottare le misure ritenute necessarie (C.M. 8/2013)."),
    faq("Entro quando va presentata la diagnosi negli anni conclusivi?",
        "Negli anni terminali di ciascun ciclo, la diagnosi va presentata di norma entro il 31 marzo, in ragione degli adempimenti connessi all'esame. Fa eccezione la prima certificazione, che può essere rilasciata in qualunque momento dell'anno; per le diagnosi successive al 31 marzo, tuttavia, le prassi delle scuole non sono uniformi ed è opportuno un confronto tempestivo con l'istituto."),
    faq("Per lo studente con ADHD il PDP è obbligatorio?",
        "L'ADHD non rientra nell'ambito della L. 170/2010: la decisione di predisporre un PDP spetta al consiglio di classe, che è tenuto a motivarla a verbale (Nota 2563/2013). In presenza di un DSA associato il PDP è obbligatorio; nei casi più gravi può essere riconosciuta una disabilità, con conseguente redazione del PEI. Indicazioni didattiche specifiche sono contenute in <a href=\"articolo-adhd-programmazione.html\">ADHD e programmazione</a>."),
    faq("Chi sottoscrive il PDP?",
        "Il PDP è di norma sottoscritto dal dirigente scolastico, dai docenti del consiglio di classe e dalla famiglia; per gli altri BES la sottoscrizione è espressamente prevista dalla C.M. 8/2013. La firma della famiglia attesta la condivisione del documento: prima di sottoscriverlo è legittimo chiedere integrazioni e, in caso di disaccordo, un nuovo incontro con il consiglio di classe."),
    faq("Che cosa fare se il PDP non viene predisposto o non viene applicato?",
        "È opportuno rivolgersi in prima istanza al docente della disciplina o al coordinatore di classe, quindi al referente per l'inclusione. Qualora il problema persista, in particolare se il PDP non risulta predisposto al termine del primo trimestre, è consigliabile una segnalazione scritta al dirigente scolastico."),
    faq("Il PDP compare sul diploma? Ha validità all'università?",
        "No: il diploma non reca menzione del PDP né delle modalità di svolgimento delle prove. Il PDP non ha validità nel contesto universitario, dove tuttavia la L. 170/2010 (art. 5, comma 4) garantisce misure specifiche, anche per i test di ammissione, da richiedere all'ufficio di ateneo competente presentando la diagnosi."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <p>Il <strong>PDP</strong> (Piano Didattico Personalizzato) è il documento con cui il consiglio di classe formalizza le scelte didattiche, gli strumenti e i criteri di valutazione per gli studenti con <strong>DSA</strong> (Disturbi Specifici dell'Apprendimento) e, quando lo ritiene necessario, per gli studenti con altri <strong>BES</strong> (Bisogni Educativi Speciali).</p>
    <p>Come docente per l'inclusività faccio parte dei consigli di classe in cui i PDP vengono redatti (<a href="/#chi-sono">chi sono</a>). In questo contributo ricostruisco il quadro normativo, i tempi, i contenuti minimi e le principali questioni applicative, con un'attenzione particolare ai profili che più spesso generano incertezze.</p>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title">Indice</h2>
      <ol>
        <li><a href="#cos-e">Natura e destinatari</a></li>
        <li><a href="#chi-quando">Redazione e tempi</a></li>
        <li><a href="#percorso">Le fasi del procedimento</a></li>
        <li><a href="#dentro">I contenuti minimi</a></li>
        <li><a href="#strumenti">Strumenti compensativi e misure dispensative</a></li>
        <li><a href="#verifiche">Verifica e valutazione</a></li>
        <li><a href="#lingue">Le lingue straniere: dispensa ed esonero</a></li>
        <li><a href="#altri-bes">Il PDP per gli altri BES</a></li>
        <li><a href="#firmare">Criteri di lettura prima della sottoscrizione</a></li>
        <li><a href="#falsi-miti">Alcuni fraintendimenti ricorrenti</a></li>
        <li><a href="#informatica">Un esempio disciplinare: l'informatica</a></li>
        <li><a href="#sintesi">Considerazioni conclusive</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <h2 id="cos-e">Natura e destinatari</h2>
    <p>Il PDP si colloca nel quadro della <strong>L. 170/2010</strong>, che riconosce dislessia, disortografia, disgrafia e discalculia come disturbi specifici dell'apprendimento, e del <strong>D.M. 5669/2011</strong>, con le annesse Linee guida.</p>
    <p>I destinatari sono due, con regimi giuridici distinti:</p>
    <ul>
      <li><strong>studenti con DSA</strong>: a seguito della presentazione della diagnosi, la predisposizione del PDP è <strong>obbligatoria</strong>. Gli obiettivi di apprendimento restano quelli della classe; ciò che si personalizza sono le strategie, gli strumenti e le modalità di verifica;</li>
      <li><strong>studenti con altri BES</strong> (ad esempio con ADHD, disturbo da deficit di attenzione e iperattività, o in situazione di svantaggio linguistico): il PDP è predisposto se il consiglio di classe lo ritiene necessario, ai sensi della Direttiva ministeriale 27 dicembre 2012 e della C.M. 8/2013, spesso con carattere temporaneo.</li>
    </ul>
    <p>Per gli studenti con disabilità certificata ai sensi della L. 104/92 lo strumento di riferimento è invece il PEI (Piano Educativo Individualizzato), illustrato nell'articolo <a href="articolo-pei-spiegato-semplice.html">Il Piano Educativo Individualizzato (PEI)</a>.</p>

    <h2 id="chi-quando">Redazione e tempi</h2>
    <p>Il PDP è redatto dal <strong>consiglio di classe</strong>; di norma il coordinatore raccoglie i contributi dei colleghi e cura la stesura del documento. La <strong>famiglia</strong> partecipa all'elaborazione, apportando la diagnosi, le indicazioni degli specialisti e la conoscenza del contesto extrascolastico.</p>
    <p>Nella secondaria di secondo grado è particolarmente opportuno coinvolgere anche lo <strong>studente</strong>, primo utilizzatore degli strumenti previsti e interlocutore privilegiato nel valutarne l'efficacia.</p>
    <p>Per i DSA, le Linee guida del 2011 prevedono che il PDP sia predisposto <strong>entro il primo trimestre</strong> dell'anno scolastico; in caso di diagnosi presentata in corso d'anno, nel più breve tempo possibile.</p>
    <p>Il documento ha validità annuale ed è aggiornato ogni anno, in ragione dell'evoluzione dello studente e del curricolo. Contenendo dati relativi alla salute, è soggetto a <strong>riservatezza</strong>: è noto ai docenti e alla famiglia, non al gruppo classe.</p>

    <h2 id="percorso">Le fasi del procedimento</h2>
    <h3>Studenti con DSA</h3>
    <ol>
      <li>valutazione specialistica e diagnosi, presso il Servizio sanitario o specialisti accreditati;</li>
      <li>presentazione della diagnosi alla segreteria della scuola, con protocollazione;</li>
      <li>osservazione da parte del consiglio di classe e incontro con la famiglia;</li>
      <li>redazione del PDP entro il primo trimestre, o tempestivamente se la diagnosi è successiva;</li>
      <li>monitoraggio in corso d'anno e aggiornamento all'inizio dell'anno successivo.</li>
    </ol>
    <h3>Studenti con altri BES</h3>
    <ol>
      <li>rilevazione del bisogno da parte dei docenti o presentazione di documentazione clinica da parte della famiglia;</li>
      <li>confronto del consiglio di classe con la famiglia;</li>
      <li>deliberazione motivata, a verbale, sulla predisposizione del PDP;</li>
      <li>eventuale redazione del PDP, anche per un periodo limitato;</li>
      <li>mancato rinnovo, una volta superata la condizione di difficoltà.</li>
    </ol>
    <p>Qualora si sospetti un DSA, il primo riferimento è il medico di medicina generale o il pediatra, che può indirizzare al servizio di neuropsichiatria dell'infanzia e dell'adolescenza dell'ASL (Azienda sanitaria locale) o a un centro accreditato.</p>

    <h2 id="dentro">I contenuti minimi</h2>
    <p>Pur in assenza di un modello nazionale vincolante, le Linee guida del 2011 indicano le voci che il PDP deve contenere, articolate per le discipline coinvolte dal disturbo:</p>
    <ol>
      <li><strong>dati anagrafici</strong> dello studente;</li>
      <li><strong>tipologia di disturbo</strong>, con la descrizione del funzionamento e dei punti di forza;</li>
      <li><strong>attività didattiche individualizzate</strong>, volte al raggiungimento degli obiettivi comuni;</li>
      <li><strong>attività didattiche personalizzate</strong>, fondate su metodologie diversificate;</li>
      <li><strong>strumenti compensativi</strong> utilizzati;</li>
      <li><strong>misure dispensative</strong> adottate;</li>
      <li><strong>forme di verifica e valutazione</strong> personalizzate.</li>
    </ol>
    <p>Un PDP efficace si distingue per la specificità delle indicazioni: non si limita a richiamare strumenti generici, ma precisa in quali discipline, in quali situazioni e con quali modalità essi trovano applicazione.</p>

    <h2 id="strumenti">Strumenti compensativi e misure dispensative</h2>
    <p>Gli <strong>strumenti compensativi</strong> sollevano lo studente da una prestazione resa difficoltosa dal disturbo, senza facilitare il compito sul piano cognitivo. Tra i più diffusi:</p>
    <ul>
      <li>sintesi vocale;</li>
      <li>programmi di videoscrittura con correttore ortografico;</li>
      <li>calcolatrice e formulari;</li>
      <li>mappe concettuali e schemi;</li>
      <li>registrazione delle lezioni, a soli fini di studio e nel rispetto della disciplina sulla protezione dei dati.</li>
    </ul>
    <p>Le <strong>misure dispensative</strong> esonerano lo studente da prestazioni che, a causa del disturbo, risulterebbero particolarmente onerose senza apportare un beneficio formativo, fermi restando gli obiettivi. Tra le più frequenti:</p>
    <ul>
      <li>lettura ad alta voce in classe;</li>
      <li>scrittura sotto dettatura veloce;</li>
      <li>copiatura di testi estesi dalla lavagna;</li>
      <li>memorizzazione di sequenze, elenchi e tabelline;</li>
      <li>svolgimento di più prove nella stessa giornata.</li>
    </ul>
    <p>L'efficacia degli strumenti dipende dalla loro adozione sistematica, a scuola e a casa, e non dal loro impiego occasionale in sede di verifica. Una rassegna ragionata è disponibile in <a href="articolo-informatica-dsa.html#strumenti">Informatica e DSA</a>; le modalità per ottenerli sono descritte in <a href="articolo-tecnologie-assistive.html#come-averle">Le tecnologie assistive a scuola</a>.</p>

    <h2 id="verifiche">Verifica e valutazione</h2>
    <p>Il PDP definisce le modalità di verifica e i criteri di valutazione. Tra le misure più ricorrenti:</p>
    <ul>
      <li>programmazione delle verifiche, evitando la sovrapposizione di più prove nella stessa giornata;</li>
      <li>tempi aggiuntivi o, in alternativa, riduzione quantitativa delle consegne a parità di obiettivi;</li>
      <li>lettura delle consegne da parte del docente o mediante sintesi vocale;</li>
      <li>compensazione orale delle prove scritte;</li>
      <li>valutazione del contenuto piuttosto che della forma, ad esempio non penalizzando gli errori ortografici in presenza di disortografia.</li>
    </ul>
    <p>Una valutazione personalizzata non equivale a una valutazione indulgente: il suo scopo è misurare gli apprendimenti effettivi, evitando che il disturbo ne alteri la rilevazione.</p>
    <p>All'<strong>esame di maturità</strong> la commissione tiene conto del PDP, ma con regimi distinti (art. 20 del D.Lgs. 62/2017 e ordinanza ministeriale annuale). Per gli studenti con <strong>DSA</strong> sono previsti tempi più lunghi e l'utilizzo degli strumenti compensativi impiegati durante l'anno. Per gli studenti con <strong>altri BES</strong> non sono previste misure dispensative; gli strumenti compensativi sono ammessi solo se indicati nel PDP e già utilizzati in corso d'anno.</p>

    <h2 id="lingue">Le lingue straniere: dispensa ed esonero</h2>
    <p>L'art. 6 del D.M. 5669/2011 disciplina due istituti distinti, con effetti molto diversi sul titolo conseguibile.</p>
    <h3>Dispensa dalle prove scritte</h3>
    <p>Lo studente segue l'insegnamento delle lingue straniere, ma le prove scritte sono sostituite da prove orali, anche in sede d'esame. La dispensa richiede una certificazione che attesti la gravità del disturbo e ne contenga esplicita richiesta, la domanda della famiglia e l'approvazione del consiglio di classe. Può avere carattere temporaneo o permanente e non preclude il conseguimento del diploma.</p>
    <p>Il consiglio di classe valuta con particolare attenzione i percorsi nei quali le lingue straniere hanno carattere caratterizzante, come il liceo linguistico o l'indirizzo turistico.</p>
    <h3>Esonero dall'insegnamento</h3>
    <p>Nei casi di particolare gravità, anche in comorbilità con altri disturbi o patologie, lo studente può essere esonerato dall'insegnamento delle lingue straniere, su richiesta della famiglia e con l'approvazione del consiglio di classe. Il percorso diventa differenziato e si conclude con un <strong>attestato di credito formativo</strong>, che non equivale al diploma, come illustrato nella sezione sui <a href="articolo-pei-spiegato-semplice.html#percorsi">percorsi della secondaria di secondo grado</a>.</p>

    <h2 id="altri-bes">Il PDP per gli altri BES</h2>
    <p>Per gli altri BES il riferimento è costituito dalla Direttiva ministeriale 27 dicembre 2012, dalla C.M. 8/2013 e dalla Nota 2563/2013. Il regime è più flessibile di quello previsto per i DSA.</p>
    <p>La predisposizione del PDP non presuppone una certificazione clinica: il consiglio di classe, sulla base dell'osservazione e del confronto con la famiglia, delibera se adottarlo e motiva in ogni caso la propria scelta a verbale.</p>
    <p>Il PDP può prevedere strumenti compensativi e misure dispensative, di norma con carattere transitorio. Per gli studenti con svantaggio linguistico, la priorità è l'acquisizione della lingua italiana. Superata la condizione di difficoltà, il PDP non viene rinnovato: si tratta di un supporto temporaneo, non di una qualificazione permanente dello studente.</p>

    <h2 id="firmare">Criteri di lettura prima della sottoscrizione</h2>
    <p>Alcuni criteri consentono di valutare la qualità di un PDP prima di sottoscriverlo:</p>
    <ul>
      <li><strong>specificità disciplinare</strong>: le misure sono declinate per le singole discipline o enunciate in modo generico?</li>
      <li><strong>concretezza</strong>: «mappe concettuali nelle interrogazioni di storia» è indicazione ben più utile di un generico «uso di mappe»;</li>
      <li><strong>applicabilità in sede di verifica</strong>: è esplicitato l'uso degli strumenti durante le prove?</li>
      <li><strong>consapevolezza dello studente</strong>: lo studente conosce il contenuto del proprio PDP?</li>
      <li><strong>monitoraggio</strong>: sono previsti momenti di verifica dell'efficacia? È opportuno acquisire copia del documento sottoscritto.</li>
    </ul>

    <h2 id="falsi-miti">Alcuni fraintendimenti ricorrenti</h2>
    <p>Alcune convinzioni sul PDP, ancora diffuse, non trovano riscontro nella normativa.</p>
    <p><strong>«Il PDP comporta un programma semplificato».</strong> Per gli studenti con DSA gli obiettivi coincidono con quelli della classe: la personalizzazione riguarda strumenti, strategie e modalità di verifica.</p>
    <p><strong>«Gli strumenti compensativi equivalgono a un vantaggio indebito».</strong> Gli strumenti compensativi rimuovono un ostacolo strumentale, senza sostituirsi allo studente nell'elaborazione cognitiva: consentono di rilevare ciò che egli effettivamente sa.</p>
    <p><strong>«Il PDP riguarda solo le verifiche».</strong> Il PDP orienta l'intera azione didattica, in classe e nello studio individuale; la sua attuazione compete a tutti i docenti delle discipline coinvolte.</p>
    <p><strong>«Il PDP, una volta redatto, ha validità permanente».</strong> Il documento è aggiornato annualmente e può essere rivisto in corso d'anno.</p>

    <h2 id="informatica">Un esempio disciplinare: l'informatica</h2>
    <p>Avendo insegnato informatica per anni, segnalo alcune misure che il laboratorio rende particolarmente agevoli:</p>
    <ul>
      <li>svolgimento delle verifiche al computer anziché su carta, specie in presenza di disgrafia;</li>
      <li>utilizzo di editor con evidenziazione della sintassi;</li>
      <li>disponibilità di una scheda di sintassi durante le prove;</li>
      <li>valutazione centrata sulla correttezza logica del programma più che sugli errori di digitazione.</li>
    </ul>
    <p>Ulteriori esemplificazioni sono raccolte nella sezione <a href="articolo-informatica-dsa.html#pdp">Cosa si può prevedere nel PDP per l'informatica</a>.</p>

    <h2 id="sintesi">Considerazioni conclusive</h2>
    <ul>
      <li>Per gli studenti con DSA il PDP è obbligatorio e gli obiettivi restano quelli della classe.</li>
      <li>Per gli altri BES la predisposizione è rimessa alla deliberazione motivata del consiglio di classe, spesso con carattere temporaneo.</li>
      <li>Il PDP è redatto dal consiglio di classe con la famiglia; per i DSA entro il primo trimestre.</li>
      <li>Contiene strumenti compensativi, misure dispensative e criteri di verifica e valutazione, declinati per disciplina.</li>
      <li>All'esame di maturità i regimi di DSA e altri BES sono distinti; dispensa ed esonero dalle lingue straniere hanno effetti diversi sul titolo.</li>
    </ul>
    <p>Un PDP efficace non è un adempimento da archiviare, ma uno strumento di lavoro quotidiano, condiviso da scuola, famiglia e studente.</p>
    <p class="norme rt-skip">Riferimenti normativi: L. 170/2010, artt. 2, 3 e 5; D.M. 5669/2011, art. 6, e Linee guida per il diritto allo studio degli alunni e degli studenti con DSA; Accordo Stato-Regioni 25 luglio 2012; Direttiva ministeriale 27 dicembre 2012; C.M. 8/2013; Nota ministeriale 2563/2013; D.Lgs. 62/2017, art. 20; ordinanza ministeriale annuale sull'esame di maturità. Aggiornato al 17 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica per una didattica inclusiva</h2>
      <p>Le lezioni gratuite del sito propongono esempi brevi e modificabili, con l'editor «Provalo tu» integrato nel browser.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai un dubbio sul PDP? Vuoi raccontarmi com'è andata nella tua scuola? <a href="contatti.html">Scrivimi</a>: ogni messaggio mi arriva e lo leggo con attenzione.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-informatica-dsa.html"><span aria-hidden="true">📖</span><strong>Informatica e DSA: strategie e strumenti compensativi</strong></a>
        <a href="articolo-bes-dsa-disabilita.html"><span aria-hidden="true">🧭</span><strong>Disabilità certificata (L. 104/92), DSA e altri BES: distinzioni normative</strong></a>
        <a href="articolo-pei-spiegato-semplice.html"><span aria-hidden="true">🤝</span><strong>Il Piano Educativo Individualizzato (PEI): elaborazione, contenuti e percorsi</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="PDP, piano didattico personalizzato, PDP DSA, PDP BES, strumenti compensativi, misure dispensative, dispensa lingue straniere, L. 170/2010, D.M. 5669/2011",
    og_alt="Il titolo «Il PDP» con il sottotitolo «Destinatari, elaborazione e contenuti per DSA e altri BES» e tre riquadri: destinatari, DSA e altri BES; redazione, consiglio di classe e famiglia; tempi, per i DSA entro il primo trimestre.",
    date_iso="2026-11-17", modified_iso="2026-11-21", date_it="17 novembre 2026",
    ld_keywords="PDP, Piano Didattico Personalizzato, DSA, BES, L. 170/2010, D.M. 5669/2011, strumenti compensativi, misure dispensative, consiglio di classe, inclusione scolastica",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Il PDP» con il sottotitolo «Destinatari, elaborazione e contenuti per DSA e altri BES» e tre riquadri: destinatari, DSA e altri BES; redazione, consiglio di classe e famiglia; tempi, per i DSA entro il primo trimestre.",
    no_rt_note=True, no_tool_icons=True,   # stile professionale (dal 21/11/2026)
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('PDP: parole', words, '| minuti', MIN)
