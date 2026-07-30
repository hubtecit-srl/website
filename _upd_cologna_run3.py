# -*- coding: utf-8 -*-
import json, urllib.parse, os
os.chdir("/tmp/hub_1785369714")
TODAY="2026-07-30"; BASE="https://hubtecit-srl.github.io/website/"
WA_TMPL=("Buongiorno,\n""Sono Laura di HubTec, azienda di Verona.\n\n"
"Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
"Se vi piace, lo attiviamo con soli 200€.\n\n"
"In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
"Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
"Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n""Laura Borin - HubTec")
def wa(intl,url): return "https://wa.me/"+intl+"?text="+urllib.parse.quote(WA_TMPL.format(url=url),safe='')
leads=[
 dict(name="FHG-Federica Hair Gallery", file="fhg-federica-hair-gallery-cologna-veneta.html", tel="371 691 0078", intl="393716910078", tel_fisso="0442 172 3805", addr="Viale del Lavoro 1", cid="3626886260224841483", tmpl="parrucchieri-revival(v3)", cat="Parrucchieri/Estetica", rating="3,8", nrev="42", labeltype="Parrucchiere", note="canale WhatsApp; cell da directory reteimprese (Places aveva solo fisso 0442 172 3805); rating 3,8"),
 dict(name="Barberoshop Bayrout", file="barberoshop-bayrout-cologna-veneta.html", tel="377 374 7221", intl="393773747221", tel_fisso="", addr="Via de Bernardino Anti 14", cid="18011962456166187664", tmpl="parrucchieri-rhazor(v2)", cat="Parrucchieri/Estetica", rating="5,0", nrev="3", labeltype="Barbiere", note="canale WhatsApp; barbiere"),
 dict(name="Parrucchiera Ricci e Capricci", file="ricci-e-capricci-cologna-veneta.html", tel="352 048 9198", intl="393520489198", tel_fisso="", addr="Via Indipendenza 11", cid="9958794653962710783", tmpl="parrucchieri-salonkit(v1)", cat="Parrucchieri/Estetica", rating="5,0", nrev="2", labeltype="Parrucchiere", note="canale WhatsApp; recensioni senza testo, usate frasi generiche"),
]
for L in leads:
    L["url"]=BASE+L["file"]; L["wa"]=wa(L["intl"],L["url"])

# ---- index.html ----
idx=open("index.html",encoding="utf-8").read()
anchor='<li><a href="./av-hair-cologna-veneta.html">AV hair di Dal Lago Valentina — Parrucchiere — Cologna Veneta</a></li>'
newlis="".join('\n<li><a href="./%s">%s — %s — Cologna Veneta</a></li>'%(L["file"],L["name"],L["labeltype"]) for L in leads if './'+L["file"] not in idx)
idx=idx.replace(anchor,anchor+newlis)
open("index.html","w",encoding="utf-8").write(idx)
print("index adds:",sum(1 for L in leads if L["file"] in idx))

# ---- whatsapp-queue.csv ----
qf="whatsapp-queue.csv"; qtxt=open(qf,encoding="utf-8").read()
names=set(l.split(";")[0].strip() for l in qtxt.splitlines() if ";" in l)
added=[]
with open(qf,"a",encoding="utf-8") as f:
    if qtxt and not qtxt.endswith("\n"): f.write("\n")
    for L in leads:
        if L["name"] in names: print("skip q dup",L["name"]); continue
        f.write(";".join([L["name"],L["tel"],L["wa"],L["url"],"Cologna Veneta",TODAY])+"\n"); added.append(L["name"])
print("queue added:",added)

# ---- _crm.json cache ----
crm=json.load(open("_crm.json",encoding="utf-8"))
cids={str(x.get("cid")) for x in crm}
for L in leads:
    if L["cid"] in cids: print("skip crm dup",L["name"]); continue
    crm.append(dict(name=L["name"],file=L["file"],phone=L["tel"],intl=L["intl"],comune="Cologna Veneta",
        cid=L["cid"],tmpl=L["tmpl"],url=L["url"],wa=L["wa"],canale="whatsapp",zona="Cologna Veneta",
        address=L["addr"]+", 37044 Cologna Veneta (VR)",stato_mail="Bozza pronta",categoria=L["cat"],
        data=TODAY,rating=L["rating"],nrev=L["nrev"],note=L["note"]))
json.dump(crm,open("_crm.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("crm total now:",len(crm))

# ---- progress.json : parrucchieri Cologna Veneta esaurita -> ristoranti ----
pr=json.load(open("progress.json",encoding="utf-8"))
pr["comuneIndex"]=15; pr["categoryIndex"]=2  # ristoranti a Cologna Veneta
open("progress.json","w",encoding="utf-8").write(json.dumps(pr,ensure_ascii=False,indent=2))
print("progress ->",pr["comuneIndex"],pr["categoryIndex"])

# ---- output for Notion step ----
json.dump(leads,open("_cologna_run3_out.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("OK")
