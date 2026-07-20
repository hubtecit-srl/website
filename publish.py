# -*- coding: utf-8 -*-
import json, urllib.parse
BASE="https://hubtecit-srl.github.io/website/"
DATA="2026-07-20"
leads=json.load(open("_leads.json"))
# name, file, phone_spaced, phone_intl(39..), comune, cid, template, photos, sitoreale

# ---- index.html ----
idx=open("index.html",encoding="utf-8").read()
add='<h2>Nuovi siti — Albaredo d\'Adige (%s)</h2><ul>\n'%DATA
label={"osteria-dogana-albaredo.html":"Osteria Dogana dal 1969 — Trattoria &amp; Pizzeria",
       "estetica-rachele-albaredo.html":"Estetica Rachele — Centro estetico",
       "salone-andrea-albaredo.html":"Salone Andrea — Parrucchiere"}
for L in leads:
    add+='<li><a href="./%s">%s — Albaredo d\'Adige</a></li>\n'%(L[1],label[L[1]])
add+='</ul>\n'
idx=idx.replace("</body></html>", add+"</body></html>")
open("index.html","w",encoding="utf-8").write(idx)
print("index updated")

# ---- whatsapp-queue.csv (all 3 leads have mobile, no email -> WhatsApp) ----
wq=open("whatsapp-queue.csv",encoding="utf-8").read()
if not wq.endswith("\n"): wq+="\n"
added=[]
for L in leads:
    name,file,phone,intl,comune,cid,tmpl,photos,real=L
    if phone in wq or phone in "\n".join(added):
        print("dup skip",name); continue
    url=BASE+file
    txt=("Buongiorno, sono di HubTec. Ho visto che %s ha ottime recensioni ma nessun sito web, "
         "cosi ne ho preparato uno gia pronto per voi: %s - se vi piace lo attiviamo con soli 200 euro "
         "una tantum, e con 100 euro in piu avete un gestionale per aggiornarlo da soli (testi, foto, orari). "
         "Fatemi sapere! (Per non ricevere altri messaggi, rispondete STOP)")%(name,url)
    link="https://wa.me/"+intl+"?text="+urllib.parse.quote(txt)
    row="%s;%s;%s;%s;%s;%s"%(name,phone,link,url,comune,DATA)
    added.append(row)
if added:
    wq=wq+"\n".join(added)+"\n"
    open("whatsapp-queue.csv","w",encoding="utf-8").write(wq)
print("wa rows added:",len(added))

# ---- brevo-leads.csv : nessun lead email in questo run ----
# (tutti e 3 senza email trovata su Google -> canale WhatsApp)

# ---- progress.json : Albaredo non del tutto esaurito -> lascio comuneIndex=1, categoryIndex=0 (dedup evita ripetizioni) ----
prog=json.load(open("progress.json"))
prog["comuneIndex"]=1
prog["categoryIndex"]=0
json.dump(prog,open("progress.json","w"),ensure_ascii=False,indent=2)
print("progress:",prog["comuneIndex"],prog["categoryIndex"])
# save wa links for CRM
json.dump([{"name":L[0],"file":L[1],"phone":L[2],"intl":L[3],"comune":L[4],"cid":L[5],"tmpl":L[6],
            "url":BASE+L[1],
            "wa":"https://wa.me/"+L[3]+"?text="+urllib.parse.quote("Buongiorno, sono di HubTec. Ho visto che %s ha ottime recensioni ma nessun sito web, cosi ne ho preparato uno gia pronto per voi: %s - se vi piace lo attiviamo con soli 200 euro una tantum, e con 100 euro in piu avete un gestionale per aggiornarlo da soli (testi, foto, orari). Fatemi sapere! (Per non ricevere altri messaggi, rispondete STOP)"%(L[0],BASE+L[1]))} for L in leads],
          open("/tmp/hubsite/_crm.json","w"),ensure_ascii=False)
print("crm data saved")
