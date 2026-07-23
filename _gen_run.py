# -*- coding: utf-8 -*-
import re,json,urllib.parse,datetime
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
DATA=json.load(open("_leads_data.json",encoding="utf-8"))
TODAY="2026-07-24"
def photo(ref,w=1200): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={KEY}"
def miss(h,old,label):
    if old not in h: print("  !!MISS",label)
def rep(h,old,new,label):
    miss(h,old,label); return h.replace(old,new)
def author(n):
    p=n.split()
    return p[0]+" "+p[1][0]+"." if len(p)>1 else p[0]
def rev_cards(revs):
    out=[]
    for rv in revs[:3]:
        t=re.sub(r'\s+',' ',rv["t"]).strip()
        if len(t)>150: t=t[:147].rsplit(' ',1)[0]+"…"
        out.append(f'<div class="rv"><div class="st">★★★★★</div><p>"{t}"</p><b>{author(rv["a"])}</b></div>')
    return "\n      ".join(out)
def hours_html(wt):
    if not wt: return "Vedi orari su Google"
    ab={"lunedì":"Lun","martedì":"Mar","mercoledì":"Mer","giovedì":"Gio","venerdì":"Ven","sabato":"Sab","domenica":"Dom"}
    lines=[]
    for x in wt:
        d,_,rest=x.partition(":")
        lines.append(ab.get(d.strip(),d.strip())+" "+rest.strip())
    return "<br>".join(lines)

def replace_pexels(h,refs):
    urls=list(dict.fromkeys(re.findall(r'https://images\.pexels\.com/[^"\')\s]+',h)))
    for i,u in enumerate(urls):
        h=h.replace(u,photo(refs[i%len(refs)]))
    return h

leads=[
 dict(key="Invino",tpl="ristorante-juniper-flagship.html",slug="invino-wine-food-bovolone.html",
      name="Invino wine food",brand_olds=["Ristorante Ginepro","Ginepro"],
      title="Invino wine food — Enoteca e cucina a Bovolone (VR) | Prenota",
      desc="Invino wine food a Bovolone (VR): vini selezionati, taglieri, aperitivi e cucina. 4,5★ su 401 recensioni Google. Prenota il tuo tavolo.",
      addr="Via Carlo Alberto 7, Bovolone (VR)",addr_full="Via Carlo Alberto 7, 37051 Bovolone (VR)",
      mail_old="info@ristoranteginepro.it",
      channel="email",email="invinowinefood@libero.it",
      nat="0458530999",fmt="045 853 0999",cell=None,cid="2067595892391824575"),
 dict(key="NightDay",tpl="ristorante-atlantic-flagship.html",slug="night-and-day-pub-bovolone.html",
      name="Night & Day Pub Irlandese",brand_olds=["Bistrot Contrada"],
      title="Night & Day Pub Irlandese — Birreria e paninoteca a Bovolone (VR)",
      desc="Night & Day Pub Irlandese a Bovolone (VR): birre, cocktail, gin tonic e panini. 4,2★ su 192 recensioni Google. Ti aspettiamo.",
      addr="Via Umberto I 16, Bovolone (VR)",addr_full="Via Umberto I 16, 37051 Bovolone (VR)",
      mail_old="info@bistrotcontrada.it",
      channel="wa",email=None,
      nat="3423543686",fmt="342 354 3686",cell="393423543686",cid="7096592465411469367"),
 dict(key="ICiuski",tpl="ristorante-auburn-flagship.html",slug="i-ciuski-bovolone.html",
      name="I Ciuski",brand_olds=["Osteria del Fuoco"],
      title="I Ciuski — Paninoteca e street food a Bovolone (VR)",
      desc="I Ciuski a Bovolone (VR): panini, piadine, taglieri e birre. 4,9★ su Google. Passa a trovarci al Piazzale Mulino.",
      addr="Piazzale Mulino, Bovolone (VR)",addr_full="Piazzale Mulino, 37051 Bovolone (VR)",
      mail_old="info@osteriadelfuoco.it",
      channel="wa",email=None,
      nat="3514494523",fmt="351 449 4523",cell="393514494523",cid="18091728821413875577"),
]

results=[]
for L in leads:
    print("==",L["name"])
    d=DATA[L["key"]]
    h=open(L["tpl"],encoding="utf-8").read()
    mapurl=f"https://maps.google.com/?cid={L['cid']}"
    # title + meta
    h=re.sub(r'<title>.*?</title>',f'<title>{L["title"]}</title>',h,flags=re.S)
    h=re.sub(r'(<meta name="description" content=")[^"]*(">)',lambda m:m.group(1)+L["desc"]+m.group(2),h)
    # brand names (longer first)
    for b in L["brand_olds"]:
        h=h.replace(b,L["name"])
    # atlantic two-line info address (specific)
    h=h.replace("Via Esempio 12<br>37121 Verona (VR)",L["addr_full"])
    # images
    h=replace_pexels(h,d["photos"])
    # reviews grid + heading
    rg=re.search(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>',h,flags=re.S)
    newgrid=f'<div class="rv-grid">\n      {rev_cards(d["reviews"])}\n    </div>\n  </div>\n</section>'
    if rg: h=h.replace(rg.group(0),newgrid)
    else: print("  !!MISS rvgrid")
    rat=("%.1f"%d["rating"]).replace(".",",") if d["rating"] else "5,0"
    tot=d["total"] or ""
    h=re.sub(r'<h2>[^<]*su[^<]*recensioni</h2>',f'<h2>{rat} su {tot} recensioni</h2>',h)
    # hours
    hh=hours_html(d["hours"])
    h=re.sub(r'<p>[^<]*\d\d:\d\d[^<]*(?:<br>[^<]*)*</p>',f'<p>{hh}</p>',h)
    # address strings (all Via Esempio variants)
    # juniper subtitle variant includes hours -> handle by replacing with addr only
    h=re.sub(r'Via Esempio 12[^<]*',L["addr_full"],h)
    # mail
    if L["channel"]=="email":
        h=h.replace(L["mail_old"],L["email"])
    else:
        h=h.replace(f'<br><a href="mailto:{L["mail_old"]}">{L["mail_old"]}</a>',f'<br><a href="{mapurl}" target="_blank" rel="noopener">Indicazioni</a>')
        h=h.replace(f'<a href="mailto:{L["mail_old"]}">{L["mail_old"]}</a>',f'<a href="{mapurl}" target="_blank" rel="noopener">Indicazioni</a>')
    # indicazioni link (#prenota -> map) only the Indicazioni anchor
    h=h.replace('<a href="#prenota">Indicazioni →</a>',f'<a href="{mapurl}" target="_blank" rel="noopener">Indicazioni →</a>')
    # WhatsApp handling
    if L["channel"]=="email":
        h=h.replace('https://wa.me/390450000000',mapurl)
        h=h.replace('>WhatsApp<','>Come arrivare<')
    else:
        h=h.replace('wa.me/390450000000','wa.me/'+L["cell"])
    # phone numbers
    h=h.replace('+390450000000','+39'+L["nat"])
    h=h.replace('390450000000','39'+L["nat"])
    h=h.replace('045 000 0000',L["fmt"])
    # city
    h=re.sub(r'\bVerona\b','Bovolone (VR)',h)
    # mobile hardening: ensure overflow-x hidden
    if 'overflow-x:hidden' not in h and 'overflow-x: hidden' not in h:
        h=h.replace('</head>','<style>html,body{overflow-x:hidden;max-width:100%}</style>\n</head>')
    open(L["slug"],"w",encoding="utf-8").write(h)
    print("  wrote",L["slug"],len(h),"| leftover placeholder:",("045 000 0000" in h or "390450000000" in h or "Esempio" in h))
    results.append((L,d))

# ---- WhatsApp queue text ----
WA_TXT=("Buongiorno,\nSono Laura di HubTec, azienda di Verona.\n\n"
"Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
"Se vi piace, lo attiviamo con soli 200€.\n\n"
"In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
"Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
"Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n"
"Laura Borin - HubTec")

# ---- update index.html ----
idx=open("index.html",encoding="utf-8").read()
block=('<h2>Nuovi siti — Bovolone (%s · ristoranti)</h2>\n<ul>\n'%TODAY
 +''.join('<li><a href="./%s">%s — Bovolone</a></li>\n'%(L["slug"],L["name"]) for L in leads)
 +'</ul>\n\n')
anchor='<h2>Nuovi siti — Bovolone (2026-07-23 · ristoranti)</h2>'
if anchor in idx:
    idx=idx.replace(anchor,block+anchor)
else:
    print("  !!MISS index anchor")
open("index.html","w",encoding="utf-8").write(idx)

# ---- append CSVs ----
def append_csv(fn,line):
    with open(fn,encoding="utf-8") as f: cur=f.read()
    if not cur.endswith("\n"): cur+="\n"
    open(fn,"w",encoding="utf-8").write(cur+line+"\n")

# brevo (Invino)
Inv=leads[0]
brevo_line=f'{Inv["email"]};{Inv["name"]};https://hubtecit-srl.github.io/website/{Inv["slug"]};Bovolone;{Inv["fmt"]};{TODAY}'
append_csv("brevo-leads.csv",brevo_line)
print("brevo+",brevo_line)

# whatsapp queue (NightDay, ICiuski)
walines=[]
for L in leads[1:]:
    url=f'https://hubtecit-srl.github.io/website/{L["slug"]}'
    txt=urllib.parse.quote(WA_TXT.format(url=url))
    link=f'https://wa.me/{L["cell"]}?text={txt}'
    line=f'{L["name"]};{L["fmt"]};{link};{url};Bovolone;{TODAY}'
    append_csv("whatsapp-queue.csv",line)
    walines.append((L,link))
    print("wa+",L["name"])

# ---- update _leads.json ----
lj=json.load(open("_leads.json",encoding="utf-8"))
tplmap={"Invino":"ristorante-juniper","NightDay":"ristorante-atlantic","ICiuski":"ristorante-auburn"}
for L in leads:
    d=DATA[L["key"]]
    lj.append([L["name"],L["slug"],L["fmt"],(L["cell"] or "39"+L["nat"]),"Bovolone",L["cid"],tplmap[L["key"]],d["photos"][:5]])
json.dump(lj,open("_leads.json","w",encoding="utf-8"),ensure_ascii=False)

# save wa links for CRM step
json.dump({L["key"]:link for (L,link) in walines},open("_wa_links.json","w",encoding="utf-8"),ensure_ascii=False)
print("DONE")
