#!/usr/bin/env python3
"""Articolo della serie inclusione: tecnologie assistive (stile professionale, riscritto il 21/11/2026)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import *

SLUG = "articolo-tecnologie-assistive"
TITLE = "Le tecnologie assistive a scuola: tipologie, modalità di accesso e integrazione nella progettazione didattica"
SEO_TITLE = "Tecnologie assistive a scuola: tipologie e accesso — AlessandroSimone.it"
DESC = "Tecnologie assistive per disabilità, DSA e altri BES: tipologie, funzioni di accessibilità integrate, comodato dei CTS, fornitura ASL, agevolazioni fiscali e PEI/PDP."
URL = f"https://alessandrosimone.it/{SLUG}.html"
IMG = f"https://alessandrosimone.it/{SLUG}.jpg"

# ------------------------------------------------------------------ FAQ
FAQS = "\n".join([
    faq("Chi sostiene il costo di un ausilio destinato all'uso scolastico?",
        "Dipende dalla natura dell'ausilio. Le dotazioni d'aula sono a carico della scuola, che per gli studenti con disabilità può ricorrere anche al comodato dei CTS. Gli ausili personali connessi alla disabilità possono essere erogati dal Servizio sanitario nazionale, su prescrizione specialistica. Gli acquisti della famiglia possono beneficiare di agevolazioni fiscali."),
    faq("È consentito l'uso di un dispositivo personale a scuola?",
        "Sì, se previsto dal PDP o dal PEI, che dovrebbero indicarne con precisione ambiti e modalità d'uso, comprese le verifiche. Per lo smartphone vale un vincolo ulteriore: nella secondaria di secondo grado l'uso in classe è vietato dalla Circ. MIM 3392/2025, salvo i casi previsti dal PEI o dal PDP."),
    faq("Un ausilio concesso in comodato dal CTS può essere utilizzato a domicilio?",
        "Dipende dal regolamento del CTS e della scuola: il comodato è concesso all'istituzione scolastica, non alla famiglia. È opportuno chiarire in anticipo modalità d'uso, effetti di un eventuale trasferimento dello studente e responsabilità in caso di guasto o smarrimento."),
    faq("Come funziona la detrazione per gli studenti con DSA?",
        "L'art. 15, comma 1, lett. e-bis) del TUIR consente di detrarre al 19% le spese per strumenti compensativi e sussidi tecnici e informatici, compresi computer e tablet, fino al completamento della secondaria di secondo grado. Occorre la diagnosi di DSA e il collegamento funzionale tra strumento e disturbo deve risultare dalla diagnosi o da una prescrizione medica. Il pagamento deve essere tracciabile e la fattura deve descrivere il bene; per i redditi più elevati possono operare limitazioni. È consigliabile rivolgersi a un CAF (Centro di assistenza fiscale) o a un commercialista."),
    faq("Sono previste agevolazioni anche per la disabilità?",
        "Sì: per i sussidi tecnici e informatici destinati a persone con disabilità sono previste una detrazione d'imposta e l'aliquota IVA agevolata, di norma subordinate a una prescrizione specialistica che attesti il collegamento funzionale con la menomazione. Poiché i requisiti variano in base alla disabilità e al sussidio, è opportuna una verifica preventiva con un CAF o un commercialista."),
    faq("Le applicazioni di intelligenza artificiale possono essere considerate tecnologie assistive?",
        "Possono svolgere una funzione di supporto rilevante, ad esempio nella sintesi, nella semplificazione dei testi o nel ripasso; il loro impiego a scuola deve però essere previsto nel PDP o nel PEI. All'esame di maturità, di norma, non sono ammessi strumenti collegati alla rete. Un approfondimento è disponibile in <a href=\"articolo-chatgpt-studiare.html\">Come usare ChatGPT per studiare</a>."),
    faq("Quali strumenti sono ammessi all'esame di maturità?",
        "Sono ammessi gli strumenti previsti dal PEI o dal PDP e utilizzati durante l'anno, anche nelle verifiche; per gli studenti con DSA sono previsti anche tempi più lunghi. Per gli altri BES il regime è più restrittivo, come illustrato in <a href=\"articolo-pdp-passo-dopo-passo.html#verifiche\">Il Piano Didattico Personalizzato (PDP)</a>."),
])

# ------------------------------------------------------------------ CORPO
BODY = f"""
    <p>Le <strong>tecnologie assistive</strong> comprendono dispositivi, apparecchiature e programmi che consentono a una persona di svolgere attività altrimenti rese molto difficoltose, o impossibili, da una disabilità, da un DSA (Disturbo Specifico dell'Apprendimento) o da un altro BES (Bisogno Educativo Speciale).</p>
    <p>Lavoro quotidianamente come docente per l'inclusività (<a href="/#chi-sono">chi sono</a>) e, prima, ho insegnato informatica per anni. In questo contributo propongo una ricognizione delle principali tipologie, delle funzioni di accessibilità già integrate nei sistemi operativi e, soprattutto, dei canali attraverso cui tali strumenti possono essere resi disponibili a scuola.</p>

    <nav class="dsa-box toc rt-skip" aria-label="Indice dell'articolo">
      <h2 class="box-title">Indice</h2>
      <ol>
        <li><a href="#cosa-sono">Definizione e funzione</a></li>
        <li><a href="#disabilita">Ausili per la disabilità</a></li>
        <li><a href="#dsa">Strumenti compensativi per i DSA</a></li>
        <li><a href="#altri-bes">Supporti per gli altri BES</a></li>
        <li><a href="#gratis">Le funzioni di accessibilità integrate</a></li>
        <li><a href="#come-averle">Modalità di accesso</a></li>
        <li><a href="#pei-pdp">L'integrazione nel PEI e nel PDP</a></li>
        <li><a href="#consigli">Criteri di scelta</a></li>
        <li><a href="#falsi-miti">Alcuni fraintendimenti ricorrenti</a></li>
        <li><a href="#informatica">Il laboratorio di informatica</a></li>
        <li><a href="#sintesi">Considerazioni conclusive</a></li>
        <li><a href="#faq">Domande frequenti</a></li>
      </ol>
    </nav>

    <h2 id="cosa-sono">Definizione e funzione</h2>
    <p>Nel lessico scolastico si parla di <strong>ausili</strong> con riferimento alla disabilità e di <strong>strumenti compensativi</strong> con riferimento ai DSA e agli altri BES. La funzione è comune: rimuovere un ostacolo strumentale, senza sostituirsi allo studente nell'elaborazione cognitiva.</p>
    <p>In questa prospettiva le tecnologie assistive operano come <strong>facilitatori</strong> nel senso dell'ICF: modificano il rapporto tra la persona e il contesto, ampliandone le possibilità di partecipazione.</p>

    <h2 id="disabilita">Ausili per la disabilità</h2>
    <p>Per gli studenti con disabilità certificata ai sensi della L. 104/92 gli ausili sono individuati in relazione al profilo di funzionamento e indicati nel PEI (Piano Educativo Individualizzato). Le principali categorie sono:</p>
    <ul>
      <li><strong>comunicatori e CAA</strong>: la Comunicazione Aumentativa e Alternativa si avvale di tabelle simboliche o di dispositivi a uscita vocale che consentono di esprimersi a chi non dispone, in tutto o in parte, del linguaggio verbale;</li>
      <li><strong>tastiere e dispositivi di puntamento adattati</strong>: tastiere a tasti ingranditi o dotate di scudo, che guida la pressione del tasto corretto; trackball e joystick in sostituzione del mouse;</li>
      <li><strong>sensori e sistemi di puntamento oculare</strong>, per chi dispone di una motricità degli arti superiori limitata;</li>
      <li><strong>lettori di schermo e display Braille</strong>: il lettore di schermo restituisce in voce testi, menu e comandi e consente di operare da tastiera; il display Braille traduce il testo in caratteri tattili;</li>
      <li><strong>ingranditori e impostazioni ad alto contrasto</strong>, per l'ipovisione;</li>
      <li><strong>sottotitolazione e sistemi di trasmissione del segnale audio</strong>, che recapitano la voce del docente direttamente alla protesi acustica o all'impianto cocleare;</li>
      <li><strong>software semplificati e agende visive</strong>, per la disabilità intellettiva: attività strutturate per immagini e simboli, articolate in passaggi brevi.</li>
    </ul>
    <p>La scelta richiede una valutazione congiunta degli specialisti che seguono lo studente, della famiglia e della scuola.</p>

    <h2 id="dsa">Strumenti compensativi per i DSA</h2>
    <p>Per gli studenti con DSA gli strumenti compensativi sono previsti dall'art. 5 della L. 170/2010 e indicati nel PDP (Piano Didattico Personalizzato), obbligatorio in presenza di diagnosi. I più diffusi sono la sintesi vocale, il correttore ortografico, le mappe concettuali e la calcolatrice; in ambito informatico risulta particolarmente utile l'evidenziazione della sintassi nell'editor.</p>
    <p>Una trattazione analitica, con esemplificazioni, è disponibile in <a href="articolo-informatica-dsa.html#strumenti">Informatica e DSA</a>.</p>

    <h2 id="altri-bes">Supporti per gli altri BES</h2>
    <p>Per gli altri BES gli strumenti sono adottati se previsti dal consiglio di classe nel PDP, spesso con carattere temporaneo. A titolo esemplificativo:</p>
    <ul>
      <li>per gli studenti con <strong>ADHD</strong> (disturbo da deficit di attenzione e iperattività): timer visivi, agende digitali per l'organizzazione del lavoro, dispositivi di riduzione del rumore; ulteriori indicazioni sono in <a href="articolo-adhd-programmazione.html">ADHD e programmazione</a>;</li>
      <li>per gli studenti in fase di <strong>apprendimento dell'italiano</strong>: dizionari visuali, sintesi vocale per l'ascolto della pronuncia, strumenti di traduzione per le consegne più complesse.</li>
    </ul>

    <h2 id="gratis">Le funzioni di accessibilità integrate</h2>
    <p>Prima di ricorrere a soluzioni dedicate, è opportuno esplorare le funzioni di accessibilità già presenti, senza costi aggiuntivi, nei principali sistemi operativi:</p>
    <ul>
      <li><strong>Windows</strong>: Assistente vocale (lettore di schermo), Lente di ingrandimento e Digitazione vocale, attivabile con la combinazione dei tasti Windows e H;</li>
      <li><strong>macOS e iPadOS</strong>: VoiceOver (lettore di schermo), Contenuto letto ad alta voce e Dettatura;</li>
      <li><strong>Android e ChromeOS</strong>: TalkBack (Android) e ChromeVox (Chromebook), entrambi lettori di schermo, e la funzione Seleziona per ascoltare;</li>
      <li><strong>software gratuito</strong>: NVDA, lettore di schermo open source per Windows; molti browser ed editor dispongono inoltre di funzioni di lettura ad alta voce.</li>
    </ul>
    <p>Anche i <strong>testi</strong> possono essere resi accessibili: per i DSA è disponibile LibroAID, la biblioteca digitale dell'Associazione Italiana Dislessia; per le persone con disabilità visiva, la Biblioteca Italiana per i Ciechi produce testi in Braille e in formato digitale.</p>

    <h2 id="come-averle">Modalità di accesso</h2>
    <p>Quando lo strumento non è già disponibile, i canali di accesso sono tre, spesso complementari.</p>
    <h3>La scuola e il CTS</h3>
    <p>La scuola può impiegare le proprie dotazioni e, per gli studenti con disabilità, richiedere ausili in <strong>comodato d'uso gratuito</strong> al <strong>CTS</strong> (Centro Territoriale di Supporto) della provincia, previsto dalla Direttiva ministeriale 27 dicembre 2012 e finanziato ai sensi dell'art. 7, comma 3, del D.Lgs. 63/2017. La richiesta è presentata dall'istituzione scolastica, sulla base di un progetto connesso al PEI. Per i DSA il CTS svolge prevalentemente funzioni di consulenza e formazione.</p>
    <h3>Il Servizio sanitario nazionale</h3>
    <p>Alcuni ausili personali, come comunicatori, sensori e tastiere speciali, rientrano nel nomenclatore dei livelli essenziali di assistenza (D.P.C.M. 12 gennaio 2017) e sono erogati dall'ASL (Azienda sanitaria locale), previa prescrizione di un medico specialista e autorizzazione. Computer e tablet di uso comune, di norma, non sono compresi; i tempi possono essere lunghi e richiedono un'attivazione tempestiva.</p>
    <h3>L'acquisto da parte della famiglia</h3>
    <p>Gli acquisti della famiglia possono beneficiare di <strong>agevolazioni fiscali</strong>: per i DSA, la detrazione del 19% prevista dall'art. 15, comma 1, lett. e-bis) del TUIR, fino al termine della secondaria di secondo grado; per la disabilità, la detrazione e l'aliquota IVA agevolata sui sussidi tecnici e informatici.</p>
    <p>Il primo interlocutore, all'interno della scuola, è il coordinatore di classe o il <a href="articolo-docente-di-sostegno.html">docente di sostegno</a>; in seconda battuta il referente per l'inclusione. Poiché le procedure dei CTS variano da provincia a provincia, è opportuno informarsi anche sui tempi e sulle conseguenze di un eventuale cambio di scuola.</p>

    <h2 id="pei-pdp">L'integrazione nel PEI e nel PDP</h2>
    <p>La disponibilità dello strumento non è sufficiente: occorre che il suo impiego sia formalizzato nel PEI, per la disabilità, o nel PDP, per i DSA e gli altri BES, con l'indicazione dello strumento, delle discipline interessate e dell'eventuale utilizzo in sede di verifica. I due documenti sono illustrati in <a href="articolo-pei-spiegato-semplice.html">Il Piano Educativo Individualizzato (PEI)</a> e in <a href="articolo-pdp-passo-dopo-passo.html">Il Piano Didattico Personalizzato (PDP)</a>.</p>
    <p>All'esame di maturità sono ammessi gli strumenti previsti e già utilizzati durante l'anno: di qui l'importanza di un impiego sistematico fin dalle classi iniziali.</p>

    <h2 id="consigli">Criteri di scelta</h2>
    <ul>
      <li><strong>Partire dal bisogno, non dallo strumento</strong>: l'analisi della difficoltà precede l'individuazione della soluzione.</li>
      <li><strong>Sperimentare prima di acquistare</strong>, avvalendosi di versioni di prova e, ove disponibile, della consulenza dei CTS.</li>
      <li><strong>Prevedere un periodo di addestramento</strong>, per lo studente e per i docenti: in una prima fase lo strumento rallenta il lavoro.</li>
      <li><strong>Garantire un uso quotidiano</strong>, a scuola e a casa, condizione essenziale della sua efficacia.</li>
      <li><strong>Ascoltare lo studente</strong>, che è il primo giudice dell'utilità e dell'accettabilità dello strumento.</li>
    </ul>

    <h2 id="falsi-miti">Alcuni fraintendimenti ricorrenti</h2>
    <p>Alcune idee circolano spesso, ma non trovano riscontro nella pratica.</p>
    <p><strong>«La tecnologia riduce l'autonomia».</strong> Lo strumento rimuove l'ostacolo, mentre l'elaborazione resta a carico dello studente; nella maggior parte dei casi ne accresce l'autonomia.</p>
    <p><strong>«Servono strumenti costosi».</strong> Numerose funzioni sono già disponibili gratuitamente nei sistemi operativi; gli ausili specifici possono essere richiesti alla scuola o all'ASL.</p>
    <p><strong>«Una prova svolta con lo strumento vale meno».</strong> La valutazione ha pieno valore: lo strumento serve proprio a rilevare gli apprendimenti effettivi.</p>
    <p><strong>«È sufficiente consegnare lo strumento».</strong> Senza formazione e senza formalizzazione nel PEI o nel PDP, lo strumento rischia di restare inutilizzato.</p>

    <h2 id="informatica">Il laboratorio di informatica</h2>
    <p>Il laboratorio di informatica è un contesto privilegiato per l'introduzione delle tecnologie assistive. Alcune indicazioni operative:</p>
    <ul>
      <li>configurare preventivamente le funzioni di accessibilità sulle postazioni;</li>
      <li>considerare che anche la programmazione è praticabile con un lettore di schermo: Visual Studio Code, ad esempio, dispone di una modalità dedicata;</li>
      <li>valorizzare la programmazione a blocchi per chi incontra difficoltà nella scrittura, tenendo presente che, basandosi sul trascinamento con il mouse, non è adatta a chi utilizza un lettore di schermo;</li>
      <li>proporre all'intera classe strumenti come la dettatura vocale e la lettura ad alta voce, utili a tutti.</li>
    </ul>
    <p>Le <a href="lezioni.html">lezioni gratuite</a> del sito funzionano interamente nel browser, senza installazioni.</p>

    <h2 id="sintesi">Considerazioni conclusive</h2>
    <ul>
      <li>Le tecnologie assistive rimuovono ostacoli strumentali senza sostituirsi allo studente.</li>
      <li>Per la disabilità si parla di ausili, indicati nel PEI; per i DSA e gli altri BES di strumenti compensativi, indicati nel PDP.</li>
      <li>Molte funzioni sono già disponibili gratuitamente nei sistemi operativi.</li>
      <li>I canali di accesso sono tre: la scuola (con il comodato dei CTS per la disabilità), il Servizio sanitario nazionale e l'acquisto con agevolazioni fiscali.</li>
      <li>L'efficacia dipende dalla formalizzazione nei documenti, dalla formazione e dall'uso quotidiano.</li>
    </ul>
    <p>La tecnologia più adeguata non è necessariamente la più sofisticata, ma quella che lo studente utilizza con continuità e consapevolezza.</p>
    <p class="norme rt-skip">Riferimenti normativi: L. 104/92, art. 13 (sussidi e attrezzature tecniche); L. 170/2010, art. 5 (strumenti compensativi); D.M. 5669/2011 e Linee guida DSA; Direttiva ministeriale 27 dicembre 2012 (Centri Territoriali di Supporto); D.Lgs. 63/2017, art. 7, comma 3 (ausili in comodato); D.Lgs. 66/2017; D.Lgs. 62/2017, art. 20; ordinanza ministeriale annuale sull'esame di maturità; Circ. MIM 3392/2025 (uso del cellulare a scuola); D.P.C.M. 12 gennaio 2017 (livelli essenziali di assistenza, allegato 5); D.P.R. 917/1986 (TUIR), art. 15, comma 1, lettere c) ed e-bis). Aggiornato al 18 novembre 2026.</p>

    <h2 id="faq">Domande frequenti</h2>
{FAQS}

    <div class="cta-banner mt-4 rt-skip">
      <h2>Lezioni di informatica per una didattica inclusiva</h2>
      <p>Le lezioni gratuite del sito propongono esempi brevi e modificabili, con l'editor «Provalo tu» integrato nel browser.</p>
      <a href="lezioni.html" class="btn btn-accent btn-lg">Vai alle lezioni gratuite →</a>
    </div>
    <p class="rt-skip" style="margin-top:1.4rem">Usi una tecnologia assistiva che ha cambiato il tuo modo di studiare o di insegnare? Hai un dubbio? <a href="contatti.html">Scrivimi</a>: mi fa piacere ricevere domande ed esperienze.</p>

    <div class="read-next rt-skip">
      <h2 class="box-title"><span aria-hidden="true">📚</span> Leggi anche</h2>
      <div class="rn-grid">
        <a href="articolo-informatica-dsa.html"><span aria-hidden="true">📖</span><strong>Informatica e DSA: strategie e strumenti compensativi</strong></a>
        <a href="articolo-pdp-passo-dopo-passo.html"><span aria-hidden="true">📝</span><strong>Il Piano Didattico Personalizzato (PDP): destinatari, elaborazione e contenuti</strong></a>
        <a href="articolo-pei-spiegato-semplice.html"><span aria-hidden="true">🤝</span><strong>Il Piano Educativo Individualizzato (PEI): elaborazione, contenuti e percorsi</strong></a>
      </div>
    </div>
"""

words, MIN = minutes(BODY, skip=('pre', 'svg', 'nav', 'details'))
META = dict(
    title=TITLE, seo_title=SEO_TITLE, desc=DESC, url=URL, img=IMG, minutes=MIN, body=BODY,
    keywords="tecnologie assistive, ausili scolastici, comunicatore CAA, lettore di schermo, strumenti compensativi, CTS comodato ausili, nomenclatore ausili ASL, detrazione DSA",
    og_alt="Il titolo «Le tecnologie assistive a scuola» con il sottotitolo «Tipologie, accesso e integrazione didattica» e tre riquadri: destinatari, disabilità, DSA e altri BES; tipologie, dagli ausili alla sintesi vocale; accesso, scuola, ASL o famiglia.",
    date_iso="2026-11-18", modified_iso="2026-11-21", date_it="18 novembre 2026",
    ld_keywords="tecnologie assistive, ausili, CAA, comunicatore, lettore di schermo, strumenti compensativi, CTS, nomenclatore, inclusione scolastica",
    hero_src=f"{SLUG}.jpg",
    hero_alt="Copertina dell'articolo: il titolo «Le tecnologie assistive a scuola» con il sottotitolo «Tipologie, accesso e integrazione didattica» e tre riquadri: destinatari, disabilità, DSA e altri BES; tipologie, dagli ausili alla sintesi vocale; accesso, scuola, ASL o famiglia.",
    no_rt_note=True, no_tool_icons=True,   # stile professionale (dal 21/11/2026)
)

if __name__ == '__main__':
    root = sys.argv[1]
    write_shared(root)
    open(os.path.join(root, f'{SLUG}.html'), 'w', encoding='utf-8').write(page(META))
    print('TECNO: parole', words, '| minuti', MIN)
