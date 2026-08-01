# -*- coding: utf-8 -*-
import re, urllib.parse
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
BASE="https://hubtecit-srl.github.io/website/"
def photo(ref,w=1200): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={KEY}"
def rep(h,old,new,label):
    if old not in h: print(f"  !! MISS [{label}]")
    return h.replace(old,new)
WATXT=("Buongiorno,\nSono Laura di HubTec, azienda di Verona.\n\n"
 "Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
 "Se vi piace, lo attiviamo con soli 200 euro.\n\n"
 "In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari), possiamo aggiungere un gestionale semplice a soli 100 euro.\n\n"
 "Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
 "Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\nLaura Borin - HubTec")
def walink(intl,url): return "https://wa.me/"+intl+"?text="+urllib.parse.quote(WATXT.format(url=url))
STK=["https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1600",
 "https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800",
 "https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800",
 "https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800",
 "https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800",
 "https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800"]

# ---- SALONKIT: Salone Bionaturale (mobile+email) ----
BIO_HERO="AWCwydhRaGLA1Z9XThimyAR5qXsath-QfSZ_2pJdHOiWSpYbwgh2onDghLsztOMU_-C2fIAcHqxG6PHgOZXz_xQxqTev_rChKn-xfJ0ErGkBbNEoVRumffAbzGLske6iqiIqmdxQMyxl7xsj-EWfAF9uBzasBpmCZQuidWZMjGR-MlPfQJvIQEcPTHxcInuDh_0QKAjN2h3ANay3vtNkg5VTit-tS0oXImkv_j0kLEcTghf-QgLr03dTt2ALKK8PDLoaZrqAtQDI21o9TVeECCRFuI-Pvhkzd2LMmQo42Klb-LtSWjGEQRNJOFnstUAtjFl92FWNzb4c6izunuAQMq1jReDmK7VUynLPAU8dsuEcz6RUd19iiNm0cEuKkDCeJ9qcOB7_X0C9EPbVXnI0wP7t3IfLHtVuRNHPCuJ6AxWNvYr44g"
BIOCID="https://maps.google.com/?cid=4208669404767654601"
B=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
B=rep(B,"<title>Salone Méta — Parrucchiere a Verona | Prenota</title>","<title>Salone Bionaturale di Alberta Scala — Parrucchiere a Grezzana (VR) | Prenota</title>","t")
B=rep(B,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="Salone Bionaturale di Alberta Scala, parrucchiere a Grezzana (VR): trattamenti naturali, colore botanico, ricostruzione e cura del capello. 4,7 stelle su 16 recensioni Google. Prenota.">',"d")
B=rep(B,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Grezzana (VR)</span>',"k")
B=rep(B,"<h1>Dove l'hairstyling è <em>olistico</em></h1>","<h1>La bellezza dei capelli, <em>al naturale</em></h1>","h1")
B=rep(B,"<p>Taglio, colore e trattamenti pensati per te e per la salute dei tuoi capelli. Un salone dove bellezza e benessere si incontrano.</p>","<p>Trattamenti naturali, colore botanico e ricostruzione per capelli sani e luminosi. Da Alberta, bellezza e benessere si incontrano, a Grezzana.</p>","hp")
B=rep(B,'<div class="hero-img"><img src="https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000" alt="Salone di parrucchiere"></div>',f'<div class="hero-img"><img src="{photo(BIO_HERO)}" alt="Salone Bionaturale — Grezzana"></div>',"hi")
B=rep(B,'<img src="https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Lavoro 1">',f'<img src="{photo(BIO_HERO,800)}" alt="Salone Bionaturale">',"g1")
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Taglio perfetto e colore stupendo. Mi trovo benissimo ogni volta."</p><b>Serena B.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Professionalità, gentilezza e attenzione ai dettagli. Per chi ama il bio è il paradiso: i capelli restano sani e belli."</p><b>Eleonora M.</b></div>',"rv1")
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente rilassante e staff super professionale. Consigliatissimo."</p><b>Marta L.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Bravissimo staff. Ottimi prodotti ed un servizio perfetto."</p><b>Grande C.</b></div>',"rv2")
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Finalmente un salone che cura davvero i capelli. Bravissimi!"</p><b>Chiara V.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Locale carino e molto pulito. Sara professionale e brava a capire le esigenze. Ottimo rapporto qualità/prezzo."</p><b>Silvia A.</b></div>',"rv3")
B=rep(B,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>',
 '<div><h4>Contatti</h4><p><a href="'+BIOCID+'" target="_blank">Viale Europa 7, Grezzana (VR)</a><br><a href="tel:+393404702269">340 470 2269</a><br><a href="https://wa.me/393404702269">WhatsApp</a><br><a href="mailto:salonebio@gmail.com">salonebio@gmail.com</a></p></div>',"fc")
B=rep(B,"<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>","<div><h4>Orari</h4><p>Mar–Mer 9–18 · Gio 9–12 / 15–21<br>Ven 9–18 · Sab 9–17 · Lun e Dom chiuso</p></div>","fh")
B=rep(B,'<div><div class="brand" style="color:#fff">Salone Méta</div><p>Parrucchiere olistico nel cuore di Verona.</p></div>','<div><div class="brand" style="color:#fff">Salone Bionaturale</div><p>Parrucchiere naturale a Grezzana, Viale Europa.</p></div>',"fbrand")
B=rep(B,'<div class="foot-bot"><span>© Salone Méta — Verona</span><span>Sito realizzato da HubTec</span></div>','<div class="foot-bot"><span>© Salone Bionaturale di Alberta Scala — Grezzana (VR)</span><span>Sito realizzato da HubTec</span></div>',"fbot")
B=B.replace("https://wa.me/390450000000","https://wa.me/393404702269").replace("tel:+390450000000","tel:+393404702269").replace("045 000 0000","340 470 2269")
B=B.replace("Salone Méta","Salone Bionaturale")
open("salone-bionaturale-grezzana.html","w",encoding="utf-8").write(B); print("A salone-bionaturale-grezzana.html",len(B))

# ---- RHAZOR: Fedrigo Luca (barbiere, landline) ----
FEDCID="https://maps.google.com/?cid=12069554526818524664"
L=open("parrucchieri-rhazor-flagship.html",encoding="utf-8").read()
L=rep(L,"<title>Barberia Rasoio — Barbiere a Verona | Prenota</title>","<title>Fedrigo Luca — Parrucchiere e barbiere a Grezzana (VR) | Prenota</title>","t")
L=rep(L,'content="Barberia Rasoio, barbiere a Verona: taglio uomo, rasatura tradizionale, barba e styling. 4,9★ su 200 recensioni. Prenota il tuo appuntamento.">','content="Fedrigo Luca, parrucchiere e barbiere a Grezzana (VR): taglio uomo, barba e styling. Bottega storica del paese. 4,9 stelle su 69 recensioni Google. Chiama e prenota.">',"d")
L=rep(L,'<a href="#top" class="brand">Barberia <b>Rasoio</b></a>','<a href="#top" class="brand">Fedrigo <b>Luca</b></a>',"navb")
L=rep(L,'<div class="brand">Barberia <b style="color:var(--gold)">Rasoio</b></div>','<div class="brand">Fedrigo <b style="color:var(--gold)">Luca</b></div>',"fb")
L=rep(L,"© Barberia Rasoio — Verona","© Fedrigo Luca — Grezzana (VR)","cp")
L=rep(L,'<span class="kick">Barbiere · Verona</span>','<span class="kick">Parrucchiere · Grezzana (VR)</span>',"k")
L=rep(L,"<p>Via Esempio 12, Verona</p>","<p>Via Roma 62, Grezzana (VR)</p>","ibaraddr")
L=rep(L,"<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>","<div><h4>Orari</h4><p>Mar–Ven 8:00–12:30 · 14:00–19:00<br>Sab 8:00–18:00 · Lun e Dom chiuso</p></div>","foothrs")
L=rep(L,'<div class="c"><div><h4>Orari</h4><p>Mar–Sab 9:00–19:00</p></div></div>','<div class="c"><div><h4>Orari</h4><p>Mar–Sab · Lun e Dom chiuso</p></div></div>',"ibarhrs")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"Miglior barbiere di Verona. Taglio sempre perfetto e ambiente top."</p><b>Luca M.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Ambiente pulito, curato e accogliente. Marco è professionale, attento ai dettagli e sa consigliare il taglio più adatto."</p><b>Thomas D.</b></div>',"rv1")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"La rasatura col panno caldo è un\'altra cosa. Bravissimi e simpatici."</p><b>Andrea P.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Maestria e perfezione nel taglio maschile. Clima accogliente e tanta cortesia, sempre col sorriso."</p><b>Giacomo L.</b></div>',"rv2")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"Professionali, veloci e curati. Ci porto anche mio figlio."</p><b>Stefano R.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Ottimo parrucchiere, ambiente rilassante e molto competenti."</p><b>Matteo T.</b></div>',"rv3")
L=rep(L,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@barberiarasoio.it">info@barberiarasoio.it</a></p></div>',f'<div><h4>Contatti</h4><p>Via Roma 62, Grezzana (VR)<br><a href="tel:+390458650609">045 865 0609</a><br><a href="{FEDCID}" target="_blank">Indicazioni</a></p></div>',"fc")
L=L.replace("+390450000000","+390458650609").replace("390450000000","390458650609").replace("045 000 0000","045 865 0609")
L=L.replace("Barberia Rasoio","Fedrigo Luca")
open("fedrigo-luca-grezzana.html","w",encoding="utf-8").write(L); print("B fedrigo-luca-grezzana.html",len(L))

# ---- REVIVAL builder ----
def build_revival(outfile,name,brand,kick,h1,herop,introh2,splitp,hours_split,bigq,bigqb,rv_html,ctap,cta_btns,foot_contacts,foot_hours,foot_brand,foot_bot,tel_repl):
    C=open("parrucchieri-revival-flagship.html",encoding="utf-8").read()
    C=rep(C,"<title>Revival Hair Studio — Parrucchiere a Verona | Prenota</title>",f"<title>{name} — Parrucchiere a Grezzana (VR) | Prenota</title>","title")
    C=rep(C,'content="Revival Hair Studio, parrucchiere a Verona: taglio, colore e styling d\'autore. Un salone dal design minimal ed elegante. 4,9★ su 180 recensioni. Prenota.">',f'content="{name} a Grezzana (VR): {kick}. Recensioni Google eccellenti. Chiama o scrivi per un appuntamento.">',"desc")
    C=rep(C,'<a href="#top" class="brand">REVIVAL</a>',f'<a href="#top" class="brand">{brand}</a>',"brand")
    C=rep(C,'<span class="kick">Hair Studio · Verona</span>','<span class="kick">Parrucchiere · Grezzana (VR)</span>',"kick")
    C=rep(C,"<h1>Revival</h1>",f"<h1>{h1}</h1>","h1")
    C=rep(C,"<p>Taglio, colore e styling d'autore. Un salone dove l'eleganza incontra la cura del dettaglio.</p>",f"<p>{herop}</p>","herop")
    C=rep(C,"<h2>Uno studio dedicato allo stile, in ogni dettaglio</h2>",f"<h2>{introh2}</h2>","introh2")
    C=rep(C,"<p>Un ambiente essenziale ed elegante, pensato per farti vivere un'esperienza di bellezza fuori dal comune. Professionisti attenti, tecniche moderne e ascolto.</p>",f"<p>{splitp}</p>","splitp")
    C=re.sub(r'<ul class="split-hours">.*?</ul>',lambda m:hours_split, C, count=1, flags=re.S)
    C=rep(C,"<q>Un salone diverso da tutti. Eleganza, competenza e un taglio impeccabile.</q>",f"<q>{bigq}</q>","bigq")
    C=rep(C,"<b>Beatrice C.</b>",f"<b>{bigqb}</b>","bigqb")
    C=re.sub(r'<div class="rv-row">.*?</div>\s*</div>\s*</section>', lambda m:rv_html+"\n  </div>\n</section>", C, count=1, flags=re.S)
    C=rep(C,"<p>Chiamaci o scrivici su WhatsApp: dai forma al tuo nuovo look.</p>",f"<p>{ctap}</p>","ctap")
    C=rep(C,'<a href="tel:+390450000000" class="btn btn-light">045 000 0000</a>\n      <a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>',cta_btns,"ctabtns")
    C=rep(C,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@revivalhair.it">info@revivalhair.it</a></p></div>',foot_contacts,"footc")
    C=rep(C,"<div><h4>Orari</h4><p>Mar–Ven 9:00–19:00<br>Sab 9:00–18:00</p></div>",foot_hours,"footh")
    C=rep(C,'<div><div class="brand" style="color:#fff;letter-spacing:.22em">REVIVAL</div><p>Hair studio d\'autore nel cuore di Verona.</p></div>',foot_brand,"footbrand")
    C=rep(C,"<span>© Revival Hair Studio — Verona</span>",foot_bot,"footbot")
    for a,b in tel_repl: C=C.replace(a,b)
    C=C.replace("Revival Hair Studio",name).replace(">Revival<",f">{name}<")
    open(outfile,"w",encoding="utf-8").write(C); print("REVIVAL",outfile,len(C))

MILCID="https://maps.google.com/?cid=2001188430499648723"
build_revival("hair-style-milena-grezzana.html","Hair Style Milena","MILENA","taglio, colore e piega",
 "Hair Style Milena",
 "Taglio, colore e piega con esperienza e passione. Da Milena i capelli sono in ottime mani, a Grezzana.",
 "Esperienza e cura, ad ogni piega",
 "Un salone di fiducia dove Milena e il suo staff seguono ogni cliente con attenzione. Specialista del biondo e del colore naturale.",
 '<ul class="split-hours">\n        <li><span>Martedì</span><span>09:00 - 15:00</span></li>\n        <li><span>Mer &amp; Gio</span><span>09:00 - 18:30</span></li>\n        <li><span>Venerdì</span><span>08:30 - 19:00</span></li>\n        <li><span>Sabato</span><span>08:00 - 14:00</span></li>\n        <li><span>Domenica &amp; Lunedì</span><span>Chiuso</span></li>\n      </ul>',
 "Sempre al top! Biondo fantastico, la tua professionalità è impeccabile.","Amalia C.",
 '<div class="rv-row">\n      <div class="c rv"><div class="st">★★★★★</div><q>"Il mio biondo perfetto! Come sempre super soddisfatta della tua professionalità."</q><b>Ieva L.</b></div>\n      <div class="c rv"><div class="st">★★★★★</div><q>"La migliore parrucchiera che abbia mai incontrato: ascolta sempre le esigenze del cliente."</q><b>Nereide C.</b></div>\n    </div>',
 "Chiamaci per prenotare il tuo appuntamento da Milena.",
 '<a href="tel:+39045907532" class="btn btn-light">Chiama 045 907532</a>\n      <a href="'+MILCID+'" class="btn btn-ghost" target="_blank" rel="noopener">Vedi su Google Maps</a>',
 '<div><h4>Contatti</h4><p><a href="'+MILCID+'" target="_blank">Via Roma 66, Grezzana (VR)</a><br><a href="tel:+39045907532">045 907532</a></p></div>',
 "<div><h4>Orari</h4><p>Mar 9–15 · Mer–Gio 9–18:30<br>Ven 8:30–19 · Sab 8–14 · Lun/Dom chiuso</p></div>",
 '<div><div class="brand" style="color:#fff;letter-spacing:.22em">HAIR STYLE MILENA</div><p>Parrucchiera a Grezzana, Via Roma.</p></div>',
 "<span>© Hair Style Milena — Grezzana (VR)</span>",
 [("https://wa.me/390450000000",MILCID),("tel:+390450000000","tel:+39045907532"),("045 000 0000","045 907532")])

SONCID="https://maps.google.com/?cid=9895309094106716671"
build_revival("parrucchiera-sonia-grezzana.html","Parrucchiera Sonia","SONIA","taglio, colore e piega",
 "Parrucchiera Sonia",
 "Taglio, colore e piega con professionalità e ottimi prezzi. Da Sonia ti senti subito a tuo agio, a Grezzana.",
 "Professionalità e cura, giorno dopo giorno",
 "Un salone accogliente dove Sonia e le sue collaboratrici seguono ogni cliente con attenzione e gentilezza.",
 '<ul class="split-hours">\n        <li><span>Mercoledì</span><span>09:00 - 12:30 / 15:00 - 19:00</span></li>\n        <li><span>Giovedì</span><span>09:00 - 17:00</span></li>\n        <li><span>Ven &amp; Sab</span><span>08:30 - 16:30</span></li>\n        <li><span>Dom · Lun · Mar</span><span>Chiuso</span></li>\n      </ul>',
 "Bravissima lei e le dipendenti, professionali e ottimi prezzi.","Silvia C.",
 '<div class="rv-row">\n      <div class="c rv"><div class="st">★★★★★</div><q>"Sonia mi ha letteralmente salvato. Gentilissima e bravissima, grazie ancora!"</q><b>Dav</b></div>\n      <div class="c rv"><div class="st">★★★★★</div><q>"Molto brava veramente. La consiglio a tutti."</q><b>Maurizio R.</b></div>\n    </div>',
 "Chiamaci o scrivici su WhatsApp: prenota il tuo appuntamento da Sonia.",
 '<a href="tel:+393914582052" class="btn btn-light">Chiama 391 458 2052</a>\n      <a href="https://wa.me/393914582052" class="btn btn-ghost">WhatsApp</a>',
 '<div><h4>Contatti</h4><p><a href="'+SONCID+'" target="_blank">Via Lussemburgo 4, Grezzana (VR)</a><br><a href="tel:+393914582052">391 458 2052</a><br><a href="https://wa.me/393914582052">WhatsApp</a></p></div>',
 "<div><h4>Orari</h4><p>Mer 9–12:30 / 15–19 · Gio 9–17<br>Ven–Sab 8:30–16:30 · Lun/Mar/Dom chiuso</p></div>",
 '<div><div class="brand" style="color:#fff;letter-spacing:.22em">PARRUCCHIERA SONIA</div><p>Parrucchiera a Grezzana, Via Lussemburgo.</p></div>',
 "<span>© Parrucchiera Sonia — Grezzana (VR)</span>",
 [("https://wa.me/390450000000","https://wa.me/393914582052"),("tel:+390450000000","tel:+393914582052"),("045 000 0000","391 458 2052")])

# ---- SILVIA: I colori di Alessia (mobile) ----
ALE_HERO="AWCwydhApSa1dd6pfT88RMFQLKQh2dQZ0RCRqdUIeU8fBZkvZS6ajAp4LXLTXthOp5mt_z-qXyt8J5MJudeHpSUCDNDQRVMkgwRwdglIUavd1bG5Sz3UDV4pQYDFaQsefJBULiwBg7si2GmiXYIg35r2hetz1iqOrbQBpBC6K8D4IIoa87k8_xdeoZ12AJsQkuJe_eF9TtUq8wSQdg3nDpJm975W3tj2BYmT30Ry41FA5cw_qYd_2VIz3tt16qtqgKLWxtQO-H7CWmYRxlTccWcdomeonlgiJjrWNhss-ZnCLB1raQzGMmulL-oph5nz-crDhebHdmManO4gmEq6lRoiq2VXs9nwOEX0tqJ4ApEi-1FIbL_HZqhFlFyX_74RMdVctSc9If2fdhJNhJTnG7xSmS4xzwe1K8mz9T752Ciab3wqeeKXePPGbME4BdbAic2M"
ALECID="https://maps.google.com/?cid=4690932495071560190"
A=open("silvia-de-guidi-capelli-verona.html",encoding="utf-8").read()
imgs=iter([photo(ALE_HERO,1600)]+STK)
A=re.sub(r'https://maps\.googleapis\.com/maps/api/place/photo\?maxwidth=\d+&photo_reference=[^"\')]+', lambda m: next(imgs,STK[-1]), A)
A=rep(A,"<title>Silvia De Guidi Capelli — Parrucchiere a Verona (Golosine)</title>","<title>I colori di Alessia — Parrucchiera a Grezzana (VR)</title>","title")
A=rep(A,'content="Silvia De Guidi Capelli, parrucchiere a Verona in Via Golosine 117. Taglio, colore, acconciature sposa e trattamenti. 4,9★ su 71 recensioni. Prenota.">','content="I colori di Alessia, parrucchiera a Grezzana (VR) in Via Fusina. Taglio, colore e sfumature su misura, ambiente green. 5,0 stelle su Google. Chiama o scrivi su WhatsApp.">',"desc")
A=rep(A,'<a href="#" class="brand"><span class="mk"></span>SILVIA DE GUIDI</a>','<a href="#" class="brand"><span class="mk"></span>I COLORI DI ALESSIA</a>',"brand")
A=rep(A,'<div class="tag"><b>#01</b> Parrucchiere · Verona Golosine</div>','<div class="tag"><b>#01</b> Parrucchiera · Grezzana (VR)</div>',"tag")
A=rep(A,'<h1 class="display">Silvia<br>De Guidi</h1>','<h1 class="display">I colori<br>di Alessia</h1>',"h1")
A=rep(A,'<p class="sub">Taglio, colore e acconciature su misura — studiati sul tuo viso, sul tuo capello e sullo stile che desideri davvero.</p>','<p class="sub">Taglio, colore e sfumature su misura, con ascolto e creatività. Un salone giovane e green dove esci sentendoti bella, a Grezzana.</p>',"sub")
A=rep(A,'<small>4,9 / 5 · 71 recensioni Google</small>','<small>5,0 / 5 · recensioni Google</small>',"badge")
A=rep(A,'<p>4,9 stelle su 71 recensioni Google verificate.</p>','<p>5 stelle su recensioni Google verificate.</p>',"revlab")
newrv='<div class="rv-grid">\n      <div class="rv"><div class="st">★★★★★</div><p>"Cinque stelle meritatissime: ha esaudito ogni desiderio senza rovinare minimamente la chioma."</p><div class="who"><div><b>Greta F.</b><span>recensione Google</span></div></div></div>\n      <div class="rv"><div class="st">★★★★★</div><p>"Ragazza molto preparata, ambiente rilassato e green, ottimi prodotti e ottime mani."</p><div class="who"><div><b>Arianna</b><span>recensione Google</span></div></div></div>\n      <div class="rv"><div class="st">★★★★★</div><p>"Fatto colore e taglio. Molto soddisfatta, cortesia e qualità top."</p><div class="who"><div><b>Jessica T.</b><span>recensione Google</span></div></div></div>\n    </div>'
A=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>', lambda m:newrv+"\n  </div>\n</section>", A, count=1, flags=re.S)
newhours='<ul class="hours-list" id="hoursList">\n          <li data-day="1"><span class="d">Lunedì</span><span>Chiuso</span></li>\n          <li data-day="2"><span class="d">Martedì</span><span>09:00 - 17:00</span></li>\n          <li data-day="3"><span class="d">Mercoledì</span><span>09:00 - 17:00</span></li>\n          <li data-day="4"><span class="d">Giovedì</span><span>09:00 - 13:00 / 15:00 - 19:00</span></li>\n          <li data-day="5"><span class="d">Venerdì</span><span>09:00 - 17:00</span></li>\n          <li data-day="6"><span class="d">Sabato</span><span>09:00 - 17:00</span></li>\n          <li data-day="0"><span class="d">Domenica</span><span>Chiuso</span></li>\n        </ul>'
A=re.sub(r'<ul class="hours-list" id="hoursList">.*?</ul>', lambda m:newhours, A, count=1, flags=re.S)
A=rep(A,"const periods={1:[830,1500],2:[900,1800],3:[900,1800],4:[1200,2100],5:[900,1800],6:[800,1600],0:null};","const periods={1:null,2:[900,1700],3:[900,1700],4:[900,1900],5:[900,1700],6:[900,1700],0:null};","periods")
A=rep(A,'<p style="margin-bottom:8px"><a href="tel:+393335037075">333 503 7075</a></p>\n        <p style="margin-bottom:8px"><a href="mailto:deguidisilvia@gmail.com">deguidisilvia@gmail.com</a></p>\n        <p><a href="https://maps.google.com/?cid=3290711706439048689" target="_blank" rel="noopener">Via Golosine 117, 37136 Verona →</a></p>',
 '<p style="margin-bottom:8px"><a href="tel:+393517436189">351 743 6189</a></p>\n        <p style="margin-bottom:8px"><a href="https://wa.me/393517436189">WhatsApp</a></p>\n        <p><a href="'+ALECID+'" target="_blank" rel="noopener">Via Fusina 5, Grezzana (VR) →</a></p>',"footcontacts")
A=rep(A,"<p>Parrucchiere unisex a Verona, zona Golosine. Taglio, colore, acconciature sposa e trattamenti con prodotti di qualità.</p>","<p>Parrucchiera a Grezzana, Via Fusina. Taglio, colore e sfumature con prodotti green di qualità.</p>","footdesc")
A=rep(A,"<span>© 2026 Silvia De Guidi Capelli · Verona</span>","<span>© 2026 I colori di Alessia · Grezzana (VR)</span>","footbot")
A=A.replace("tel:+393335037075","tel:+393517436189").replace("333 503 7075","351 743 6189")
A=A.replace("Silvia De Guidi","I colori di Alessia").replace("SILVIA DE GUIDI","I COLORI DI ALESSIA")
open("i-colori-di-alessia-grezzana.html","w",encoding="utf-8").write(A); print("SILVIA i-colori-di-alessia-grezzana.html",len(A))

print("ALESSIA_WA="+walink("393517436189",BASE+"i-colori-di-alessia-grezzana.html"))
print("SONIA_WA="+walink("393914582052",BASE+"parrucchiera-sonia-grezzana.html"))
