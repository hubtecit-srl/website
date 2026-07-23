# -*- coding: utf-8 -*-
import json
DATA="2026-07-23"; BASE="https://hubtecit-srl.github.io/website/"
R=json.load(open("_run_results.json",encoding="utf-8"))

# 1) whatsapp-queue.csv : append WhatsApp leads (dedup by phone)
wq="whatsapp-queue.csv"
rows=open(wq,encoding="utf-8").read()
added=[]
with open(wq,"a",encoding="utf-8") as f:
    for r in R:
        if r["channel"]!="whatsapp": continue
        if r["tel"] in rows or r["tel"] in "".join(added):
            print("wa dup skip",r["name"]); continue
        line="%s;%s;%s;%s;Bovolone;%s\n"%(r["name"],r["tel"],r["wa"],BASE+r["file"],DATA)
        f.write(line); added.append(r["tel"]); print("wa added",r["name"])

# 2) index.html : insert new section after intro paragraph
idx=open("index.html",encoding="utf-8").read()
anchor='<p>Siti dimostrativi generati per attività locali senza sito. Pagina interna.</p>'
lis="\n".join('<li><a href="./%s">%s — Bovolone</a></li>'%(r["file"],r["name"].replace("&","&amp;")) for r in R)
block=anchor+'\n<h2>Aggiornamento — Bovolone (%s · parrucchieri)</h2>\n<ul>\n%s\n</ul>'%(DATA,lis)
if anchor in idx and "salone-lorella-leielui-bovolone.html" not in idx:
    idx=idx.replace(anchor,block,1); open("index.html","w",encoding="utf-8").write(idx); print("index updated")
else:
    print("index skip (anchor missing or already present)")

# 3) progress.json : parrucchieri page-1 exhausted -> advance to ristoranti (categoryIndex 1->2), comune stays Bovolone
pr=json.load(open("progress.json",encoding="utf-8"))
pr["categoryIndex"]=2
json.dump(pr,open("progress.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("progress ->",pr["comuneIndex"],pr["categoryIndex"])

# 4) _crm.json : append local mirror rows
crm=json.load(open("_crm.json",encoding="utf-8"))
for r in R:
    canale="WhatsApp" if r["channel"]=="whatsapp" else "Da contattare a mano"
    note="Canale %s · template %s"%(canale,r["tmpl"])
    crm.append(dict(name=r["name"],file=r["file"],phone=r["tel"],intl="",comune="Bovolone",zona=r["addr"],
                    cid=r["cid"],tmpl=r["tmpl"],cat="parrucchieri",url=BASE+r["file"],email="",
                    canale=canale,sito_reale="No",data=DATA,note=note))
json.dump(crm,open("_crm.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("crm rows now",len(crm))
print("DONE")
