#!/usr/bin/env python3
"""Libreria condivisa per gli articoli «lettura facilitata» di alessandrosimone.it."""
import html, os, re

ASSET_V = 4   # aumentare quando cambiano css/lettura-facilitata.css o js/lettura-facilitata.js

KW = {'if','elif','else','for','while','in','def','return','and','or','not','True','False','None','import','from'}
FN = {'print','input','int','len','range','float','str'}
TOK = re.compile(r'(?P<c>#[^\n]*)|(?P<s>"[^"\n]*"|\'[^\'\n]*\')|(?P<n>\b\d+(?:\.\d+)?\b)|(?P<w>\b[A-Za-z_][A-Za-z_0-9]*\b)|(?P<o>.)')

def hl_line(line, lang):
    out = []
    if lang == 'json':
        for m in re.finditer(r'(?P<k>"[^"]*"(?=\s*:))|(?P<s>"[^"]*")|(?P<n>\b\d+(?:\.\d+)?\b)|(?P<b>\btrue\b|\bfalse\b)|(?P<o>.)', line):
            t = html.escape(m.group(0), quote=False)
            cls = {'k': 'p', 's': 's', 'n': 'n', 'b': 'k'}.get(m.lastgroup)
            out.append(f'<span class="{cls}">{t}</span>' if cls else t)
        return ''.join(out)
    for m in TOK.finditer(line):
        t = html.escape(m.group(0), quote=False)
        g = m.lastgroup
        if g == 'w':
            cls = 'k' if m.group(0) in KW else 'f' if m.group(0) in FN else None
        else:
            cls = {'c': 'c', 's': 's', 'n': 'n'}.get(g)
        out.append(f'<span class="{cls}">{t}</span>' if cls else t)
    return ''.join(out)

def code(src, lang='python', label=None, numbers=True):
    lines = src.strip('\n').split('\n')
    body = '\n'.join(f'<span class="l">{hl_line(l, lang)}</span>' for l in lines)
    cls = 'code-dsa' + ('' if numbers else ' no-ln')
    aria = f' role="figure" aria-label="{html.escape(label)}"' if label else ''
    return f'<pre class="{cls}"{aria}><code>{body}</code></pre>'

def plain(src):
    return '<pre class="code-plain"><code>' + html.escape(src.strip('\n'), quote=False) + '</code></pre>'

def mini(src):
    """Codice colorato senza numeri di riga, per la scheda della sintassi."""
    return code(src, numbers=False)


def faq(q, a):
    return f'''    <details class="dsa-faq">
      <summary>{q}<span aria-hidden="true">+</span></summary>
      <p>{a}</p>
    </details>'''

# ------------------------------------------------------------------ FAQ

def minutes(body, skip=('pre', 'svg', 'figure', 'nav', 'details')):
    prose = body
    for tag in skip:
        prose = re.sub(rf'<{tag}\b.*?</{tag}>', ' ', prose, flags=re.S)
    words = len(re.sub(r'<[^>]+>', ' ', prose).split())
    return words, max(1, round(words / 200))

CSS_TEXT = r'''    /* ---- Articolo pensato per lettori con DSA ---- */
    .article-dsa { --rt-scale: 1; padding: 28px 32px 36px; border-radius: 18px; transition: background .2s; }
    .article.article-dsa { max-width: 640px; }
    .article-dsa .back-link { color: #0f766e; font-weight: 600; font-size: 1rem; }
    .article-dsa .dsa-eyebrow { color: #0f766e; display: block; text-transform: none; letter-spacing: 0; font-size: 1rem; }
    .article-dsa .byline { color: #475569; }
    .article-dsa.dsa-bg { background: #fcf8ee; }
    .article-dsa .article-body :is(p, li) { font-size: calc(1.15rem * var(--rt-scale)); line-height: 1.8; letter-spacing: .012em; word-spacing: .06em; color: #1f2937; text-align: left; }
    .article-dsa .article-body h2 { font-size: calc(1.6rem * var(--rt-scale)); margin: 2.8rem 0 1rem; line-height: 1.3; scroll-margin-top: 90px; }
    .article-dsa .article-body h3 { font-size: calc(1.3rem * var(--rt-scale)); margin: 2rem 0 .7rem; color: #1e1b4b; line-height: 1.35; }
    .article-dsa.dsa-font,
    .article-dsa.dsa-font :is(h1, h2, h3, p, li, summary, figcaption, small, div, .eyebrow, .back-link) { font-family: 'Atkinson Hyperlegible', Verdana, Arial, sans-serif; }
    .article-dsa .article-body em { font-style: normal; }
    .article-dsa .article-body p a, .article-dsa .article-body li a { font-weight: 700; }
    .article-dsa .article-body :is(p, li, .step-card) code { font-family: 'JetBrains Mono', Consolas, monospace; font-size: .9em; background: #eef2ff; color: #3730a3; padding: .1em .35em; border-radius: 6px; }
    .article-dsa .cta-banner p { color: #fff; text-align: center; }
    .article-dsa .cta-banner h2 { margin-top: 0; }
    .article-dsa .hero-img { width: 100%; height: auto; border-radius: 16px; margin: 1.2rem 0 1rem; display: block; box-shadow: 0 6px 24px rgba(30,27,75,.12); }

    /* Barra strumenti di lettura */
    .reading-tools { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; background: #fff; border: 2px solid #e0e7ff; border-radius: 14px; padding: .7rem .8rem; margin: 1rem 0 1.4rem; }
    .reading-tools .rt-label { font-weight: 700; color: #1e1b4b; margin-right: .2rem; font-size: .95rem; }
    .rt-btn { font: 600 .95rem/1.2 'Atkinson Hyperlegible', Verdana, Arial, sans-serif; border: 2px solid #c7d2fe; background: #fff; color: #1e1b4b; padding: .5rem .8rem; border-radius: 10px; cursor: pointer; min-height: 44px; }
    .rt-btn:hover { background: #eef2ff; }
    .rt-btn:focus-visible { outline: 3px solid #1e1b4b; outline-offset: 2px; }
    .rt-player button:focus-visible { outline: 3px solid #f59e0b; outline-offset: 2px; }
    .rt-btn[aria-disabled="true"] { opacity: .45; cursor: not-allowed; }
    .rt-btn[aria-pressed="true"] { background: #4f46e5; border-color: #4f46e5; color: #fff; }
    .rt-btn.rt-listen { background: #0f766e; border-color: #0f766e; color: #fff; }
    .rt-btn.rt-listen:hover { background: #115e59; }
    .rt-note { font-size: .92rem; color: #475569; margin: -.6rem 0 1.4rem; }
    .rt-reading { background: #fef08a !important; box-shadow: 0 0 0 6px #fef08a; border-radius: 4px; }
    .rt-player { position: fixed; right: 16px; bottom: 16px; z-index: 1300; background: #1e1b4b; color: #fff; border-radius: 16px; padding: .7rem .8rem; display: flex; gap: .5rem; align-items: center; box-shadow: 0 10px 30px rgba(0,0,0,.25); font-family: 'Atkinson Hyperlegible', Verdana, Arial, sans-serif; }
    .rt-player[hidden] { display: none; }
    .rt-player .rp-label { font-weight: 700; margin-right: .3rem; }
    .rt-player button { font: 700 .95rem 'Atkinson Hyperlegible', Verdana, Arial, sans-serif; border: none; border-radius: 10px; padding: .5rem .8rem; cursor: pointer; min-height: 44px; }
    .rt-player .rp-pause { background: #fde047; color: #1e1b4b; }
    .rt-player .rp-stop { background: #fff; color: #1e1b4b; }

    /* Riquadri */
    .dsa-box { border: 2px solid; border-radius: 16px; padding: 1.1rem 1.3rem; margin: 1.6rem 0; }
    .dsa-box .box-title { font-size: calc(1.25rem * var(--rt-scale)) !important; margin: 0 0 .6rem !important; }
    .dsa-box ul, .dsa-box ol { margin: 0; padding-left: 1.3rem; }
    .dsa-box li { margin-bottom: .55rem; }
    .tldr { background: #eef2ff; border-color: #c7d2fe; }
    .toc { background: #fff; border-color: #e2e8f0; }
    .toc li { margin-bottom: .3rem; }
    .toc a { color: #4338ca; font-weight: 700; text-decoration: underline; text-underline-offset: 3px; }
    .glossary { background: #f0fdfa; border-color: #99f6e4; }
    .tip { background: #fffbeb; border-color: #fde68a; }
    .tip p { margin: 0; }
    .prompt-box { background: #f5f3ff; border: 2px dashed #a78bfa; border-radius: 14px; padding: 1rem 1.2rem; margin: 1rem 0 1.4rem; font-size: calc(1.1rem * var(--rt-scale)); line-height: 1.7; color: #3b0764; font-weight: 600; }

    /* Elenchi con icone */
    .icon-list, .dsa-types { list-style: none; padding-left: 0 !important; }
    .icon-list li, .dsa-types li { display: grid; grid-template-columns: 2.2rem 1fr; gap: .5rem; align-items: start; background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; padding: .75rem .9rem; margin-bottom: .6rem; }
    .dsa-types li { display: block; padding-left: 3.2rem; position: relative; }
    .dsa-types .t-ico { position: absolute; left: .9rem; top: .75rem; }
    .t-ico { font-size: 1.4rem; line-height: 1.5; }
    .steps-list { padding-left: 0; list-style: none; counter-reset: st; }
    .steps-list li { counter-increment: st; position: relative; padding: .8rem .9rem .8rem 3.6rem; background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; margin-bottom: .6rem; }
    .steps-list li::before { content: counter(st); position: absolute; left: .8rem; top: .75rem; width: 2rem; height: 2rem; border-radius: 50%; background: #4f46e5; color: #fff; font-weight: 700; display: grid; place-items: center; font-size: 1rem; }
    .step-card { display: grid; grid-template-columns: 2.6rem 1fr; gap: .8rem; align-items: start; background: #fff; border: 2px solid #e0e7ff; border-radius: 14px; padding: .9rem 1rem; margin: 1.2rem 0 .8rem; font-size: calc(1.15rem * var(--rt-scale)); line-height: 1.75; color: #1f2937; }
    .step-n { width: 2.4rem; height: 2.4rem; border-radius: 50%; background: #0f766e; color: #fff; font-weight: 800; display: grid; place-items: center; font-size: 1.15rem; }

    /* Codice */
    .article-dsa pre.code-dsa { background: #1e293b; color: #e5e7eb; font-family: 'JetBrains Mono', Consolas, monospace; font-size: calc(1rem * var(--rt-scale)); line-height: 1.75; padding: 1rem 1.1rem 1rem .6rem; border-radius: 12px; counter-reset: ln; overflow-x: auto; margin: .6rem 0 1.4rem; }
    .article-dsa pre.code-dsa code, .article-dsa pre.code-plain code { font-family: inherit; font-size: inherit; background: none; color: inherit; padding: 0; }
    .article-dsa :is(pre, code, .gc-code span) { font-variant-ligatures: none; font-feature-settings: "calt" 0, "liga" 0; }
    .code-dsa .l::before { counter-increment: ln; content: counter(ln); display: inline-block; width: 2em; margin-right: 1em; text-align: right; color: #94a3b8; user-select: none; -webkit-user-select: none; }
    .code-dsa.no-ln { padding-left: 1.1rem; }
    .code-dsa.no-ln .l::before { display: none; }
    .code-dsa .k { color: #c4b5fd; font-weight: 600; } .code-dsa .f { color: #7dd3fc; } .code-dsa .s { color: #86efac; }
    .code-dsa .n { color: #fdba74; } .code-dsa .c { color: #94a3b8; } .code-dsa .p { color: #93c5fd; }
    .article-dsa pre.code-plain { background: #fff; color: #111827; border: 2px solid #d1d5db; font-family: 'JetBrains Mono', Consolas, monospace; font-size: calc(1rem * var(--rt-scale)); line-height: 1.75; padding: 1rem 1.1rem; border-radius: 12px; overflow-x: auto; margin: .6rem 0 1.4rem; }
    .error-box mark { padding: .05em .25em; border-radius: 4px; }
    .error-box .em-line { background: #fde047; color: #1e1b4b; }
    .error-box .em-err { background: #fecaca; color: #7f1d1d; font-weight: 700; }

    /* Figure */
    .dsa-figure { margin: 1.8rem 0; }
    .dsa-figure figcaption { font-size: calc(.98rem * var(--rt-scale)); color: #475569; margin-top: .6rem; line-height: 1.6; text-align: left; }
    .dsa-svg { width: 100%; height: auto; display: block; margin: 0 auto; }
    .two-col { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 1rem; }
    .two-col pre { margin: 0 !important; height: calc(100% - 2rem); }
    .panel-title { font-weight: 700; color: #1e1b4b; margin-bottom: .4rem; font-size: 1rem; }
    .glyph-compare { background: #fff; border: 2px solid #e5e7eb; border-radius: 16px; padding: 1rem; display: grid; gap: .9rem; }
    .gc-title { font-weight: 700; color: #1e1b4b; margin-bottom: .4rem; }
    .gc-cells { display: grid; grid-template-columns: repeat(3, 1fr); gap: .6rem; }
    .gc-cells > div { background: #f8fafc; border-radius: 12px; padding: .6rem .4rem; text-align: center; }
    .gc-cells span { display: block; font-size: 2.2rem; line-height: 1.3; color: #111827; }
    .gc-cells small { display: block; font-size: calc(.95rem * var(--rt-scale)); color: #475569; line-height: 1.3; }
    .gc-common span { font-family: Arial, 'Liberation Sans', Helvetica, sans-serif; }
    .gc-code span { font-family: 'JetBrains Mono', Consolas, monospace; }
    .syntax-card { background: #fff; border: 3px solid #4f46e5; border-radius: 18px; overflow: hidden; }
    .sc-head { background: #4f46e5; color: #fff; font-weight: 800; font-size: 1.15rem; padding: .7rem 1rem; }
    .sc-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .8rem; padding: 1rem; }
    .sc-item { background: #f8fafc; border-radius: 12px; padding: .6rem .7rem; }
    .sc-t { font-weight: 700; color: #1e1b4b; margin-bottom: .35rem; }
    .sc-item pre.code-dsa { margin: 0 !important; font-size: calc(.92rem * var(--rt-scale)); }
    .sc-foot { background: #fffbeb; border-top: 2px solid #fde68a; padding: .7rem 1rem; color: #1f2937; line-height: 1.6; }

    /* PDP, FAQ, leggi anche */
    .pdp-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 1rem; }
    .pdp-col { background: #fff; border-color: #e0e7ff; margin: 0; }
    .pdp-col h3 { margin-top: .2rem !important; }
    .pdp-wide { margin-top: 1rem; }
    .norme { font-size: calc(.98rem * var(--rt-scale)) !important; color: #475569 !important; }
    .dsa-faq { border-bottom: 1px solid #e3e7ee; padding: 14px 0; }
    .dsa-faq summary { cursor: pointer; font-weight: 700; color: #1e1b4b; font-size: calc(1.1rem * var(--rt-scale)); list-style: none; display: flex; justify-content: space-between; align-items: center; gap: 1rem; }
    .dsa-faq summary::-webkit-details-marker { display: none; }
    .dsa-faq summary span { font-size: 1.5rem; font-weight: 400; }
    .dsa-faq[open] summary span { transform: rotate(45deg); }
    .dsa-faq p { margin: .7rem 0 0; }
    .read-next { margin-top: 2.4rem; }
    .rn-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .8rem; }
    .rn-grid a { display: flex; flex-direction: column; gap: .4rem; background: #fff; border: 2px solid #e0e7ff; border-radius: 14px; padding: 1rem; color: #1e1b4b; text-decoration: none; line-height: 1.45; }
    .rn-grid a:hover { border-color: #4f46e5; }
    .rn-grid span { font-size: 1.6rem; }

    .sc-t, .sc-foot, .panel-title, .gc-title, .rn-grid a { font-size: calc(1rem * var(--rt-scale)); }
    .sc-head { font-size: calc(1.15rem * var(--rt-scale)); }
    .article-dsa.dsa-bg :is(.toc, .icon-list li, .dsa-types li, .steps-list li, .step-card, .pdp-col, .rn-grid a, .glyph-compare, .syntax-card, .reading-tools) { background: #fffaf0; }
    .article-dsa .article-body :is(p, li) a:hover { color: #3730a3; text-decoration-thickness: 2px; }
    .article-dsa .cta-banner .btn-accent { color: #1a1a1a; }
    .tip ul { margin-top: .5rem; }
    .vscode-box { margin: .4rem 0 1.4rem; border-top: 1px solid #e3e7ee; }
    .vscode-box > p:first-of-type { margin-top: .8rem; }
    .map-list { display: none; }
    @media (max-width: 760px) {
      .map-svg { display: none; }
      .map-list { display: block; }
      .article-dsa { padding: 18px 14px 26px; border-radius: 14px; }
      .two-col, .pdp-grid, .rn-grid, .sc-grid { grid-template-columns: minmax(0, 1fr); }
      .gc-cells span { font-size: 1.7rem; }
      .rt-player { left: 12px; right: 12px; justify-content: center; flex-wrap: wrap; }
    }
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
    /* ---- Gruppi di BES: un colore per gruppo, sempre insieme a icona e testo ---- */
    .g1 { --g: #6d28d9; --g-bg: #f5f3ff; --g-bd: #c4b5fd; }
    .g2 { --g: #0f766e; --g-bg: #f0fdfa; --g-bd: #99f6e4; }
    .g3 { --g: #c2410c; --g-bg: #fff7ed; --g-bd: #fdba74; }
    .umbrella { display: block; width: 100%; max-width: 420px; height: auto; margin: 0 auto .2rem; }
    .group-cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .8rem; }
    .g-card { background: var(--g-bg); border: 2px solid var(--g-bd); border-top: 6px solid var(--g); border-radius: 14px; padding: .8rem .9rem; }
    .g-card .g-ico { font-size: 1.8rem; display: block; line-height: 1.2; }
    .g-card .g-num { display: block; font-weight: 800; color: var(--g); font-size: calc(.95rem * var(--rt-scale)); margin-top: .2rem; }
    .g-card .g-name { display: block; font-weight: 700; color: #1f2937; font-size: calc(1.02rem * var(--rt-scale)); line-height: 1.35; margin: .3rem 0 .5rem; }
    .g-card .g-doc { display: inline-block; background: #fff; border: 1px solid var(--g-bd); color: var(--g); font-weight: 700; border-radius: 999px; padding: .1rem .6rem; font-size: calc(1rem * var(--rt-scale)); }
    .group-box { background: var(--g-bg); border: 2px solid var(--g-bd); border-left: 8px solid var(--g); border-radius: 16px; padding: .3rem 1.2rem .5rem; margin: 1.2rem 0; }
    .article-dsa .article-body .group-box h3 { margin-top: .9rem; color: var(--g); }
    .article-dsa .article-body .note-dir { font-size: calc(1rem * var(--rt-scale)); color: #374151; border-top: 1px dashed var(--g-bd); padding-top: .7rem; }
    .cmp-table { width: 100%; border-collapse: separate; border-spacing: 0; background: #fff; border: 2px solid #e5e7eb; border-radius: 14px; overflow: hidden; font-size: calc(1rem * var(--rt-scale)); line-height: 1.5; }
    .cmp-table th, .cmp-table td { padding: .7rem .8rem; text-align: left; vertical-align: top; border-bottom: 1px solid #e5e7eb; color: #1f2937; }
    .cmp-table thead th { color: #fff; font-weight: 700; background: #1e1b4b; }
    .cmp-table thead th.g1, .cmp-table thead th.g2, .cmp-table thead th.g3 { background: var(--g); }
    .cmp-table tbody th { background: #f8fafc; font-weight: 700; width: 24%; color: #1e1b4b; }
    .cmp-table tbody tr:last-child > * { border-bottom: none; }
    .cmp-cards { display: none; }
    .cmp-card { background: var(--g-bg); border: 2px solid var(--g-bd); border-top: 6px solid var(--g); border-radius: 14px; padding: .8rem 1rem; }
    .cmp-card .cc-title { font-weight: 800; color: var(--g); font-size: calc(1.15rem * var(--rt-scale)); }
    .cmp-card dl { margin: 0; }
    .cmp-card dt { font-weight: 700; color: #1e1b4b; margin-top: .55rem; }
    .cmp-card dd { margin: 0; color: #1f2937; line-height: 1.6; }
    .cmp-card :is(dt, dd) { font-size: calc(1.02rem * var(--rt-scale)); }
    .sigle-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .7rem; }
    .sigla { background: #fff; border: 2px solid #e0e7ff; border-radius: 14px; padding: .7rem .9rem; }
    .sigla b { display: block; font-size: calc(1.35rem * var(--rt-scale)); color: #3730a3; letter-spacing: .02em; }
    .sigla span { display: block; color: #1f2937; line-height: 1.55; font-size: calc(1rem * var(--rt-scale)); }
    .myth { border: 2px solid #e5e7eb; border-radius: 14px; overflow: hidden; margin: .9rem 0; background: #fff; }
    .article-dsa .article-body .myth p { margin: 0; padding: .7rem 1rem; }
    .article-dsa .article-body .myth .m-false { background: #fef2f2; color: #7f1d1d; font-weight: 700; }
    .path-grid { display: grid; grid-template-columns: minmax(0, 1fr); gap: .9rem; }
    .path-col { background: var(--g-bg); border: 2px solid var(--g-bd); border-radius: 14px; padding: .8rem; }
    .path-col .pc-title { font-weight: 800; color: var(--g); margin-bottom: .6rem; font-size: calc(1.1rem * var(--rt-scale)); }
    .path-col ol { list-style: none; padding: 0 !important; margin: 0; counter-reset: pst; }
    .article-dsa .article-body .path-col li { counter-increment: pst; background: #fff; border: 1px solid var(--g-bd); border-radius: 10px; padding: .55rem .7rem .55rem 2.5rem; position: relative; margin: 0 0 1.5rem; font-size: calc(1rem * var(--rt-scale)); line-height: 1.5; }
    .path-col li::before { content: counter(pst); position: absolute; left: .55rem; top: .55rem; width: 1.7rem; height: 1.7rem; border-radius: 50%; background: var(--g); color: #fff; font-weight: 700; display: grid; place-items: center; font-size: 1rem; }
    .path-col li:not(:last-child)::after { content: "↓"; content: "↓" / ""; position: absolute; left: 50%; bottom: -1.4rem; transform: translateX(-50%); color: var(--g); font-weight: 800; font-size: 1.2rem; line-height: 1; }
    .article-dsa .article-body .path-col li:last-child { margin-bottom: 0; }
    .article-dsa.dsa-bg :is(.cmp-table, .sigla, .myth, .path-col li) { background: #fffaf0; }
    .article-dsa.dsa-bg .cmp-table tbody th { background: #f8f1e3; }
    @media (max-width: 760px) {
      .group-cards, .sigle-grid { grid-template-columns: minmax(0, 1fr); }
      .cmp-table { display: none; }
      .cmp-cards { display: grid; gap: .8rem; }
    }
    .article-dsa.rt-big .cmp-table { display: none; }
    .article-dsa.rt-big .cmp-cards { display: grid; gap: .8rem; }
    @media (prefers-reduced-motion: reduce) { .article-dsa { transition: none; } }
    /* ---- Articolo PEI: avviso di aggiornamento e tre percorsi (colori neutri, non quelli dei gruppi) ---- */
    .update-box { background: #fefce8; border-color: #facc15; }
    .update-box p { margin: 0 0 .5rem; }
    .update-box p:last-child { margin-bottom: 0; }
    .perc-grid { display: grid; gap: .8rem; margin: 1.2rem 0; }
    .perc { display: grid; grid-template-columns: 2.8rem minmax(0, 1fr); gap: .8rem; align-items: start; background: #fff; border: 2px solid #c7d2fe; border-radius: 14px; padding: .9rem 1rem; }
    .perc-l { width: 2.6rem; height: 2.6rem; border-radius: 12px; background: #1e1b4b; color: #fff; font-weight: 800; display: grid; place-items: center; font-size: 1.3rem; }
    .perc .perc-t { font-weight: 800; color: #1e1b4b; font-size: calc(1.12rem * var(--rt-scale)); margin-bottom: .2rem; }
    .article-dsa .article-body .perc p { margin: .2rem 0 .4rem; }
    .perc .perc-out { display: inline-block; background: #eef2ff; border: 1px solid #c7d2fe; color: #3730a3; font-weight: 700; border-radius: 999px; padding: .1rem .7rem; font-size: calc(1rem * var(--rt-scale)); }
    .article-dsa.dsa-bg .perc { background: #fffaf0; }
    .t-let { width: 1.9rem; height: 1.9rem; margin-top: .2rem; border-radius: 8px; background: #1e1b4b; color: #fff; font-weight: 800; font-size: 1.05rem; display: grid; place-items: center; line-height: 1; }
  '''

JS_TEXT = r'''/* Strumenti di lettura: carattere, sfondo, dimensione e sintesi vocale */
(function () {
  var art = document.querySelector('.article-dsa');
  if (!art) return;
  var KEY = 'as-dsa-lettura', MIN = 0.9, MAX = 1.5;
  var st = { font: true, bg: true, scale: 1 };
  try { var sv = JSON.parse(localStorage.getItem(KEY) || 'null'); if (sv) { for (var k in st) if (k in sv) st[k] = sv[k]; } } catch (e) {}
  function save() { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {} }
  var $ = function (id) { return document.getElementById(id); };
  function apply() {
    art.classList.toggle('dsa-font', !!st.font);
    art.classList.toggle('dsa-bg', !!st.bg);
    art.style.setProperty('--rt-scale', st.scale);
    art.classList.toggle('rt-big', st.scale > 1.05);
    $('rt-font').setAttribute('aria-pressed', st.font ? 'true' : 'false');
    $('rt-bg').setAttribute('aria-pressed', st.bg ? 'true' : 'false');
    $('rt-bigger').setAttribute('aria-disabled', st.scale >= MAX ? 'true' : 'false');
    $('rt-smaller').setAttribute('aria-disabled', st.scale <= MIN ? 'true' : 'false');
  }
  apply();
  $('rt-font').addEventListener('click', function () { st.font = !st.font; apply(); save(); });
  $('rt-bg').addEventListener('click', function () { st.bg = !st.bg; apply(); save(); });
  $('rt-bigger').addEventListener('click', function () { st.scale = Math.min(MAX, Math.round((st.scale + 0.1) * 10) / 10); apply(); save(); });
  $('rt-smaller').addEventListener('click', function () { st.scale = Math.max(MIN, Math.round((st.scale - 0.1) * 10) / 10); apply(); save(); });

  /* ---- Sintesi vocale ---- */
  var synth = window.speechSynthesis;
  var bListen = $('rt-listen'), player = $('rt-player'), bPause = $('rp-pause'), bStop = $('rp-stop');
  if (!synth || typeof SpeechSynthesisUtterance === 'undefined') { bListen.hidden = true; return; }
  try { synth.cancel(); } catch (e) {}
  var queue = [], idx = 0, current = null, playing = false, gen = 0, voice = null, fails = 0;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var EMOJI = /\p{Extended_Pictographic}|[\u{FE0F}\u{200D}\u{20E3}]/gu;

  function clean(t) { return t.replace(EMOJI, '').replace(/\s*→\s*/g, ', ').replace(/\s*·\s*/g, ', ').replace(/\s+/g, ' ').trim(); }
  /* frasi brevi: alcune voci online si interrompono sui testi lunghi */
  function push(el, t) {
    var parts = [], buf = '';
    (t.match(/[^.!?;:]+[.!?;:]*\s*/g) || [t]).forEach(function (p) {
      if (p.length <= 160) parts.push(p); else parts.push.apply(parts, p.match(/[^,]+,?\s*/g) || [p]);
    });
    parts.forEach(function (p) {
      if (buf && (buf + p).length > 160) { queue.push({ el: el, text: buf.trim() }); buf = ''; }
      buf += p;
    });
    if (buf.trim()) queue.push({ el: el, text: buf.trim() });
  }
  function build() {
    queue = [];
    art.querySelectorAll('h1, .article-body h2, .article-body h3, .article-body p, .article-body li, .article-body figcaption, .article-body .step-card > div, .article-body .prompt-box, .article-body .dsa-faq summary, .article-body pre[aria-label], .article-body .pc-title, .article-body .sigla, .article-body .cmp-table tbody tr, .article-body .cmp-card').forEach(function (el) {
      var isPre = el.matches('pre');
      if (el.closest('.rt-skip, .reading-tools, .syntax-card')) return;
      if (!isPre && el.closest('pre')) return;
      if (el.matches('li') && el.closest('.toc')) return;
      if (el.matches('.cmp-table tr, .cmp-card') && !el.getClientRects().length) return;  /* solo la versione visibile */
      var t;
      if (isPre) {
        t = 'Riquadro di codice: ' + el.getAttribute('aria-label') + '.';
      } else if (el.matches('.sigla')) {
        t = clean(el.querySelector('b').textContent) + ': ' + clean(el.querySelector('span').textContent);
      } else if (el.matches('.cmp-table tr')) {
        var hs = el.closest('table').tHead.rows[0].cells;
        t = Array.prototype.map.call(el.cells, function (c, i) { return i ? clean(hs[i].textContent) + ': ' + clean(c.textContent) : clean(c.textContent).replace(/\?$/, ''); }).join('. ') + '.';
      } else if (el.matches('.cmp-card')) {
        t = clean(el.querySelector('.cc-title').textContent) + '. ' + Array.prototype.map.call(el.querySelectorAll('dt'), function (dt) { return clean(dt.textContent).replace(/\?$/, '') + ': ' + clean(dt.nextElementSibling.textContent); }).join('. ') + '.';
      } else {
        t = clean(el.innerText || el.textContent);
        if (el.matches('.pc-title')) t = (/^Percorso/i.test(t) ? t : 'Percorso: ' + t) + '.';
        if (el.matches('.path-col li')) t = 'Passo ' + (Array.prototype.indexOf.call(el.parentNode.children, el) + 1) + '. ' + t + '.';
        if (el.matches('summary')) t = t.replace(/\s*\+$/, '');
        if (el.matches('.steps-list > li')) t = 'Strategia ' + (Array.prototype.indexOf.call(el.parentNode.children, el) + 1) + '. ' + t;
        if (el.matches('.step-card > div')) t = 'Passo ' + el.parentNode.querySelector('.step-n').textContent + '. ' + t;
      }
      if (t) push(el, t);
    });
  }
  function itVoice() {
    var v = synth.getVoices().filter(function (x) { return /^it/i.test(x.lang); });
    return v.filter(function (x) { return /Google|Natural|Online|Neural/i.test(x.name); })[0] || v[0] || null;
  }
  /* la voce si sceglie prima di iniziare e non cambia durante la lettura */
  function pickVoice() { if (!playing) voice = itVoice() || voice; }
  pickVoice();
  if (synth.addEventListener) synth.addEventListener('voiceschanged', pickVoice);
  function mark(el) {
    if (current && current !== el) current.classList.remove('rt-reading');
    current = el;
    if (!el) return;
    var d = el.closest('details'); if (d && !d.open) d.open = true;
    el.classList.add('rt-reading');
    var r = el.getBoundingClientRect();
    if (r.top < 90 || r.bottom > window.innerHeight - 110) el.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' });
  }
  /* il lettore audio non deve finire sotto il banner dei cookie */
  function placePlayer() {
    var cb = document.getElementById('as-cookie-banner');
    var off = (cb && cb.parentNode && cb.style.opacity !== '0') ? cb.offsetHeight : 0;
    player.style.bottom = (16 + off) + 'px';
  }
  if (window.MutationObserver) new MutationObserver(placePlayer).observe(document.body, { childList: true });
  window.addEventListener('resize', placePlayer);
  function ui() {
    placePlayer();
    player.hidden = !(playing || idx > 0);
    player.querySelector('.rp-state').textContent = playing ? 'In ascolto' : 'In pausa';
    bPause.innerHTML = playing ? '<span aria-hidden="true">⏸</span> Pausa' : '<span aria-hidden="true">▶</span> Riprendi';
    bListen.innerHTML = playing ? '<span aria-hidden="true">⏸</span> Metti in pausa'
      : (idx > 0 ? '<span aria-hidden="true">▶</span> Riprendi l\'ascolto' : '<span aria-hidden="true">🔊</span> Ascolta l\'articolo');
  }
  function speakNext() {
    if (!playing) return;
    if (idx >= queue.length) { stop(); return; }
    var item = queue[idx], my = gen, done = false;
    mark(item.el);
    var u = new SpeechSynthesisUtterance(item.text);
    u.lang = 'it-IT'; u.rate = 0.95;
    if (voice) u.voice = voice;
    function next(ok) {
      if (done || my !== gen || !playing) return;
      done = true;
      fails = ok ? 0 : fails + 1;
      if (fails >= 3) { stop(); bListen.innerHTML = '<span aria-hidden="true">🔊</span> Sintesi vocale non disponibile'; return; }
      idx++; speakNext();
    }
    u.onend = function () { next(true); };
    u.onerror = function (e) { if (e.error === 'interrupted' || e.error === 'canceled') return; next(false); };
    synth.speak(u);
  }
  function play() { if (!queue.length || idx >= queue.length) { build(); idx = 0; } voice = voice || itVoice(); fails = 0; gen++; playing = true; ui(); speakNext(); }
  function pause() { gen++; playing = false; try { synth.cancel(); } catch (e) {} ui(); }
  function stop() {
    gen++; playing = false; try { synth.cancel(); } catch (e) {}
    idx = 0; mark(null);
    if (player.contains(document.activeElement)) bListen.focus();
    ui();
  }
  bListen.addEventListener('click', function () { playing ? pause() : play(); });
  bPause.addEventListener('click', function () { playing ? pause() : play(); });
  bStop.addEventListener('click', stop);
  window.addEventListener('pagehide', function () { if (playing) pause(); else { try { synth.cancel(); } catch (e) {} } });
  document.addEventListener('click', function (e) { if (e.target && /^as-(accept|reject)$/.test(e.target.id)) setTimeout(placePlayer, 350); });
})();'''

def write_shared(root):
    with open(os.path.join(root, 'css', 'lettura-facilitata.css'), 'w', encoding='utf-8') as f:
        f.write('/* Articoli a lettura facilitata (DSA/BES): tipografia, riquadri, figure e strumenti di lettura */\n' + CSS_TEXT.replace('\n    ', '\n') .lstrip() + '\n')
    with open(os.path.join(root, 'js', 'lettura-facilitata.js'), 'w', encoding='utf-8') as f:
        f.write(JS_TEXT.strip() + '\n')

def page(m):
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-9X6ETTP6Y0"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-9X6ETTP6Y0');
  </script>
  <meta charset="UTF-8">
  <meta http-equiv="Cache-Control" content="no-cache, must-revalidate">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{m["seo_title"]}</title>
  <meta name="description" content="{m["desc"]}">
  <meta name="keywords" content="{m["keywords"]}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&family=Poppins:wght@700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v=10">
  <link rel="stylesheet" href="css/lettura-facilitata.css?v={ASSET_V}">
  <link rel="canonical" href="{m["url"]}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <meta name="theme-color" content="#4f46e5">
  <meta property="og:locale" content="it_IT">
  <meta property="og:site_name" content="AlessandroSimone.it">
  <meta property="og:url" content="{m["url"]}">
  <meta property="og:title" content="{m["title"]}">
  <meta property="og:description" content="{m["desc"]}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="{m["img"]}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{m["og_alt"]}">
  <meta property="article:published_time" content="{m["date_iso"]}">
  <meta property="article:section" content="Inclusione">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{m["title"]}">
  <meta name="twitter:description" content="{m["desc"]}">
  <meta name="twitter:image" content="{m["img"]}">
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{m["title"]}",
  "description": "{m["desc"]}",
  "image": "{m["img"]}",
  "inLanguage": "it-IT",
  "url": "{m["url"]}",
  "datePublished": "{m["date_iso"]}",
  "dateModified": "{m.get("modified_iso", m["date_iso"])}",
  "articleSection": "Inclusione",
  "keywords": "{m["ld_keywords"]}",
  "author": {{
    "@type": "Person",
    "name": "Alessandro Simone",
    "jobTitle": "Docente di Inclusione e di Informatica",
    "url": "https://alessandrosimone.it"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "AlessandroSimone.it",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://alessandrosimone.it/favicon.svg"
    }}
  }},
  "mainEntityOfPage": "{m["url"]}"
}}
  </script>
</head>
<body>

<header class="site-header">
  <div class="container nav-inner">
    <a href="/" class="brand"><img src="logo-alessandro-simone-trasparente.png" alt="Logo Alessandro Simone - informatica e inclusione a scuola" class="brand-logo"><span class="brand-name">Alessandro<span class="brand-accent">Simone</span>.it</span></a>
    <button class="nav-toggle" aria-label="Apri menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav-menu">
      <a href="/">Home</a>
      <a href="lezioni.html">Lezioni gratuite</a>
      <a href="blog.html">Blog</a>
      <a href="contatti.html">Contatti</a>
    </nav>
  </div>
</header>

<section class="section">
  <article class="container article article-dsa dsa-font dsa-bg">
    <a href="blog.html" class="back-link">← Torna al blog</a>
    <span class="eyebrow mt-2 dsa-eyebrow">Inclusione · {m["minutes"]} min di lettura (o da ascoltare)</span>
    <h1>{m["title"]}</h1>
    <p class="byline">{m["date_it"]} — di Alessandro Simone, docente di inclusione e di informatica</p>

    <img class="hero-img" src="{m["hero_src"]}" width="1200" height="630" alt="{m["hero_alt"]}">

    <div class="reading-tools" role="group" aria-label="Strumenti di lettura">
      <span class="rt-label">Leggi come preferisci:</span>
      <button type="button" class="rt-btn rt-listen" id="rt-listen"><span aria-hidden="true">🔊</span> Ascolta l'articolo</button>
      <button type="button" class="rt-btn" id="rt-smaller" aria-label="Riduci il testo">A−</button>
      <button type="button" class="rt-btn" id="rt-bigger" aria-label="Ingrandisci il testo">A+</button>
      <button type="button" class="rt-btn" id="rt-font" aria-pressed="true"><span aria-hidden="true">🔤</span> Carattere leggibile</button>
      <button type="button" class="rt-btn" id="rt-bg" aria-pressed="true"><span aria-hidden="true">🟨</span> Sfondo crema</button>
    </div>
    <p class="rt-note">Questa pagina è pensata per essere letta con meno fatica: puoi ascoltarla, ingrandire il testo e scegliere carattere e sfondo. Le tue scelte restano salvate su questo dispositivo.</p>

    <div class="article-body">
{m["body"]}
    </div>
  </article>
</section>

<div class="rt-player" id="rt-player" hidden role="region" aria-label="Controlli di ascolto">
  <span class="rp-label"><span aria-hidden="true">🔊</span> <span class="rp-state">In ascolto</span></span>
  <button type="button" class="rp-pause" id="rp-pause"><span aria-hidden="true">⏸</span> Pausa</button>
  <button type="button" class="rp-stop" id="rp-stop"><span aria-hidden="true">⏹</span> Ferma</button>
</div>

<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <div class="footer-brand"><img src="logo-alessandro-simone-bianco.png" alt="Logo Alessandro Simone" class="footer-logo"><span class="brand-name">Alessandro<span class="brand-accent">Simone</span>.it</span></div>
      <p class="mt-1" style="font-size:.9rem">Docente di informatica felicemente prestato all'inclusione nella scuola secondaria di II grado a Roma. Lezioni, guide e materiali gratuiti.</p>
    </div>
    <div><h4>Naviga</h4><a href="/#chi-sono">Chi sono</a><a href="lezioni.html">Lezioni gratuite</a><a href="blog.html">Blog</a></div>
    <div><h4>Contatti</h4><a href="mailto:alessandrosimone.it@gmail.com">alessandrosimone.it@gmail.com</a><a href="contatti.html">Contattami</a></div>
  </div>
  <div class="footer-bottom">© <span id="year"></span> AlessandroSimone.it — Tutti i diritti riservati &nbsp;·&nbsp; <a href="cookie-policy.html" style="color:rgba(255,255,255,.5)">Cookie Policy</a></div>
</footer>
<script src="js/lettura-facilitata.js?v={ASSET_V}"></script>
<script src="js/main.js?v=10"></script>
<script src="js/search.js"></script>
<script src="js/cookie-consent.js"></script>
</body>
</html>
'''
