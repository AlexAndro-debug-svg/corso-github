#!/usr/bin/env python3
"""Articolo della serie inclusione: chi è il docente di sostegno e cosa fa alle superiori."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-docente-di-sostegno"
TITLE = "Chi è il docente di sostegno e cosa fa alle superiori"
SEO_TITLE = "Docente di sostegno: chi è e cosa fa alle superiori — AlessandroSimone.it"
DESC = "Il docente di sostegno è un docente della classe, non dello studente. Che cosa fa alle superiori, quante ore ha e come collaborare con lui."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FIGURE
FA = [
    ("🔍", "Osserva", "conosce lo studente: punti di forza, difficoltà, che cosa lo aiuta. Le osservazioni servono a scrivere il PEI."),
    ("🗂️", "Progetta", "prepara con i colleghi la proposta di PEI e partecipa al GLO (Gruppo di Lavoro Operativo per l'inclusione), il gruppo che lo approva."),
    ("👩‍🏫", "Insegna in classe", "lavora nelle ore di lezione insieme al docente della materia, con lo studente e con tutta la classe."),
    ("✂️", "Adatta i materiali", "semplifica testi, prepara schemi e mappe, propone verifiche adatte al percorso dello studente."),
    ("💬", "Tiene i contatti", "con la famiglia, gli specialisti e le altre figure che seguono lo studente."),
    ("📊", "Valuta", "partecipa agli scrutini, le riunioni in cui si decidono i voti, e valuta tutti gli studenti della classe, non solo quello con disabilità."),
]
FIG_FA = """
    <figure class="dsa-figure" aria-labelledby="cap-fa">
      <ul class="icon-list">
""" + '\n'.join(f'        <li><span class="t-ico" aria-hidden="true">{i}</span><span><strong>{t}</strong>: {d}</span></li>' for i, t, d in FA) + """
      </ul>
      <figcaption id="cap-fa">Le sei cose principali che fa il docente di sostegno. Le fa sempre insieme agli altri docenti della classe.</figcaption>
    </figure>"""

FIGURE = [
    ("Docente di sostegno", "Docente della scuola, contitolare della classe. Si occupa della didattica e del progetto educativo."),
    ("Docenti delle materie", "Anche loro sono responsabili dello studente con disabilità e del suo PEI, nelle loro ore."),
    ("Assistente all'autonomia e alla comunicazione", "Figura esterna alla scuola, pagata dal Comune o dalla Regione. Alle superiori del Lazio la finanzia la Regione, su progetto della scuola. Aiuta lo studente nell'autonomia e nella comunicazione."),
    ("Collaboratore scolastico", "Personale della scuola che, tra le altre cose, aiuta lo studente nell'assistenza di base, per esempio negli spostamenti e nell'igiene."),
    ("Referente per l'inclusione", "In molte scuole c'è un docente che coordina le attività di inclusione e aiuta i colleghi e le famiglie."),
]
FIG_FIGURE = """
    <figure class="dsa-figure" aria-labelledby="cap-fig">
      <div class="sigle-grid">
""" + '\n'.join(f'        <div class="sigla"><b>{a}</b><span>{b}</span></div>' for a, b in FIGURE) + """
      </div>
      <figcaption id="cap-fig">Le principali figure che lavorano per l'inclusione a scuola. Hanno compiti diversi e lavorano insieme.</figcaption>
    </figure>"""

COLLAB = """
    <div class="pdp-grid">
      <div class="dsa-box pdp-col">
        <h3><span aria-hidden="true">🏠</span> Per le famiglie</h3>
        <ul>
          <li>chiedete un <strong>colloquio</strong> a inizio anno, per presentare vostro figlio;</li>
          <li>raccontate che cosa funziona a casa e che cosa lo stanca;</li>
          <li>portate le <strong>relazioni aggiornate</strong> degli specialisti;</li>
          <li>ricordate che anche gli <strong>altri docenti</strong> sono vostri interlocutori.</li>
        </ul>
      </div>
      <div class="dsa-box pdp-col">
        <h3><span aria-hidden="true">🏫</span> Per i colleghi</h3>
        <ul>
          <li>condividete in anticipo <strong>argomenti e verifiche</strong>, così c'è il tempo di adattarli;</li>
          <li>le verifiche adattate le prepara il <strong>docente della materia</strong>, con il supporto del docente di sostegno;</li>
          <li>decidete insieme <strong>chi fa che cosa</strong> durante la lezione;</li>
          <li>coinvolgete il docente di sostegno anche nel lavoro con la <strong>classe intera</strong>;</li>
          <li>ricordate che il PEI riguarda <strong>anche le vostre ore</strong>.</li>
        </ul>
      </div>
    </div>"""

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Il docente di sostegno è assegnato allo studente o alla classe?",
        "Alla classe. La legge dice che il docente di sostegno è contitolare della classe in cui lavora. Segue in particolare lo studente con disabilità, ma è un docente di tutti."),
    faq("Chi decide quante ore di sostegno ci sono?",
        "Le indica il GLO nel PEI, spiegando il motivo, in base ai bisogni dello studente. Poi è l'Ufficio scolastico regionale ad assegnare i docenti alla scuola. Le regole su questo punto sono state cambiate da un decreto-legge del 2026, che può ancora cambiare con la conversione in legge: le spiego nella guida <a href=\"articolo-pei-spiegato-semplice.html#calendario\">Il PEI spiegato semplice</a>."),
    faq("Il docente di sostegno cambia ogni anno?",
        "Può succedere, soprattutto con i supplenti. Se il docente dell'anno prima era un supplente, la famiglia può chiedere di confermarlo. Decide il dirigente scolastico, dopo aver sentito il GLO, e serve che il docente sia d'accordo. La richiesta va fatta entro la scadenza fissata dal Ministero: nel 2025 era il 31 maggio. Se il docente cambia, il PEI resta valido e passa al nuovo docente."),
    faq("Che cosa succede quando il docente di sostegno è assente?",
        "Per le assenze lunghe arriva un supplente. Nelle assenze brevi lo studente resta in classe con i docenti delle materie, che conoscono il PEI e lo applicano. Non è giusto chiedere alla famiglia di tenerlo a casa."),
    faq("Che cosa faccio se il docente di sostegno non arriva, o le ore sono meno di quelle del PEI?",
        "Parlane con il dirigente scolastico, meglio per iscritto, e con il referente per l'inclusione, se c'è. Le associazioni delle famiglie possono aiutarti a capire come tutelare i diritti dello studente."),
    faq("Il docente di sostegno può portare lo studente fuori dalla classe?",
        "L'inclusione si fa in classe, con i compagni. Si può lavorare fuori dall'aula solo se il PEI lo prevede, indicando il motivo e i tempi. Uscire dalla classe non deve diventare un'abitudine."),
    faq("Lo studente può chiedere di non avere sempre il docente accanto?",
        "Sì, può chiederlo. Se ne parla nel GLO, a cui alle superiori lo studente partecipa, e la decisione si scrive nel PEI. Uno degli obiettivi del sostegno è proprio l'autonomia: a volte aiutare vuol dire fare un passo indietro."),
    faq("Come posso parlare con il docente di sostegno?",
        "Come con gli altri docenti: con i colloqui previsti dalla scuola o chiedendo un appuntamento, per esempio tramite il registro elettronico."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <div class="dsa-box tldr" id="in-breve">
      <h2 class="box-title"><span aria-hidden="true">📌</span> L'articolo in 30 secondi</h2>
      <ul>
        <li>Il <strong>docente di sostegno</strong> è un docente, di solito specializzato, che lavora nelle classi in cui c'è uno studente con <strong>disabilità certificata</strong> (Legge 104).</li>
        <li>È un docente <strong>della classe</strong>, non l'«insegnante personale» dello studente: ha le stesse responsabilità degli altri docenti.</li>
        <li>Osserva, progetta il <strong>PEI</strong> (Piano Educativo Individualizzato), insegna in classe, adatta i materiali e valuta <strong>tutti</strong> gli studenti.</li>
        <li>L'inclusione funziona quando lavorano <strong>insieme</strong> docente di sostegno, colleghi, famiglia e studente.</li>
      </ul>
    </div>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title"><span aria-hidden="true">🧭</span> Indice</h2>
      <ol>
        <li><a href="#chi-e">Chi è il docente di sostegno</a></li>
        <li><a href="#cosa-fa">Che cosa fa, in sei punti</a></li>
        <li><a href="#ore">Quante ore e con quale continuità</a></li>
        <li><a href="#figure">Chi non è: le altre figure dell'inclusione</a></li>
        <li><a href="#esame">All'esame di maturità</a></li>
        <li><a href="#collaborare">Come collaborare</a></li>
        <li><a href="#falsi-miti">Quattro equivoci da chiarire</a></li>
        <li><a href="#informatica">E in un istituto tecnico?</a></li>
        <li><a href="#sintesi">In sintesi</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <p>A scuola tutti ne parlano, ma pochi sanno davvero che cosa fa. Il <strong>docente di sostegno</strong> è una figura importante e spesso fraintesa.</p>
    <p>È il mio lavoro di ogni giorno. Nei documenti ufficiali si chiama «docente di sostegno». Nel mio istituto, il Giovanni XXIII di Roma, si chiama <strong>docente per l'inclusività</strong> (<a href="/#chi-sono">chi sono</a>).</p>
    <p>In questa guida ti spiego chi è e che cosa fa alle superiori. Ti dico anche come collaborare con lui, che tu sia studente, genitore o collega.</p>

    <h2 id="chi-e">Chi è il docente di sostegno</h2>
    <div class="group-box g1">
      <h3><span aria-hidden="true">🤝</span> Gruppo 1 · Disabilità certificata</h3>
      <p>Il docente di sostegno è previsto per le classi in cui c'è uno studente con <strong>disabilità certificata</strong> secondo la Legge 104. Per i <strong>DSA</strong> (Disturbi Specifici dell'Apprendimento) e gli altri <strong>BES</strong> (Bisogni Educativi Speciali), se non c'è anche una disabilità certificata, non è previsto. Le differenze sono nella guida <a href="articolo-bes-dsa-disabilita.html">Disabilità 104, DSA e BES</a>.</p>
    </div>
    <p>Di solito è un docente con una <strong>specializzazione</strong> apposita. Si ottiene con un corso universitario per le attività di sostegno o, per alcuni docenti, con percorsi organizzati dal Ministero.</p>
    <p>Non sempre ci sono abbastanza docenti specializzati. Per questo su alcuni posti di sostegno lavorano anche docenti senza specializzazione.</p>
    <p>La parola chiave è <strong>contitolare</strong>. Vuol dire che il docente di sostegno è titolare della classe insieme agli altri docenti, con gli stessi diritti e le stesse responsabilità.</p>
    <p>Per questo partecipa ai consigli di classe e agli scrutini, e vota per tutti gli studenti, non solo per quello con disabilità.</p>

    <h2 id="cosa-fa">Che cosa fa, in sei punti</h2>
    <p>Il lavoro del docente di sostegno è più vario di quanto si pensi. Ecco le sue attività principali.</p>
{FIG_FA}
    <p>Il centro di tutto è il <strong>PEI</strong>, il documento che dice obiettivi, aiuti e percorso dello studente. Come funziona lo spiego nella guida <a href="articolo-pei-spiegato-semplice.html">Il PEI spiegato semplice</a>.</p>

    <h2 id="ore">Quante ore e con quale continuità</h2>
    <p>Le ore di sostegno <strong>non sono uguali per tutti</strong>. Dipendono dai bisogni dello studente e sono indicate nel PEI.</p>
    <p>Un decreto-legge del 2026 ha cambiato alcune regole sulle ore. Può ancora cambiare con la conversione in legge, prevista entro fine novembre 2026.</p>
    <p>Non sempre il docente di sostegno è presente per tutto l'orario. Nelle altre ore lo studente è seguito dai docenti delle materie, che conoscono e applicano il PEI.</p>
    <p>Un tema delicato è la <strong>continuità</strong>: cambiare docente ogni anno può pesare molto su uno studente. Se il docente dell'anno prima era un supplente, la famiglia può chiedere di confermarlo. Decide il dirigente scolastico, dopo aver sentito il GLO, e serve che il docente sia d'accordo.</p>

    <h2 id="figure">Chi non è: le altre figure dell'inclusione</h2>
    <p>Intorno a uno studente con disabilità possono lavorare più persone. È facile confonderle, ma hanno compiti diversi.</p>
{FIG_FIGURE}
    <p>Il docente di sostegno <strong>non sostituisce</strong> queste figure, e loro non sostituiscono lui. Ognuno fa la sua parte, e il PEI dice chi fa che cosa.</p>

    <h2 id="esame">All'esame di maturità</h2>
    <p>All'esame di maturità lo studente con disabilità segue il percorso previsto dal suo PEI.</p>
    <p>La commissione può farsi aiutare dai docenti che hanno seguito lo studente durante l'anno, compreso il docente di sostegno. Così le prove possono svolgersi in modo simile a quanto fatto durante l'anno.</p>
    <p>Il docente di sostegno aiuta la commissione, ma non ne fa parte e non dà il voto.</p>
    <p>Non tutti i percorsi portano al diploma. Che cosa cambia lo spiego nella sezione <a href="articolo-pei-spiegato-semplice.html#percorsi">I tre percorsi alle superiori</a>.</p>

    <h2 id="collaborare">Come collaborare</h2>
    <p>Il docente di sostegno non può fare tutto da solo. Ecco qualche idea pratica per lavorare bene insieme.</p>
{COLLAB}
    <p>E per gli <strong>studenti</strong>: il docente di sostegno è un alleato. Digli che cosa ti aiuta e che cosa ti mette a disagio. Insieme potete decidere quando serve la sua presenza e quando puoi farcela da solo.</p>

    <h2 id="falsi-miti">Quattro equivoci da chiarire</h2>
    <p>Sul docente di sostegno circolano alcune idee diffuse, ma sbagliate. Sgombriamo il campo da questi equivoci, uno alla volta.</p>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «È l'insegnante personale dello studente».</p><p><strong>In realtà</strong> è un docente della classe. Cura in particolare il percorso dello studente con disabilità, ma lavora con tutti.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Se c'è il sostegno, gli altri docenti non c'entrano».</p><p><strong>In realtà</strong> lo studente con disabilità è uno studente di tutta la classe. Ogni docente è responsabile del PEI nelle sue ore.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «Il sostegno si fa fuori dall'aula».</p><p><strong>In realtà</strong> l'inclusione si fa in classe, con i compagni. Lavorare fuori è un'eccezione, prevista dal PEI e con un motivo preciso.</p></div>
    <div class="myth"><p class="m-false"><span aria-hidden="true">❌</span> Falso: «È un docente di serie B».</p><p><strong>In realtà</strong> ha gli stessi diritti degli altri docenti: è contitolare, partecipa agli scrutini e vota per tutti gli studenti.</p></div>

    <h2 id="informatica">E in un istituto tecnico?</h2>
    <p>Negli istituti tecnici molte ore si svolgono in <strong>laboratorio</strong>. Qui il docente di sostegno lavora insieme al docente della materia e al docente tecnico-pratico, che guida le esercitazioni di laboratorio.</p>
    <p>Prima di avere questo ruolo ho insegnato informatica per anni, e il laboratorio offre molte occasioni. Si possono dividere i compiti in passi brevi, usare le <a href="articolo-tecnologie-assistive.html">tecnologie assistive</a> e lavorare in piccoli gruppi.</p>
    <p>Se c'è un DSA o un ADHD (disturbo da deficit di attenzione e iperattività) senza certificazione di disabilità, il docente di sostegno non è previsto. In questi casi trovo utili le guide <a href="articolo-informatica-dsa.html">Informatica e DSA</a> e <a href="articolo-adhd-programmazione.html">ADHD e programmazione</a>.</p>

    <h2 id="sintesi">In sintesi</h2>
    <ul class="icon-list">
      <li><span class="t-ico" aria-hidden="true">🤝</span><span>Il <strong>docente di sostegno</strong> è previsto per le classi con uno studente con <strong>disabilità certificata</strong>.</span></li>
      <li><span class="t-ico" aria-hidden="true">🏫</span><span>È un docente <strong>della classe</strong>: contitolare, con gli stessi diritti e responsabilità degli altri.</span></li>
      <li><span class="t-ico" aria-hidden="true">🗂️</span><span>Osserva, progetta il <strong>PEI</strong>, insegna in classe, adatta i materiali e valuta tutti gli studenti.</span></li>
      <li><span class="t-ico" aria-hidden="true">⏱️</span><span>Le <strong>ore</strong> dipendono dal PEI; nelle altre ore lo studente è seguito da tutti i docenti.</span></li>
      <li><span class="t-ico" aria-hidden="true">👥</span><span>L'inclusione funziona solo se si lavora <strong>insieme</strong>.</span></li>
    </ul>
    <p>Un buon docente di sostegno non rende lo studente dipendente da sé. Lo aiuta a crescere e, dove è possibile, a fare da solo.</p>
    <p class="norme rt-skip">Riferimenti normativi: Legge 5 febbraio 1992, n. 104, art. 13 (comma 6, contitolarità); D.Lgs. 16 aprile 1994, n. 297, art. 315; D.P.R. 22 giugno 2009, n. 122, art. 4 (valutazione di tutti gli studenti, come modificato dal D.P.R. 8 agosto 2025, n. 135); D.Lgs. 13 aprile 2017, n. 66, artt. 3 e 15; D.Lgs. 13 aprile 2017, n. 62, art. 20 (esame di maturità); D.I. 29 dicembre 2020, n. 182 e D.I. 1 agosto 2023, n. 153 (PEI e GLO); D.L. 31 maggio 2024, n. 71, art. 8, convertito dalla L. 29 luglio 2024, n. 106, e D.M. 26 febbraio 2025, n. 32 (continuità dei supplenti su richiesta della famiglia, prorogata dal D.L. 127/2025); D.L. 30 settembre 2026, n. 170 (ore di sostegno nel PEI, in corso di conversione). Aggiornato al 20 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica pensate per tutti</h2>
      <p>Nelle lezioni gratuite trovi esempi brevi da modificare e l'editor «Provalo tu» per vedere subito il risultato, senza installare nulla.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Sei un genitore, uno studente o un collega e hai una domanda sul sostegno? <a href="contatti.html">Scrivimi</a>: rispondo a tutti i messaggi.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-pei-spiegato-semplice.html"><span aria-hidden="true">🤝</span><strong>Il PEI spiegato semplice: cos'è, chi lo scrive e come funziona</strong></a>
        <a href="articolo-bes-dsa-disabilita.html"><span aria-hidden="true">🧭</span><strong>Disabilità 104, DSA e BES: che differenza c'è?</strong></a>
        <a href="articolo-tecnologie-assistive.html"><span aria-hidden="true">🛠️</span><strong>Tecnologie assistive per studiare: quali sono e come averle a scuola</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="docente di sostegno, insegnante di sostegno, cosa fa il docente di sostegno, sostegno superiori, contitolarità, ore di sostegno, continuità sostegno, legge 104 scuola",
    og_alt="Il titolo «Chi è il docente di sostegno» e tre riquadri: chi è, un docente della classe; cosa fa, progetta, insegna, collabora; con chi, studenti, famiglie e colleghi.",
    date_iso="2026-11-20", date_it="20 novembre 2026",
    ld_keywords="docente di sostegno, insegnante di sostegno, Legge 104, disabilità, PEI, GLO, contitolarità, inclusione scolastica, scuola secondaria di secondo grado",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Chi è il docente di sostegno» e tre riquadri: chi è, un docente della classe; cosa fa, progetta, insegna, collabora; con chi, studenti, famiglie e colleghi.",
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('SOSTEGNO: parole', words, '| minuti', MIN)
