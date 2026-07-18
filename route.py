# -*- coding: utf-8 -*-
import urllib.parse, os
BASE="https://hubtecit-srl.github.io/website/"
DATA="2026-07-18"
# LOVED whatsapp
site="loved-centro-estetico-affi.html"
url=BASE+site
txt=("Buongiorno, sono di HubTec. Ho visto che LOVED centro estetico ha ottime recensioni "
     "ma nessun sito web, cosi ne ho preparato uno gia pronto per voi: "+url+
     " - se vi piace e vostro a 600 euro una tantum, senza impegno. Fatemi sapere! "
     "(Per non ricevere altri messaggi, rispondete STOP)")
link="https://wa.me/393396099603?text="+urllib.parse.quote(txt)
# append whatsapp-queue.csv (dedup by phone)
wq="whatsapp-queue.csv"
rows=open(wq,encoding="utf-8").read()
if "339 609 9603" not in rows:
    with open(wq,"a",encoding="utf-8") as f:
        f.write("LOVED centro estetico;339 609 9603;%s;%s;Affi;%s\n"%(link,url,DATA))
    print("whatsapp row added")
else:
    print("whatsapp dup skip")
open("loved_wa_link.txt","w").write(link)
print("LINK_LEN",len(link))
