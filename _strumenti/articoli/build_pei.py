#!/usr/bin/env python3
"""Articolo della serie inclusione: il PEI (stile professionale, riscritto il 21/11/2026)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-pei-spiegato-semplice"
TITLE = "Il Piano Educativo Individualizzato (PEI): elaborazione, contenuti e percorsi nella secondaria di secondo grado"
SEO_TITLE = "Il PEI: elaborazione, contenuti e percorsi — AlessandroSimone.it"
DESC = "Natura, elaborazione e contenuti del PEI, ruolo del GLO, modello nazionale, percorsi della secondaria di II grado e novità del D.L. 170/2026."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Il PEI si applica anche agli studenti con DSA o con altri BES?",
        "No. Il PEI è riservato agli studenti con disabilità certificata ai sensi della L. 104/92. Per gli studenti con DSA (L. 170/2010) e con altri BES (Direttiva ministeriale 27 dicembre 2012) lo strumento di riferimento è il PDP, illustrato nell'articolo <a href=\"articolo-pdp-passo-dopo-passo.html\">Il Piano Didattico Personalizzato (PDP)</a>. Le distinzioni sono approfondite in <a href=\"articolo-bes-dsa-disabilita.html\">Disabilità 104, DSA e BES</a>."),
    faq("Qual è il ruolo dello studente nel GLO?",
        "Nella secondaria di secondo grado lo studente partecipa al GLO in attuazione del principio di autodeterminazione. Può esprimere esigenze, preferenze e obiettivi; è opportuno che la sua partecipazione sia preparata, anche con il supporto di un docente o della famiglia."),
    faq("La famiglia può farsi affiancare da un esperto di fiducia?",
        "Sì, nel limite di un esperto, previa autorizzazione del dirigente scolastico (art. 3, comma 6, del D.I. 182/2020). La sua partecipazione ha valore consultivo e non decisionale."),
    faq("Come può la famiglia manifestare un dissenso sul PEI?",
        "Il dissenso va espresso in sede di GLO, chiedendone la verbalizzazione. Qualora permanga, è possibile richiedere un incontro con il dirigente scolastico."),
    faq("Che cosa comporta il diniego della famiglia al percorso differenziato?",
        "In presenza di un diniego espresso per iscritto, lo studente è valutato secondo i criteri della classe (art. 15 dell'O.M. 90/2001): conserva il sostegno, ma non ha alcuna garanzia di ammissione alla classe successiva. Il silenzio della famiglia entro il termine fissato dalla scuola equivale ad assenso. È opportuno che il consiglio di classe illustri con chiarezza le ragioni della proposta."),
    faq("Il PEI può essere modificato in corso d'anno?",
        "Sì. Le verifiche intermedie hanno proprio la funzione di accertare l'efficacia di obiettivi, strategie e risorse e, ove necessario, di rimodularli."),
    faq("Chi determina le ore di sostegno?",
        "Il GLO le indica nel PEI con adeguata motivazione, in relazione ai bisogni dello studente e del contesto classe. Il D.L. 170/2026 ha previsto che il PEI «definisca» le ore, superando la precedente formula della «proposta»; l'assegnazione dei posti resta di competenza dell'Ufficio scolastico regionale. Il testo è in corso di conversione e potrebbe essere modificato."),
    faq("Il progetto di vita sostituisce il PEI?",
        "No. Il progetto di vita individuale, personalizzato e partecipato, introdotto dal D.Lgs. 62/2024, riguarda l'intero arco dell'esistenza della persona; il PEI ne costituisce la declinazione scolastica, come evidenzia la sezione di raccordo con il Progetto individuale prevista dal modello nazionale. La riforma è in fase di attuazione progressiva sul territorio."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <p>Il <strong>PEI</strong> (Piano Educativo Individualizzato) è il documento con cui la scuola progetta il percorso degli studenti con <strong>disabilità certificata</strong> ai sensi della <strong>L. 104/92</strong>. Ne definisce obiettivi, strategie, strumenti e risorse e individua gli interventi necessari a rimuovere le barriere presenti nel contesto.</p>
    <p>Partecipo ai GLO come docente per l'inclusività (<a href="/#chi-sono">chi sono</a>). In questo contributo ricostruisco il quadro normativo del PEI, le modalità della sua elaborazione, la struttura del modello nazionale e i percorsi previsti nella secondaria di secondo grado, alla luce delle novità introdotte nel 2026.</p>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title">Indice</h2>
      <ol>
        <li><a href="#cos-e">Natura e destinatari</a></li>
        <li><a href="#glo">L'elaborazione: il GLO</a></li>
        <li><a href="#dentro">L'impianto concettuale</a></li>
        <li><a href="#modello">Il modello nazionale</a></li>
        <li><a href="#percorsi">I percorsi nella secondaria di secondo grado</a></li>
        <li><a href="#calendario">Tempi e scadenze: le novità del 2026</a></li>
        <li><a href="#partecipare">Indicazioni per la partecipazione al GLO</a></li>
        <li><a href="#falsi-miti">Alcuni fraintendimenti ricorrenti</a></li>
        <li><a href="#informatica">Un esempio disciplinare: l'informatica</a></li>
        <li><a href="#sintesi">Considerazioni conclusive</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <h2 id="cos-e">Natura e destinatari</h2>
    <p>Il PEI è disciplinato dall'art. 7 del <strong>D.Lgs. 66/2017</strong>, come modificato dal D.Lgs. 96/2019, ed è redatto secondo i modelli nazionali adottati con il <strong>D.I. 182/2020</strong>, successivamente integrato dal D.I. 153/2023.</p>
    <p>Destinatari sono esclusivamente gli studenti con disabilità certificata ai fini dell'inclusione scolastica. Per gli studenti con DSA (L. 170/2010) e con altri BES lo strumento di riferimento è invece il PDP (Piano Didattico Personalizzato).</p>
    <p>Il PEI si fonda sulla certificazione e sul <strong>Profilo di funzionamento</strong>, documento redatto dall'unità di valutazione multidisciplinare che descrive punti di forza e bisogni dello studente. Nelle more della piena attuazione della riforma, in assenza del Profilo si fa riferimento alla Diagnosi funzionale.</p>
    <p>Il documento è redatto ogni anno scolastico ed è soggetto a verifiche periodiche; nella secondaria di secondo grado accompagna lo studente fino all'esame di maturità.</p>

    <h2 id="glo">L'elaborazione: il GLO</h2>
    <p>Il PEI è elaborato e approvato dal <strong>GLO</strong> (Gruppo di Lavoro Operativo per l'inclusione), disciplinato dall'art. 15 della L. 104/92 e dall'art. 3 del D.I. 182/2020. Ne fanno parte:</p>
    <ul>
      <li>il <strong>consiglio di classe</strong>, compreso il <a href="articolo-docente-di-sostegno.html">docente di sostegno</a>;</li>
      <li>il <strong>dirigente scolastico</strong>, che lo presiede o ne delega la presidenza;</li>
      <li>i <strong>genitori</strong> o gli esercenti la responsabilità genitoriale, che vi partecipano a pieno titolo;</li>
      <li>lo <strong>studente</strong>, nella secondaria di secondo grado, in attuazione del principio di autodeterminazione;</li>
      <li>un rappresentante dell'<strong>unità di valutazione multidisciplinare</strong> dell'ASL (Azienda sanitaria locale);</li>
      <li>le <strong>figure professionali</strong> interne ed esterne che operano con lo studente, come l'assistente all'autonomia e alla comunicazione;</li>
      <li>non più di un <strong>esperto indicato dalla famiglia</strong>, su autorizzazione del dirigente, con funzione consultiva e non decisionale.</li>
    </ul>
    <p>La redazione della proposta è di norma curata dal docente di sostegno in collaborazione con i colleghi. Il documento, tuttavia, è del GLO: famiglia e studente possono proporre integrazioni e modifiche prima dell'approvazione.</p>

    <h2 id="dentro">L'impianto concettuale</h2>
    <p>Il PEI adotta la prospettiva bio-psico-sociale dell'<strong>ICF</strong> (Classificazione Internazionale del Funzionamento, della Disabilità e della Salute) dell'Organizzazione Mondiale della Sanità. Il funzionamento della persona è letto come esito dell'interazione tra condizioni di salute e fattori contestuali.</p>
    <p>Ne discende la centralità dell'analisi del contesto, articolata in <strong>barriere</strong>, ossia i fattori che ostacolano la partecipazione, e <strong>facilitatori</strong>, ossia i fattori che la sostengono: dall'accessibilità degli spazi alle modalità di presentazione dei contenuti, fino al ruolo dei compagni.</p>
    <p>L'osservazione dello studente si sviluppa lungo quattro <strong>dimensioni</strong>, per ciascuna delle quali il PEI individua obiettivi, strategie e strumenti:</p>
    <ul>
      <li>relazione, interazione e socializzazione;</li>
      <li>comunicazione e linguaggio;</li>
      <li>autonomia e orientamento;</li>
      <li>dimensione cognitiva, neuropsicologica e dell'apprendimento.</li>
    </ul>
    <p>A questa analisi si affianca la progettazione del percorso curricolare, condotta disciplina per disciplina, con l'indicazione degli obiettivi, delle modalità di verifica e dei criteri di valutazione.</p>

    <h2 id="modello">Il modello nazionale</h2>
    <p>Il D.I. 182/2020 ha introdotto modelli nazionali di PEI differenziati per grado di scuola. Il modello per la secondaria di secondo grado si articola in dodici sezioni:</p>
    <ol>
      <li><strong>Quadro informativo</strong>, con la descrizione dello studente a cura della famiglia o dello studente stesso;</li>
      <li><strong>Elementi generali desunti dal Profilo di funzionamento</strong>;</li>
      <li><strong>Raccordo con il Progetto individuale</strong>, ove redatto;</li>
      <li><strong>Osservazioni sullo studente</strong> nelle quattro dimensioni;</li>
      <li><strong>Interventi per lo studente</strong>: obiettivi, strategie e strumenti;</li>
      <li><strong>Osservazioni sul contesto</strong>: barriere e facilitatori;</li>
      <li><strong>Interventi sul contesto</strong> per un ambiente di apprendimento inclusivo;</li>
      <li><strong>Interventi sul percorso curricolare</strong>, per discipline, con l'indicazione del tipo di percorso;</li>
      <li><strong>Organizzazione generale del progetto di inclusione</strong> e utilizzo delle risorse;</li>
      <li><strong>Certificazione delle competenze</strong>, al termine del secondo anno;</li>
      <li><strong>Verifica finale</strong> e proposte per l'anno successivo;</li>
      <li><strong>PEI provvisorio</strong>, per gli studenti al primo inserimento o di nuova certificazione.</li>
    </ol>
    <p>Le sezioni dalla 4 alla 7 costituiscono il nucleo progettuale del documento. La sezione 8 chiama in causa direttamente i docenti curricolari: il loro contributo è essenziale e non delegabile al solo docente di sostegno.</p>

    <h2 id="percorsi">I percorsi nella secondaria di secondo grado</h2>
    <p>Nella secondaria di secondo grado il PEI indica il tipo di percorso seguito dallo studente, scelta che determina il titolo conseguibile al termine degli studi.</p>
    <h3>Percorso ordinario</h3>
    <p>Lo studente persegue gli stessi obiettivi della classe, con l'eventuale ausilio di strumenti e strategie specifiche. Consegue il diploma, previo superamento dell'esame di maturità.</p>
    <h3>Percorso personalizzato con prove equipollenti</h3>
    <p>Gli obiettivi sono riconducibili ai nuclei essenziali delle discipline. Le prove <strong>equipollenti</strong> possono differire per tempi, strumenti, modalità e anche contenuti, purché accertino una preparazione culturale e professionale equivalente. Anche in questo caso si consegue il diploma.</p>
    <h3>Percorso differenziato</h3>
    <p>Gli obiettivi sono diversi da quelli della classe e calibrati sulle potenzialità dello studente. Al termine si consegue un <strong>attestato di credito formativo</strong> (art. 20 del D.Lgs. 62/2017), che certifica le competenze acquisite e consente l'accesso ai percorsi di istruzione e formazione professionale, ma non equivale al diploma e non permette l'iscrizione all'università.</p>
    <p>Il percorso differenziato richiede il <strong>consenso della famiglia</strong> (art. 15 dell'O.M. 90/2001). Il consiglio di classe formula la proposta fissando un termine per la risposta, decorso il quale il silenzio equivale ad assenso. In caso di diniego espresso, lo studente è valutato secondo i criteri della classe: conserva il sostegno, ma non ha garanzia di ammissione alla classe successiva.</p>
    <p>Il percorso è rivedibile. Qualora il consiglio di classe accerti il raggiungimento di livelli di apprendimento corrispondenti agli obiettivi della classe, può disporre il passaggio a un percorso valido per il diploma, senza necessità di prove di idoneità relative agli anni precedenti.</p>

    <h2 id="calendario">Tempi e scadenze: le novità del 2026</h2>
    <p><strong>Avvertenza (aggiornata al 15 novembre 2026).</strong> Il D.L. 30 settembre 2026, n. 170, in vigore dal 1° ottobre 2026, ha modificato le scadenze del PEI. Il provvedimento deve essere convertito in legge entro il 29 novembre 2026 e il testo potrebbe essere modificato in sede di conversione; l'articolo sarà aggiornato non appena il quadro sarà definitivo.</p>
    <p>Fino a settembre 2026 il PEI definitivo era approvato, di norma, entro il 31 ottobre. Secondo il testo del decreto, come riportato dalla stampa specializzata, le scadenze sono ora differenziate:</p>
    <ul>
      <li><strong>studenti già frequentanti</strong>: verifica finale e approvazione del PEI definitivo per l'anno successivo entro giugno, con possibilità di aggiornamento nelle prime due settimane di ottobre;</li>
      <li><strong>nuovi iscritti o studenti di prima certificazione</strong>: PEI provvisorio entro giugno e PEI definitivo entro il 15 ottobre.</li>
    </ul>
    <p>In entrambi i casi restano le verifiche intermedie nel corso dell'anno. Poiché il decreto è entrato in vigore ad anno scolastico avviato, per il PEI dell'anno in corso è opportuno verificare con la scuola quale scadenza sia stata applicata.</p>
    <p>Il decreto interviene anche sulle <strong>ore di sostegno</strong>, che il PEI «definisce» con adeguata motivazione anziché limitarsi a proporle; l'assegnazione dei docenti resta di competenza dell'Ufficio scolastico regionale. È inoltre prevista la validità dell'approvazione del PEI anche in assenza di una componente regolarmente convocata, allo scopo di evitare che un'assenza comprometta il rispetto dei termini; le condizioni precise saranno definite dal testo convertito.</p>
    <p>La famiglia impossibilitata a partecipare a una riunione del GLO dovrebbe darne tempestiva comunicazione alla scuola, chiedendo un rinvio o trasmettendo per iscritto le proprie osservazioni.</p>

    <h2 id="partecipare">Indicazioni per la partecipazione al GLO</h2>
    <p>Una partecipazione preparata accresce la qualità del documento. Alcune indicazioni operative:</p>
    <ul>
      <li>richiedere la bozza del PEI con anticipo rispetto alla riunione;</li>
      <li>disporre della documentazione specialistica aggiornata;</li>
      <li>fornire elementi sul contesto extrascolastico: interessi, fattori di affaticamento, strategie efficaci;</li>
      <li>formulare obiettivi osservabili e verificabili: «utilizzare il computer in autonomia per la stesura di un testo» è più utile di un generico «migliorare l'autonomia»;</li>
      <li>valorizzare la voce dello studente, preparandone insieme l'intervento;</li>
      <li>richiedere copia del PEI approvato e del verbale, annotando le date delle verifiche.</li>
    </ul>

    <h2 id="falsi-miti">Alcuni fraintendimenti ricorrenti</h2>
    <p>Alcune convinzioni diffuse sul PEI non trovano riscontro nella normativa.</p>
    <p><strong>«Il PEI comporta un programma ridotto».</strong> Dipende dal percorso: nel percorso ordinario gli obiettivi coincidono con quelli della classe, e il PEI interviene su modalità, strumenti e supporti.</p>
    <p><strong>«Il PEI è redatto dal solo docente di sostegno».</strong> Il documento è elaborato e approvato collegialmente dal GLO, con il contributo di tutti i docenti, della famiglia, dei servizi e dello studente.</p>
    <p><strong>«Con il PEI non si consegue il diploma».</strong> Il diploma si consegue sia nel percorso ordinario sia in quello personalizzato con prove equipollenti; solo il percorso differenziato si conclude con l'attestato di credito formativo.</p>
    <p><strong>«Il PEI, una volta approvato, è immodificabile».</strong> È redatto annualmente e sottoposto a verifiche periodiche, che ne consentono la rimodulazione.</p>

    <h2 id="informatica">Un esempio disciplinare: l'informatica</h2>
    <p>Ho insegnato informatica per anni: un'esemplificazione disciplinare aiuta a cogliere la differenza tra i tre percorsi, ferma restando l'unicità di ogni progettazione.</p>
    <ul>
      <li><strong>Percorso ordinario</strong>: lo studente sviluppa gli stessi programmi della classe, ad esempio sulle <a href="articolo-if-else-python.html">strutture condizionali in Python</a>, con tempi aggiuntivi, sintesi vocale o periferiche adattate, come illustrato in <a href="articolo-tecnologie-assistive.html">Tecnologie assistive per studiare</a>.</li>
      <li><strong>Percorso personalizzato</strong>: gli obiettivi si concentrano sui nuclei essenziali; una prova equipollente può consistere nel completamento di un programma dato o nell'analisi di un <a href="articolo-diagramma-di-flusso.html">diagramma di flusso</a>, anziché nella scrittura del codice ex novo.</li>
      <li><strong>Percorso differenziato</strong>: gli obiettivi riguardano competenze funzionali all'autonomia e all'inserimento lavorativo, come l'uso autonomo del computer, la gestione dei file, la posta elettronica, la programmazione a blocchi.</li>
    </ul>
    <p>In tutti i casi il laboratorio di informatica si configura come un potente facilitatore: consente l'apprendimento attraverso l'esperienza, offre un riscontro immediato e rende l'errore parte naturale del processo.</p>

    <h2 id="sintesi">Considerazioni conclusive</h2>
    <ul>
      <li>Il PEI è il documento di progettazione per gli studenti con disabilità certificata ai sensi della L. 104/92.</li>
      <li>È elaborato e approvato dal GLO, di cui fanno parte anche la famiglia e, nella secondaria di secondo grado, lo studente.</li>
      <li>Adotta la prospettiva ICF e definisce obiettivi, strategie, risorse e interventi sul contesto, disciplina per disciplina.</li>
      <li>I percorsi ordinario e personalizzato conducono al diploma; il percorso differenziato, subordinato al consenso della famiglia, all'attestato di credito formativo.</li>
      <li>È redatto annualmente e verificato in corso d'anno; le scadenze sono state modificate dal D.L. 170/2026, in corso di conversione.</li>
    </ul>
    <p>Un PEI efficace non è un adempimento formale, ma un progetto condiviso: la sua qualità dipende dalla capacità di scuola, famiglia, servizi e studente di costruirlo e verificarlo insieme.</p>
    <p class="norme rt-skip">Riferimenti normativi: L. 104/92, artt. 12, 13 e 15; D.Lgs. 66/2017, art. 7, come modificato dal D.Lgs. 96/2019; D.I. 182/2020, modificato dal D.I. 153/2023, con modelli di PEI e Linee guida; D.Lgs. 62/2017, art. 20; O.M. 90/2001, art. 15; D.M. 9/2010 (certificazione delle competenze); D.Lgs. 62/2024 (progetto di vita); D.L. 170/2026 (G.U. n. 227 del 30 settembre 2026), in corso di conversione in legge. Aggiornato al 15 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica per una didattica inclusiva</h2>
      <p>Le lezioni gratuite del sito propongono esempi brevi e modificabili, con l'editor «Provalo tu» integrato nel browser.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai un dubbio sul PEI o sul GLO? Vuoi raccontarmi la tua esperienza? <a href="contatti.html">Scrivimi</a>: leggo tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-docente-di-sostegno.html"><span aria-hidden="true">🏫</span><strong>Il docente di sostegno nella scuola secondaria di secondo grado</strong></a>
        <a href="articolo-pdp-passo-dopo-passo.html"><span aria-hidden="true">📝</span><strong>Il PDP passo dopo passo: cos'è, chi lo scrive e cosa contiene</strong></a>
        <a href="articolo-bes-dsa-disabilita.html"><span aria-hidden="true">🧭</span><strong>Disabilità 104, DSA e BES: che differenza c'è?</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="PEI, piano educativo individualizzato, GLO, modello nazionale PEI, percorso differenziato, prove equipollenti, D.I. 182/2020, D.L. 170/2026 PEI, legge 104/92",
    og_alt="Il titolo «Il PEI» con il sottotitolo «Elaborazione, contenuti e percorsi alle superiori» e tre riquadri: chi lo elabora, il GLO; impianto, prospettiva ICF; percorsi, tre opzioni alle superiori.",
    date_iso="2026-11-15", modified_iso="2026-11-21", date_it="15 novembre 2026",
    ld_keywords="PEI, Piano Educativo Individualizzato, GLO, L. 104/92, D.Lgs. 66/2017, D.I. 182/2020, ICF, percorso differenziato, prove equipollenti, inclusione scolastica",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Il PEI» con il sottotitolo «Elaborazione, contenuti e percorsi alle superiori» e tre riquadri: chi lo elabora, il GLO; impianto, prospettiva ICF; percorsi, tre opzioni alle superiori.",
    no_rt_note=True, no_tool_icons=True,   # stile professionale (dal 21/11/2026)
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('PEI: parole', words, '| minuti', MIN)
