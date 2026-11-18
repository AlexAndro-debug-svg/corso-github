#!/usr/bin/env python3
"""Articolo 5 della serie inclusione: tecnologie assistive per studiare."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-tecnologie-assistive"
TITLE = "Tecnologie assistive per studiare: quali sono e come averle a scuola"
SEO_TITLE = "Tecnologie assistive per studiare: quali sono — AlessandroSimone.it"
DESC = "Comunicatori, tastiere speciali, lettori di schermo, sintesi vocale: le tecnologie per studiare con disabilità, DSA e altri BES, e come averle a scuola."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FIGURE
G1 = [
    ("💬", "Comunicatori e CAA", "La <strong>CAA</strong> (Comunicazione Aumentativa e Alternativa) aiuta chi non parla, o parla poco, a farsi capire. Si usano tabelle con simboli o un <strong>comunicatore</strong>, cioè un dispositivo che pronuncia le parole scelte."),
    ("⌨️", "Tastiere e mouse speciali", "Tastiere con tasti grandi, con una griglia che evita di premere due tasti insieme, oppure trackball e joystick al posto del mouse."),
    ("🔘", "Sensori e puntamento con lo sguardo", "Per chi muove poco le mani ci sono <strong>sensori</strong> da premere con una parte del corpo e sistemi che seguono il movimento degli occhi."),
    ("🔊", "Lettori di schermo e Braille", "Per chi non vede, il <strong>lettore di schermo</strong> legge ad alta voce tutto quello che c'è sul monitor. Il <strong>display Braille</strong> lo trasforma in puntini da leggere con le dita."),
    ("🔍", "Ingranditori e alto contrasto", "Per chi vede poco: programmi che ingrandiscono lo schermo e colori più netti, che rendono il testo più leggibile."),
    ("📝", "Sottotitoli e microfoni", "Per chi sente poco: la trascrizione automatica di quello che si dice e i sistemi che portano la voce del docente direttamente all'apparecchio acustico."),
]
FIG_G1 = """
    <ul class="icon-list">
""" + '\n'.join(f'      <li><span class="t-ico" aria-hidden="true">{i}</span><span><strong>{t}.</strong> {d}</span></li>' for i, t, d in G1) + """
    </ul>"""

GRATIS = [
    ("Computer Windows", "<strong>Assistente vocale</strong> (lettore di schermo), <strong>Lente di ingrandimento</strong> e <strong>dettatura vocale</strong>, che si apre con i tasti Windows e H."),
    ("Mac, iPhone e iPad", "<strong>VoiceOver</strong> (lettore di schermo), <strong>Contenuto letto ad alta voce</strong> e <strong>Dettatura</strong>."),
    ("Android e Chromebook", "<strong>TalkBack</strong> e <strong>ChromeVox</strong> (lettori di schermo) e <strong>Seleziona per ascoltare</strong>, che legge ad alta voce il testo che tocchi."),
    ("Programmi gratuiti", "<strong>NVDA</strong>, un lettore di schermo gratuito per Windows, e le funzioni di lettura ad alta voce dei browser e degli editor di testo."),
]
FIG_GRATIS = """
    <figure class="dsa-figure" aria-labelledby="cap-gratis">
      <div class="sigle-grid">
""" + '\n'.join(f'        <div class="sigla"><b>{a}</b><span>{b}</span></div>' for a, b in GRATIS) + """
      </div>
      <figcaption id="cap-gratis">Molte tecnologie assistive sono già dentro computer, tablet e telefoni, senza costi. I nomi sono quelli delle impostazioni di accessibilità.</figcaption>
    </figure>"""

VIE = [
    ("A", "Dalla scuola e dal CTS", "La scuola può usare i suoi strumenti o chiederli in <strong>prestito gratuito</strong> al <strong>CTS</strong> (Centro Territoriale di Supporto), che ha ausili per le scuole della provincia. La richiesta la fa la scuola, di solito con un progetto per lo studente.", "Per: ausili da usare a scuola"),
    ("B", "Dalla ASL", "Alcuni ausili personali, come i comunicatori o certi ausili per usare il computer, sono forniti dal Servizio sanitario. Serve la <strong>prescrizione di un medico specialista</strong> e l'autorizzazione della ASL (Azienda sanitaria locale).", "Per: ausili personali per la disabilità"),
    ("C", "Acquisto della famiglia", "Se la famiglia compra uno strumento, può avere <strong>agevolazioni fiscali</strong>. Per i DSA c'è una detrazione del 19% sugli strumenti compensativi, fino alla fine delle superiori.", "Per: strumenti personali da usare anche a casa"),
]
FIG_VIE = """
    <figure class="dsa-figure" aria-labelledby="cap-vie">
      <div class="perc-grid">
""" + '\n'.join(
    f'        <div class="perc"><span class="perc-l" aria-hidden="true">{l}</span><div><div class="perc-t"><span class="sr-only">Strada {l}: </span>{t}</div><p>{d}</p><span class="perc-out">{o}</span></div></div>'
    for l, t, d, o in VIE) + """
      </div>
      <figcaption id="cap-vie">Le tre strade per avere una tecnologia assistiva. Spesso si usano insieme: per esempio, un ausilio dato dalla ASL che la scuola impara a usare in classe.</figcaption>
    </figure>"""

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Chi paga un ausilio da usare a scuola?",
        "Dipende dall'ausilio. Gli strumenti per la classe li mette a disposizione la scuola, anche con il prestito del CTS. Gli ausili personali legati alla disabilità possono essere forniti dalla ASL, con la prescrizione di uno specialista. Gli strumenti comprati dalla famiglia possono dare diritto ad agevolazioni fiscali."),
    faq("Posso usare il mio computer o il mio tablet a scuola?",
        "Sì, se è previsto dal PDP o dal PEI. Conviene scrivere con precisione per quali attività si usa e se si usa anche nelle verifiche. Così tutti i docenti sanno che cosa è permesso."),
    faq("Un ausilio prestato dal CTS si può portare a casa?",
        "Dipende dalle regole del CTS e della scuola. Il prestito di solito è fatto alla scuola, non alla famiglia. Chiedi alla scuola come funziona nella tua provincia."),
    faq("Come funziona la detrazione per i DSA?",
        "Le spese per strumenti compensativi e sussidi tecnici e informatici si possono detrarre al 19%, fino alla fine delle superiori. Serve la certificazione di DSA e un legame tra lo strumento e il disturbo: un computer da solo non basta. Conserva le fatture e chiedi al CAF o al commercialista."),
    faq("Ci sono agevolazioni anche per la disabilità?",
        "Sì, esistono agevolazioni fiscali per l'acquisto di sussidi tecnici e informatici da parte delle persone con disabilità. Le regole dipendono dal tipo di disabilità e dal sussidio. Prima di comprare, chiedi al CAF o al commercialista quali documenti servono."),
    faq("Le app di intelligenza artificiale sono tecnologie assistive?",
        "Possono aiutare molto: per esempio a riassumere, a spiegare un testo in modo più semplice o a ripassare. Per usarle a scuola, però, devono essere previste nel PDP o nel PEI. Come usarle bene lo spiego nella guida <a href=\"articolo-chatgpt-studiare.html\">Come usare ChatGPT per studiare</a>."),
    faq("Posso usare questi strumenti all'esame di maturità?",
        "Si possono usare gli strumenti previsti dal PEI o dal PDP e usati durante l'anno. Per gli altri BES le regole sono più strette: le spiego nella guida <a href=\"articolo-pdp-passo-dopo-passo.html#verifiche\">Il PDP passo dopo passo</a>."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <div class="dsa-box tldr" id="in-breve">
      <h2 class="box-title"><span aria-hidden="true">📌</span> L'articolo in 30 secondi</h2>
      <ul>
        <li>Le <strong>tecnologie assistive</strong> sono strumenti che aiutano a studiare superando l'ostacolo di una disabilità, di un DSA o di un altro bisogno educativo speciale.</li>
        <li>Vanno dai <strong>comunicatori</strong> e dalle <strong>tastiere speciali</strong> alla <strong>sintesi vocale</strong>. Molte sono già, gratis, dentro computer e telefoni.</li>
        <li>Si hanno in <strong>tre modi</strong>: dalla scuola e dal CTS, dalla ASL, oppure comprandole con agevolazioni fiscali.</li>
        <li>Per usarle a scuola e nelle verifiche, vanno <strong>scritte nel PEI o nel PDP</strong> e usate ogni giorno.</li>
      </ul>
    </div>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title"><span aria-hidden="true">🧭</span> Indice</h2>
      <ol>
        <li><a href="#cosa-sono">Che cosa sono le tecnologie assistive</a></li>
        <li><a href="#disabilita">Per la disabilità</a></li>
        <li><a href="#dsa">Per i DSA</a></li>
        <li><a href="#altri-bes">Per gli altri BES</a></li>
        <li><a href="#gratis">Quelle che hai già, gratis</a></li>
        <li><a href="#come-averle">Come averle a scuola: tre strade</a></li>
        <li><a href="#pei-pdp">Scriverle nel PEI o nel PDP</a></li>
        <li><a href="#consigli">Prima di scegliere: cinque consigli</a></li>
        <li><a href="#falsi-miti">Quattro falsi miti</a></li>
        <li><a href="#informatica">E in laboratorio di informatica?</a></li>
        <li><a href="#sintesi">In sintesi</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <p>Un computer che legge ad alta voce. Una tastiera con i tasti grandi. Un tablet che parla al posto tuo. Sono <strong>tecnologie assistive</strong>, e possono cambiare il modo di studiare.</p>
    <p>Lavoro ogni giorno come docente per l'inclusività (<a href="/#chi-sono">chi sono</a>) e prima ho insegnato informatica per anni. In questa guida ti mostro quali tecnologie esistono e, soprattutto, come averle a scuola.</p>
    <p>Per ogni strumento ti dico a chi può servire, seguendo i tre gruppi della guida <a href="articolo-bes-dsa-disabilita.html">Disabilità 104, DSA e BES</a>.</p>

    <h2 id="cosa-sono">Che cosa sono le tecnologie assistive</h2>
    <p>Una <strong>tecnologia assistiva</strong> è uno strumento, un apparecchio o un programma che aiuta una persona a fare qualcosa che, a causa di una difficoltà, le riuscirebbe molto faticoso o impossibile.</p>
    <p>A scuola si parla anche di <strong>ausili</strong>, per la disabilità, e di <strong>strumenti compensativi</strong>, per i DSA e gli altri BES. L'idea è la stessa: togliere un ostacolo, non fare il lavoro al posto dello studente.</p>
    <p>Pensa agli <strong>occhiali</strong>: non ti fanno capire meglio un libro, ma ti permettono di leggerlo. Le tecnologie assistive funzionano allo stesso modo.</p>

    <h2 id="disabilita">Per la disabilità</h2>
    <div class="group-box g1">
      <h3><span aria-hidden="true">🤝</span> Gruppo 1 · Disabilità certificata</h3>
      <p>Per gli studenti con disabilità certificata (Legge 104) gli strumenti si scelgono in base al tipo di difficoltà: motoria, visiva, uditiva, della comunicazione o cognitiva. Si indicano nel <strong>PEI</strong> (Piano Educativo Individualizzato).</p>
    </div>
{FIG_G1}
    <p>Sono strumenti molto diversi tra loro. Per sceglierli servono gli specialisti che seguono lo studente, la famiglia e la scuola insieme.</p>

    <h2 id="dsa">Per i DSA</h2>
    <div class="group-box g2">
      <h3><span aria-hidden="true">📖</span> Gruppo 2 · DSA</h3>
      <p>Per i <strong>DSA</strong> (Disturbi Specifici dell'Apprendimento) si parla di <strong>strumenti compensativi</strong>. Si scrivono nel <strong>PDP</strong> (Piano Didattico Personalizzato), che con una diagnosi è obbligatorio.</p>
    </div>
    <p>I più usati sono la <strong>sintesi vocale</strong>, che legge i testi ad alta voce, il <strong>correttore ortografico</strong>, le <strong>mappe concettuali</strong> e la <strong>calcolatrice</strong>. In informatica aiuta molto anche un editor che colora il codice.</p>
    <p>Li ho spiegati uno per uno, con esempi, nella guida <a href="articolo-informatica-dsa.html#strumenti">Informatica e DSA</a>.</p>

    <h2 id="altri-bes">Per gli altri BES</h2>
    <div class="group-box g3">
      <h3><span aria-hidden="true">🧩</span> Gruppo 3 · Altri BES</h3>
      <p>Per gli altri bisogni educativi speciali gli strumenti si usano se il consiglio di classe li prevede nel <strong>PDP</strong>. Spesso servono per un periodo limitato.</p>
    </div>
    <p>Ecco qualche esempio. Sono solo idee: ogni studente è diverso.</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">⏲️</span><span>Con l'<strong>ADHD</strong> (disturbo da deficit di attenzione e iperattività): un <strong>timer visivo</strong> che mostra il tempo che resta, un'agenda digitale per organizzare i compiti, cuffie che riducono i rumori.</span></li>
      <li><span class="t-ico" aria-hidden="true">🌍</span><span>Per chi <strong>sta imparando l'italiano</strong>: dizionari con immagini, la sintesi vocale per ascoltare come si pronunciano le parole, un traduttore per le consegne più difficili.</span></li>
    </ul>

    <h2 id="gratis">Quelle che hai già, gratis</h2>
    <p>Prima di comprare qualcosa, guarda nelle <strong>impostazioni di accessibilità</strong> del computer o del telefono. Molte tecnologie assistive sono già lì.</p>
{FIG_GRATIS}
    <p>Provale con calma, a casa. Molte si attivano e si spengono con una combinazione di tasti.</p>

    <h2 id="come-averle">Come averle a scuola: tre strade</h2>
    <p>Quando uno strumento non c'è già, le strade per averlo sono tre. Cambiano in base al tipo di strumento e a chi lo usa.</p>
{FIG_VIE}
    <p>Le regole del CTS cambiano da provincia a provincia. Per sapere che cosa è disponibile, chiedi al referente per l'inclusione della scuola, cioè il docente che coordina queste attività.</p>
    <p>Per gli ausili della ASL, il primo passo è parlarne con lo specialista che segue lo studente.</p>

    <h2 id="pei-pdp">Scriverle nel PEI o nel PDP</h2>
    <p>Avere uno strumento non basta: bisogna poterlo <strong>usare a scuola</strong>. Per questo va scritto nel PEI, per la disabilità, o nel PDP, per i DSA e gli altri BES.</p>
    <p>Chiedi che sia scritto in modo preciso: <strong>quale</strong> strumento, in <strong>quali materie</strong> e se vale anche <strong>nelle verifiche</strong>. Come si costruiscono questi documenti lo spiego nelle guide <a href="articolo-pei-spiegato-semplice.html">Il PEI spiegato semplice</a> e <a href="articolo-pdp-passo-dopo-passo.html">Il PDP passo dopo passo</a>.</p>
    <p>Anche all'esame di maturità si possono usare gli strumenti previsti e già usati durante l'anno. Per questo conviene usarli con regolarità fin dalle prime classi.</p>

    <h2 id="consigli">Prima di scegliere: cinque consigli</h2>
    <ol class="steps-list">
      <li><strong>Parti dal bisogno, non dallo strumento.</strong> Prima chiediti che cosa è difficile, poi cerca che cosa può aiutare.</li>
      <li><strong>Prova prima di comprare.</strong> Molti strumenti hanno versioni gratuite o di prova, e alcuni CTS offrono anche consulenza.</li>
      <li><strong>Impara a usarlo.</strong> Uno strumento nuovo all'inizio rallenta. Servono tempo e un po' di allenamento, anche per i docenti.</li>
      <li><strong>Usalo ogni giorno.</strong> Lo strumento funziona solo se diventa un'abitudine, a scuola e a casa.</li>
      <li><strong>Ascolta lo studente.</strong> È lui a sapere se uno strumento lo aiuta davvero o se lo fa sentire a disagio.</li>
    </ol>

    <h2 id="falsi-miti">Quattro falsi miti</h2>
    <p>Ci sono alcune idee sbagliate sulle tecnologie assistive che sento spesso. Vediamole una per una.</p>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Con la tecnologia lo studente non impara più a fare da solo».</p><p><strong>In realtà</strong> lo strumento toglie l'ostacolo, ma il lavoro di capire e di ragionare resta dello studente. Spesso lo rende più autonomo, non meno.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Servono strumenti costosi».</p><p><strong>In realtà</strong> molte funzioni sono già gratis nei computer e nei telefoni. Gli ausili più specifici si possono avere dalla scuola, dal CTS o dalla ASL.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Se usa lo strumento nella verifica, il voto vale meno».</p><p><strong>In realtà</strong> il voto ha lo stesso valore. Lo strumento serve proprio a misurare quello che lo studente sa davvero.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Basta consegnare lo strumento».</p><p><strong>In realtà</strong> lo studente e i docenti devono imparare a usarlo, e va previsto nel PEI o nel PDP. Senza questi passi, spesso resta in un cassetto.</p></div>

    <h2 id="informatica">E in laboratorio di informatica?</h2>
    <p>Il laboratorio di informatica è un luogo ideale per provare le tecnologie assistive. Ecco alcune idee.</p>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">🖥️</span><span>Attivare le funzioni di <strong>accessibilità</strong> sui computer del laboratorio, così sono pronte per chi ne ha bisogno.</span></li>
      <li><span class="t-ico" aria-hidden="true">🧑‍💻</span><span>Programmare si può anche con un <strong>lettore di schermo</strong>: per esempio Visual Studio Code, un editor molto usato, ha una modalità pensata apposta.</span></li>
      <li><span class="t-ico" aria-hidden="true">🧱</span><span>La <strong>programmazione a blocchi</strong>, dove si trascinano blocchi colorati invece di scrivere comandi, aiuta chi fa fatica a scrivere.</span></li>
      <li><span class="t-ico" aria-hidden="true">🏫</span><span>Far conoscere questi strumenti a <strong>tutta la classe</strong>: la dettatura vocale o la lettura ad alta voce sono utili a tutti.</span></li>
    </ul>
    <p>Le mie <a href="lezioni.html">lezioni gratuite</a> funzionano nel browser e si possono usare con le funzioni di accessibilità del computer.</p>

    <h2 id="sintesi">In sintesi</h2>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">🛠️</span><span>Le <strong>tecnologie assistive</strong> tolgono un ostacolo, non fanno il lavoro al posto dello studente.</span></li>
      <li><span class="t-ico" aria-hidden="true">🤝</span><span>Per la <strong>disabilità</strong> ci sono comunicatori, tastiere speciali, lettori di schermo e altri ausili, indicati nel PEI.</span></li>
      <li><span class="t-ico" aria-hidden="true">📖</span><span>Per i <strong>DSA</strong> e gli <strong>altri BES</strong> si parla di strumenti compensativi, indicati nel PDP.</span></li>
      <li><span class="t-ico" aria-hidden="true">🆓</span><span>Molte funzioni sono già <strong>gratis</strong> nei computer e nei telefoni.</span></li>
      <li><span class="t-ico" aria-hidden="true">🧭</span><span>Le strade per averle sono tre: <strong>scuola e CTS</strong>, <strong>ASL</strong>, <strong>acquisto con agevolazioni</strong>.</span></li>
    </ul>
    <p>La tecnologia giusta non è la più costosa: è quella che lo studente usa volentieri, ogni giorno.</p>
    <p class="norme rt-skip">Riferimenti normativi: Legge 5 febbraio 1992, n. 104, art. 13 (sussidi e attrezzature tecniche); Legge 8 ottobre 2010, n. 170, art. 5 (strumenti compensativi); D.M. 12 luglio 2011, n. 5669 e Linee guida DSA; Direttiva ministeriale 27 dicembre 2012 (Centri Territoriali di Supporto); D.Lgs. 13 aprile 2017, n. 66; D.P.C.M. 12 gennaio 2017 (livelli essenziali di assistenza, allegato 5 sugli ausili); D.P.R. 22 dicembre 1986, n. 917 (TUIR), art. 15, comma 1, lettere c) ed e-bis). Aggiornato al 18 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica pensate per tutti</h2>
      <p>Nelle lezioni gratuite trovi esempi da modificare e l'editor «Provalo tu» per vedere subito il risultato, senza installare nulla.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Usi una tecnologia assistiva che ti ha cambiato lo studio? Hai un dubbio? <a href="contatti.html">Scrivimi</a>: leggo tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-informatica-dsa.html"><span aria-hidden="true">📖</span><strong>Informatica e DSA: strategie e strumenti compensativi</strong></a>
        <a href="articolo-pdp-passo-dopo-passo.html"><span aria-hidden="true">📝</span><strong>Il PDP passo dopo passo: cos'è, chi lo scrive e cosa contiene</strong></a>
        <a href="articolo-pei-spiegato-semplice.html"><span aria-hidden="true">🤝</span><strong>Il PEI spiegato semplice: cos'è, chi lo scrive e come funziona</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="tecnologie assistive, ausili scuola, comunicatore CAA, sintesi vocale, lettore di schermo, strumenti compensativi, CTS comodato ausili, detrazione DSA",
    og_alt="Il titolo «Tecnologie assistive per studiare» e tre riquadri: per chi, disabilità, DSA e altri BES; quali, comunicatori e sintesi vocale; come averle, scuola, ASL o famiglia.",
    date_iso="2026-11-18", date_it="18 novembre 2026",
    ld_keywords="tecnologie assistive, ausili, CAA, comunicatore, sintesi vocale, lettore di schermo, strumenti compensativi, CTS, inclusione scolastica",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Tecnologie assistive per studiare» e tre riquadri: per chi, disabilità, DSA e altri BES; quali, comunicatori e sintesi vocale; come averle, scuola, ASL o famiglia.",
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('TECNO: parole', words, '| minuti', MIN)
