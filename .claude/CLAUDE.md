# Sito alessandrosimone.it — contesto di lavoro

Questo file viene letto in automatico da Claude Code all'inizio di ogni chat.
Sta in `.claude/`, quindi GitHub Pages **non lo pubblica** (come `_strumenti/`).
Rispondi all'autore **in italiano**, in modo semplice e diretto.

## Chi è l'autore e che cos'è il sito

- **Alessandro Simone**, «docente di informatica felicemente prestato all'inclusione»:
  oggi è **docente di inclusione** (sostegno) all'**Istituto Tecnico Industriale Statale
  Giovanni XXIII di Roma**. In passato docente d'informatica all'Istituto Tecnico Industriale
  Informatico Alfred Nobel di Roma.
- Titoli (sezione Titoli della home): Master in Informatica, Master in Project Management,
  Abilitazione alla docenza di Informatica, Specializzazione in Marketing e Comunicazione,
  Specializzazione ADSS (BES, DSA, disabilità certificata, PEI e PDP).
- Il sito è **informativo**: lezioni gratuite di informatica, blog, contatti. **Non offre più
  ripetizioni**: non reintrodurre mai riferimenti a ripetizioni, prenotazioni, tariffe o lezioni a pagamento.
- Motto della home: «L'informatica inclusiva spiegata in modo semplice».

## Struttura

- Sito statico HTML/CSS/JS su **GitHub Pages** (dominio in `CNAME`), repository
  `AlexAndro-debug-svg/corso-github`. Nessun build: si modificano direttamente i file.
- Menu: **Home · Lezioni gratuite · Blog · Contatti**. «Chi sono» è una sezione della home (`/#chi-sono`).
- Pagine principali: `index.html`, `lezioni.html` (ex corsi), `blog.html`, `contatti.html` (solo email),
  `corso-*.html` (lezioni, con esempi «Provalo tu»), `articolo-*.html` (blog), `cookie-policy.html`.
- Pagine eliminate = **file di reindirizzamento** (meta refresh + `location.replace` + `noindex`):
  `ripetizioni.html`, `prenota.html`, `area-studenti.html`, `esercizi.html` → home; `chi-sono.html` → `/#chi-sono`;
  `corsi.html` → `lezioni.html`; vecchi articoli → blog o articolo sostitutivo. Si riconoscono da `http-equiv="refresh"`.
- In ogni pagina: Google Analytics `G-9X6ETTP6Y0` subito dopo `<head>`; in fondo
  `js/main.js?v=10`, `js/search.js`, `js/cookie-consent.js`; stile `css/style.css?v=10`.
  Quando cambi un file JS/CSS già pubblicato, **alza il `?v=`** in tutte le pagine che lo usano.
- `sitemap.xml` e `robots.txt` puntano a `https://alessandrosimone.it/`.

## Pubblicazione

1. Lavora sul ramo di sviluppo indicato dalla sessione (commit con messaggi in italiano).
2. `git push -u origin <ramo>`.
3. Per pubblicare: `git checkout main && git merge --ff-only <ramo> && git push -u origin main`, poi torna sul ramo.
   Il sito si aggiorna in 1-2 minuti (l'autore ricarica con Ctrl+F5).
- Se il lavoro non è finito, fai commit e push **solo sul ramo** (non su main).
- Dall'ambiente di lavoro il proxy **blocca** `alessandrosimone.it` e i CDN (cdnjs, jsdelivr…):
  le verifiche si fanno in locale (vedi «Verifiche»).

## Serie «inclusione» a lettura facilitata

Articoli pubblicati: `articolo-informatica-dsa.html` («Informatica e DSA»),
`articolo-bes-dsa-disabilita.html` («Disabilità 104, DSA e BES: che differenza c'è?», articolo guida),
`articolo-pei-spiegato-semplice.html` («Il PEI spiegato semplice», 15/11/2026, generatore `build_pei.py`),
`articolo-pdp-passo-dopo-passo.html` («Il PDP passo dopo passo», 17/11/2026, generatore `build_pdp.py`).
- **Da fare dopo il 29/11/2026**: l'articolo PEI cita il D.L. 30 settembre 2026, n. 170 (scadenze del PEI, ore di
  sostegno «definite» dal PEI, GLO valido con una componente assente), in conversione con molti emendamenti.
  Ricontrolla il testo della legge di conversione, aggiorna calendario, FAQ, riquadro «Regole in cambiamento» e `modified_iso`.
  C'è un promemoria programmato per il 30/11/2026 alle 9:47 (ora di Roma): mostra le modifiche all'autore
  **prima** di pubblicarle; dopo, togli questo punto.

- **Si generano da script**: `_strumenti/articoli/build_*.py` (testo e figure) + `artlib.py`
  (funzioni comuni, CSS e JS condivisi, modello di pagina). Modifica il testo **nel generatore** e rigenera:
  `python3 _strumenti/articoli/build_bes.py .` (dalla radice). Se correggi a mano l'HTML, riporta la
  modifica anche nel generatore, altrimenti si perde alla prossima rigenerazione.
- Stili e script condivisi: `css/lettura-facilitata.css` e `js/lettura-facilitata.js` (scritti da `artlib.py`,
  versione in `ASSET_V`, ora **4**: alzala quando li cambi). Contengono: sintesi vocale «Ascolta l'articolo»
  (legge solo la versione visibile, salta `.rt-skip`, toglie emoji e frecce, frasi ≤160 caratteri),
  A−/A+ (con A+ la tabella diventa a schede), carattere Atkinson Hyperlegible, sfondo crema, memoria in localStorage.
- Regole di scrittura (pensate per lettori con DSA, guida British Dyslexia Association):
  frasi brevi (≤ ~25 parole), un concetto per paragrafo, niente corsivi, grassetto per le parole chiave,
  termini e sigle spiegati alla prima occorrenza, «tu» al lettore, prima persona per Alessandro,
  **niente aneddoti o dati inventati**. Struttura: riassunto «in 30 secondi», indice, sezioni con figure,
  «In sintesi», domande frequenti, riferimenti normativi (`.norme rt-skip`), «Leggi anche».
- **Gruppi, sempre con lo stesso colore, icona e numero** (il colore non è mai l'unica informazione):
  - Gruppo 1 · Disabilità certificata (Legge 104 · PEI · docente di sostegno) — viola, 🤝, classe `g1`
  - Gruppo 2 · DSA (Legge 170 · PDP obbligatorio) — verde acqua, 📖, classe `g2`
  - Gruppo 3 · Altri BES (ADHD e altri disturbi, svantaggio; PDP se lo decide il consiglio di classe) — arancione, 🧩, classe `g3`
  - **I BES sono una voce a sé, dopo 104 e DSA, non un «ombrello»** (scelta dell'autore; c'è una sola nota
    che ricorda il senso ampio della direttiva del 2012).
- Prossimi articoli (in quest'ordine): 5 «Tecnologie assistive per studiare», 6 «ADHD e programmazione», 4 «Legge 104 a scuola»,
  7 «Esame di maturità con DSA, BES o disabilità» (da pubblicare a marzo-aprile, quando esce l'ordinanza).
  Alternativa proposta: «Chi è il docente di sostegno e cosa fa alle superiori».
- Per ogni nuovo articolo: copertina 1200×630 (`node _strumenti/genera_copertina.js <modello> <uscita.jpg>`,
  modelli in `_strumenti/copertine/`), scheda **in cima** a `blog.html`, voce in `js/search.js`, `sitemap.xml`,
  link interni pertinenti e **link di ritorno** dagli articoli collegati, revisione indipendente
  (normativa, leggibilità DSA, italiano, SEO/codice, punto di vista del genitore) prima di pubblicare.
- Normativa: verificala su fonti ufficiali; nome attuale dell'esame finale: «esame di maturità»
  (D.L. 127/2025, conv. L. 164/2025); riforma disabilità D.Lgs. 62/2024 («valutazione di base» INPS).

## Lezioni (`corso-*.html`): attenzione

- Gli esempi «Provalo tu» stanno in `<script type="text/plain" class="code">…</script>`: dentro un esempio
  ogni `</script>` va scritto `<\/script>` (la pagina lo riconverte), altrimenti l'esempio si spezza.
- **Mai sostituzioni di massa alla cieca**: esempi e stringhe JS contengono `</body>`, `<head>`, «Corsi» ecc.
  Un vecchio inserimento di `search.js` prima di ogni `</body>` aveva rotto 7 lezioni. Dopo modifiche di massa
  lancia sempre `python3 _strumenti/controllo_statico.py` e la prova nel browser.

## Verifiche (prima di pubblicare)

Dipendenze: `cd _strumenti && npm install` (cartella `node_modules` ignorata da git; Chromium è in
`/opt/pw-browsers/chromium`, non lanciare `playwright install`).

- Server locale: `(python3 -m http.server 8767 &)` dalla radice. Per fermarlo usa
  `pkill -f "http[.]server"` (un pattern senza parentesi ucciderebbe anche la shell).
- `python3 _strumenti/controllo_statico.py` — script interni e blocchi degli esempi.
- `node _strumenti/audit.js http://localhost:8767 . /tmp/esito.json [pagine]` — prova di tutte le pagine
  (testo fuori posto, errori JS, ogni «Provalo tu»). Esito atteso oggi: 80 pagine, 1179/1179 «Provalo tu».
- `node _strumenti/test_lettura.js http://localhost:8767 articolo-XXX.html` — strumenti di lettura facilitata.
- Guarda anche le pagine a 390 px e a 1280 px con screenshot (niente scorrimento orizzontale).

## Cose da sapere

- Intestazione di `blog.html` (scelta dall'autore il 15/11/2026): etichetta «Blog & Guide», titolo
  «Articoli per studenti, famiglie e docenti», sottotitolo «Inclusività e Informatica al passo coi tempi» (senza punto; nella home il punto c'è).
  Per Google e condivisioni: `<title>` «Blog di informatica e inclusione a scuola — AlessandroSimone.it»,
  descrizione «Guide gratuite di informatica e inclusione scolastica: Python, reti e algoritmi, ma anche PEI,
  PDP, DSA e BES spiegati in modo semplice.» (uguali in `og:` e `twitter:`).
  Nella home, scheda del blog in «Scegli il tuo percorso»: icona 📖, etichetta «Blog & Guide», stesso titolo e
  sottotitolo del blog, «Vai al blog →». Scheda BES nel blog: icona 🧭 (niente ombrelli, i BES non sono un «ombrello»).
- Tasto «Torna su» (15/11/2026) su tutte le pagine: lo crea `js/main.js`, stile `.to-top` in fondo a `css/style.css`.
  Computer (≥1024 px): a metà del lato destro; telefono e tablet: in basso a destra. Compare dopo 400 px di scorrimento,
  porta in cima in ~0,4 s; si nasconde con il banner cookie (su telefono) e con l'editor «Provalo tu» aperto,
  si alza sopra il lettore vocale degli articoli. Esclusi `landing.html` e `mockup.html` (vecchie pagine noindex, senza main.js).
- La home ha i titoli e le esperienze in schede; il footer di tutte le pagine dice
  «Docente di informatica felicemente prestato all'inclusione nella scuola secondaria di II grado a Roma.
  Lezioni, guide e materiali gratuiti.»
- Problemi noti non ancora risolti (proposti all'autore, in attesa di risposta): il pulsante arancione dei
  riquadri finali (`.cta-banner .btn-accent`) ha testo bianco con contrasto 2,15:1 in tutto il sito
  (corretto solo negli articoli della serie); molti articoli indicano un'immagine `og:image` che non esiste.
