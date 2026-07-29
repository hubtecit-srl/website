# -*- coding: utf-8 -*-
import json, urllib.parse
DATA="2026-07-29"; BASE="https://hubtecit-srl.github.io/website/"

leads=[
 dict(name="Nose' Gloria", file="nose-gloria-castel-dazzano.html", tel="045 519953", intl="+39045519953",
      wa=None, cid="10973556078385396931", addr="Via Cavour 28", email="", channel="mano",
      tmpl="gen_castel palette rosé", label="Nose' Gloria — Parrucchiere — Castel d'Azzano"),
 dict(name="Sinergie Capelli", file="sinergie-capelli-castel-dazzano.html", tel="351 378 7938", intl="+393513787938",
      wa="393513787938", cid="797286574749834856", addr="Via Cecco Angiolieri", email="", channel="whatsapp",
      tmpl="gen_castel palette viola", label="Sinergie Capelli — Parrucchiere — Castel d'Azzano"),
]

# 1) index.html : insert <li> after the Castel d'Azzano <ul> opening
idx=open("index.html",encoding="utf-8").read()
anchor="<h2>Nuovi siti — Castel d'Azzano (2026-07-29 · parrucchieri)</h2>\n<ul>\n"
lis="".join('<li><a href="./%s">%s</a></li>\n'%(l["file"], l["label"].replace("&","&amp;")) for l in leads)
if anchor in idx and "sinergie-capelli-castel-dazzano.html" not in idx:
    idx=idx.replace(anchor, anchor+lis, 1)
    open("index.html","w",encoding="utf-8").write(idx); print("index updated")
else:
    print("index skip")

# 2) whatsapp-queue.csv : Sinergie only (dedup by phone)
wa_msg=("Buongiorno,\nSono Laura di HubTec, azienda di Verona.\n\n"
"Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
"Se vi piace, lo attiviamo con soli 200€.\n\n"
"In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
"Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
"Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n"
"Laura Borin - HubTec")
wq="whatsapp-queue.csv"; rows=open(wq,encoding="utf-8").read()
walink_map={}
with open(wq,"a",encoding="utf-8") as f:
    for l in leads:
        if l["channel"]!="whatsapp": continue
        if l["intl"].lstrip("+") in rows or l["tel"] in rows:
            print("wa dup skip",l["name"]); continue
        url=BASE+l["file"]
        link="https://wa.me/%s?text=%s"%(l["wa"], urllib.parse.quote(wa_msg.format(url=url)))
        walink_map[l["name"]]=link
        f.write("%s;%s;%s;%s;Castel d'Azzano;%s\n"%(l["name"], l["tel"], link, url, DATA))
        print("wa added",l["name"])

# 3) brevo-leads.csv : none (no emails)
print("brevo: 0 (nessuna email trovata)")

# 4) _crm.json mirror
crm=json.load(open("_crm.json",encoding="utf-8"))
have={c.get("cid") for c in crm}
for l in leads:
    if l["cid"] in have: print("crm dup skip",l["name"]); continue
    canale="WhatsApp" if l["channel"]=="whatsapp" else "Da contattare a mano"
    stato_mail="Bozza pronta" if l["channel"]=="whatsapp" else "Da fare"
    crm.append(dict(name=l["name"], file=l["file"], phone=l["tel"], intl=l["intl"], comune="Castel d'Azzano",
        zona=l["addr"], cid=l["cid"], tmpl=l["tmpl"], cat="parrucchieri", url=BASE+l["file"], email="",
        wa=walink_map.get(l["name"],""), canale=canale, sito_reale="No", stato_mail=stato_mail,
        data=DATA, note="Canale %s · template %s"%(canale,l["tmpl"])))
    print("crm added",l["name"])
json.dump(crm,open("_crm.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)

# 5) progress.json : Castel d'Azzano parrucchieri exhausted -> categoryIndex 1->2 (ristoranti)
pr=json.load(open("progress.json",encoding="utf-8"))
pr["categoryIndex"]=2
json.dump(pr,open("progress.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("progress -> comuneIndex",pr["comuneIndex"],"categoryIndex",pr["categoryIndex"])
print("DONE")
