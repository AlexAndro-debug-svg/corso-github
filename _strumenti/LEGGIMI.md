# Strumenti di lavoro del sito (non pubblicati)

Questa cartella inizia con `_`, quindi GitHub Pages non la pubblica.
Il contesto completo del sito è in `.claude/CLAUDE.md`.

| File | A cosa serve |
|---|---|
| `articoli/artlib.py` | Funzioni comuni degli articoli a lettura facilitata: codice colorato, domande frequenti, CSS e JS condivisi, modello di pagina |
| `articoli/build_dsa.py`, `articoli/build_bes.py` | Testo e figure dei due articoli della serie. Uso: `python3 _strumenti/articoli/build_bes.py .` dalla radice del sito |
| `copertine/*.html` + `genera_copertina.js` | Copertine 1200×630: `node _strumenti/genera_copertina.js _strumenti/copertine/copertina-XXX.html articolo-XXX.jpg` |
| `controllo_statico.py` | Controlla gli script interni e gli esempi «Provalo tu» di tutte le pagine |
| `audit.js` + `fontroute.js` | Prova nel browser di tutte le pagine, con clic su ogni «Provalo tu» |
| `test_lettura.js` | Prova degli strumenti di lettura facilitata di un articolo |

Prima volta: `cd _strumenti && npm install`.
