# alessandrosimone.it

Sito web personale di **Alessandro Simone** — ripetizioni di informatica a Roma e online in tutta Italia.

## Stack

Sito statico, zero dipendenze:

- `index.html` — markup e contenuti
- `style.css` — design system (dark, gradient, responsive)
- `script.js` — menu mobile, anno footer, reveal-on-scroll
- `CNAME` — dominio custom per GitHub Pages (`alessandrosimone.it`)
- `robots.txt` + `sitemap.xml` — SEO di base

## Come vederlo in locale

Apri semplicemente `index.html` nel browser, oppure:

```bash
python3 -m http.server 8080
# poi apri http://localhost:8080
```

## Deploy su GitHub Pages con dominio custom

1. Vai su **Settings → Pages** del repo.
2. Source: `Deploy from a branch` → branch `main` (o quello pubblicato) → `/ (root)`.
3. Il file `CNAME` nella root configura automaticamente il dominio `alessandrosimone.it`.
4. Nel DNS del dominio:
   - Record `A` verso gli IP di GitHub Pages:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
   - Record `CNAME` `www` → `<username>.github.io`
5. Abilita **Enforce HTTPS** su GitHub Pages.

## Personalizzazione

Contenuti testuali e sezioni sono in `index.html`. Le sezioni principali:

- **Hero** — titolo + CTA
- **Chi sono** — bio e card profilo
- **Servizi** — tipologie di lezioni
- **Materie** — linguaggi e argomenti
- **Metodo** — 4 step del percorso
- **FAQ** — domande frequenti
- **Contatti** — form (submit via `mailto:`)

Sostituisci l'email `info@alessandrosimone.it` con la tua vera email in `index.html` se diversa.
