# -*- coding: utf-8 -*-
import re, urllib.parse, itertools
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
BASE="https://hubtecit-srl.github.io/website/"
def photo(ref,w=1200): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={KEY}"
def rep(html,old,new,label):
    if old not in html: print(f"  !! MISS [{label}]")
    return html.replace(old,new)
WATXT=("Buongiorno,\nSono Laura di HubTec, azienda di Verona.\n\n"
 "Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
 "Se vi piace, lo attiviamo con soli 200€.\n\n"
 "In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
 "Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
 "Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\nLaura Borin - HubTec")
def walink(intl,url): return "https://wa.me/"+intl+"?text="+urllib.parse.quote(WATXT.format(url=url))
STK=["https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1600",
 "https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800",
 "https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800",
 "https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800",
 "https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800",
 "https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800"]

##################### LEAD 1: Kime's Hair -> SALONKIT #####################
K_HERO="AWCwydjCVdBeEtdoDujjBNBbuO1rvai_HG6E4nwwSilP-pMje6N3PluEiIhdZYoCSH6WnZSgUi9dCeFmhJEYwQVqF-6gAIMztJ74o-K78NI4lH2orRgGrnlAY-Dw6yzKDP1Fxjx0nZDrvRFmz7cZOhmcLGM5TdfphfFa1cK5u3-P2FtVxs6nLlUIT06GZs1YhVjk1QRsiypPHcLgjNSsKuf-2JDFYYRExhY0ZDFBvNn6FGs5v2o0GMM9ilKmd0xr9k5xIe_8mAJuuF_x-ARqDgZdbp8yM65bjKSjgLlTKeBm8HY-71Rgknz7L19oS1a3QLXwZZiTjh4fMLMU1d92uFlRl6V7cKDCSvQFLPBw_SykUgqJRhPC6vAn57-ufpvKO0Ys_ZUuEpn5JejQgHT_6XIXWBebVfb5tghZhpn5-g51QgZoYDiH"
K_G="AWCwydgaCOtF7TVAA4HwBwhSy_v8xbcJ-Nk95YHW5ZKwP5h0JTc_9LvLEe91rZR-qb-DTZdEGQJHJPYAOqYppsYKoon1jBHOaSd-plXM23gLGf5PPUiqhUO3w5VB1KeR_LaPEChsGoHfi9rasbZX6IvxSVKxqRv2ScO5gKberrNXVgJMEwFV1cwkZZaCB6FOmE7Db0anuqO9tRuJorgTHRWgGHB6W-gCtOC10VRaMJaik7XFBzE-55U7RNNDmEWRxI3lY7CF26OZ6d3OHTmIPusQ8FeMjo_BwkRXb6PzPHnJmpC7WqijoNcUxIKs_QwX5FPgBs2kj-75YFBVxfJl3bdWkkJ_Qc6XYsURXLcIF5YC6bnK5NNRMwAoUp2yWhT0XO0KX03xu2ULzZkdkU4JdQq6AnJcMvVVXhQO1GNkSyTlMgA"
KCID="https://maps.google.com/?cid=17882621022209920205"
B=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
B=rep(B,"<title>Salone Méta — Parrucchiere a Verona | Prenota</title>","<title>Kime's Hair — Parrucchiere a Colognola ai Colli (VR) | Prenota</title>","title")
B=rep(B,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="Kime\'s Hair, parrucchiere a Colognola ai Colli (VR): taglio, colore, specialista del colore e trattamenti. 5,0★ su 39 recensioni Google. Prenota il tuo appuntamento.">',"desc")
B=rep(B,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Colognola ai Colli (VR)</span>',"kick")
B=rep(B,"<h1>Dove l'hairstyling è <em>olistico</em></h1>","<h1>Il colore che fa <em>rinascere</em> i capelli</h1>","h1")
B=rep(B,"<p>Taglio, colore e trattamenti pensati per te e per la salute dei tuoi capelli. Un salone dove bellezza e benessere si incontrano.</p>","<p>Kime è specialista del colore: taglio, colore e trattamenti su misura, con ascolto e creatività. Un salone dove esci sentendoti bella.</p>","herop")
B=rep(B,'<div class="hero-img"><img src="https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000" alt="Salone di parrucchiere"></div>',f'<div class="hero-img"><img src="{photo(K_HERO)}" alt="Kime\'s Hair — salone"></div>',"heroimg")
B=rep(B,'<img src="https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Lavoro 1">',f'<img src="{photo(K_G,800)}" alt="Lavoro Kime\'s Hair">',"gal1")
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Taglio perfetto e colore stupendo. Mi trovo benissimo ogni volta."</p><b>Serena B.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Finalmente ho trovato Kime! Tra taglio, colore e trattamento i miei capelli sono rinati. Professionalità, serietà e gentilezza."</p><b>Cetty S.</b></div>',"rv1")
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente rilassante e staff super professionale. Consigliatissimo."</p><b>Marta L.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Professionale, competente, bravissima. Decolorare i miei capelli non è facile ma ci è riuscita al 100%."</p><b>Elisabetta D.</b></div>',"rv2")
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Finalmente un salone che cura davvero i capelli. Bravissimi!"</p><b>Chiara V.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Sempre aggiornata, piena di proposte e creatività in linea con la cliente. Esci e ti senti bella!"</p><b>Elisa B.</b></div>',"rv3")
B=rep(B,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>',
 '<div><h4>Contatti</h4><p><a href="'+KCID+'" target="_blank">Piazza Donatore 10/C, Colognola ai Colli (VR)</a><br><a href="tel:+393470903503">347 090 3503</a><br><a href="https://wa.me/393470903503">WhatsApp</a></p></div>',"footc")
B=rep(B,"<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>","<div><h4>Orari</h4><p>Mar 9–18:30 · Mer 11–21 · Gio 9–18:30<br>Ven 9–19 · Sab 8:30–17 · Lun e Dom chiuso</p></div>","footh")
B=rep(B,'<div><div class="brand" style="color:#fff">Salone Méta</div><p>Parrucchiere olistico nel cuore di Verona.</p></div>','<div><div class="brand" style="color:#fff">Kime\'s Hair</div><p>Parrucchiere e specialista del colore a Colognola ai Colli.</p></div>',"footbrand")
B=rep(B,'<div class="foot-bot"><span>© Salone Méta — Verona</span><span>Sito realizzato da HubTec</span></div>','<div class="foot-bot"><span>© Kime\'s Hair — Colognola ai Colli (VR)</span><span>Sito realizzato da HubTec</span></div>',"footbot")
B=B.replace("https://wa.me/390450000000","https://wa.me/393470903503").replace("tel:+390450000000","tel:+393470903503").replace("045 000 0000","347 090 3503")
B=B.replace("Salone Méta","Kime's Hair")
open("kimes-hair-colognola.html","w",encoding="utf-8").write(B); print("1 kimes-hair-colognola.html",len(B))

##################### LEAD 2: Francesco Benini -> RHAZOR #####################
BEN_HERO="AWCwydj3brRdGB7hSFkkOOf8yVd45vbQQtySAp38xaFezebzPe29JinlU6OJ0brW1yKevUEvFNZJmfqj9-fYWLs6lxQthZE7_s3fxz020d5BHTWibSnaYD9PewFJREtzUaUr-YMIR6rzMNe_tDph-I5-vfrV41i6GnBnDPHfVZFqteacjYdmCrjRn-_DUEpzk33V9mlkSbDJGZ07ip_gBmIWJodtvpETMCIz20r11IKz8lPcsyoG1_DuB1J-In2qOi5OMO7o25d-GZHKC8SYkAFkbEPsJOYO7PDAsG1wMAJIp8uyxTesAq3Zx244rOJBIJfyjQZrVBf-chL154XAKKM-OPFaV-1S1tFG2q03C3fNF4zuOCT3YzSw8wIUM3BaE0h_f3P7VHbXlCjhup_gY4hviGnQAW48y6JINaNEOZ_7q34Weexr"
BEN_AB="AWCwydi-S5caBGT-cRngf6zS_JqH0nPysFyxe9tg5DDWNLzklSxXmH2zDgcKXc9x1mSU6tDjZpwTkfdp0bwePKAM-11rZubbaMPnhvFC3nSWuEyO6ibRNyZFBXZHhoFNqPS-eIlUniddMbliWp2HCZ446pn699MTYE3EoFqobIsEs6pBsGOuyMnABruCLD4xUX1qC4s3q6YvXXvJED3H4syRkmeSXWAmkwufWkICcVgC3IH12LwOccnC1u6WjkhrohgVgXNAM0pE_7QzlKgUARmbOHJmJ4uMnwKaUh0BEGGpO1uU7y5qP2LLCnEzYn8PndyG7ADDWigSCsac4_YWQ8b6A7tGBrZ-f486e8cldQCl3s5Pv0OTJydTDOKv_nV8wQkDY48cNpjoVl9jCUjPdteKO9G0GkvsVtZIE4x0LU_5juHSS4c"
BENCID="https://maps.google.com/?cid=15172908600741323374"
L=open("parrucchieri-rhazor-flagship.html",encoding="utf-8").read()
L=rep(L,"<title>Barberia Rasoio — Barbiere a Verona | Prenota</title>","<title>Parrucchiere Francesco Benini — Colognola ai Colli (VR) | Prenota</title>","t")
L=rep(L,'content="Barberia Rasoio, barbiere a Verona: taglio uomo, rasatura tradizionale, barba e styling. 4,9★ su 200 recensioni. Prenota il tuo appuntamento.">','content="Parrucchiere Francesco Benini a Colognola ai Colli (VR): taglio uomo e donna, barba, cura del capello. 4,9★ su 24 recensioni Google. Chiama e prenota.">',"d")
L=rep(L,'<a href="#top" class="brand">Barberia <b>Rasoio</b></a>','<a href="#top" class="brand">Francesco <b>Benini</b></a>',"navb")
L=rep(L,'<div class="brand">Barberia <b style="color:var(--gold)">Rasoio</b></div>','<div class="brand">Francesco <b style="color:var(--gold)">Benini</b></div>',"fb")
L=rep(L,"© Barberia Rasoio — Verona","© Parrucchiere Francesco Benini — Colognola ai Colli (VR)","cp")
L=rep(L,'<span class="kick">Barbiere · Verona</span>','<span class="kick">Parrucchiere · Colognola ai Colli (VR)</span>',"k")
L=rep(L,"https://images.pexels.com/photos/1319460/pexels-photo-1319460.jpeg?auto=compress&cs=tinysrgb&w=1600",photo(BEN_HERO,1600),"hero")
L=rep(L,"https://images.pexels.com/photos/1570807/pexels-photo-1570807.jpeg?auto=compress&cs=tinysrgb&w=1000",photo(BEN_AB,1000),"about")
L=rep(L,"<p>Via Esempio 12, Verona</p>","<p>Via Unità d'Italia 9/e, Colognola ai Colli (VR)</p>","ibaraddr")
L=rep(L,"<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>","<div><h4>Orari</h4><p>Mar–Ven 8:30–12:00 · 14:30–19:00<br>Sab 8:00–17:00 · Lun e Dom chiuso</p></div>","foothrs")
L=rep(L,'<div class="c"><div><h4>Orari</h4><p>Mar–Sab 9:00–19:00</p></div></div>','<div class="c"><div><h4>Orari</h4><p>Mar–Sab · Lun e Dom chiuso</p></div></div>',"ibarhrs")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"Miglior barbiere di Verona. Taglio sempre perfetto e ambiente top."</p><b>Luca M.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Due grandi professionisti! Francesco sa consigliare al meglio, taglio impeccabile e prezzi umani."</p><b>Silvia M.</b></div>',"rv1")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"La rasatura col panno caldo è un\'altra cosa. Bravissimi e simpatici."</p><b>Andrea P.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Professionista serio e capace. Ottimi prezzi, locale confortevole."</p><b>Ignazio T.</b></div>',"rv2")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"Professionali, veloci e curati. Ci porto anche mio figlio."</p><b>Stefano R.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Bel negozio rinnovato, ottimo servizio e gentilezza, comodo parcheggio."</p><b>Corrado A.</b></div>',"rv3")
L=rep(L,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@barberiarasoio.it">info@barberiarasoio.it</a></p></div>',f'<div><h4>Contatti</h4><p>Via Unità d\'Italia 9/e, Colognola ai Colli (VR)<br><a href="tel:+390456150738">045 615 0738</a><br><a href="{BENCID}" target="_blank">Indicazioni</a></p></div>',"fc")
L=L.replace("+390450000000","+390456150738").replace("390450000000","390456150738").replace("045 000 0000","045 615 0738")
L=L.replace("Barberia Rasoio","Francesco Benini").replace("Barbiere","Parrucchiere").replace("barbiere","parrucchiere")
open("parrucchiere-francesco-benini-colognola.html","w",encoding="utf-8").write(L); print("2 parrucchiere-francesco-benini-colognola.html",len(L))

##################### LEAD 3: Parrucchiera Susy -> REVIVAL (no photos, stock) #####################
SUCID="https://maps.google.com/?cid=9048187910769023703"
C=open("parrucchieri-revival-flagship.html",encoding="utf-8").read()
C=rep(C,"<title>Revival Hair Studio — Parrucchiere a Verona | Prenota</title>","<title>Parrucchiera Susy — Colognola ai Colli (VR) | Prenota</title>","title")
C=rep(C,'content="Revival Hair Studio, parrucchiere a Verona: taglio, colore e styling d\'autore. Un salone dal design minimal ed elegante. 4,9★ su 180 recensioni. Prenota.">','content="Parrucchiera Susy (Cacciatori Susanna) a Colognola ai Colli (VR): taglio, colore, piega e acconciature. 4,6★ su Google. Chiama o scrivi su WhatsApp.">',"desc")
C=rep(C,'<a href="#top" class="brand">REVIVAL</a>','<a href="#top" class="brand">SUSY</a>',"brand")
C=rep(C,'<span class="kick">Hair Studio · Verona</span>','<span class="kick">Parrucchiera · Colognola ai Colli (VR)</span>',"kick")
C=rep(C,"<h1>Revival</h1>","<h1>Parrucchiera Susy</h1>","h1")
C=rep(C,"<p>Taglio, colore e styling d'autore. Un salone dove l'eleganza incontra la cura del dettaglio.</p>","<p>Taglio, colore, piega e acconciature con professionalità e gentilezza. Da Susy ti senti subito a tuo agio, a Colognola ai Colli.</p>","herop")
C=rep(C,"<h2>Uno studio dedicato allo stile, in ogni dettaglio</h2>","<h2>Professionalità e gentilezza, ogni giorno</h2>","introh2")
C=rep(C,"<p>Un ambiente essenziale ed elegante, pensato per farti vivere un'esperienza di bellezza fuori dal comune. Professionisti attenti, tecniche moderne e ascolto.</p>","<p>Un salone accogliente dove Susanna segue ogni cliente con cura e attenzione. Orario continuato dal martedì al sabato, per venirti incontro quando vuoi tu.</p>","splitp")
C=re.sub(r'<ul class="split-hours">.*?</ul>','<ul class="split-hours">\n        <li><span>Martedì – Sabato</span><span>07:00 – 19:00</span></li>\n        <li><span>Domenica &amp; Lunedì</span><span>Chiuso</span></li>\n      </ul>', C, count=1, flags=re.S)
C=rep(C,"<q>Un salone diverso da tutti. Eleganza, competenza e un taglio impeccabile.</q>","<q>Professionalità e gentilezza. Mi trovo sempre benissimo.</q>","bigq")
C=rep(C,"<b>Beatrice C.</b>","<b>Virginia M.</b>","bigqb")
newrv='''<div class="rv-row">
      <div class="c rv"><div class="st">★★★★★</div><q>"Sempre disponibile e attenta, esco sempre soddisfatta del risultato."</q><b>Francesca P.</b></div>
      <div class="c rv"><div class="st">★★★★☆</div><q>"Brava e cordiale, la consiglio a chi cerca un salone di fiducia in paese."</q><b>Cristian B.</b></div>
    </div>'''
C=re.sub(r'<div class="rv-row">.*?</div>\s*</div>\s*</section>', newrv+"\n  </div>\n</section>", C, count=1, flags=re.S)
C=rep(C,"<p>Chiamaci o scrivici su WhatsApp: dai forma al tuo nuovo look.</p>","<p>Chiamaci o scrivici su WhatsApp: prenota il tuo appuntamento da Susy.</p>","ctap")
C=rep(C,'<a href="tel:+390450000000" class="btn btn-light">045 000 0000</a>\n      <a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>','<a href="tel:+393472445676" class="btn btn-light">Chiama 347 244 5676</a>\n      <a href="https://wa.me/393472445676" class="btn btn-ghost">WhatsApp</a>',"ctabtns")
C=rep(C,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@revivalhair.it">info@revivalhair.it</a></p></div>','<div><h4>Contatti</h4><p><a href="'+SUCID+'" target="_blank">Via Giacomo Zanella 11/D, Colognola ai Colli (VR)</a><br><a href="tel:+393472445676">347 244 5676</a><br><a href="https://wa.me/393472445676">WhatsApp</a></p></div>',"footc")
C=rep(C,"<div><h4>Orari</h4><p>Mar–Ven 9:00–19:00<br>Sab 9:00–18:00</p></div>","<div><h4>Orari</h4><p>Mar–Sab 7:00–19:00<br>Lun &amp; Dom chiuso</p></div>","footh")
C=rep(C,'<div><div class="brand" style="color:#fff;letter-spacing:.22em">REVIVAL</div><p>Hair studio d\'autore nel cuore di Verona.</p></div>','<div><div class="brand" style="color:#fff;letter-spacing:.22em">PARRUCCHIERA SUSY</div><p>Parrucchiera a Colognola ai Colli, Via Zanella.</p></div>',"footbrand")
C=rep(C,"<span>© Revival Hair Studio — Verona</span>","<span>© Parrucchiera Susy — Colognola ai Colli (VR)</span>","footbot")
C=C.replace("https://wa.me/390450000000","https://wa.me/393472445676").replace("tel:+390450000000","tel:+393472445676").replace("045 000 0000","347 244 5676")
C=C.replace("Revival Hair Studio","Parrucchiera Susy").replace(">Revival<",">Parrucchiera Susy<")
open("parrucchiera-susy-colognola.html","w",encoding="utf-8").write(C); print("3 parrucchiera-susy-colognola.html",len(C))

##################### LEAD 4: Maschi Stefania -> SILVIA (no photos -> stock) #####################
MACID="https://maps.google.com/?cid=7996801349306858428"
A=open("silvia-de-guidi-capelli-verona.html",encoding="utf-8").read()
# replace ALL baked google photos with stock atmosphere
it=iter(STK)
A=re.sub(r'https://maps\.googleapis\.com/maps/api/place/photo\?maxwidth=\d+&photo_reference=[^"\')]+', lambda m: next(it), A)
A=rep(A,"<title>Silvia De Guidi Capelli — Parrucchiere a Verona (Golosine)</title>","<title>Maschi Stefania — Parrucchiere a Colognola ai Colli (VR)</title>","title")
A=rep(A,'content="Silvia De Guidi Capelli, parrucchiere a Verona in Via Golosine 117. Taglio, colore, acconciature sposa e trattamenti. 4,9★ su 71 recensioni. Prenota.">','content="Maschi Stefania, parrucchiera a Colognola ai Colli (VR) in Via Strà. Taglio, colore, piega e acconciature. 5,0★ su Google. Chiama per un appuntamento.">',"desc")
A=rep(A,'<a href="#" class="brand"><span class="mk"></span>SILVIA DE GUIDI</a>','<a href="#" class="brand"><span class="mk"></span>MASCHI STEFANIA</a>',"brand")
A=rep(A,'<div class="tag"><b>#01</b> Parrucchiere · Verona Golosine</div>','<div class="tag"><b>#01</b> Parrucchiera · Colognola ai Colli (VR)</div>',"tag")
A=rep(A,'<h1 class="display">Silvia<br>De Guidi</h1>','<h1 class="display">Maschi<br>Stefania</h1>',"h1")
A=rep(A,'<p class="sub">Taglio, colore e acconciature su misura — studiati sul tuo viso, sul tuo capello e sullo stile che desideri davvero.</p>','<p class="sub">Taglio, colore, piega e acconciature con cortesia e professionalità. Un salone di fiducia nel cuore di Colognola ai Colli.</p>',"sub")
A=rep(A,'<small>4,9 / 5 · 71 recensioni Google</small>','<small>5,0 / 5 · 3 recensioni Google</small>',"badge")
A=rep(A,'<p>4,9 stelle su 71 recensioni Google verificate.</p>','<p>5 stelle su 3 recensioni Google verificate.</p>',"revlab")
newrv='''<div class="rv-grid">
      <div class="rv"><div class="st">★★★★★</div><p>“Cortesia e professionalità rendono perfetto questo salone.”</p><div class="who"><div><b>Fiorella R.</b><span>recensione Google</span></div></div></div>
      <div class="rv"><div class="st">★★★★★</div><p>“Bravissima, sempre gentile e precisa. Consigliata.”</p><div class="who"><div><b>Dorotea P.</b><span>recensione Google</span></div></div></div>
      <div class="rv"><div class="st">★★★★★</div><p>“Cliente affezionata: mi trovo sempre benissimo.”</p><div class="who"><div><b>Fabio C.</b><span>recensione Google</span></div></div></div>
    </div>'''
A=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>', newrv+"\n  </div>\n</section>", A, count=1, flags=re.S)
newhours='''<ul class="hours-list" id="hoursList">
          <li data-day="1"><span class="d">Lunedì</span><span>Chiuso</span></li>
          <li data-day="2"><span class="d">Martedì</span><span>Su appuntamento</span></li>
          <li data-day="3"><span class="d">Mercoledì</span><span>Su appuntamento</span></li>
          <li data-day="4"><span class="d">Giovedì</span><span>Su appuntamento</span></li>
          <li data-day="5"><span class="d">Venerdì</span><span>Su appuntamento</span></li>
          <li data-day="6"><span class="d">Sabato</span><span>Su appuntamento</span></li>
          <li data-day="0"><span class="d">Domenica</span><span>Chiuso</span></li>
        </ul>'''
A=re.sub(r'<ul class="hours-list" id="hoursList">.*?</ul>', newhours, A, count=1, flags=re.S)
A=rep(A,"const periods={1:[830,1500],2:[900,1800],3:[900,1800],4:[1200,2100],5:[900,1800],6:[800,1600],0:null};","const periods={1:null,2:null,3:null,4:null,5:null,6:null,0:null};","periods")
A=rep(A,'<p style="margin-bottom:8px"><a href="tel:+393335037075">333 503 7075</a></p>\n        <p style="margin-bottom:8px"><a href="mailto:deguidisilvia@gmail.com">deguidisilvia@gmail.com</a></p>\n        <p><a href="https://maps.google.com/?cid=3290711706439048689" target="_blank" rel="noopener">Via Golosine 117, 37136 Verona →</a></p>',
 '<p style="margin-bottom:8px"><a href="tel:+390456150312">045 615 0312</a></p>\n        <p><a href="'+MACID+'" target="_blank" rel="noopener">Via Strà 94, Colognola ai Colli (VR) →</a></p>',"footcontacts")
A=rep(A,"<p>Parrucchiere unisex a Verona, zona Golosine. Taglio, colore, acconciature sposa e trattamenti con prodotti di qualità.</p>","<p>Parrucchiera a Colognola ai Colli, Via Strà. Taglio, colore, piega e acconciature con cura e cortesia.</p>","footdesc")
A=rep(A,"<span>© 2026 Silvia De Guidi Capelli · Verona</span>","<span>© 2026 Maschi Stefania · Colognola ai Colli (VR)</span>","footbot")
A=A.replace("tel:+393335037075","tel:+390456150312").replace("333 503 7075","045 615 0312")
A=A.replace("Silvia De Guidi","Maschi Stefania").replace("SILVIA DE GUIDI","MASCHI STEFANIA")
open("maschi-stefania-colognola.html","w",encoding="utf-8").write(A); print("4 maschi-stefania-colognola.html",len(A))

# WA links for queue/CRM (mobile leads only)
print("KIME_WA="+walink("393470903503",BASE+"kimes-hair-colognola.html"))
print("SUSY_WA="+walink("393472445676",BASE+"parrucchiera-susy-colognola.html"))
