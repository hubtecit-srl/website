# -*- coding: utf-8 -*-
import json, urllib.parse
DATE='2026-07-30'
BASE='https://hubtecit-srl.github.io/website/'
msg=("Buongiorno,\n"
"Sono Laura di HubTec, azienda di Verona.\n\n"
"Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
"Se vi piace, lo attiviamo con soli 200€.\n\n"
"In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
"Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
"Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n"
"Laura Borin - HubTec")
def wa(num, url):
    t=urllib.parse.quote(msg.format(url=url), safe='')
    return 'https://wa.me/39'+num+'?text='+t

leads=[
 dict(name='Estetica Nynfea di Sabrina Zanini', num='3406707816', tel='340 670 7816',
      slug='estetica-nynfea-colognola-ai-colli.html'),
 dict(name='Beauty Point di Dal Forno Michela', num='3663770444', tel='366 377 0444',
      slug='beauty-point-colognola-ai-colli.html'),
]
for l in leads:
    l['url']=BASE+l['slug']
    l['wa']=wa(l['num'], l['url'])

# whatsapp-queue.csv append (dedup by name)
qf='whatsapp-queue.csv'
q=open(qf,encoding='utf-8').read()
added=[]
for l in leads:
    if l['name'] in q:
        continue
    line='{n};{t};{w};{s};{c};{d}'.format(n=l['name'],t=l['tel'],w=l['wa'],s=l['url'],c='Colognola ai Colli',d=DATE)
    if not q.endswith('\n'): q+='\n'
    q+=line+'\n'
    added.append(l['name'])
open(qf,'w',encoding='utf-8').write(q)
print('WA queue added:', added)

# progress.json advance estetiste(0) -> parrucchieri(1), same comune 16
p=json.load(open('progress.json'))
p['comuneIndex']=16
p['categoryIndex']=1
json.dump(p, open('progress.json','w'), ensure_ascii=False, indent=2)
print('progress ->', p['comuneIndex'], p['categoryIndex'])

# index.html add section
idx=open('index.html',encoding='utf-8').read()
sec='<h2>Nuovi siti — Colognola ai Colli (2026-07-30 · estetiste)</h2>\n<ul>\n'
for l in leads:
    label={'estetica-nynfea-colognola-ai-colli.html':'Estetica Nynfea di Sabrina Zanini — Centro estetico — Colognola ai Colli',
           'beauty-point-colognola-ai-colli.html':'Beauty Point di Dal Forno Michela — Centro estetico — Colognola ai Colli'}[l['slug']]
    sec+='<li><a href="./{s}">{lab}</a></li>\n'.format(s=l['slug'],lab=label)
sec+='</ul>\n'
if 'Colognola ai Colli (2026-07-30' not in idx:
    idx=idx.replace('</body></html>', sec+'</body></html>')
    open('index.html','w',encoding='utf-8').write(idx)
    print('index.html updated')
else:
    print('index section already present')

# emit wa links for CRM
for l in leads:
    print('WA_LINK::'+l['name']+'::'+l['wa'][:80]+'...')
