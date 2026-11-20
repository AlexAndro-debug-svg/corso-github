#!/usr/bin/env python3
"""Articolo della serie inclusione: il docente di sostegno (registro professionale, scelta dell'autore del 20/11/2026)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-docente-di-sostegno"
TITLE = "Il docente di sostegno nella scuola secondaria di secondo grado: ruolo, funzioni e responsabilità"
SEO_TITLE = "Docente di sostegno alle superiori: ruolo e funzioni — AlessandroSimone.it"
DESC = "Contitolarità, funzioni, risorse orarie, continuità e rapporti con le altre figure: il docente di sostegno nella secondaria di II grado, alla luce della normativa vigente."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Il docente di sostegno è assegnato all'alunno o alla classe?",
        "Alla classe. L'art. 13, comma 6, della L. 104/92 stabilisce che i docenti di sostegno assumono la contitolarità delle sezioni e delle classi in cui operano. L'attenzione specifica allo studente con disabilità non ne fa un docente «dedicato»: la responsabilità educativa resta condivisa dall'intero consiglio di classe."),
    faq("Chi determina il numero di ore di sostegno?",
        "Il fabbisogno è individuato dal GLO nel PEI, con adeguata motivazione; l'assegnazione dei posti spetta poi all'Ufficio scolastico regionale. Il D.L. 170/2026 ha modificato la formulazione, prevedendo che il PEI «definisca» le ore anziché limitarsi a proporle; il testo è tuttavia in corso di conversione e potrebbe subire modifiche. Il quadro è illustrato nell'articolo <a href=\"articolo-pei-spiegato-semplice.html#calendario\">Il PEI spiegato semplice</a>."),
    faq("È possibile garantire la continuità del docente da un anno all'altro?",
        "Per i docenti a tempo determinato, sì, a determinate condizioni. L'art. 8 del D.L. 71/2024, attuato dal D.M. 32/2025 e prorogato dal D.L. 127/2025, consente alla famiglia di richiedere la conferma del supplente dell'anno precedente. La decisione spetta al dirigente scolastico, sentito il GLO, ed è subordinata all'assenso del docente e alla sua posizione utile in graduatoria. La richiesta va presentata entro i termini fissati dal Ministero (nel 2025, il 31 maggio). In caso di avvicendamento, il PEI conserva piena validità."),
    faq("Come si gestisce l'assenza del docente di sostegno?",
        "Per le assenze prolungate si provvede alla nomina di un supplente. Nelle assenze brevi lo studente resta in classe con i docenti curricolari, che sono tenuti a conoscere e ad applicare il PEI. Non è legittimo chiedere alla famiglia di trattenere lo studente a casa."),
    faq("Che cosa fare se il docente non viene nominato o le ore assegnate sono inferiori a quelle del PEI?",
        "È opportuno rivolgersi per iscritto al dirigente scolastico e, ove presente, al referente per l'inclusione. Le associazioni delle famiglie possono offrire indicazioni sulle forme di tutela disponibili."),
    faq("È ammesso il lavoro individuale fuori dall'aula?",
        "Solo in via eccezionale e se previsto dal PEI, che ne deve indicare motivazioni e tempi. L'inclusione si realizza nel contesto della classe; il ricorso sistematico ad attività separate ne contraddice il principio."),
    faq("Lo studente può chiedere una presenza meno costante del docente?",
        "Sì. Nella secondaria di secondo grado lo studente partecipa al GLO, secondo il principio di autodeterminazione, e può esprimere le proprie esigenze; la decisione viene formalizzata nel PEI. Lo sviluppo dell'autonomia è, del resto, uno degli obiettivi qualificanti dell'intervento di sostegno."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <p>Il <strong>docente di sostegno</strong> è una figura centrale del sistema scolastico inclusivo e, al tempo stesso, una delle più fraintese. Alla percezione diffusa di un insegnante «dedicato» al singolo alunno, la normativa contrappone un profilo diverso: quello di un docente <strong>contitolare della classe</strong>, corresponsabile della progettazione e della valutazione di tutti gli studenti.</p>
    <p>È il ruolo che svolgo quotidianamente. Nei documenti ufficiali è denominato «docente di sostegno»; nel mio istituto, il Giovanni XXIII di Roma, la denominazione adottata è <strong>docente per l'inclusività</strong> (<a href="/#chi-sono">chi sono</a>).</p>
    <p>Questo contributo si rivolge a docenti, dirigenti, professionisti e famiglie. Ricostruisce lo status giuridico del docente di sostegno nella secondaria di secondo grado, ne descrive le funzioni e ne chiarisce i rapporti con le altre figure dell'inclusione, alla luce della normativa vigente.</p>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title">Indice</h2>
      <ol>
        <li><a href="#chi-e">Status giuridico e contitolarità</a></li>
        <li><a href="#formazione">Formazione e reclutamento</a></li>
        <li><a href="#cosa-fa">Le funzioni</a></li>
        <li><a href="#ore">Risorse orarie e continuità</a></li>
        <li><a href="#figure">Le altre figure dell'inclusione</a></li>
        <li><a href="#esame">L'esame di maturità</a></li>
        <li><a href="#collaborare">La collaborazione</a></li>
        <li><a href="#falsi-miti">Alcuni fraintendimenti ricorrenti</a></li>
        <li><a href="#informatica">Il contesto degli istituti tecnici</a></li>
        <li><a href="#sintesi">Considerazioni conclusive</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <h2 id="chi-e">Status giuridico e contitolarità</h2>
    <p>Il docente di sostegno è assegnato alle classi in cui è presente uno studente con <strong>disabilità certificata</strong> ai sensi della <strong>L. 104/92</strong>. Non è invece previsto per gli studenti con DSA (Disturbi Specifici dell'Apprendimento, L. 170/2010) né per gli altri BES (Bisogni Educativi Speciali, Direttiva ministeriale 27 dicembre 2012), salvo che non sussista anche una certificazione di disabilità. Le distinzioni sono approfondite nell'articolo <a href="articolo-bes-dsa-disabilita.html">Disabilità 104, DSA e BES</a>.</p>
    <p>Il fondamento del ruolo è l'art. 13, comma 6, della L. 104/92, secondo cui i docenti di sostegno <strong>assumono la contitolarità</strong> delle classi in cui operano. Ne discendono la partecipazione a pieno titolo alla programmazione educativa e didattica e ai lavori del consiglio di classe, come ribadito dall'art. 315 del D.Lgs. 297/94.</p>
    <p>Sul piano valutativo, l'art. 4 del D.P.R. 122/2009, nella formulazione introdotta dal D.P.R. 135/2025, stabilisce che i docenti di sostegno partecipano alla valutazione <strong>di tutti gli studenti</strong> della classe. In sede di scrutinio, dunque, il loro voto concorre alle deliberazioni relative all'intero gruppo classe, non al solo studente con disabilità.</p>

    <h2 id="formazione">Formazione e reclutamento</h2>
    <p>Il docente di sostegno è, di norma, in possesso di una <strong>specializzazione</strong> specifica, conseguita mediante i corsi universitari per le attività di sostegno didattico oppure, per determinate categorie di docenti, mediante i percorsi formativi istituiti dal D.L. 71/2024.</p>
    <p>La disponibilità di docenti specializzati non è tuttavia sufficiente a coprire il fabbisogno. Una quota dei posti di sostegno è perciò affidata a docenti privi di specializzazione, individuati attraverso le graduatorie: una criticità strutturale che incide sulla qualità e sulla continuità del servizio.</p>

    <h2 id="cosa-fa">Le funzioni</h2>
    <p>Le funzioni del docente di sostegno si articolano su più piani, che vanno sempre intesi in un'ottica di corresponsabilità con il consiglio di classe.</p>
    <ul>
      <li><strong>Osservazione e conoscenza dello studente.</strong> L'osservazione sistematica, integrata con il Profilo di funzionamento redatto dagli specialisti, consente di individuare punti di forza, bisogni e facilitatori.</li>
      <li><strong>Progettazione.</strong> Il docente di sostegno contribuisce in modo determinante alla stesura del PEI (Piano Educativo Individualizzato), elaborato e approvato dal GLO (Gruppo di Lavoro Operativo per l'inclusione) secondo la prospettiva bio-psico-sociale dell'ICF.</li>
      <li><strong>Azione didattica.</strong> Opera in compresenza con i docenti curricolari, svolgendo una funzione di mediazione didattica a beneficio dello studente e dell'intera classe.</li>
      <li><strong>Adattamento dei materiali.</strong> Collabora alla semplificazione dei testi, alla predisposizione di mappe e schemi e alla progettazione di verifiche coerenti con il percorso previsto dal PEI.</li>
      <li><strong>Raccordo.</strong> Cura i rapporti con la famiglia, con i servizi sanitari e con le figure professionali che seguono lo studente.</li>
      <li><strong>Valutazione.</strong> Partecipa agli scrutini e alla valutazione di tutti gli studenti della classe.</li>
    </ul>
    <p>Il PEI rappresenta il riferimento unitario di queste funzioni. Struttura, tempi e percorsi sono illustrati nell'articolo <a href="articolo-pei-spiegato-semplice.html">Il PEI spiegato semplice</a>.</p>

    <h2 id="ore">Risorse orarie e continuità</h2>
    <p>Le ore di sostegno non sono attribuite in misura uniforme, ma in funzione dei bisogni dello studente, e sono indicate nel PEI. Il D.L. 170/2026 ha previsto che il PEI «definisca» tali ore con adeguata motivazione; il provvedimento è tuttavia in corso di conversione in legge, con termine al 29 novembre 2026, e potrebbe essere modificato.</p>
    <p>La presenza del docente di sostegno non copre necessariamente l'intero orario settimanale. Nelle restanti ore la responsabilità dell'attuazione del PEI ricade sui docenti curricolari, nell'ambito della comune contitolarità.</p>
    <p>La <strong>continuità didattica</strong> costituisce un nodo particolarmente rilevante. L'art. 8 del D.L. 71/2024, attuato dal D.M. 32/2025 e successivamente prorogato, consente alla famiglia di chiedere la conferma del docente a tempo determinato che ha seguito lo studente nell'anno precedente. La decisione spetta al dirigente scolastico, sentito il GLO, ed è subordinata all'assenso del docente.</p>

    <h2 id="figure">Le altre figure dell'inclusione</h2>
    <p>Attorno allo studente con disabilità operano figure diverse, con competenze distinte e non sovrapponibili. Il PEI ne definisce ruoli e modalità di intervento.</p>
    <h3>I docenti curricolari</h3>
    <p>Sono contitolari della classe al pari del docente di sostegno e corresponsabili dell'attuazione del PEI nelle rispettive discipline, con particolare riferimento alla progettazione del percorso curricolare.</p>
    <h3>L'assistente all'autonomia e alla comunicazione</h3>
    <p>È una figura esterna alla scuola, il cui servizio è a carico degli enti territoriali. Nel Lazio, per la secondaria di secondo grado, il servizio è finanziato dalla Regione sulla base dei progetti presentati dalle istituzioni scolastiche. Interviene sul piano dell'autonomia personale e della comunicazione, non su quello didattico.</p>
    <h3>Il collaboratore scolastico</h3>
    <p>Appartiene al personale della scuola e garantisce, tra gli altri compiti, l'assistenza di base, ad esempio negli spostamenti e nella cura dell'igiene personale, come previsto dall'art. 3 del D.Lgs. 66/2017.</p>
    <h3>Il referente per l'inclusione</h3>
    <p>In molte istituzioni scolastiche è individuato un docente che coordina le azioni di inclusione, supporta i colleghi e costituisce un punto di riferimento per le famiglie.</p>

    <h2 id="esame">L'esame di maturità</h2>
    <p>All'esame di maturità lo studente con disabilità sostiene le prove secondo il percorso definito nel PEI, ai sensi dell'art. 20 del D.Lgs. 62/2017.</p>
    <p>La commissione può avvalersi del supporto dei docenti e degli esperti che hanno seguito lo studente durante l'anno scolastico, compreso il docente di sostegno. Questi, tuttavia, non fa parte della commissione e non partecipa all'attribuzione del punteggio.</p>
    <p>Non tutti i percorsi conducono al diploma: le differenze tra percorso ordinario, personalizzato e differenziato sono trattate nella sezione <a href="articolo-pei-spiegato-semplice.html#percorsi">I tre percorsi alle superiori</a>.</p>

    <h2 id="collaborare">La collaborazione</h2>
    <p>L'efficacia dell'intervento dipende in larga misura dalla qualità della collaborazione tra i diversi soggetti coinvolti.</p>
    <h3>Con i colleghi</h3>
    <ul>
      <li>condividere con anticipo argomenti e prove di verifica, così da consentirne l'adattamento;</li>
      <li>tenere presente che la predisposizione delle verifiche adattate compete al docente della disciplina, con il supporto del docente di sostegno;</li>
      <li>concordare la distribuzione dei compiti durante le ore di compresenza;</li>
      <li>valorizzare il docente di sostegno anche nelle attività rivolte all'intero gruppo classe.</li>
    </ul>
    <h3>Con le famiglie</h3>
    <ul>
      <li>prevedere un colloquio all'inizio dell'anno scolastico;</li>
      <li>acquisire le osservazioni della famiglia sul contesto extrascolastico;</li>
      <li>disporre della documentazione specialistica aggiornata;</li>
      <li>ricordare che tutti i docenti del consiglio di classe sono interlocutori della famiglia.</li>
    </ul>
    <h3>Con lo studente</h3>
    <p>Nella secondaria di secondo grado lo studente è soggetto attivo del proprio percorso. Il principio di autodeterminazione, che ne prevede la partecipazione al GLO, impone di ascoltarne le esigenze e di calibrare la presenza del docente in funzione dello sviluppo dell'autonomia.</p>

    <h2 id="falsi-miti">Alcuni fraintendimenti ricorrenti</h2>
    <p>Alcune rappresentazioni del ruolo, ancora diffuse, non trovano riscontro né nella normativa né nella pratica professionale.</p>
    <p><strong>«È l'insegnante personale dello studente».</strong> Il docente di sostegno è contitolare della classe: cura in modo specifico il percorso dello studente con disabilità, ma opera per l'intero gruppo.</p>
    <p><strong>«Con il sostegno, gli altri docenti sono sollevati da ogni responsabilità».</strong> Lo studente con disabilità appartiene alla classe; ciascun docente è responsabile dell'attuazione del PEI nelle proprie ore.</p>
    <p><strong>«Il sostegno si svolge fuori dall'aula».</strong> L'inclusione si realizza nel contesto della classe. Le attività separate costituiscono un'eccezione, da motivare e prevedere nel PEI.</p>
    <p><strong>«È un docente di secondo livello».</strong> Gode degli stessi diritti degli altri docenti: è contitolare, partecipa agli scrutini e concorre alla valutazione di tutti gli studenti.</p>

    <h2 id="informatica">Il contesto degli istituti tecnici</h2>
    <p>Negli istituti tecnici una parte significativa dell'orario si svolge in <strong>laboratorio</strong>, dove il docente di sostegno opera insieme al docente della disciplina e all'insegnante tecnico-pratico.</p>
    <p>Prima di assumere questo ruolo ho insegnato informatica per anni. Il laboratorio offre condizioni favorevoli alla personalizzazione: la scomposizione delle consegne in fasi brevi, l'impiego delle <a href="articolo-tecnologie-assistive.html">tecnologie assistive</a> e il lavoro in piccoli gruppi.</p>
    <p>Per gli studenti con DSA o con ADHD (disturbo da deficit di attenzione e iperattività) privi di certificazione di disabilità il sostegno non è previsto. Indicazioni specifiche sono contenute negli articoli <a href="articolo-informatica-dsa.html">Informatica e DSA</a> e <a href="articolo-adhd-programmazione.html">ADHD e programmazione</a>.</p>

    <h2 id="sintesi">Considerazioni conclusive</h2>
    <ul>
      <li>Il docente di sostegno è previsto per le classi con studenti con disabilità certificata ai sensi della L. 104/92.</li>
      <li>È contitolare della classe, con i medesimi diritti e le medesime responsabilità degli altri docenti.</li>
      <li>Osserva, progetta, media, adatta e valuta, sempre in corresponsabilità con il consiglio di classe.</li>
      <li>Le ore sono definite nel PEI; nelle restanti ore l'attuazione del PEI spetta ai docenti curricolari.</li>
      <li>La qualità dell'inclusione dipende dalla collaborazione tra scuola, famiglia, servizi e studente.</li>
    </ul>
    <p>L'obiettivo ultimo dell'intervento di sostegno non è la presenza costante del docente, ma la crescita dell'autonomia dello studente: un buon sostegno, in questo senso, lavora anche per rendersi progressivamente meno necessario.</p>
    <p class="norme rt-skip">Riferimenti normativi: L. 104/92, art. 13, comma 6 (contitolarità); D.Lgs. 297/94, art. 315; D.P.R. 122/2009, art. 4, come modificato dal D.P.R. 135/2025 (valutazione di tutti gli studenti); L. 170/2010 (DSA); Direttiva ministeriale 27 dicembre 2012 (BES); D.Lgs. 66/2017, artt. 3 e 15; D.Lgs. 62/2017, art. 20 (esame di maturità); D.I. 182/2020 e D.I. 153/2023 (PEI e GLO); D.L. 71/2024, art. 8, conv. L. 106/2024, e D.M. 32/2025 (continuità dei docenti a tempo determinato), prorogati dal D.L. 127/2025; D.L. 170/2026 (ore di sostegno nel PEI, in corso di conversione). Aggiornato al 20 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica per una didattica inclusiva</h2>
      <p>Le lezioni gratuite del sito propongono esempi brevi e modificabili, con l'editor «Provalo tu» integrato nel browser.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Per domande o per condividere esperienze professionali sul sostegno è possibile <a href="contatti.html">scrivermi</a>: ogni messaggio riceve risposta.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title">Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-pei-spiegato-semplice.html"><strong>Il PEI spiegato semplice: cos'è, chi lo scrive e come funziona</strong></a>
        <a href="articolo-bes-dsa-disabilita.html"><strong>Disabilità 104, DSA e BES: che differenza c'è?</strong></a>
        <a href="articolo-tecnologie-assistive.html"><strong>Tecnologie assistive per studiare: quali sono e come averle a scuola</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="docente di sostegno, insegnante di sostegno, cosa fa il docente di sostegno, sostegno superiori, contitolarità, ore di sostegno, continuità sostegno, legge 104 scuola",
    og_alt="Il titolo «Il docente di sostegno» con il sottotitolo «Ruolo, funzioni e responsabilità alle superiori» e tre riquadri: status, contitolare della classe; funzioni, progettazione e didattica; interlocutori, colleghi, famiglie e servizi.",
    date_iso="2026-11-20", date_it="20 novembre 2026",
    ld_keywords="docente di sostegno, insegnante di sostegno, Legge 104, disabilità, PEI, GLO, contitolarità, inclusione scolastica, scuola secondaria di secondo grado",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Il docente di sostegno» con il sottotitolo «Ruolo, funzioni e responsabilità alle superiori» e tre riquadri: status, contitolare della classe; funzioni, progettazione e didattica; interlocutori, colleghi, famiglie e servizi.",
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    html_out = page(META)
    # Registro professionale: niente icone nei pulsanti di lettura (anche quelle aggiunte dallo script durante l'ascolto)
    NO_ICONS = '  <style>.reading-tools .rt-btn span[aria-hidden="true"], .rt-player span[aria-hidden="true"] { display: none; }</style>\n</head>'
    assert html_out.count('</head>') == 1
    html_out = html_out.replace('</head>', NO_ICONS)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(html_out)
    print('SOSTEGNO: parole', words, '| minuti', MIN)
