# -*- coding: utf-8 -*-
import json, urllib.parse
BASE="https://hubtecit-srl.github.io/website/"
DATE="2026-07-29"
leads=[
 {"name":"Casa Pomari Ristorante & Lounge bar","file":"casa-pomari-cerea.html","phone":"339 183 3334","intl":"393391833334","cid":"3356799635808851068","tmpl":"ristorante-auburn","label":"Ristorante — Cerea"},
 {"name":"BuffoOsteria","file":"buffoosteria-cerea.html","phone":"338 167 7420","intl":"393381677420","cid":"16739140940002306136","tmpl":"ristorante-juniper","label":"Osteria — Cerea"},
 {"name":"da Gioia Trattoria e...","file":"da-gioia-trattoria-cerea.html","phone":"350 994 7932","intl":"393509947932","cid":"14045401954028729376","tmpl":"il-vicoletto-trattoria","label":"Trattoria — Cerea (Asparetto)"},
]

def wa_text(site):
    t=("Buongiorno,\n"
       "Sono Laura di HubTec, azienda di Verona.\n\n"
       "Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: "+site+"\n\n"
       "Se vi piace, lo attiviamo con soli 200€.\n\n"
       "In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
       "Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
       "Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n"
       "Laura Borin - HubTec")
    return urllib.parse.quote(t, safe='')

# 1) index.html — insert new block at top of list
idx=open("index.html",encoding="utf-8").read()
anchor="<p>Siti dimostrativi generati per attività locali senza sito. Pagina interna.</p>"
block="\n<h2>Nuovi siti — Cerea (%s · ristoranti)</h2>\n<ul>\n"%DATE
for l in leads:
    block+='<li><a href="./%s">%s — %s</a></li>\n'%(l["file"], l["name"].replace("&","&amp;"), l["label"])
block+="</ul>\n"
assert anchor in idx, "index anchor MISS"
idx=idx.replace(anchor, anchor+block, 1)
open("index.html","w",encoding="utf-8").write(idx)
print("index.html updated")

# 2) whatsapp-queue.csv — append 3 rows (dedup by intl)
rows=open("whatsapp-queue.csv",encoding="utf-8").read()
added=0
with open("whatsapp-queue.csv","a",encoding="utf-8") as f:
    for l in leads:
        if l["intl"] in rows:
            print("  dup skip", l["name"]); continue
        site=BASE+l["file"]
        link="https://wa.me/%s?text=%s"%(l["intl"], wa_text(site))
        f.write("%s;%s;%s;%s;Cerea;%s\n"%(l["name"], l["phone"], link, site, DATE))
        added+=1
print("whatsapp rows added:", added)

# 3) progress.json — pair NOT exhausted (molti ristoranti senza sito restano) -> resta 14/2
prog=json.load(open("progress.json",encoding="utf-8"))
prog["comuneIndex"]=14
prog["categoryIndex"]=2
json.dump(prog, open("progress.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("progress.json ->", prog["comuneIndex"], prog["categoryIndex"])

# 4) _crm.json cache — append for future dedup/rotation
crm=json.load(open("_crm.json",encoding="utf-8"))
have={r.get("cid") for r in crm}
for l in leads:
    if l["cid"] in have: continue
    crm.append({"name":l["name"],"file":l["file"],"phone":l["phone"],"intl":l["intl"],
        "comune":"Cerea","cid":l["cid"],"tmpl":l["tmpl"],"url":BASE+l["file"],
        "wa":"https://wa.me/%s?text=%s"%(l["intl"], wa_text(BASE+l["file"]))})
json.dump(crm, open("_crm.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("_crm.json total:", len(crm))
print("PREP DONE")
