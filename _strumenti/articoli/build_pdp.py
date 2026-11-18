#!/usr/bin/env python3
"""Articolo 3 della serie inclusione: il PDP passo dopo passo."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-pdp-passo-dopo-passo"
TITLE = "Il PDP passo dopo passo: cos'è, chi lo scrive e cosa contiene"
SEO_TITLE = "PDP per DSA e BES: cos'è, chi lo scrive, cosa contiene — AlessandroSimone.it"
DESC = "Cos'è il PDP per DSA e altri BES, chi lo scrive, entro quando, strumenti compensativi e misure dispensative. Guida semplice per famiglie e studenti."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FIGURE
VOCI = [
    "<strong>Dati dello studente</strong>: chi è, che classe frequenta, chi ha fatto la diagnosi.",
    "<strong>Descrizione del disturbo</strong>: che cosa fa fatica a fare e quali sono i suoi punti di forza.",
    "<strong>Attività individualizzate</strong>: esercizi e momenti di lavoro pensati per lui, per raggiungere gli stessi obiettivi della classe.",
    "<strong>Attività personalizzate</strong>: modi di insegnare diversi, scelti per valorizzare il suo modo di imparare.",
    "<strong>Strumenti compensativi</strong>: gli strumenti che può usare, a lezione e nelle verifiche.",
    "<strong>Misure dispensative</strong>: le attività da cui è dispensato, cioè che non gli vengono chieste.",
    "<strong>Verifiche e valutazione</strong>: come si fanno le prove e come si danno i voti.",
]
FIG_VOCI = """
    <figure class="dsa-figure" aria-labelledby="cap-voci">
      <ol class="steps-list">
""" + '\n'.join(f'        <li>{x}</li>' for x in VOCI) + """
      </ol>
      <figcaption id="cap-voci">Le sette voci che ogni PDP per i DSA deve contenere secondo le Linee guida del 2011. Si scrivono per ogni materia in cui il disturbo pesa.</figcaption>
    </figure>"""

FIG_SM = """
    <figure class="dsa-figure" aria-labelledby="cap-sm">
      <div class="pdp-grid">
        <div class="dsa-box pdp-col">
          <h3><span aria-hidden="true">🧰</span> Strumenti compensativi</h3>
          <p>Ti aiutano a superare l'ostacolo che il disturbo mette sulla tua strada.</p>
          <ul>
            <li>sintesi vocale, che legge i testi ad alta voce;</li>
            <li>computer con correttore ortografico;</li>
            <li>calcolatrice e tabelle delle formule;</li>
            <li>mappe concettuali e schemi;</li>
            <li>registrazione delle lezioni, solo per studiare e con le regole della scuola sulla privacy.</li>
          </ul>
        </div>
        <div class="dsa-box pdp-col">
          <h3><span aria-hidden="true">✋</span> Misure dispensative</h3>
          <p>Tolgono le attività che il disturbo rende molto faticose, senza abbassare gli obiettivi.</p>
          <ul>
            <li>leggere ad alta voce davanti alla classe;</li>
            <li>prendere appunti sotto dettatura veloce;</li>
            <li>copiare lunghi testi dalla lavagna;</li>
            <li>imparare a memoria liste, date o tabelline;</li>
            <li>fare più verifiche nello stesso giorno.</li>
          </ul>
        </div>
      </div>
      <figcaption id="cap-sm">Esempi di strumenti compensativi e di misure dispensative. Sono solo esempi: nel PDP si scelgono quelli utili a quello studente.</figcaption>
    </figure>"""

PATHS = [
    ("g2", "📖", "Percorso del gruppo 2 · DSA", [
        "Valutazione specialistica e diagnosi di DSA, nel Servizio sanitario o presso specialisti accreditati",
        "La famiglia consegna la diagnosi alla segreteria della scuola",
        "Il consiglio di classe osserva lo studente e incontra la famiglia",
        "Il PDP si scrive entro il primo trimestre, o appena possibile se la diagnosi arriva durante l'anno",
        "Durante l'anno si controlla se funziona; l'anno dopo si aggiorna"]),
    ("g3", "🧩", "Percorso del gruppo 3 · Altri BES", [
        "I docenti notano una difficoltà, oppure la famiglia porta una diagnosi, per esempio di ADHD",
        "Il consiglio di classe ne parla con la famiglia",
        "Decide se serve un PDP e scrive il motivo nel verbale della riunione",
        "Il PDP può valere solo per un periodo: dura il tempo necessario",
        "Quando la difficoltà è superata, il PDP non si rinnova"]),
]
FIG_PERCORSI = """
    <figure class="dsa-figure" aria-labelledby="cap-per">
      <div class="path-grid">
""" + '\n'.join(
    f'        <div class="path-col {g}"><div class="pc-title"><span aria-hidden="true">{ico}</span> {name}</div><ol role="list">'
    + ''.join(f'<li>{step}</li>' for step in steps) + '</ol></div>'
    for g, ico, name, steps in PATHS) + """
      </div>
      <figcaption id="cap-per">Come si arriva al PDP. Il primo riquadro vale per i DSA, il secondo per gli altri bisogni educativi speciali.</figcaption>
    </figure>"""

LINGUE = [
    ("A", "Dispensa dalle prove scritte", "Lo studente studia le lingue come i compagni, ma al posto degli scritti fa <strong>prove orali</strong>, anche all'esame di maturità. Servono tre cose: una diagnosi che descrive un disturbo grave e chiede la dispensa, la richiesta della famiglia e il sì del consiglio di classe.", "Alla fine: diploma"),
    ("B", "Esonero dalle lingue straniere", "Lo studente <strong>non studia</strong> le lingue straniere. È previsto solo nei casi più gravi, anche con altri disturbi, su richiesta della famiglia e con il sì del consiglio di classe. Il percorso diventa <strong>differenziato</strong>, cioè con obiettivi diversi da quelli della classe.", "Alla fine: attestato di credito formativo, non diploma"),
]
FIG_LINGUE = """
    <figure class="dsa-figure" aria-labelledby="cap-lin">
      <div class="perc-grid">
""" + '\n'.join(
    f'        <div class="perc"><span class="perc-l" aria-hidden="true">{l}</span><div><div class="perc-t">{t}</div><p>{d}</p><span class="perc-out">{o}</span></div></div>'
    for l, t, d, o in LINGUE) + """
      </div>
      <figcaption id="cap-lin">Dispensa ed esonero dalle lingue straniere sono due cose molto diverse: con la dispensa si prende il diploma, con l'esonero no.</figcaption>
    </figure>"""

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Se mio figlio va bene a scuola, serve comunque il PDP?",
        "Se la famiglia ha consegnato una diagnosi di DSA, la scuola deve preparare il PDP. Può essere un PDP leggero, con poche misure. Va bene così: il PDP descrive ciò che serve a quello studente, non di più."),
    faq("Una diagnosi fatta da uno specialista privato è valida?",
        "La diagnosi deve venire dal Servizio sanitario nazionale o, se la Regione lo prevede, da strutture e professionisti accreditati. Le regole cambiano da regione a regione: se hai una diagnosi privata, chiedi alla ASL o alla scuola se è valida. Mentre aspetti la diagnosi valida, il consiglio di classe può già decidere di usare alcune misure."),
    faq("Entro quando va consegnata la diagnosi all'ultimo anno?",
        "Negli anni in cui c'è un esame, come la quinta superiore, la diagnosi va consegnata di norma entro il 31 marzo. La prima diagnosi in assoluto può essere rilasciata in qualunque momento dell'anno. Se arriva dopo il 31 marzo, però, le scuole non si comportano tutte allo stesso modo: parlane subito con la scuola."),
    faq("Con l'ADHD serve il PDP?",
        "L'ADHD non rientra nella Legge 170. Per questo è il consiglio di classe a decidere se preparare un PDP, e deve scrivere il motivo nel verbale. Se lo studente ha anche un DSA, il PDP è obbligatorio. Nei casi più gravi può essere riconosciuta una disabilità: allora la scuola prepara il PEI."),
    faq("La famiglia deve firmare il PDP?",
        "Di solito il PDP lo firmano il dirigente scolastico, i docenti e la famiglia. Per gli altri BES lo prevede una circolare del 2013. Con la firma dici che lo hai letto e condiviso. Prima di firmare, chiedi le modifiche che ti sembrano utili. Se non sei d'accordo, chiedi un nuovo incontro con il consiglio di classe."),
    faq("Che cosa posso fare se il PDP non viene preparato o non viene rispettato?",
        "Parlane prima con il docente della materia o con il coordinatore di classe. Se non basta, chiedi un colloquio con il referente per l'inclusione, cioè il docente che coordina queste attività nella scuola. Se il problema resta, scrivi al dirigente scolastico, soprattutto se il PDP non è pronto dopo il primo trimestre."),
    faq("Il PDP si vede sul diploma? Vale anche all'università?",
        "No, il diploma è uguale a quello dei compagni e non parla del PDP. All'università il PDP della scuola non vale. La Legge 170 prevede però aiuti anche lì, compresi i test d'ingresso: si chiedono all'ufficio dell'università che segue gli studenti con DSA, portando la diagnosi."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <div class="dsa-box tldr" id="in-breve">
      <h2 class="box-title"><span aria-hidden="true">📌</span> L'articolo in 30 secondi</h2>
      <ul>
        <li>Il <strong>PDP</strong> (Piano Didattico Personalizzato) è il documento che dice <strong>come la scuola aiuta</strong> uno studente a imparare e come lo valuta.</li>
        <li>Con una diagnosi di <strong>DSA</strong> (Disturbi Specifici dell'Apprendimento) il PDP è <strong>obbligatorio</strong>. Per gli <strong>altri BES</strong> (Bisogni Educativi Speciali) lo decide il consiglio di classe.</li>
        <li>Lo scrive il <strong>consiglio di classe</strong> insieme alla <strong>famiglia</strong>, per i DSA entro il <strong>primo trimestre</strong>.</li>
        <li>Contiene gli <strong>strumenti compensativi</strong>, le <strong>misure dispensative</strong> e il modo di fare verifiche e voti. Con un DSA gli <strong>obiettivi restano quelli della classe</strong>.</li>
      </ul>
    </div>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title"><span aria-hidden="true">🧭</span> Indice</h2>
      <ol>
        <li><a href="#cos-e">Che cos'è il PDP e per chi è</a></li>
        <li><a href="#chi-quando">Chi lo scrive e quando</a></li>
        <li><a href="#percorso">Il PDP passo dopo passo</a></li>
        <li><a href="#dentro">Che cosa c'è dentro il PDP</a></li>
        <li><a href="#strumenti">Strumenti compensativi e misure dispensative</a></li>
        <li><a href="#verifiche">Verifiche e voti</a></li>
        <li><a href="#lingue">Le lingue straniere: dispensa ed esonero</a></li>
        <li><a href="#altri-bes">Il PDP per gli altri BES</a></li>
        <li><a href="#firmare">Prima di firmare: cinque domande da farsi</a></li>
        <li><a href="#falsi-miti">Quattro falsi miti</a></li>
        <li><a href="#informatica">E in informatica?</a></li>
        <li><a href="#sintesi">In sintesi</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <p>Hai appena consegnato a scuola una diagnosi di DSA? Oppure la scuola ti ha proposto un <strong>PDP</strong>? In questa guida ti spiego che cos'è e come si costruisce, un passo alla volta.</p>
    <p>Lavoro ogni giorno come docente per l'inclusività (<a href="/#chi-sono">chi sono</a>) e faccio parte dei consigli di classe, dove i PDP si scrivono. Ho cercato di rispondere alle domande che una famiglia o uno studente si fanno davanti a questo documento.</p>
    <p>Se le sigle ti confondono, parti dalla guida <a href="articolo-bes-dsa-disabilita.html">Disabilità 104, DSA e BES: che differenza c'è?</a></p>

    <h2 id="cos-e">Che cos'è il PDP e per chi è</h2>
    <p><strong>PDP</strong> vuol dire <strong>Piano Didattico Personalizzato</strong>. È un documento scritto, che la scuola prepara per uno studente.</p>
    <p>Nel PDP la scuola scrive <strong>come</strong> lo studente impara meglio, quali <strong>aiuti</strong> riceve e <strong>come</strong> si fanno le verifiche. Lo scopo è permettergli di mostrare davvero quello che sa.</p>
    <p>Il PDP riguarda due gruppi di studenti, con regole diverse.</p>
    <div class="group-box g2">
      <h3><span aria-hidden="true">📖</span> Gruppo 2 · DSA: il PDP è obbligatorio</h3>
      <p>I <strong>DSA</strong> sono la <strong>dislessia</strong>, la <strong>disortografia</strong>, la <strong>disgrafia</strong> e la <strong>discalculia</strong>. Li riconosce la <strong>Legge 170 del 2010</strong>.</p>
      <p>Quando la famiglia consegna la diagnosi, la scuola <strong>deve</strong> preparare il PDP. Con un DSA gli <strong>obiettivi restano quelli della classe</strong>: cambia la strada per arrivarci.</p>
    </div>
    <div class="group-box g3">
      <h3><span aria-hidden="true">🧩</span> Gruppo 3 · Altri BES: il PDP se serve</h3>
      <p>Sono gli studenti con un bisogno educativo speciale che non è una disabilità e non è un DSA. Per esempio chi ha l'<strong>ADHD</strong> (disturbo da deficit di attenzione e iperattività) o chi sta ancora imparando l'italiano.</p>
      <p>In questi casi è il <strong>consiglio di classe</strong> a decidere se serve un PDP. Spesso il PDP vale <strong>per un periodo limitato</strong>.</p>
    </div>
    <p>Per gli studenti con <strong>disabilità certificata</strong> (Legge 104), invece, la scuola prepara un altro documento, il <strong>PEI</strong> (Piano Educativo Individualizzato). Lo spiego nella guida <a href="articolo-pei-spiegato-semplice.html">Il PEI spiegato semplice</a>.</p>

    <h2 id="chi-quando">Chi lo scrive e quando</h2>
    <p>Il PDP lo scrive il <strong>consiglio di classe</strong>, cioè tutti i docenti della classe. Di solito il coordinatore di classe raccoglie le proposte dei colleghi e prepara il testo.</p>
    <p>La <strong>famiglia</strong> partecipa: racconta come va lo studio a casa, porta la diagnosi e le indicazioni degli specialisti, propone modifiche.</p>
    <p>Alle superiori è molto utile coinvolgere anche lo <strong>studente</strong>. Chi usa gli strumenti ogni giorno sa meglio di tutti quali funzionano.</p>
    <p>Per i DSA il PDP va preparato <strong>entro il primo trimestre</strong> dell'anno scolastico. Se la diagnosi arriva durante l'anno, va preparato <strong>appena possibile</strong>.</p>
    <p>Il PDP vale per <strong>un anno scolastico</strong>. Ogni anno si aggiorna, perché lo studente cresce e cambiano le materie.</p>
    <p>Il PDP contiene informazioni sulla salute dello studente, quindi è <strong>riservato</strong>: lo conoscono i docenti e la famiglia, non i compagni.</p>

    <h2 id="percorso">Il PDP passo dopo passo</h2>
    <p>Il punto di partenza è quasi sempre lo stesso: qualcuno nota una difficoltà. Può essere la famiglia, un docente o lo studente stesso. Poi le strade si dividono.</p>
{FIG_PERCORSI}
    <p>Pensi che tu o tuo figlio possiate avere un DSA? Parlane con il medico di famiglia o con il pediatra. Può indirizzarti al servizio di neuropsichiatria infantile della ASL, l'Azienda sanitaria locale, oppure a un centro accreditato.</p>

    <h2 id="dentro">Che cosa c'è dentro il PDP</h2>
    <p>Ogni scuola usa il suo modello di PDP, ma alcune voci ci devono essere sempre. Le indicano le <strong>Linee guida sui DSA</strong> del 2011.</p>
{FIG_VOCI}
    <p>La parola chiave è <strong>«materia per materia»</strong>, almeno per le materie in cui il disturbo pesa. Un buon PDP non dice solo «usa la calcolatrice»: dice in quali materie, in quali verifiche e come.</p>

    <h2 id="strumenti">Strumenti compensativi e misure dispensative</h2>
    <p>Sono il cuore del PDP. Hanno nomi difficili, ma l'idea è semplice.</p>
    <p>Gli <strong>strumenti compensativi</strong> sono come gli <strong>occhiali</strong> per chi vede poco. Non rendono il compito più facile da capire: tolgono l'ostacolo del disturbo.</p>
    <p>Le <strong>misure dispensative</strong> tolgono un'attività che, a causa del disturbo, costerebbe troppa fatica senza insegnare nulla di più.</p>
{FIG_SM}
    <p>Gli strumenti funzionano solo se si usano <strong>con regolarità</strong>, a lezione e a casa, non solo il giorno della verifica. Quali strumenti esistono e come si usano lo spiego nella guida <a href="articolo-informatica-dsa.html#strumenti">Informatica e DSA</a>. Come averli a scuola lo trovi in <a href="articolo-tecnologie-assistive.html#come-averle">Tecnologie assistive per studiare</a>.</p>

    <h2 id="verifiche">Verifiche e voti</h2>
    <p>Il PDP dice anche <strong>come</strong> si fanno le verifiche e <strong>come</strong> si valutano. Ecco alcune misure che si trovano spesso.</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">📅</span><span><strong>Verifiche programmate</strong>, con la data decisa in anticipo e non più di una al giorno.</span></li>
      <li><span class="t-ico" aria-hidden="true">⏱️</span><span><strong>Più tempo</strong>, oppure <strong>meno esercizi</strong> con gli stessi obiettivi.</span></li>
      <li><span class="t-ico" aria-hidden="true">🔊</span><span><strong>Consegne lette ad alta voce</strong> dal docente o dalla sintesi vocale.</span></li>
      <li><span class="t-ico" aria-hidden="true">🗣️</span><span><strong>Interrogazioni orali</strong> per recuperare uno scritto andato male.</span></li>
      <li><span class="t-ico" aria-hidden="true">🎯</span><span><strong>Si valuta il contenuto</strong>, non la forma: per esempio, con la disortografia non si tolgono punti per gli errori di ortografia.</span></li>
    </ul>
    <p>Valutare in modo personalizzato <strong>non vuol dire regalare voti</strong>. Vuol dire misurare quello che lo studente sa, senza che il disturbo lo nasconda.</p>
    <p>Anche all'<strong>esame di maturità</strong> la commissione tiene conto del PDP, ma con regole diverse. Con un <strong>DSA</strong> si possono avere più tempo e gli strumenti compensativi usati durante l'anno.</p>
    <p>Per gli <strong>altri BES</strong> all'esame non ci sono misure dispensative. Gli strumenti compensativi si possono usare solo se erano nel PDP e sono stati usati durante l'anno. Per questo conviene usarli con regolarità, fin dalle classi precedenti.</p>

    <h2 id="lingue">Le lingue straniere: dispensa ed esonero</h2>
    <p>Per le lingue straniere ci sono due possibilità. Hanno nomi simili, ma conseguenze molto diverse.</p>
{FIG_LINGUE}
    <p>La dispensa dagli scritti può essere <strong>temporanea</strong> o valere per tutto il percorso: lo decide il consiglio di classe. Il consiglio valuta con attenzione le scuole in cui le lingue sono materie principali, come il liceo linguistico o il tecnico per il turismo.</p>
    <p>Prima di chiedere l'esonero, parlane con la scuola e fatti spiegare bene che cosa comporta. L'<a href="articolo-pei-spiegato-semplice.html#percorsi">attestato di credito formativo</a> non è un diploma.</p>

    <h2 id="altri-bes">Il PDP per gli altri BES</h2>
    <p>Per gli altri BES le regole vengono da una direttiva del Ministero del 2012 e da una circolare del 2013. Sono più flessibili di quelle dei DSA.</p>
    <p>Non serve una diagnosi. Il consiglio di classe osserva lo studente, ne parla con la famiglia e decide se preparare un PDP. In ogni caso deve <strong>scrivere il motivo</strong> della sua scelta nel verbale, il documento che riassume la riunione.</p>
    <p>Il PDP può prevedere strumenti compensativi e misure dispensative, spesso <strong>per un periodo limitato</strong>. Per chi sta imparando l'italiano, per esempio, conta soprattutto imparare bene la lingua.</p>
    <p>Quando la difficoltà è superata, il PDP <strong>non si rinnova</strong>. È un aiuto per un tratto di strada, non un'etichetta.</p>

    <h2 id="firmare">Prima di firmare: cinque domande da farsi</h2>
    <p>Quando la scuola ti consegna il PDP, prenditi il tempo di leggerlo. Queste domande ti aiutano a capire se è scritto bene.</p>
    <ol class="steps-list">
      <li><strong>È scritto materia per materia?</strong> Le misure generiche, uguali per tutte le materie, servono poco.</li>
      <li><strong>Gli strumenti sono concreti?</strong> «Mappe concettuali nelle interrogazioni di storia» è più utile di «uso di mappe».</li>
      <li><strong>Vale anche nelle verifiche?</strong> Controlla che gli strumenti si possano usare anche durante le prove.</li>
      <li><strong>Lo studente sa che cosa c'è scritto?</strong> Se non conosce il suo PDP, difficilmente lo userà.</li>
      <li><strong>Quando si controlla se funziona?</strong> Chiedi quando ci sarà il prossimo incontro e fatti dare una copia del PDP firmato.</li>
    </ol>

    <h2 id="falsi-miti">Quattro falsi miti</h2>
    <p>Ci sono alcune idee sbagliate sul PDP che sento spesso. Vediamole una per una.</p>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Con il PDP si fa un programma più facile».</p><p><strong>In realtà</strong>, con un DSA gli obiettivi sono gli stessi della classe. Cambiano gli strumenti e il modo di fare le verifiche, non il traguardo.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Usare gli strumenti compensativi è come copiare».</p><p><strong>In realtà</strong> sono come gli occhiali: permettono di mostrare quello che sai. Il lavoro di pensare e di capire resta tuo.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Il PDP serve solo nelle verifiche».</p><p><strong>In realtà</strong> vale anche a lezione e a casa. Gli strumenti funzionano davvero solo se si usano ogni giorno. Il PDP lo applicano tutti i docenti della classe, in ogni materia coinvolta.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Il PDP si scrive una volta e vale per sempre».</p><p><strong>In realtà</strong> il PDP si aggiorna ogni anno e si può cambiare durante l'anno, se qualcosa non funziona.</p></div>

    <h2 id="informatica">E in informatica?</h2>
    <p>Ho insegnato informatica per anni, e il laboratorio offre tanti strumenti utili per un PDP. Per esempio:</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">💻</span><span><strong>verifiche al computer</strong> invece che su carta, soprattutto con la disgrafia;</span></li>
      <li><span class="t-ico" aria-hidden="true">🎨</span><span>un <strong>editor con i colori</strong>, che rende il codice più facile da leggere;</span></li>
      <li><span class="t-ico" aria-hidden="true">📋</span><span>una <strong>scheda della sintassi</strong> da tenere accanto durante le prove;</span></li>
      <li><span class="t-ico" aria-hidden="true">🎯</span><span>una valutazione attenta alla <strong>logica del programma</strong> più che agli errori di battitura.</span></li>
    </ul>
    <p>Trovi altri esempi, spiegati uno per uno, nella sezione <a href="articolo-informatica-dsa.html#pdp">Cosa si può prevedere nel PDP per l'informatica</a>.</p>

    <h2 id="sintesi">In sintesi</h2>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">📖</span><span>Con una diagnosi di <strong>DSA</strong> il PDP è <strong>obbligatorio</strong> e gli obiettivi restano quelli della classe.</span></li>
      <li><span class="t-ico" aria-hidden="true">🧩</span><span>Per gli <strong>altri BES</strong> il PDP lo decide il consiglio di classe, spesso per un periodo limitato.</span></li>
      <li><span class="t-ico" aria-hidden="true">👥</span><span>Lo scrive il <strong>consiglio di classe</strong> insieme alla <strong>famiglia</strong>; per i DSA entro il primo trimestre.</span></li>
      <li><span class="t-ico" aria-hidden="true">🧰</span><span>Contiene <strong>strumenti compensativi</strong>, <strong>misure dispensative</strong> e il modo di fare <strong>verifiche e voti</strong>, materia per materia.</span></li>
      <li><span class="t-ico" aria-hidden="true">📅</span><span>Si <strong>aggiorna ogni anno</strong> e si può cambiare quando serve.</span></li>
    </ul>
    <p>Un buon PDP non è un modulo da firmare e mettere in un cassetto. È uno <strong>strumento di lavoro</strong> che scuola, famiglia e studente usano insieme, ogni giorno.</p>
    <p class="norme rt-skip">Riferimenti normativi: Legge 8 ottobre 2010, n. 170 (artt. 2, 3, 5); D.M. 12 luglio 2011, n. 5669 (art. 6, lingue straniere) e Linee guida per il diritto allo studio degli alunni e degli studenti con DSA; Accordo Stato-Regioni 25 luglio 2012 sulla diagnosi e la certificazione dei DSA; Direttiva ministeriale 27 dicembre 2012; Circolare ministeriale 6 marzo 2013, n. 8; Nota ministeriale 22 novembre 2013, prot. 2563; D.Lgs. 13 aprile 2017, n. 62, art. 20; ordinanza ministeriale annuale sull'esame di maturità. Aggiornato al 17 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica pensate per tutti</h2>
      <p>Nelle lezioni gratuite trovi esempi da modificare e l'editor «Provalo tu» per vedere subito il risultato, senza installare nulla.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai un dubbio sul PDP? Vuoi raccontarmi la tua esperienza? <a href="contatti.html">Scrivimi</a>: leggo tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-informatica-dsa.html"><span aria-hidden="true">📖</span><strong>Informatica e DSA: strategie e strumenti compensativi</strong></a>
        <a href="articolo-bes-dsa-disabilita.html"><span aria-hidden="true">🧭</span><strong>Disabilità 104, DSA e BES: che differenza c'è?</strong></a>
        <a href="articolo-pei-spiegato-semplice.html"><span aria-hidden="true">🤝</span><strong>Il PEI spiegato semplice: cos'è, chi lo scrive e come funziona</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="PDP, piano didattico personalizzato, PDP DSA, PDP BES, strumenti compensativi, misure dispensative, dispensa lingue straniere, legge 170, PDP cosa contiene",
    og_alt="Il titolo «Il PDP passo dopo passo» e tre riquadri: per chi, DSA e altri BES; chi lo scrive, consiglio di classe e famiglia; quando, per i DSA entro il primo trimestre.",
    date_iso="2026-11-17", modified_iso="2026-11-18", date_it="17 novembre 2026",
    ld_keywords="PDP, Piano Didattico Personalizzato, DSA, BES, Legge 170, strumenti compensativi, misure dispensative, consiglio di classe, inclusione scolastica",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Il PDP passo dopo passo» e tre riquadri: per chi, DSA e altri BES; chi lo scrive, consiglio di classe e famiglia; quando, per i DSA entro il primo trimestre.",
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('PDP: parole', words, '| minuti', MIN)
