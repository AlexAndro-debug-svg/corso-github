#!/usr/bin/env python3
"""Articolo 1 della serie inclusione: BES, DSA e disabilità."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-bes-dsa-disabilita"
TITLE = "Disabilità 104, DSA e BES: che differenza c'è?"
SEO_TITLE = "Disabilità 104, DSA e BES: che differenza c'è? — AlessandroSimone.it"
DESC = "Che differenza c'è tra disabilità (Legge 104), DSA e BES, e tra PEI e PDP? Una guida semplice con tabella, schemi e lettura facilitata."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FIGURE
FIG_TRE = """
    <figure class="dsa-figure" aria-labelledby="cap-tre">
      <div class="group-cards">
        <div class="g-card g1"><span class="g-ico" aria-hidden="true">🤝</span><span class="g-num">Gruppo 1</span><span class="g-name">Disabilità certificata</span><span class="g-doc">Legge 104 · PEI</span></div>
        <div class="g-card g2"><span class="g-ico" aria-hidden="true">📖</span><span class="g-num">Gruppo 2</span><span class="g-name">DSA: dislessia, disortografia, disgrafia, discalculia</span><span class="g-doc">Legge 170 · PDP</span></div>
        <div class="g-card g3"><span class="g-ico" aria-hidden="true">🧩</span><span class="g-num">Gruppo 3</span><span class="g-name">Altri BES: per esempio ADHD o difficoltà con l'italiano</span><span class="g-doc">PDP se serve</span></div>
      </div>
      <figcaption id="cap-tre">Tre situazioni diverse, ognuna con le sue regole e il suo documento: disabilità, DSA e altri bisogni educativi speciali.</figcaption>
    </figure>"""

ROWS = [
    ("Cosa serve", "Una certificazione di disabilità ai fini dell'inclusione scolastica", "Una diagnosi di DSA del Servizio sanitario nazionale o di specialisti accreditati", "Nessuna certificazione obbligatoria: valuta il consiglio di classe"),
    ("Norme di riferimento", "Legge 104 del 1992 e decreto legislativo 66 del 2017", "Legge 170 del 2010 e Linee guida del 2011", "Direttiva del 27 dicembre 2012 e circolari del 2013"),
    ("Documento", "PEI (Piano Educativo Individualizzato)", "PDP (Piano Didattico Personalizzato)", "PDP, se il consiglio di classe lo decide"),
    ("Chi lo scrive", "Il GLO (Gruppo di Lavoro Operativo per l'inclusione)", "Il consiglio di classe, insieme alla famiglia", "Il consiglio di classe, insieme alla famiglia"),
    ("È obbligatorio?", "Sì", "Sì", "No: decide il consiglio di classe e spiega per iscritto il perché"),
    ("Docente di sostegno", "Sì, assegnato alla classe", "No", "No"),
    ("Titolo finale", "Diploma; attestato se il percorso è differenziato", "Diploma; attestato solo con esonero dalle lingue straniere", "Diploma"),
]
GROUPS = [("g1", "🤝", "Gruppo 1 · Disabilità"), ("g2", "📖", "Gruppo 2 · DSA"), ("g3", "🧩", "Gruppo 3 · Altri BES")]
FULL = {"g1": "Gruppo 1 · Disabilità certificata", "g2": "Gruppo 2 · DSA (Disturbi Specifici dell'Apprendimento)", "g3": "Gruppo 3 · Altri BES (bisogni educativi speciali)"}

def cmp_table():
    head = '<tr><th scope="col">Che cosa</th>' + ''.join(
        f'<th scope="col" class="{g}"><span aria-hidden="true">{ico}</span> {name}</th>' for g, ico, name in GROUPS) + '</tr>'
    body = '\n'.join('          <tr><th scope="row">' + r[0] + '</th>' + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in ROWS)
    cards = '\n'.join(
        f'        <div class="cmp-card {g}"><div class="cc-title"><span aria-hidden="true">{ico}</span> {FULL[g]}</div><dl>'
        + ''.join(f'<dt>{r[0]}</dt><dd>{r[i + 1]}</dd>' for r in ROWS) + '</dl></div>'
        for i, (g, ico, name) in enumerate(GROUPS))
    return f"""
    <figure class="dsa-figure" aria-labelledby="cap-tab">
      <table class="cmp-table">
        <caption class="sr-only">Confronto tra disabilità, DSA e altri BES</caption>
        <thead>{head}</thead>
        <tbody>
{body}
        </tbody>
      </table>
      <div class="cmp-cards">
{cards}
      </div>
      <figcaption id="cap-tab">Per ognuno dei tre gruppi la tabella indica cosa serve, le norme, il documento e chi lo scrive. Indica anche se il documento è obbligatorio, se c'è il docente di sostegno e quale titolo si ottiene alla fine.</figcaption>
    </figure>"""

SIGLE = [
    ("L. 104", "La legge del 1992 sui diritti delle persone con disabilità."),
    ("PEI", "Piano Educativo Individualizzato: il documento per gli studenti con disabilità certificata."),
    ("GLO", "Gruppo di Lavoro Operativo per l'inclusione: il gruppo che elabora il PEI."),
    ("DSA", "Disturbi Specifici dell'Apprendimento: dislessia, disortografia, disgrafia, discalculia."),
    ("L. 170", "La legge del 2010 sui DSA a scuola."),
    ("PDP", "Piano Didattico Personalizzato: il documento per gli studenti con DSA o con altri BES."),
    ("BES", "Bisogni Educativi Speciali: a scuola indica di solito chi ha bisogno di un'attenzione in più senza certificazione di disabilità né diagnosi di DSA."),
    ("ADHD", "Disturbo da deficit di attenzione e iperattività."),
]
FIG_SIGLE = """
    <figure class="dsa-figure" aria-labelledby="cap-sig">
      <div class="sigle-grid">
""" + '\n'.join(f'        <div class="sigla"><b>{a}</b><span>{b}</span></div>' for a, b in SIGLE) + """
      </div>
      <figcaption id="cap-sig">Le otto sigle più usate a scuola e il loro significato, nell'ordine dei tre gruppi.</figcaption>
    </figure>"""

PATHS = [
    ("g1", "🤝", "Percorso del gruppo 1 · Disabilità certificata", [
        "Il medico invia all'INPS il certificato medico introduttivo",
        "Una commissione accerta la disabilità ai fini dell'inclusione scolastica",
        "La famiglia consegna alla scuola la certificazione e il Profilo di funzionamento",
        "Il GLO approva il PEI, di norma entro il 31 ottobre, e lo verifica durante l'anno"]),
    ("g2", "📖", "Percorso del gruppo 2 · DSA", [
        "Valutazione specialistica (ASL o centro accreditato) e diagnosi di DSA",
        "La famiglia consegna la diagnosi alla scuola",
        "Il consiglio di classe scrive il PDP insieme alla famiglia",
        "Il PDP va preparato entro il primo trimestre di scuola, o appena possibile se la diagnosi arriva durante l'anno"]),
    ("g3", "🧩", "Percorso del gruppo 3 · Altri BES", [
        "I docenti notano una difficoltà, oppure la famiglia porta una diagnosi (per esempio di ADHD)",
        "Il consiglio di classe ne parla con la famiglia",
        "Decide se serve un PDP e spiega per iscritto la sua scelta",
        "Il PDP può essere temporaneo: dura il tempo necessario"]),
]
FIG_PERCORSI = """
    <figure class="dsa-figure" aria-labelledby="cap-per">
      <div class="path-grid">
""" + '\n'.join(
    f'        <div class="path-col {g}"><div class="pc-title"><span aria-hidden="true">{ico}</span> {name}</div><ol role="list">'
    + ''.join(f'<li>{step}</li>' for step in steps) + '</ol></div>'
    for g, ico, name, steps in PATHS) + """
      </div>
      <figcaption id="cap-per">I tre percorsi, passo dopo passo: dalla difficoltà notata al documento che la scuola prepara.</figcaption>
    </figure>"""

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("BES e DSA sono la stessa cosa?",
        "No. I DSA hanno una legge tutta loro, la 170, e con la diagnosi il PDP è obbligatorio. Con «BES», a scuola, si indicano di solito gli altri bisogni educativi speciali, come l'ADHD o una difficoltà con l'italiano: per questi il PDP lo decide il consiglio di classe."),
    faq("Per avere un PDP serve per forza una diagnosi?",
        "Per i DSA sì: con la diagnosi, il PDP è obbligatorio. Per gli altri BES no: il consiglio di classe può preparare un PDP anche senza certificazione. Se la famiglia porta una diagnosi che non rientra nella Legge 104 o nella Legge 170, per esempio di ADHD, il consiglio decide in autonomia, ma deve scrivere a verbale il perché, sia che faccia il PDP sia che non lo faccia."),
    faq("Con un DSA o un altro BES c'è il docente di sostegno?",
        "No. Il docente di sostegno è previsto per gli studenti con disabilità certificata secondo la Legge 104. Per i DSA e gli altri BES si lavora con il PDP, gli strumenti compensativi e le misure dispensative."),
    faq("Che differenza c'è tra PEI e PDP?",
        "Il PEI è il documento per gli studenti con disabilità certificata e lo elabora il GLO. Il PDP è il documento per gli studenti con DSA o con altri BES e lo scrive il consiglio di classe insieme alla famiglia."),
    faq("Con il PEI si prende il diploma?",
        "Sì, se il percorso segue gli obiettivi della classe, o obiettivi riconducibili a quelli, anche con prove equipollenti, cioè adattate nei tempi, negli strumenti o nei modi. Se invece il percorso è differenziato, cioè ha obiettivi diversi da quelli della classe, alla fine non si riceve il diploma: si riceve un attestato di credito formativo con le competenze raggiunte."),
    faq("Chi decide se uno studente ha un BES?",
        "È il consiglio di classe a riconoscere il bisogno, osservando lo studente, coinvolgendo la famiglia e tenendo conto di eventuali diagnosi. Per la disabilità e per i DSA, invece, servono la certificazione o la diagnosi dei professionisti della salute."),
    faq("Un BES è per sempre? Resta scritto sul diploma?",
        "Dipende dal bisogno. Una difficoltà legata alla lingua o a un periodo complicato spesso è temporanea: il PDP si rivede ogni anno e, quando non serve più, non si rinnova. Un DSA o una disabilità accompagnano lo studente più a lungo, ma con gli aiuti giusti si può arrivare al diploma e anche all'università. Il diploma ha lo stesso valore di quello dei compagni e non riporta il PDP né gli strumenti usati. Le informazioni sulla salute dello studente restano riservate."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <div class="dsa-box tldr" id="in-breve">
      <h2 class="box-title"><span aria-hidden="true">📌</span> L'articolo in 30 secondi</h2>
      <ul>
        <li>A scuola ci sono <strong>tre situazioni diverse</strong>, ognuna con le sue regole: <strong>disabilità</strong>, <strong>DSA</strong> e <strong>altri bisogni educativi speciali (BES)</strong>.</li>
        <li><strong>Disabilità certificata</strong> (Legge 104): la scuola prepara il <strong>PEI</strong> (Piano Educativo Individualizzato) e alla classe è assegnato un <strong>docente di sostegno</strong>.</li>
        <li><strong>DSA</strong> (Legge 170): la scuola prepara il <strong>PDP</strong> (Piano Didattico Personalizzato), che è obbligatorio. <strong>Non</strong> c'è il docente di sostegno.</li>
        <li><strong>Altri BES</strong>, come l'ADHD o una difficoltà con l'italiano: il <strong>PDP</strong> si prepara se lo decide il consiglio di classe, anche solo per un periodo.</li>
      </ul>
    </div>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title"><span aria-hidden="true">🧭</span> Indice</h2>
      <ol>
        <li><a href="#tre-situazioni">Tre situazioni diverse</a></li>
        <li><a href="#tre-gruppi">Disabilità, DSA e BES, uno per uno</a></li>
        <li><a href="#tabella">Disabilità, DSA e BES: la tabella che chiarisce tutto</a></li>
        <li><a href="#sigle">Le sigle da conoscere</a></li>
        <li><a href="#falsi-miti">Quattro falsi miti</a></li>
        <li><a href="#percorsi">Come si arriva al PEI o al PDP?</a></li>
        <li><a href="#informatica">E in informatica, cosa cambia?</a></li>
        <li><a href="#sintesi">In sintesi</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <p>BES, DSA, 104, PDP, PEI, GLO: a scuola si sentono tante sigle, e spesso vengono usate come se fossero la stessa cosa. <strong>Non lo sono.</strong></p>
    <p>Capire la differenza è importante: a seconda del caso cambiano i <strong>documenti</strong> che la scuola prepara, <strong>chi</strong> li scrive e quali <strong>aiuti</strong> arrivano in classe.</p>
    <p>In questa guida ti spiego queste sigle una alla volta, con una tabella e qualche schema. Se una ti sfugge, la trovi in <a href="#sigle">Le sigle da conoscere</a>.</p>
    <p>Lavoro ogni giorno come <a href="/#chi-sono">docente di inclusione</a>, cioè docente di sostegno, e vorrei che tutti gli studenti e tutte le famiglie avessero le idee chiare su queste differenze.</p>

    <h2 id="tre-situazioni">Tre situazioni diverse</h2>
    <p>Quando uno studente ha bisogno di un aiuto in più, la scuola parte da una domanda: <strong>in quale situazione si trova?</strong> Le situazioni sono tre, e ognuna ha le sue regole.</p>
    <p>Le prime due hanno una <strong>legge tutta loro</strong>: la Legge 104 per la disabilità e la Legge 170 per i DSA. La terza, quella dei <strong>BES</strong>, si basa su una direttiva del Ministero ed è la più flessibile.</p>
{FIG_TRE}

    <h2 id="tre-gruppi">Disabilità, DSA e BES, uno per uno</h2>
    <p>Vediamo i tre gruppi nell'ordine: prima la disabilità, poi i DSA, infine gli altri BES.</p>

    <div class="group-box g1">
      <h3><span aria-hidden="true">🤝</span> 1. Disabilità certificata</h3>
      <p>Riguarda gli studenti con una <strong>disabilità certificata</strong> secondo la <strong>Legge 104 del 1992</strong>.</p>
      <p>Per loro la scuola prepara il <strong>PEI</strong>, il Piano Educativo Individualizzato, e alla classe viene assegnato un <strong>docente di sostegno</strong>.</p>
      <p>Il PEI lo elabora e lo approva il <strong>GLO</strong> (Gruppo di Lavoro Operativo per l'inclusione), presieduto dal dirigente scolastico. Ne fanno parte i docenti della classe, la famiglia, le figure professionali che seguono lo studente e un rappresentante dell'ASL. Alle superiori partecipa anche lo studente stesso.</p>
      <p>Come si scrive il PEI, cosa contiene e quali percorsi prevede alle superiori lo spiego nella guida <a href="articolo-pei-spiegato-semplice.html">Il PEI spiegato semplice</a>.</p>
    </div>

    <div class="group-box g2">
      <h3><span aria-hidden="true">📖</span> 2. DSA: Disturbi Specifici dell'Apprendimento</h3>
      <p>Qui ci sono la <strong>dislessia</strong>, la <strong>disortografia</strong>, la <strong>disgrafia</strong> e la <strong>discalculia</strong>, riconosciute dalla <strong>Legge 170 del 2010</strong>.</p>
      <p>Con una diagnosi di DSA del Servizio sanitario nazionale o di specialisti accreditati dalla Regione, la scuola deve preparare il <strong>PDP</strong>, il Piano Didattico Personalizzato.</p>
      <p>Per i DSA <strong>non è previsto il docente di sostegno</strong>, a meno che non ci sia anche una disabilità certificata. Se hai un DSA e studi informatica, ho scritto per te la guida <a href="articolo-informatica-dsa.html">Informatica e DSA</a>.</p>
      <p>Come si scrive il PDP e che cosa contiene lo spiego nella guida <a href="articolo-pdp-passo-dopo-passo.html">Il PDP passo dopo passo</a>.</p>
    </div>

    <div class="group-box g3">
      <h3><span aria-hidden="true">🧩</span> 3. Altri BES: i bisogni educativi speciali</h3>
      <p><strong>BES</strong> significa <strong>Bisogni Educativi Speciali</strong>. A scuola, con questa sigla, si indicano gli studenti che hanno bisogno di un'attenzione in più ma <strong>non</strong> hanno una certificazione di disabilità né una diagnosi di DSA.</p>
      <p>Un BES <strong>non è una diagnosi</strong>: è un modo di guardare lo studente. Il bisogno può essere permanente oppure temporaneo. Ci sono due grandi casi:</p>
      <ul>
        <li><strong>altri disturbi evolutivi</strong>, come l'<strong>ADHD</strong> (disturbo da deficit di attenzione e iperattività), i disturbi del linguaggio o della coordinazione motoria, o il funzionamento intellettivo limite, detto anche «borderline», che non è una disabilità intellettiva ma può rendere lo studio più faticoso;</li>
        <li><strong>svantaggio economico, sociale, linguistico o culturale</strong>: per esempio chi è arrivato da poco in Italia e sta ancora imparando l'italiano, o chi sta vivendo un periodo difficile in famiglia.</li>
      </ul>
      <p>In questi casi è il <strong>consiglio di classe</strong> a decidere se serve un PDP, spiegando per iscritto la sua scelta, spesso <strong>per un periodo limitato</strong>. Non è necessaria una certificazione medica e non è previsto il docente di sostegno.</p>
      <p class="note-dir">Una precisazione: nella direttiva ministeriale del 27 dicembre 2012, che ha introdotto i BES, il termine ha un senso più ampio e comprende anche disabilità e DSA. Nella pratica della scuola, però, si usa di solito per gli altri casi, ed è questo il significato che uso nella guida.</p>
    </div>

    <h2 id="tabella">Disabilità, DSA e BES: la tabella che chiarisce tutto</h2>
    <p>Ecco le differenze principali tra i tre gruppi, una accanto all'altra. Sul telefono, o se ingrandisci il testo, la tabella diventa tre schede, una per gruppo.</p>
{cmp_table()}
    <p>«Percorso differenziato» vuol dire con obiettivi diversi da quelli della classe: ne parlo nelle <a href="#faq">domande frequenti</a>.</p>

    <h2 id="sigle">Le sigle da conoscere</h2>
    <p>Se una sigla ti sfugge, torna qui: trovi le più usate, ognuna spiegata in una riga.</p>
{FIG_SIGLE}

    <h2 id="falsi-miti">Quattro falsi miti</h2>
    <p>Ci sono alcune idee sbagliate che sento spesso. Vediamole una per una.</p>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «BES, DSA e disabilità sono la stessa cosa».</p><p><strong>In realtà</strong> sono tre situazioni diverse, con leggi, documenti e aiuti diversi. Confonderle porta a chiedere aiuti sbagliati, o a non chiedere quelli giusti.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Con un DSA arriva l'insegnante di sostegno».</p><p><strong>In realtà</strong> il sostegno è previsto per la disabilità certificata. Con un DSA si lavora con il PDP. Il PDP prevede <a href="articolo-informatica-dsa.html#cosa-sono">strumenti compensativi</a>, come la sintesi vocale, e misure dispensative, come più tempo nelle verifiche.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Con il PDP si fa un programma più facile».</p><p><strong>In realtà</strong> il PDP non abbassa il traguardo. Con un DSA gli obiettivi restano quelli della classe: cambiano il modo di studiare e quello di fare le verifiche. Per altri BES, per esempio chi sta ancora imparando l'italiano, il PDP può alleggerire alcuni contenuti per un periodo, per riportare lo studente al passo con la classe.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Il docente di sostegno è l'insegnante personale dello studente».</p><p><strong>In realtà</strong> è un docente <strong>della classe</strong>: è contitolare, cioè ha le stesse responsabilità degli altri docenti verso tutti gli studenti. Cura in particolare il percorso previsto dal PEI, ma lavora con tutti e aiuta l'intera classe a diventare più inclusiva: è il lavoro che faccio ogni giorno.</p></div>

    <h2 id="percorsi">Come si arriva al PEI o al PDP?</h2>
    <p>Il punto di partenza è quasi sempre lo stesso: qualcuno nota una difficoltà. Può essere la famiglia, un docente o lo studente stesso. Poi le strade si dividono.</p>
{FIG_PERCORSI}
    <p>Il <strong>Profilo di funzionamento</strong> è un documento che descrive i punti di forza e i bisogni dello studente. Con la riforma della disabilità (decreto legislativo 62 del 2024), l'accertamento dell'INPS sta diventando la «valutazione di base».</p>
    <p>Per la disabilità e per i DSA il primo passo è una <strong>valutazione da parte di professionisti della salute</strong>. Pensi che tu o tuo figlio possiate avere un DSA o una disabilità? Parlane con il medico di famiglia o con il pediatra: può indirizzarti al servizio di neuropsichiatria infantile della ASL (a Roma si chiama TSMREE) o a un centro accreditato.</p>
    <p>Se invece è la scuola a dirti che tuo figlio ha un BES, chiedi un colloquio con il coordinatore di classe o con il referente per l'inclusione. Fatti spiegare che cosa hanno osservato e quali aiuti propongono. Il PDP si scrive insieme alla famiglia: puoi fare domande, raccontare come va a casa e proporre modifiche.</p>

    <h2 id="informatica">E in informatica, cosa cambia?</h2>
    <p>Da docente di informatica, ti mostro cosa può cambiare in laboratorio. Sono solo esempi: <strong>ogni studente è diverso</strong>.</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">🤝</span><span><strong>Con una disabilità</strong> il lavoro segue il PEI, che può mantenere gli stessi obiettivi della classe. Possono servire <strong>ausili</strong>, come tastiere facilitate, ingranditori dello schermo o sintesi vocale. Quando serve, si procede per gradi, per esempio con la <strong>programmazione a blocchi</strong>: invece di scrivere i comandi, si trascinano blocchi colorati.</span></li>
      <li><span class="t-ico" aria-hidden="true">📖</span><span><strong>Con un DSA</strong> sono utili l'editor con i colori, la sintesi vocale, i diagrammi di flusso e le verifiche al computer. Trovi tutto nella guida <a href="articolo-informatica-dsa.html#strumenti">Informatica e DSA</a>.</span></li>
      <li><span class="t-ico" aria-hidden="true">🧩</span><span><strong>Con un altro BES</strong> sono utili consegne brevi, una richiesta alla volta e attività pratiche al computer. <strong>Se l'italiano è ancora difficile</strong>, l'informatica ha un vantaggio: le parole chiave del codice, come <code>if</code>, <code>for</code> e <code>print</code>, sono poche, sempre le stesse in tutto il mondo e non dipendono dall'italiano. Può aiutare anche un <strong>glossario dei termini</strong>, con immagini e schemi visivi come il <a href="articolo-diagramma-di-flusso.html">diagramma di flusso</a>.</span></li>
      <li><span class="t-ico" aria-hidden="true">🏫</span><span><strong>Per tutta la classe</strong> consegne chiare, esempi in formato digitale e schemi visivi aiutano chi ha un bisogno educativo speciale e, in realtà, tutti. È l'idea della <strong>didattica inclusiva</strong>, la stessa con cui ho costruito le <a href="lezioni.html">lezioni gratuite</a> di questo sito.</span></li>
    </ul>

    <h2 id="sintesi">In sintesi</h2>
    <p>Disabilità, DSA e BES sono <strong>tre situazioni diverse</strong>, ognuna con il suo documento:</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">🤝</span><span><strong>disabilità certificata</strong> (Legge 104): PEI e docente di sostegno;</span></li>
      <li><span class="t-ico" aria-hidden="true">📖</span><span><strong>DSA</strong> (Legge 170): PDP obbligatorio;</span></li>
      <li><span class="t-ico" aria-hidden="true">🧩</span><span><strong>altri BES</strong>, come l'ADHD o una difficoltà con l'italiano: PDP se lo decide il consiglio di classe, anche per un periodo limitato.</span></li>
    </ul>
    <p>Qualunque sia la situazione, l'obiettivo è lo stesso: permettere a ogni studente di imparare <strong>al meglio delle sue possibilità</strong>. E le idee che aiutano chi ha un bisogno in più finiscono quasi sempre per aiutare tutta la classe.</p>
    <p class="norme rt-skip">Riferimenti normativi: Legge 5 febbraio 1992, n. 104 (art. 13, c. 6); Legge 8 ottobre 2010, n. 170; D.M. 12 luglio 2011, n. 5669 e Linee guida allegate; Direttiva ministeriale 27 dicembre 2012; Circolare ministeriale 6 marzo 2013, n. 8; Nota ministeriale 22 novembre 2013, prot. 2563; D.Lgs. 13 aprile 2017, n. 62, art. 20; D.Lgs. 13 aprile 2017, n. 66 (modificato dal D.Lgs. 96/2019); D.I. 29 dicembre 2020, n. 182, modificato dal D.I. 1 agosto 2023, n. 153 (modelli di PEI); D.Lgs. 3 maggio 2024, n. 62 (valutazione di base).</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica pensate per tutti</h2>
      <p>Nelle lezioni gratuite trovi esempi da modificare e l'editor «Provalo tu» per vedere subito il risultato, senza installare nulla.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai un dubbio su BES, PDP o PEI? Vuoi raccontarmi la tua esperienza? <a href="contatti.html">Scrivimi</a>: leggo tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-informatica-dsa.html"><span aria-hidden="true">📖</span><strong>Informatica e DSA: strategie e strumenti compensativi</strong></a>
        <a href="articolo-pdp-passo-dopo-passo.html"><span aria-hidden="true">📝</span><strong>Il PDP passo dopo passo: cos'è, chi lo scrive e cosa contiene</strong></a>
        <a href="articolo-pei-spiegato-semplice.html"><span aria-hidden="true">🤝</span><strong>Il PEI spiegato semplice: cos'è, chi lo scrive e come funziona</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(re.sub(r'<div class="cmp-cards">.*?\n      </div>', ' ', BODY, flags=re.S), skip=('pre', 'svg', 'nav', 'details'))  # il confronto si conta una volta
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="BES, bisogni educativi speciali, differenza BES DSA, BES DSA disabilità, differenza PEI PDP, legge 104 scuola, docente di sostegno, PDP BES",
    og_alt="Il titolo «Disabilità 104, DSA e BES» e tre riquadri separati e numerati: 1 disabilità con il PEI, 2 DSA con il PDP, 3 altri BES con il PDP se serve.",
    date_iso="2026-11-14", modified_iso="2026-11-17", date_it="14 novembre 2026",
    ld_keywords="BES, bisogni educativi speciali, DSA, disabilità, Legge 104, Legge 170, PEI, PDP, GLO, inclusione scolastica",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Disabilità 104, DSA e BES» e tre riquadri separati e numerati: 1 disabilità con il PEI, 2 DSA con il PDP, 3 altri BES con il PDP se serve.",
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('BES: parole', words, '| minuti', MIN)
