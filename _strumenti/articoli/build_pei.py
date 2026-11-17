#!/usr/bin/env python3
"""Articolo 2 della serie inclusione: il PEI spiegato semplice."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-pei-spiegato-semplice"
TITLE = "Il PEI spiegato semplice: cos'è, chi lo scrive e come funziona"
SEO_TITLE = "Il PEI spiegato semplice: cos'è, chi lo scrive e come funziona — AlessandroSimone.it"
DESC = "Cos'è il PEI, chi lo scrive nel GLO, cosa contiene, i tre percorsi alle superiori e le scadenze 2026. Guida semplice per famiglie, studenti e docenti."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FIGURE
GLO = [
    ("Consiglio di classe", "Tutti i docenti della classe, compreso il docente di sostegno."),
    ("Dirigente scolastico", "Presiede il GLO, oppure delega un docente a farlo."),
    ("Famiglia", "I genitori, o chi ha la responsabilità dello studente, partecipano con gli stessi diritti degli altri."),
    ("Studente", "Alle superiori partecipa anche lo studente: ha il diritto di decidere per sé (principio di autodeterminazione)."),
    ("ASL", "Un rappresentante dell'Azienda sanitaria locale: viene dal gruppo di specialisti che ha valutato lo studente."),
    ("Altre figure", "Chi lavora con lo studente a scuola, per esempio l'assistente all'autonomia e alla comunicazione."),
    ("Un esperto della famiglia", "Al massimo uno, se il dirigente lo autorizza. Dà un parere, ma non decide."),
]
FIG_GLO = """
    <figure class="dsa-figure" aria-labelledby="cap-glo">
      <div class="sigle-grid">
""" + '\n'.join(f'        <div class="sigla"><b>{a}</b><span>{b}</span></div>' for a, b in GLO) + """
      </div>
      <figcaption id="cap-glo">Chi fa parte del GLO, il gruppo che scrive e approva il PEI.</figcaption>
    </figure>"""

DIM = [
    ("🗣️", "Relazione, interazione e socializzazione", "come lo studente sta con i compagni e con gli adulti."),
    ("💬", "Comunicazione e linguaggio", "come capisce e come si esprime, anche con strumenti diversi dalla voce."),
    ("🧭", "Autonomia e orientamento", "come si muove, si organizza e si prende cura di sé."),
    ("🧠", "Cognitiva, neuropsicologica e dell'apprendimento", "come ragiona, ricorda, presta attenzione e impara."),
]
FIG_DIM = """
    <ul class="icon-list">
""" + '\n'.join(f'      <li><span class="t-ico" aria-hidden="true">{i}</span><span><strong>{a}</strong>: {b}</span></li>' for i, a, b in DIM) + """
    </ul>"""

SEZ = [
    "<strong>Quadro informativo</strong>: lo studente descritto dalla famiglia o da lui stesso.",
    "<strong>Elementi dal Profilo di funzionamento</strong>: punti di forza e bisogni, come li descrivono gli specialisti.",
    "<strong>Raccordo con il Progetto individuale</strong>: il collegamento con il progetto di vita, se c'è.",
    "<strong>Osservazioni sullo studente</strong>: cosa notano i docenti nelle quattro dimensioni.",
    "<strong>Interventi per lo studente</strong>: obiettivi, strategie e strumenti per ogni dimensione.",
    "<strong>Osservazioni sul contesto</strong>: le barriere e i facilitatori a scuola.",
    "<strong>Interventi sul contesto</strong>: cosa cambia la scuola per essere più inclusiva.",
    "<strong>Interventi sul percorso curricolare</strong>: materia per materia, obiettivi, verifiche e tipo di percorso.",
    "<strong>Organizzazione del progetto di inclusione</strong>: orario, risorse e chi fa che cosa.",
    "<strong>Certificazione delle competenze</strong>: alle superiori si compila alla fine del secondo anno.",
    "<strong>Verifica finale</strong>: com'è andata e cosa serve per l'anno dopo.",
    "<strong>PEI provvisorio</strong>: si prepara entro giugno per chi inizia il percorso, per esempio dopo una nuova certificazione.",
]
FIG_SEZ = """
    <figure class="dsa-figure" aria-labelledby="cap-sez">
      <ol class="steps-list">
""" + '\n'.join(f'        <li>{x}</li>' for x in SEZ) + """
      </ol>
      <figcaption id="cap-sez">Le dodici sezioni del modello nazionale di PEI, spiegate in una riga ciascuna.</figcaption>
    </figure>"""

PERC = [
    ("A", "Percorso ordinario", "Lo studente segue <strong>gli stessi obiettivi della classe</strong>. Può usare aiuti e strumenti diversi, ma il traguardo è lo stesso dei compagni.", "Diploma, se supera l'esame"),
    ("B", "Percorso personalizzato, con prove equipollenti", "Gli obiettivi sono <strong>quelli essenziali della classe</strong>. Le verifiche sono <strong>equipollenti</strong>: possono cambiare i tempi, gli strumenti, il modo e anche i contenuti, ma devono dimostrare una preparazione equivalente.", "Diploma, se supera l'esame"),
    ("C", "Percorso differenziato", "Gli obiettivi sono <strong>diversi da quelli della classe</strong>, pensati sulle possibilità dello studente. Serve il <strong>consenso della famiglia</strong>.", "Attestato di credito formativo"),
]
FIG_PERC = """
    <figure class="dsa-figure" aria-labelledby="cap-perc">
      <div class="perc-grid">
""" + '\n'.join(
    f'        <div class="perc"><span class="perc-l" aria-hidden="true">{l}</span><div><div class="perc-t"><span class="sr-only">Percorso {l}: </span>{t}</div><p>{d}</p><span class="perc-out">Alla fine: {o}</span></div></div>'
    for l, t, d, o in PERC) + """
      </div>
      <figcaption id="cap-perc">I tre percorsi previsti alle superiori. Con i percorsi A e B si ottiene il diploma, se si supera l'esame di maturità. Con il percorso C si ottiene un attestato con le competenze raggiunte.</figcaption>
    </figure>"""

CAL = [
    ("g1", "🤝", "Studente già iscritto nella scuola", [
        "Durante l'anno il GLO controlla il PEI nelle verifiche intermedie",
        "Entro giugno fa la verifica finale dell'anno che si chiude",
        "Entro giugno approva il PEI definitivo per l'anno successivo, con le ore di sostegno",
        "Nelle prime due settimane di ottobre può aggiornarlo, dopo aver conosciuto la nuova classe"]),
    ("g1", "🤝", "Nuovo iscritto o prima certificazione", [
        "La famiglia consegna alla scuola la certificazione",
        "Entro giugno il GLO prepara il PEI provvisorio",
        "Entro il 15 ottobre approva il PEI definitivo",
        "Durante l'anno lo controlla nelle verifiche intermedie"]),
]
FIG_CAL = """
    <figure class="dsa-figure" aria-labelledby="cap-cal">
      <div class="path-grid">
""" + '\n'.join(
    f'        <div class="path-col {g}"><div class="pc-title"><span aria-hidden="true">{ico}</span> {name}</div><ol role="list">'
    + ''.join(f'<li>{step}</li>' for step in steps) + '</ol></div>'
    for g, ico, name, steps in CAL) + """
      </div>
      <figcaption id="cap-cal">Il calendario del PEI secondo il decreto-legge 170 del 2026, ancora da convertire in legge. Il primo riquadro vale per chi è già nella scuola, il secondo per chi arriva o è stato appena certificato.</figcaption>
    </figure>"""

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Il PEI serve anche per i DSA o per gli altri BES?",
        "No. Il PEI è il documento per gli studenti con disabilità certificata secondo la Legge 104. Per i DSA e per gli altri BES la scuola prepara il PDP, il Piano Didattico Personalizzato: lo spiego nella guida <a href=\"articolo-pdp-passo-dopo-passo.html\">Il PDP passo dopo passo</a>. Le differenze sono spiegate nella guida <a href=\"articolo-bes-dsa-disabilita.html\">Disabilità 104, DSA e BES</a>."),
    faq("Lo studente può partecipare al GLO?",
        "Sì. Alle superiori lo studente partecipa al GLO. È il principio di autodeterminazione, cioè il diritto di decidere per sé: può dire cosa gli serve, cosa funziona e quali obiettivi vuole raggiungere. Se gli è difficile parlare in una riunione, può preparare prima qualche appunto, anche con l'aiuto di un docente o della famiglia."),
    faq("La famiglia può portare un esperto di fiducia?",
        "Sì, ma al massimo uno. La famiglia lo chiede alla scuola e il dirigente scolastico autorizza la partecipazione. L'esperto può dare il suo parere, ma non vota e non decide."),
    faq("Che cosa posso fare se non sono d'accordo con il PEI?",
        "Dillo durante il GLO e chiedi che il tuo parere sia scritto nel verbale, cioè nel documento che riassume la riunione. Se il disaccordo resta, puoi chiedere un colloquio con il dirigente scolastico."),
    faq("Che cosa succede se la famiglia rifiuta il percorso differenziato?",
        "Se la famiglia dice di no per iscritto, lo studente viene valutato con gli stessi criteri dei compagni. Continua ad avere il sostegno, ma non ha la certezza di essere promosso. Se invece la famiglia non risponde entro la data fissata dalla scuola, la proposta vale come accettata. Prima di decidere, chiedi al consiglio di classe di spiegarti bene i motivi della proposta."),
    faq("Il PEI si può cambiare durante l'anno?",
        "Sì. Il PEI non è scritto una volta per tutte. Nelle verifiche intermedie il GLO controlla se gli obiettivi e gli aiuti funzionano e, se serve, li cambia."),
    faq("Chi decide le ore di sostegno?",
        "Le indica il GLO nel PEI, spiegando il motivo, in base ai bisogni dello studente e della classe. Con il decreto-legge del 2026 il PEI definisce le ore di sostegno, mentre prima conteneva solo una proposta. Poi è l'Ufficio scolastico regionale ad assegnare i docenti di sostegno alla scuola. Il testo del decreto può ancora cambiare con la conversione in legge."),
    faq("Che cos'è il progetto di vita? Sostituisce il PEI?",
        "No, non lo sostituisce. Il progetto di vita è previsto dalla riforma della disabilità, cioè il decreto legislativo 62 del 2024. Riguarda tutta la vita della persona, non solo la scuola. Il PEI ne diventa la parte scolastica: per questo nel modello c'è una sezione di raccordo con il progetto individuale. La riforma si sta applicando per gradi: chiedi al tuo Comune se riguarda già la tua zona."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <div class="dsa-box tldr" id="in-breve">
      <h2 class="box-title"><span aria-hidden="true">📌</span> L'articolo in 30 secondi</h2>
      <ul>
        <li>Il <strong>PEI</strong> (Piano Educativo Individualizzato) è il documento della scuola per gli studenti con <strong>disabilità certificata</strong> (Legge 104).</li>
        <li>Lo scrive e lo approva il <strong>GLO</strong>, un gruppo di lavoro. Ne fanno parte i docenti, la famiglia, gli specialisti e, alle superiori, <strong>lo studente stesso</strong>.</li>
        <li>Dice <strong>quali obiettivi</strong> ha lo studente, <strong>quali aiuti</strong> riceve e che cosa cambia la scuola per togliere gli ostacoli.</li>
        <li>Alle superiori ci sono <strong>tre percorsi</strong>: con i primi due si prende il <strong>diploma</strong>, con il terzo, il percorso differenziato, un <strong>attestato</strong>.</li>
      </ul>
    </div>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title"><span aria-hidden="true">🧭</span> Indice</h2>
      <ol>
        <li><a href="#cos-e">Che cos'è il PEI e per chi è</a></li>
        <li><a href="#glo">Chi lo scrive: il GLO</a></li>
        <li><a href="#dentro">Cosa c'è dentro il PEI</a></li>
        <li><a href="#modello">Per i docenti: il modello in dodici sezioni</a></li>
        <li><a href="#percorsi">I tre percorsi alle superiori</a></li>
        <li><a href="#calendario">Quando si scrive: il calendario e le novità del 2026</a></li>
        <li><a href="#partecipare">Come partecipare al GLO</a></li>
        <li><a href="#falsi-miti">Quattro falsi miti</a></li>
        <li><a href="#informatica">E in informatica, che cosa cambia?</a></li>
        <li><a href="#sintesi">In sintesi</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <p>Se tuo figlio ha una disabilità certificata, o se sei uno studente con una certificazione, prima o poi senti parlare del <strong>PEI</strong>.</p>
    <p>È un documento importante: decide <strong>come</strong> lo studente impara a scuola, <strong>con quali aiuti</strong> e <strong>verso quali traguardi</strong>.</p>
    <p>Lavoro ogni giorno come <a href="/#chi-sono">docente per l'inclusività</a> e partecipo ai GLO, i gruppi che scrivono il PEI. In questa guida ti spiego il PEI passo dopo passo, senza dare nulla per scontato.</p>
    <p>Ci sono anche due parti pensate per i colleghi docenti: il modello nazionale e i tre percorsi delle superiori. Se una sigla ti sfugge, trovi tutto nella guida <a href="articolo-bes-dsa-disabilita.html#sigle">Disabilità 104, DSA e BES</a>.</p>

    <h2 id="cos-e">Che cos'è il PEI e per chi è</h2>
    <p><strong>PEI</strong> vuol dire <strong>Piano Educativo Individualizzato</strong>. «Individualizzato» significa costruito su misura per <strong>quello</strong> studente, non per una categoria.</p>
    <p>Il PEI riguarda solo gli studenti con <strong>disabilità certificata</strong> ai fini dell'inclusione scolastica, secondo la <strong>Legge 104 del 1992</strong>. È il gruppo 1 della guida sulle differenze tra disabilità, DSA e BES.</p>
    <div class="group-box g1">
      <h3><span aria-hidden="true">🤝</span> Gruppo 1 · Disabilità certificata</h3>
      <p>Con la certificazione la scuola prepara il <strong>PEI</strong> e alla classe viene assegnato un <strong>docente di sostegno</strong>. Per i <strong>DSA</strong> (Disturbi Specifici dell'Apprendimento) e per gli altri <strong>BES</strong> (Bisogni Educativi Speciali), invece, c'è il <strong>PDP</strong> (Piano Didattico Personalizzato).</p>
    </div>
    <p>Il PEI si basa sulla certificazione e sul <strong>Profilo di funzionamento</strong>. È il documento degli specialisti che descrive i punti di forza e i bisogni dello studente.</p>
    <p>Molti studenti non hanno ancora il Profilo di funzionamento, perché la riforma è in corso. In questo caso si usa la <strong>Diagnosi funzionale</strong>, il documento che c'era prima.</p>
    <p>Il PEI <strong>si scrive ogni anno</strong> e si controlla durante l'anno. Alle superiori accompagna lo studente fino all'esame di maturità.</p>

    <h2 id="glo">Chi lo scrive: il GLO</h2>
    <p>Il PEI non lo scrive una persona sola. Lo elabora e lo approva il <strong>GLO</strong>, il <strong>Gruppo di Lavoro Operativo per l'inclusione</strong>.</p>
    <p>Il GLO è una squadra: ognuno porta quello che sa dello studente. Ecco chi ne fa parte.</p>
{FIG_GLO}
    <p>Il docente di sostegno di solito prepara una <strong>bozza</strong>, insieme ai colleghi. Ma il PEI è del GLO: la famiglia e lo studente possono proporre modifiche prima che venga approvato.</p>

    <h2 id="dentro">Cosa c'è dentro il PEI</h2>
    <p>Il PEI parte da un'idea semplice: le difficoltà non dipendono solo dalla persona, ma anche dall'<strong>ambiente</strong> in cui vive e studia.</p>
    <p>Per questo il PEI guarda a due cose. Le <strong>barriere</strong> sono gli ostacoli, per esempio una scala senza ascensore o una spiegazione solo a voce. I <strong>facilitatori</strong> sono gli aiuti, per esempio un computer con la sintesi vocale o un compagno che fa da tutor.</p>
    <p>Questo modo di vedere viene dall'<strong>ICF</strong> (Classificazione Internazionale del Funzionamento), creata dall'Organizzazione Mondiale della Sanità.</p>
    <p>I docenti osservano lo studente in <strong>quattro dimensioni</strong>. Per ognuna il PEI indica gli <strong>obiettivi</strong>, le <strong>strategie</strong> e gli <strong>strumenti</strong>.</p>
{FIG_DIM}
    <p>Poi il PEI scende nel concreto: <strong>materia per materia</strong>, dice quali obiettivi ha lo studente, come si fanno le verifiche e come si valuta.</p>

    <h2 id="modello">Per i docenti: il modello in dodici sezioni</h2>
    <p>Il decreto interministeriale 182 del 2020 ha introdotto un <strong>modello nazionale di PEI</strong>, uguale in tutta Italia e diverso per ogni grado di scuola. Nel 2023 il modello è stato corretto.</p>
    <p>Il modello delle superiori ha <strong>dodici sezioni</strong>. Le sezioni dalla 4 alla 7 sono il cuore del PEI: prima si osserva, poi si interviene, sia sullo studente sia sul contesto.</p>
{FIG_SEZ}
    <p>Un consiglio per i colleghi delle altre materie: la <strong>sezione 8</strong> riguarda proprio la vostra materia. Il contributo di ogni docente della classe è necessario, non solo quello del docente di sostegno.</p>

    <h2 id="percorsi">I tre percorsi alle superiori</h2>
    <p>Alle superiori il PEI indica anche il <strong>tipo di percorso</strong> dello studente. È una scelta importante, perché decide il titolo che si ottiene alla fine.</p>
{FIG_PERC}
    <p>Il percorso differenziato <strong>non è una bocciatura</strong> e non è un percorso «di serie B». È la scelta giusta quando gli obiettivi della classe non sono adatti allo studente.</p>
    <p>L'attestato riporta le competenze raggiunte e permette di iscriversi ai corsi di formazione professionale. Attenzione però: <strong>non è un diploma</strong>. Non permette di iscriversi all'università né di partecipare ai concorsi che chiedono il diploma.</p>
    <p>Per questo serve il <strong>consenso della famiglia</strong>. Il consiglio di classe propone il percorso C e fissa una data entro cui rispondere. Se la famiglia non risponde entro quella data, la proposta vale come accettata.</p>
    <p>Se la famiglia dice di no per iscritto, lo studente viene <strong>valutato con gli stessi criteri dei compagni</strong>. Continua ad avere il sostegno, ma non ha la certezza di essere promosso.</p>
    <p>Il percorso si può rivedere. Se il consiglio di classe accerta che lo studente ha raggiunto gli obiettivi della classe, può farlo passare a un percorso che porta al diploma. Non servono esami sugli anni precedenti.</p>

    <h2 id="calendario">Quando si scrive: il calendario e le novità del 2026</h2>
    <div class="dsa-box update-box" role="note">
      <h3 class="box-title"><span aria-hidden="true">🔔</span> Regole in cambiamento</h3>
      <p>Il <strong>decreto-legge 30 settembre 2026, n. 170</strong> ha cambiato le scadenze del PEI. È in vigore dal 1° ottobre 2026.</p>
      <p>Però il Parlamento deve <strong>convertirlo in legge entro il 29 novembre 2026</strong>, e in quel passaggio può essere modificato.</p>
      <p>Qui trovi le regole del testo del decreto, come le riportano le riviste per la scuola, aggiornate al 15 novembre 2026. Aggiornerò l'articolo quando il testo sarà definitivo.</p>
    </div>
    <p>Fino a settembre 2026 il PEI definitivo si approvava di norma <strong>entro il 31 ottobre</strong>. Con il decreto-legge le scadenze cambiano, e sono diverse per chi è già nella scuola e per chi arriva.</p>
{FIG_CAL}
    <p>Il decreto è arrivato a ottobre, con l'anno scolastico già iniziato. Per il PEI di quest'anno, chiedi alla scuola quale scadenza ha seguito.</p>
    <p>Il decreto cambia anche le <strong>ore di sostegno</strong>: il PEI non contiene più solo una proposta, ma <strong>definisce le ore</strong>, spiegando il motivo. Poi è l'Ufficio scolastico regionale ad assegnare i docenti di sostegno alla scuola.</p>
    <p>Inoltre il GLO può approvare il PEI anche se una delle parti, regolarmente invitata, non è presente. Lo scopo è evitare che un'assenza faccia saltare le scadenze. Le condizioni precise le chiarirà il testo definitivo.</p>
    <p>Se non puoi partecipare a un GLO, avvisa subito la scuola. Chiedi un'altra data, oppure manda le tue osservazioni per iscritto.</p>
    <p>Come si applicheranno queste regole nel dettaglio lo chiariranno la legge di conversione e le indicazioni del Ministero. Per le date precise, chiedi sempre alla scuola.</p>

    <h2 id="partecipare">Come partecipare al GLO</h2>
    <p>La riunione del GLO può mettere un po' a disagio: tante persone intorno a un tavolo, tante sigle. Prepararsi aiuta molto. Ecco alcuni consigli pratici.</p>
    <ol class="steps-list">
      <li><strong>Chiedi la bozza prima della riunione.</strong> Così puoi leggerla con calma e segnare i dubbi.</li>
      <li><strong>Porta i documenti aggiornati.</strong> Per esempio nuove relazioni degli specialisti o dei terapisti.</li>
      <li><strong>Racconta come va a casa.</strong> Che cosa piace allo studente, cosa lo stanca, cosa lo aiuta: sono informazioni che a scuola non sempre si vedono.</li>
      <li><strong>Proponi obiettivi concreti.</strong> «Usare il computer da solo per scrivere un testo» è più utile di «migliorare l'autonomia».</li>
      <li><strong>Dai spazio allo studente.</strong> Alle superiori può parlare per sé: preparate insieme due o tre cose da dire.</li>
      <li><strong>Chiedi una copia del PEI approvato e del verbale</strong> della riunione, e annota le date delle verifiche.</li>
    </ol>

    <h2 id="falsi-miti">Quattro falsi miti</h2>
    <p>Ci sono alcune idee sbagliate sul PEI che sento spesso. Vediamole una per una.</p>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Con il PEI si fa un programma più facile».</p><p><strong>In realtà</strong> dipende dal percorso. Con il percorso ordinario gli obiettivi sono quelli della classe. Il PEI cambia il modo, gli strumenti e gli aiuti, non per forza il traguardo.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Il PEI lo scrive il docente di sostegno da solo».</p><p><strong>In realtà</strong> lo elabora e lo approva il GLO: tutti i docenti della classe, la famiglia, gli specialisti e lo studente.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Con il PEI non si prende il diploma».</p><p><strong>In realtà</strong> con il percorso ordinario e con quello personalizzato si prende il diploma, uguale a quello dei compagni. Solo con il percorso differenziato si riceve un attestato.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Una volta scritto, il PEI non si tocca più».</p><p><strong>In realtà</strong> il PEI si scrive ogni anno e si controlla durante l'anno. Se qualcosa non funziona, il GLO lo cambia.</p></div>

    <h2 id="informatica">E in informatica, che cosa cambia?</h2>
    <p>Ho insegnato informatica per anni: ti mostro come i tre percorsi possono diventare obiettivi concreti in laboratorio. Sono <strong>solo esempi</strong>: ogni PEI è diverso, perché ogni studente è diverso.</p>
    <ul class="icon-list">
      <li><span class="t-ico t-let" aria-hidden="true">A</span><span><strong>Percorso ordinario.</strong> Lo studente scrive gli stessi programmi della classe, per esempio con le <a href="articolo-if-else-python.html">condizioni if ed else in Python</a>. Può avere più tempo, la sintesi vocale o una tastiera adattata.</span></li>
      <li><span class="t-ico t-let" aria-hidden="true">B</span><span><strong>Percorso personalizzato.</strong> Gli obiettivi sono i contenuti essenziali della materia. La verifica è equipollente: per esempio, invece di scrivere il codice da zero, lo studente completa un programma o spiega un <a href="articolo-diagramma-di-flusso.html">diagramma di flusso</a>.</span></li>
      <li><span class="t-ico t-let" aria-hidden="true">C</span><span><strong>Percorso differenziato.</strong> Gli obiettivi riguardano competenze utili per la vita e per il lavoro. Per esempio: usare il computer in autonomia, salvare e ritrovare i file, scrivere una email, programmare con i blocchi colorati.</span></li>
    </ul>
    <p>In tutti e tre i casi il laboratorio di informatica è un ottimo <strong>facilitatore</strong>. Si impara facendo, si vede subito il risultato e si può riprovare senza paura di sbagliare.</p>

    <h2 id="sintesi">In sintesi</h2>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">🤝</span><span>Il <strong>PEI</strong> è il documento per gli studenti con <strong>disabilità certificata</strong> (Legge 104).</span></li>
      <li><span class="t-ico" aria-hidden="true">👥</span><span>Lo elabora e lo approva il <strong>GLO</strong>, di cui fanno parte anche la <strong>famiglia</strong> e, alle superiori, lo <strong>studente</strong>.</span></li>
      <li><span class="t-ico" aria-hidden="true">🎯</span><span>Indica <strong>obiettivi</strong>, <strong>aiuti</strong> e <strong>cambiamenti</strong> della scuola, materia per materia.</span></li>
      <li><span class="t-ico" aria-hidden="true">🎓</span><span>Alle superiori i percorsi A e B portano al <strong>diploma</strong>, se si supera l'esame. Il percorso C porta a un <strong>attestato</strong> e richiede il consenso della famiglia.</span></li>
      <li><span class="t-ico" aria-hidden="true">📅</span><span>Si scrive <strong>ogni anno</strong> e si controlla durante l'anno. Le scadenze sono cambiate nel 2026 e potrebbero cambiare ancora.</span></li>
    </ul>
    <p>Un buon PEI non è un modulo da riempire: è un <strong>progetto condiviso</strong>. Funziona davvero quando scuola, famiglia e studente lo costruiscono insieme.</p>
    <p class="norme rt-skip">Riferimenti normativi: Legge 5 febbraio 1992, n. 104 (artt. 12, 13 e 15); D.Lgs. 13 aprile 2017, n. 66, artt. 7 e 9 (modificato dal D.Lgs. 96/2019); D.I. 29 dicembre 2020, n. 182, modificato dal D.I. 1 agosto 2023, n. 153, con modelli di PEI e Linee guida; D.Lgs. 13 aprile 2017, n. 62, art. 20; D.M. 27 gennaio 2010, n. 9 (certificazione delle competenze); O.M. 21 maggio 2001, n. 90, art. 15; D.Lgs. 3 maggio 2024, n. 62 (progetto di vita); D.L. 30 settembre 2026, n. 170 (G.U. n. 227 del 30 settembre 2026), in corso di conversione in legge. Aggiornato al 15 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica pensate per tutti</h2>
      <p>Nelle lezioni gratuite trovi esempi da modificare e l'editor «Provalo tu» per vedere subito il risultato, senza installare nulla.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai un dubbio sul PEI o sul GLO? Vuoi raccontarmi la tua esperienza? <a href="contatti.html">Scrivimi</a>: leggo tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-bes-dsa-disabilita.html"><span aria-hidden="true">🧭</span><strong>Disabilità 104, DSA e BES: che differenza c'è?</strong></a>
        <a href="articolo-informatica-dsa.html"><span aria-hidden="true">📖</span><strong>Informatica e DSA: strategie e strumenti compensativi</strong></a>
        <a href="articolo-pdp-passo-dopo-passo.html"><span aria-hidden="true">📝</span><strong>Il PDP passo dopo passo: cos'è, chi lo scrive e cosa contiene</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="PEI, piano educativo individualizzato, cos'è il PEI, GLO, percorso differenziato, prove equipollenti, docente di sostegno, legge 104 scuola, decreto scuola 2026 PEI",
    og_alt="Il titolo «Il PEI spiegato semplice» e tre riquadri: chi lo scrive, il GLO; che cosa contiene, obiettivi e aiuti; quando, ogni anno.",
    date_iso="2026-11-15", modified_iso="2026-11-17", date_it="15 novembre 2026",
    ld_keywords="PEI, Piano Educativo Individualizzato, GLO, Legge 104, disabilità, inclusione scolastica, percorso differenziato, prove equipollenti, docente di sostegno",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Il PEI spiegato semplice» e tre riquadri: chi lo scrive, il GLO; che cosa contiene, obiettivi e aiuti; quando, ogni anno.",
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('PEI: parole', words, '| minuti', MIN)
