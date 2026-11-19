#!/usr/bin/env python3
"""Articolo 6 della serie inclusione: ADHD e programmazione."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-adhd-programmazione"
TITLE = "ADHD e programmazione: strategie pratiche per studiare informatica"
SEO_TITLE = "ADHD e programmazione: strategie per studiare informatica — AlessandroSimone.it"
DESC = "Hai l'ADHD e studi informatica? Strategie pratiche per programmare con più concentrazione, idee per il PDP e consigli per docenti e famiglie."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FIGURE
PRESENTAZIONI = [
    ("🎯", "Soprattutto disattenzione", "fatica a restare concentrato, si perde i dettagli, dimentica le cose, si distrae facilmente."),
    ("⚡", "Soprattutto iperattività e impulsività", "fatica a stare fermo, interrompe, risponde prima che la domanda sia finita."),
    ("🔀", "Combinata", "ci sono entrambi gli aspetti, in misura diversa da persona a persona."),
]
FIG_PRES = """
    <ul class="icon-list">
""" + '\n'.join(f'      <li><span class="t-ico" aria-hidden="true">{i}</span><span><strong>{t}</strong>: {d}</span></li>' for i, t, d in PRESENTAZIONI) + """
    </ul>"""

PRO_CONTRO = """
    <figure class="dsa-figure" aria-labelledby="cap-pc">
      <div class="pdp-grid">
        <div class="dsa-box pdp-col">
          <h3><span aria-hidden="true">👍</span> Che cosa aiuta</h3>
          <ul>
            <li>vedi <strong>subito il risultato</strong> di quello che scrivi;</li>
            <li>un programma si può costruire <strong>a piccoli passi</strong>;</li>
            <li>ogni errore risolto è una <strong>piccola vittoria</strong>;</li>
            <li>c'è spazio per la <strong>creatività</strong>: lo stesso problema si risolve in tanti modi.</li>
          </ul>
        </div>
        <div class="dsa-box pdp-col">
          <h3><span aria-hidden="true">🚧</span> Dove si inciampa</h3>
          <ul>
            <li>errori di <strong>distrazione</strong>, come una parentesi o due punti dimenticati;</li>
            <li><strong>consegne lunghe</strong>, con tante richieste insieme;</li>
            <li>la parte noiosa: <strong>cercare un errore</strong> per molto tempo;</li>
            <li>perdere la cognizione del tempo quando un problema ti appassiona.</li>
          </ul>
        </div>
      </div>
      <figcaption id="cap-pc">Che cosa della programmazione aiuta chi ha l'ADHD, e dove invece è più facile inciampare.</figcaption>
    </figure>"""

MEDIA = '''
# Passo 1: chiedo tre voti
voto1 = float(input("Primo voto: "))
voto2 = float(input("Secondo voto: "))
voto3 = float(input("Terzo voto: "))

# Passo 2: calcolo la media
media = (voto1 + voto2 + voto3) / 3

# Passo 3: stampo il risultato
print("Media:", round(media, 1))

# Passo 4: aggiungo un messaggio
if media >= 6:
    print("Sufficiente")
else:
    print("Da recuperare")
'''

CHECK = [
    "Ho messo i <strong>due punti</strong> dopo <code>if</code>, <code>else</code>, <code>for</code> e <code>def</code>?",
    "Le righe dentro un blocco sono <strong>rientrate</strong> tutte allo stesso modo?",
    "Ogni parentesi e ogni virgoletta che <strong>apro</strong>, la <strong>chiudo</strong>?",
    "Ho scritto i nomi delle variabili <strong>sempre allo stesso modo</strong>?",
    "Ho <strong>salvato</strong> il file prima di eseguirlo?",
]
FIG_CHECK = """
    <figure class="dsa-figure" aria-labelledby="cap-check">
      <ol class="steps-list">
""" + '\n'.join(f'        <li>{x}</li>' for x in CHECK) + """
      </ol>
      <figcaption id="cap-check">Una lista di controllo per gli errori di distrazione più comuni in Python. Puoi stamparla e tenerla accanto al computer.</figcaption>
    </figure>"""

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Con l'ADHD si ha diritto al PDP?",
        "L'ADHD non rientra nella Legge 170 sui DSA. Per questo è il consiglio di classe a decidere se preparare un PDP, e deve scrivere il motivo nel verbale. Se c'è anche un DSA, il PDP è obbligatorio. Nei casi più gravi può essere riconosciuta una disabilità: allora la scuola prepara il PEI."),
    faq("Chi fa la diagnosi di ADHD?",
        "La fanno gli specialisti, di solito il servizio di neuropsichiatria infantile della ASL (Azienda sanitaria locale) o un centro accreditato. Se pensi che tu o tuo figlio possiate avere l'ADHD, parlane prima con il medico di famiglia o con il pediatra."),
    faq("E i farmaci?",
        "Le decisioni sulle terapie spettano solo agli specialisti che seguono lo studente. In questa guida parlo di strategie di studio, che servono in ogni caso. Se un farmaco va preso durante l'orario scolastico, la scuola ha una procedura apposta: chiedi al dirigente scolastico."),
    faq("Posso usare un timer o le cuffie in classe?",
        "Sì, se sono previsti nel PDP. Ricorda che alle superiori il cellulare in classe è vietato, tranne nei casi previsti dal PEI o dal PDP. Per questo un timer separato dal telefono può essere più semplice da far accettare."),
    faq("L'intelligenza artificiale può aiutarmi?",
        "Sì, se la usi come un tutor: per esempio per farti dividere un esercizio lungo in passi più piccoli, o per farti spiegare un messaggio di errore. Non usarla per farti scrivere il programma. Come usarla bene lo spiego nella guida <a href=\"articolo-chatgpt-studiare.html\">Come usare ChatGPT per studiare</a>."),
    faq("Devo dire ai compagni che ho l'ADHD?",
        "È una scelta solo tua e della tua famiglia. Le informazioni sulla tua salute sono riservate: i docenti non possono comunicarle ai compagni senza il tuo consenso."),
    faq("All'esame di maturità che cosa vale?",
        "Per l'ADHD valgono le regole degli altri BES: all'esame non ci sono misure dispensative. Si possono usare gli strumenti compensativi previsti nel PDP e già usati durante l'anno. Se c'è anche un DSA, valgono le regole dei DSA, che prevedono anche più tempo."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <div class="dsa-box tldr" id="in-breve">
      <h2 class="box-title"><span aria-hidden="true">📌</span> L'articolo in 30 secondi</h2>
      <ul>
        <li>L'<strong>ADHD</strong> (disturbo da deficit di attenzione e iperattività) rende più difficile <strong>concentrarsi</strong>, <strong>organizzarsi</strong> e <strong>aspettare</strong>. Non dipende dalla volontà.</li>
        <li>La programmazione può essere un'ottima alleata: dà <strong>risultati immediati</strong> e si costruisce <strong>a piccoli passi</strong>.</li>
        <li>Le strategie chiave: <strong>dividere</strong> il lavoro, lavorare a <strong>blocchi di tempo</strong>, <strong>togliere le distrazioni</strong> e <strong>provare spesso</strong> il codice.</li>
        <li>A scuola il <strong>PDP</strong> (Piano Didattico Personalizzato) si prepara se lo decide il consiglio di classe. Se c'è anche un DSA, è obbligatorio.</li>
      </ul>
    </div>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title"><span aria-hidden="true">🧭</span> Indice</h2>
      <ol>
        <li><a href="#cos-e">Che cos'è l'ADHD</a></li>
        <li><a href="#scuola">L'ADHD a scuola: PDP o PEI?</a></li>
        <li><a href="#programmazione">ADHD e programmazione: che cosa aiuta</a></li>
        <li><a href="#strategie">Sei strategie per programmare con l'ADHD</a></li>
        <li><a href="#esempio">Un esempio: un programma a piccoli passi</a></li>
        <li><a href="#verifiche">Nelle verifiche</a></li>
        <li><a href="#docenti">Per docenti e famiglie: che cosa prevedere</a></li>
        <li><a href="#falsi-miti">Quattro falsi miti</a></li>
        <li><a href="#sintesi">In sintesi</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <p>Ti siedi davanti al computer per fare un esercizio di programmazione. Dopo pochi minuti stai pensando ad altro, oppure hai già aperto tre finestre diverse. Ti suona familiare?</p>
    <p>Se hai l'<strong>ADHD</strong>, questa guida è per te. Ti spiego che cos'è, che cosa prevede la scuola e, soprattutto, quali strategie ti aiutano a programmare con meno fatica.</p>
    <p>Lavoro ogni giorno come docente per l'inclusività (<a href="/#chi-sono">chi sono</a>) e ho insegnato informatica per anni. In fondo c'è anche una parte per <strong>docenti e famiglie</strong>.</p>

    <h2 id="cos-e">Che cos'è l'ADHD</h2>
    <p><strong>ADHD</strong> è la sigla inglese del <strong>disturbo da deficit di attenzione e iperattività</strong>. È un disturbo del <strong>neurosviluppo</strong>: riguarda il modo in cui il cervello si sviluppa e funziona.</p>
    <p>Chi ha l'ADHD fa più fatica a <strong>regolare l'attenzione</strong>, il <strong>movimento</strong> e gli <strong>impulsi</strong>. Non è pigrizia e non è maleducazione: non dipende dalla volontà.</p>
    <p>L'ADHD si presenta in modi diversi. Gli specialisti ne descrivono tre.</p>
{FIG_PRES}
    <p>Spesso l'ADHD si presenta insieme ad altre difficoltà, per esempio un <strong>DSA</strong> (Disturbo Specifico dell'Apprendimento). Ogni persona è diversa: per questo la diagnosi la fanno gli specialisti.</p>

    <h2 id="scuola">L'ADHD a scuola: PDP o PEI?</h2>
    <div class="group-box g3">
      <h3><span aria-hidden="true">🧩</span> Gruppo 3 · Altri BES</h3>
      <p>A scuola l'ADHD rientra tra i <strong>BES</strong> (Bisogni Educativi Speciali), il gruppo 3 della guida <a href="articolo-bes-dsa-disabilita.html">Disabilità 104, DSA e BES</a>.</p>
      <p>Il consiglio di classe decide se preparare un <strong>PDP</strong> e deve scrivere il motivo nel verbale della riunione.</p>
    </div>
    <p>Ci sono due casi particolari. Se lo studente ha <strong>anche un DSA</strong>, il PDP è <strong>obbligatorio</strong>. Nei casi più gravi può essere riconosciuta una <strong>disabilità</strong>: allora la scuola prepara il <strong>PEI</strong> (Piano Educativo Individualizzato) e c'è il docente di sostegno.</p>
    <p>Come si costruiscono questi documenti lo spiego nelle guide <a href="articolo-pdp-passo-dopo-passo.html">Il PDP passo dopo passo</a> e <a href="articolo-pei-spiegato-semplice.html">Il PEI spiegato semplice</a>.</p>

    <h2 id="programmazione">ADHD e programmazione: che cosa aiuta</h2>
    <p>La programmazione ha alcune caratteristiche che possono aiutare molto chi ha l'ADHD. Ne ha anche altre che possono mettere in difficoltà.</p>
{PRO_CONTRO}
    <p>Le strategie che seguono servono proprio a sfruttare i punti a favore e a ridurre gli inciampi.</p>

    <h2 id="strategie">Sei strategie per programmare con l'ADHD</h2>
    <p>Non servono tutte. Provale una alla volta e tieni quelle che funzionano per te.</p>

    <h3>1. Dividi il problema in passi piccoli</h3>
    <p>Un esercizio lungo spaventa e fa perdere il filo. Prima di scrivere codice, scrivi in italiano i <strong>passi</strong> da fare, uno per riga. Poi affrontane <strong>uno alla volta</strong>.</p>
    <p>Per vedere i passi può aiutarti un <a href="articolo-diagramma-di-flusso.html">diagramma di flusso</a>.</p>

    <h3>2. Lavora a blocchi di tempo</h3>
    <p>Lavora per un tempo breve, per esempio <strong>20-25 minuti</strong>, poi fai una <strong>pausa di 5 minuti</strong>. Usa un timer, meglio se separato dal telefono.</p>
    <p>Nella pausa <strong>muoviti</strong>: alzati, bevi un bicchiere d'acqua, cammina un po'. Il movimento aiuta a ripartire.</p>

    <h3>3. Togli le distrazioni</h3>
    <p>Spegni le <strong>notifiche</strong> e chiudi le finestre che non servono. Tieni aperto solo l'editor e la consegna.</p>
    <p>In Visual Studio Code c'è la <strong>modalità Zen</strong>, che nasconde tutto tranne il codice. Si apre dal menu Visualizza.</p>

    <h3>4. Prova il codice spesso</h3>
    <p>Non scrivere tutto il programma e poi provarlo alla fine. Scrivi <strong>poche righe</strong> e <strong>eseguile subito</strong>. Così vedi il risultato e trovi gli errori quando sono ancora piccoli.</p>

    <h3>5. Usa una lista di controllo</h3>
    <p>Molti errori nascono dalla <strong>distrazione</strong>, non dal non sapere. Una lista di controllo ti aiuta a trovarli da solo, prima di chiedere aiuto.</p>
{FIG_CHECK}
    <p>Altri trucchi per trovare gli errori li trovi nella guida <a href="articolo-debug.html">Debug: come trovare e correggere i bug</a>.</p>

    <h3>6. Metti una sveglia anche quando sei concentrato</h3>
    <p>Con l'ADHD a volte succede il contrario: un problema ti appassiona così tanto che perdi la cognizione del tempo. È l'<strong>iperfocalizzazione</strong>.</p>
    <p>Può essere una risorsa, ma rischia di farti trascurare il resto, come gli altri compiti o la pausa. Una sveglia ti aiuta a <strong>fermarti</strong> al momento giusto.</p>

    <h2 id="esempio">Un esempio: un programma a piccoli passi</h2>
    <p>Mettiamo in pratica le strategie 1 e 4. Il compito è: <strong>chiedere tre voti, calcolare la media e dire se è sufficiente</strong>.</p>
    <p>Invece di scrivere tutto insieme, lo dividiamo in quattro passi. <strong>Dopo ogni passo, esegui il programma</strong> e controlla che funzioni.</p>
    {code(MEDIA, label="Programma in Python diviso in quattro passi: chiede tre voti, calcola la media, la stampa e aggiunge un messaggio")}
    <p>I commenti che iniziano con <code>#</code> ti ricordano a che punto sei. Se ti distrai, guardi l'ultimo passo finito e riparti da lì.</p>
    <p>Se le condizioni ti creano dubbi, ripassale nella guida <a href="articolo-if-else-python.html">if, elif e else in Python</a>.</p>

    <h2 id="verifiche">Nelle verifiche</h2>
    <p>In una verifica il tempo stringe e la tensione sale. Ecco alcune abitudini che aiutano.</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">📖</span><span><strong>Leggi tutta la consegna</strong> prima di cominciare e sottolinea che cosa ti chiede.</span></li>
      <li><span class="t-ico" aria-hidden="true">1️⃣</span><span><strong>Una domanda alla volta</strong>: finita una, segnala come fatta e passa alla successiva.</span></li>
      <li><span class="t-ico" aria-hidden="true">✅</span><span>Negli ultimi minuti <strong>ripassa la lista di controllo</strong> degli errori di distrazione.</span></li>
      <li><span class="t-ico" aria-hidden="true">🙋</span><span>Se non capisci una richiesta, <strong>chiedi</strong> al docente invece di tirare a indovinare.</span></li>
    </ul>

    <h2 id="docenti">Per docenti e famiglie: che cosa prevedere</h2>
    <p>Ecco alcune idee da valutare insieme, anche nel PDP. Sono <strong>esempi</strong>, non una lista da copiare: ogni studente è diverso.</p>
    <div class="pdp-grid">
      <div class="dsa-box pdp-col">
        <h3><span aria-hidden="true">🏫</span> In classe e in laboratorio</h3>
        <ul>
          <li><strong>consegne scritte</strong>, brevi, una richiesta alla volta;</li>
          <li>un <strong>posto</strong> lontano da porte e finestre, vicino al docente;</li>
          <li><strong>routine</strong> chiare: come inizia e come finisce ogni lezione;</li>
          <li><strong>pause brevi</strong> programmate o piccoli incarichi che permettono di muoversi;</li>
          <li><strong>riscontri frequenti</strong> e positivi, appena il lavoro è fatto bene.</li>
        </ul>
      </div>
      <div class="dsa-box pdp-col">
        <h3><span aria-hidden="true">📝</span> Nelle verifiche</h3>
        <ul>
          <li>verifiche <strong>divise in parti</strong>, con una consegna per volta;</li>
          <li><strong>più tempo</strong>, oppure meno esercizi con gli stessi obiettivi;</li>
          <li>verifiche <strong>programmate</strong>, non più di una al giorno;</li>
          <li><strong>interrogazioni orali</strong> per recuperare uno scritto;</li>
          <li>valutare la <strong>logica</strong> del programma più degli errori di distrazione.</li>
        </ul>
      </div>
    </div>
    <p>In laboratorio funziona bene anche la <strong>programmazione in coppia</strong>: uno scrive il codice e l'altro controlla, poi ci si scambia i ruoli dopo pochi minuti. Il cambio frequente aiuta a restare attivi.</p>
    <p>Per le famiglie: a casa aiutano un <strong>posto fisso</strong> per studiare, un orario regolare e un'agenda dei compiti da controllare insieme, senza sostituirsi al ragazzo.</p>

    <h2 id="falsi-miti">Quattro falsi miti</h2>
    <p>Ci sono alcune idee sbagliate sull'ADHD che sento spesso. Vediamole una per una.</p>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Basterebbe un po' più di impegno».</p><p><strong>In realtà</strong> l'ADHD non dipende dalla volontà. Servono strategie e aiuti adatti, non rimproveri.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Se riesce a concentrarsi sui videogiochi, non ha l'ADHD».</p><p><strong>In realtà</strong> con l'ADHD è più difficile concentrarsi sulle cose poco interessanti. Su quelle che appassionano, a volte succede il contrario: è l'iperfocalizzazione.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Crescendo, l'ADHD sparisce».</p><p><strong>In realtà</strong> in molte persone continua anche da adulti, anche se spesso cambia forma. Per questo conviene imparare presto strategie che durano nel tempo.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Con l'ADHD non si può diventare programmatori».</p><p><strong>In realtà</strong> non c'è nessun motivo per rinunciare. Con le strategie giuste, la programmazione può diventare uno dei tuoi punti di forza.</p></div>

    <h2 id="sintesi">In sintesi</h2>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">🧠</span><span>L'<strong>ADHD</strong> rende più difficile concentrarsi, organizzarsi e aspettare. <strong>Non dipende dalla volontà</strong>.</span></li>
      <li><span class="t-ico" aria-hidden="true">🧩</span><span>A scuola rientra tra gli <strong>altri BES</strong>: il PDP lo decide il consiglio di classe, ed è obbligatorio se c'è anche un DSA.</span></li>
      <li><span class="t-ico" aria-hidden="true">🪜</span><span>Per programmare: <strong>passi piccoli</strong>, <strong>blocchi di tempo</strong>, <strong>niente distrazioni</strong>, <strong>prove frequenti</strong>.</span></li>
      <li><span class="t-ico" aria-hidden="true">✅</span><span>Una <strong>lista di controllo</strong> aiuta a trovare da solo gli errori di distrazione.</span></li>
      <li><span class="t-ico" aria-hidden="true">🤝</span><span>Scuola, famiglia e studente funzionano meglio <strong>insieme</strong>.</span></li>
    </ul>
    <p>L'ADHD non decide che cosa puoi diventare. Decide solo che ti serve un modo tuo per arrivarci, e questa guida è un punto di partenza.</p>
    <p class="norme rt-skip">Riferimenti normativi: Nota ministeriale 15 giugno 2010, prot. 4089 (alunni con ADHD); Legge 8 ottobre 2010, n. 170 (in caso di DSA associato); Direttiva ministeriale 27 dicembre 2012 (BES e disturbi evolutivi specifici); Circolare ministeriale 6 marzo 2013, n. 8; Nota ministeriale 22 novembre 2013, prot. 2563; Legge 5 febbraio 1992, n. 104 (nei casi in cui è riconosciuta una disabilità); Circolare MIM 16 giugno 2025, n. 3392 (uso del cellulare a scuola); ordinanza ministeriale annuale sull'esame di maturità. Aggiornato al 19 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Programma un passo alla volta</h2>
      <p>Nelle lezioni gratuite trovi esempi brevi da modificare e l'editor «Provalo tu» per vedere subito il risultato, senza installare nulla.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Hai l'ADHD e studi informatica? Hai una strategia che funziona e vuoi raccontarmela? <a href="contatti.html">Scrivimi</a>: leggo tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-informatica-dsa.html"><span aria-hidden="true">📖</span><strong>Informatica e DSA: strategie e strumenti compensativi</strong></a>
        <a href="articolo-pdp-passo-dopo-passo.html"><span aria-hidden="true">📝</span><strong>Il PDP passo dopo passo: cos'è, chi lo scrive e cosa contiene</strong></a>
        <a href="articolo-tecnologie-assistive.html"><span aria-hidden="true">🛠️</span><strong>Tecnologie assistive per studiare: quali sono e come averle a scuola</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="ADHD programmazione, ADHD informatica, studiare con ADHD, ADHD scuola, ADHD PDP, strategie ADHD studio, deficit di attenzione e iperattività",
    og_alt="Il titolo «ADHD e programmazione» e tre riquadri: per chi, studenti con ADHD; strategie, passi piccoli e pause; a scuola, PDP se serve.",
    date_iso="2026-11-19", date_it="19 novembre 2026",
    ld_keywords="ADHD, disturbo da deficit di attenzione e iperattività, programmazione, informatica, BES, PDP, strategie di studio, inclusione scolastica",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «ADHD e programmazione» e tre riquadri: per chi, studenti con ADHD; strategie, passi piccoli e pause; a scuola, PDP se serve.",
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('ADHD: parole', words, '| minuti', MIN)
