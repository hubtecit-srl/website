# -*- coding: utf-8 -*-
import json, urllib.parse
BASE="https://hubtecit-srl.github.io/website/"; DATA="2026-07-27"
WATXT=("Buongiorno,\nSono Laura di HubTec, azienda di Verona.\n\n"
 "Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
 "Se vi piace, lo attiviamo con soli 200€.\n\n"
 "In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
 "Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
 "Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\nLaura Borin - HubTec")
def wa(intl,url): return "https://wa.me/"+intl+"?text="+urllib.parse.quote(WATXT.format(url=url))

leads=[
 dict(name="Parrucchiera Ilaria", file="parrucchiera-ilaria-caldiero.html", phone="347 935 8389", intl="393479358389", comune="Caldiero", cid="9394358184494081475", tmpl="parrucchieri-silvia", chan="wa"),
 dict(name="Molinari Ornella", file="parrucchiera-molinari-ornella-caldiero.html", phone="388 649 2751", intl="393886492751", comune="Caldiero", cid="14581294625844458251", tmpl="parrucchieri-salonkit", chan="wa"),
 dict(name="Betty Acconciature", file="betty-acconciature-caldiero.html", phone="045 615 1817", intl="", comune="Caldiero", cid="17005739071905855816", tmpl="parrucchieri-revival", chan="mano"),
]
for L in leads:
    L["url"]=BASE+L["file"]
    L["wa"]=wa(L["intl"],L["url"]) if L["chan"]=="wa" else ""

# --- _crm.json ---
crm=json.load(open("_crm.json",encoding="utf-8"))
have={x.get("cid") for x in crm}
added=0
for L in leads:
    if L["cid"] in have: 
        print("CRM dup skip",L["name"]); continue
    crm.append({k:L[k] for k in ["name","file","phone","intl","comune","cid","tmpl","url","wa"]}); added+=1
json.dump(crm,open("_crm.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("CRM added",added,"total",len(crm))

# --- whatsapp-queue.csv (only chan==wa, dedup by phone) ---
q=open("whatsapp-queue.csv",encoding="utf-8").read()
rows=[]
for L in leads:
    if L["chan"]!="wa": continue
    if L["phone"] in q: print("WA dup skip",L["name"]); continue
    rows.append(";".join([L["name"],L["phone"],L["wa"],L["url"],L["comune"],DATA]))
if rows:
    if not q.endswith("\n"): q+="\n"
    open("whatsapp-queue.csv","w",encoding="utf-8").write(q+"\n".join(rows)+"\n")
print("WA rows added",len(rows))

# --- index.html: insert after Parrucchiera Rosalba li ---
idx=open("index.html",encoding="utf-8").read()
anchor='<li><a href="./parrucchiera-rosalba-caldiero.html">Parrucchiera Rosalba — Caldiero</a></li>'
newlis="".join('\n<li><a href="./%s">%s — Caldiero</a></li>'%(L["file"],L["name"]) for L in leads)
if all(L["file"] not in idx for L in leads):
    idx=idx.replace(anchor, anchor+newlis,1)
    open("index.html","w",encoding="utf-8").write(idx)
    print("index updated")
else:
    print("index: some already present")

# --- progress.json: keep 8/1 (parrucchieri Caldiero non ancora esaurito) ---
pr=json.load(open("progress.json",encoding="utf-8"))
pr["comuneIndex"]=8; pr["categoryIndex"]=1
json.dump(pr,open("progress.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("progress",pr["comuneIndex"],pr["categoryIndex"])
