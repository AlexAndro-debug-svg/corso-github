#!/usr/bin/env python3
"""Controllo statico di tutte le pagine: script interni (node --check) e blocchi degli esempi che finiscono nel punto giusto.
Uso, dalla radice del sito: python3 _strumenti/controllo_statico.py"""
import re,glob,os,subprocess,collections,sys
import tempfile
S=sys.argv[1] if len(sys.argv)>1 else tempfile.mkdtemp()
os.makedirs(os.path.join(S,'js'),exist_ok=True)
OPEN=re.compile(r'<script\b([^>]*)>',re.I)
CLOSE=re.compile(r'</script[\s/>]',re.I)
after=collections.Counter(); problems=[]
jsfiles=[]
for f in sorted(glob.glob('*.html')):
    s=open(f,encoding='utf-8').read()
    if 'http-equiv="refresh"' in s: continue
    pos=0
    while True:
        m=OPEN.search(s,pos)
        if not m: break
        attrs=m.group(1); c=CLOSE.search(s,m.end())
        if not c: problems.append((f,'script senza chiusura',s.count('\n',0,m.start())+1)); break
        body=s[m.end():c.start()]; ln=s.count('\n',0,m.start())+1
        typ=re.search(r'type\s*=\s*["\']([^"\']+)',attrs)
        typ=typ.group(1).lower() if typ else ''
        if 'class="code"' in attrs or "class='code'" in attrs:
            tail=s[c.end()-1:c.end()+40]
            nxt=re.match(r'>\s*(<[^>]{0,12})',tail)
            key=nxt.group(1) if nxt else repr(tail[:20])
            after[key]+=1
            if not (nxt and re.match(r'</(div|pre|details|section|article|li|td)\b',nxt.group(1))):
                problems.append((f,'blocco esempio finisce in un punto strano',ln,repr(s[c.start()-60:c.end()+60])))
        elif 'src=' not in attrs and typ in('','text/javascript','module','application/javascript'):
            p=os.path.join(S,'js',f'{f}.{ln}.js'); open(p,'w',encoding='utf-8').write(body); jsfiles.append((f,ln,p,typ))
        pos=c.end()
print('Cosa segue la fine dei blocchi esempio:',dict(after.most_common(12)))
bad=0
for f,ln,p,typ in jsfiles:
    args=['node','--check',p] if typ!='module' else ['node','--input-type=module','--check']
    r=subprocess.run(['node','--check',p],capture_output=True,text=True)
    if r.returncode: bad+=1; problems.append((f,'errore di sintassi JS nello script interno',ln,r.stderr.strip().splitlines()[-1] if r.stderr else ''))
print('Script interni controllati:',len(jsfiles),'con errori:',bad)
for p in problems: print('PROBLEMA',*p)
print('Totale problemi:',len(problems))
