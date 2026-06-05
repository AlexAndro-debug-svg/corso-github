# alessandrosimone.it

Sito web di **Alessandro Simone**, docente di informatica nella scuola secondaria di II grado.
Sito statico (HTML/CSS/JS), pronto per la pubblicazione gratuita su **GitHub Pages**.

## 📂 Struttura del sito

| File | Pagina |
|------|--------|
| `index.html` | Home — bivio tra studenti e ripetizioni |
| `chi-sono.html` | Biografia ed esperienza |
| `ripetizioni.html` | Servizio di ripetizioni e prezzi |
| `prenota.html` | Prenotazione online |
| `esercizi.html` | Esercizi con filtri e soluzioni |
| `blog.html` | Lista articoli/guide |
| `articolo.html` | Articolo di esempio (da duplicare) |
| `contatti.html` | Modulo contatti e FAQ |
| `css/style.css` | Stile condiviso (qui cambi i **colori**) |
| `js/main.js` | Menu mobile, filtri esercizi |

> I file `mockup.html` e `landing.html` sono le bozze iniziali: puoi eliminarli quando vuoi.

## 🚀 Come pubblicare il sito (GitHub Pages)

1. Vai su **Settings → Pages** nel repository
2. In *Source* seleziona il branch `main` e cartella `/ (root)`
3. Salva: dopo qualche minuto il sito sarà online su
   `https://<tuo-username>.github.io/<repository>/`

## 🎨 Personalizzare

- **Colori**: modifica le variabili all'inizio di `css/style.css` (sezione `:root`)
- **Testi**: modifica direttamente il contenuto delle pagine `.html`
- **Nuovo articolo**: duplica `articolo.html`, cambia testo e aggiungi una card in `blog.html`
- **Nuovo esercizio**: copia un blocco `.ex-item` in `esercizi.html` (occhio all'attributo `data-cat`)

## ⚙️ Funzioni da collegare

### 📅 Calendario prenotazioni (`prenota.html`)
Sostituisci il riquadro `.embed-box` con un widget gratuito:
- **Google Calendar** → crea una "pagina di prenotazione appuntamenti"
- **Calendly** → `<iframe src="https://calendly.com/tuo-nome" width="100%" height="700"></iframe>`
- **Cal.com** → embed open source gratuito

### 📨 Modulo contatti (`contatti.html`)
Il form usa [Formspree](https://formspree.io) (gratuito, senza backend):
1. Crea un account e un nuovo form
2. Copia l'URL e incollalo nell'attributo `action` del `<form>`

## 🌐 Dominio personalizzato `alessandrosimone.it`

1. **Settings → Pages → Custom domain**: inserisci `alessandrosimone.it`
2. Dal tuo registrar DNS aggiungi:
   ```
   A     185.199.108.153
   A     185.199.109.153
   A     185.199.110.153
   A     185.199.111.153
   CNAME www → <tuo-username>.github.io
   ```
3. Attiva **Enforce HTTPS**
