# -*- coding: utf-8 -*-
import re, json, urllib.parse
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def photo(ref,w=1200): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={KEY}"
def rep(html,old,new,label):
    if old not in html: print(f"  !! MISS [{label}]")
    return html.replace(old,new)
BASE="https://hubtecit-srl.github.io/website/"
DATA="2026-07-27"
WATXT=("Buongiorno,\nSono Laura di HubTec, azienda di Verona.\n\n"
 "Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
 "Se vi piace, lo attiviamo con soli 200€.\n\n"
 "In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
 "Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
 "Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\nLaura Borin - HubTec")
def walink(intl,url): return "https://wa.me/"+intl+"?text="+urllib.parse.quote(WATXT.format(url=url))
S1="https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800"
S2="https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800"
S3="https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800"

########## LEAD A: Parrucchiera Ilaria — silvia template ##########
IL_P1="AWCwydguQfnr_r9Qs_-8eeIzfG4a7pOm0UHdhht-PadP9HIZ2NdtCiOswTBY3X1PwcvcsuMOd4-OyHplMXDWZ5fwf4NoQji8O2r1t3I0zSdfCkgxpuiI_jIagOBig1lp3mjA6XRLZr1OAjGsalsB4Wn4GMALx7c3u_EvvarbtknU4lqZ-2BAHcJd-ga-pRgeYrxF85G0jL2FEI9kd2vYcAhXCLazsa1y7pxfIlDgWOLvFMmxS9cHf_b69TmhA5BGFQAtcCL93ZwObgK5oEppwTDG3V56F95eFNdOiqPH9a7CZYb3ZSzN-Qz4QE89hLMjIJdhRnuMFx_yAXuW5KuUJ61V_A2SJGYIgwzwhZbABHlXOaxLQb-LE4tm7y-XYJa2tgcDIrsbQgovnWdK1DlwfyDGE2rNHOrDb4STCE-3fc4"
IL_P2="AWCwydhvhFH_4oVzgJkx2fd2k5oEgXN-SGeyt4_YyG59lQ5qtSLUy8du3K7dVH0oDGKdxOUQ2fM5PFsTv-iPlt_5yLt-yYzVjiq1-zlIIyjqhKmunWN7lMCHkxmCexYVgN3YjQ1zf3fKv1Kr7ncGW4dtj8lVfnSGJC5F_PsYE-1uBF0p6DWIG4gTqyya5u4Eh_xfctkL_Or2vrDIeRriwSUtBoKG4ixhZkpr6aDgsiJpQaexkJOYefPqOZbLekorpSbHEhsFsnmK0UJuYd0RJGB1KvFg5mPBfrdTNrah628-3b-bzAObxIcObcaJcmEbI7ozgSa1QU113Ke1S6NoP3TmjFElZJPx-dNAA0RE-76VolCbTT2UuibP4RxCNHW3QZ4IOng1A8ienfcihj2Eh1z0m3D3jvjOhCHi3mK2g2VnZXIZ6CJr"
IL_P3="AWCwydjvLkL9tKtXlOjMsvHukBwtAGxVmuNUUERA5r7lJSZGumfs7ZGFAxrGIkgyuTFOF6FEvTg8jNvxZAz5ruG5j1KfNjQjmfAglKSBysBwVV7JzTmSSMLdhBM4wVhSavJ8BeV3LXoIm8gMXrx_-wrsTj17DXsAEyp9WvVJwM7z8VxRNp5LyrkcaSZxmvBu4_sa9qyHqmdoFaAnPif6j2ZWoQMJQOr6pSFS07xsucCArqrIdrD0wotvVGJXdSfO_5gwjmhcQmk-GrclM8L_0q6_RD8kDzpRvpeN5CdwcGS-m7tUgWEwt1wAPHdr6G7rrBDWAYRDnvVSEmS7uIDd3MF_k1J2LhniacsaMlxsceswm3XItzf_znlxfBEMsuPLvsfgGHp0Wl5ZmXKk-UdlmzbcH_TejvSvuHs7kBa0qLwnBOzV_mMm"
A=open("silvia-de-guidi-capelli-verona.html",encoding="utf-8").read()
ILCID="https://maps.google.com/?cid=9394358184494081475"
A=rep(A,"<title>Silvia De Guidi Capelli — Parrucchiere a Verona (Golosine)</title>","<title>Parrucchiera Ilaria — Parrucchiere a Caldiero (Strà-Montanara) | Prenota</title>","title")
A=rep(A,'content="Silvia De Guidi Capelli, parrucchiere a Verona in Via Golosine 117. Taglio, colore, acconciature sposa e trattamenti. 4,9★ su 71 recensioni. Prenota.">','content="Parrucchiera Ilaria a Caldiero (Strà-Montanara-Pieve): taglio, colore, acconciature e trattamenti. 4,9★ su 37 recensioni Google. Chiama e prenota.">',"desc")
# hero bg (1600) + float (200)
A=re.sub(r'(maxwidth=1600&photo_reference=)[^&]+', r'\g<1>'+IL_P1, A, count=1)
A=re.sub(r'(maxwidth=200&photo_reference=)[^&]+', r'\g<1>'+IL_P2, A, count=1)
A=rep(A,'<a href="#" class="brand"><span class="mk"></span>SILVIA DE GUIDI</a>','<a href="#" class="brand"><span class="mk"></span>PARRUCCHIERA ILARIA</a>',"brand")
A=rep(A,'<div class="tag"><b>#01</b> Parrucchiere · Verona Golosine</div>','<div class="tag"><b>#01</b> Parrucchiera · Caldiero (VR)</div>',"tag")
A=rep(A,'<h1 class="display">Silvia<br>De Guidi</h1>','<h1 class="display">Parrucchiera<br>Ilaria</h1>',"h1")
A=rep(A,'<p class="sub">Taglio, colore e acconciature su misura — studiati sul tuo viso, sul tuo capello e sullo stile che desideri davvero.</p>','<p class="sub">Taglio, colore, piega e acconciature con cura, simpatia e prezzi onesti. Un salone dove ti senti subito a casa, a Strà di Caldiero.</p>',"sub")
A=rep(A,'<small>4,9 / 5 · 71 recensioni Google</small>','<small>4,9 / 5 · 37 recensioni Google</small>',"badge")
A=rep(A,'<p>4,9 stelle su 71 recensioni Google verificate.</p>','<p>4,9 stelle su 37 recensioni Google verificate.</p>',"revlab")
# gallery4 wholesale
A=re.sub(r'<div class="gallery4">.*?</div>\s*</div>\s*</section>',
 '<div class="gallery4">\n'
 f'      <img loading="lazy" src="{photo(IL_P3,700)}" alt="Lavoro capelli">\n'
 f'      <img loading="lazy" src="{S1}" alt="Ambiente salone">\n'
 f'      <img loading="lazy" src="{S2}" alt="Piega e styling">\n'
 f'      <img loading="lazy" src="{S3}" alt="Colore">\n'
 '    </div>\n  </div>\n</section>', A, count=1, flags=re.S)
# reviews (real)
newrv='''<div class="rv-grid">
      <div class="rv">
        <div class="st">★★★★★</div>
        <p>“Fantastica, professionale, rapida. Ha sempre modo di trovare tempo per chiunque, splendida nel dare consigli su taglio e colore. Consigliatissima anche per i prezzi!”</p>
        <div class="who"><img src="https://lh3.googleusercontent.com/a/ACg8ocLHjwwXXRvEhzwZFmWShLUV0976bqNZa2S7VOMpac223Sv3-Q=s128-c0x00000000-cc-rp-mo" alt="Chiara"><div><b>Chiara Olivieri</b><span>recensione Google</span></div></div>
      </div>
      <div class="rv">
        <div class="st">★★★★★</div>
        <p>“Ilaria molto simpatica, spigliata e brava. Sono molto contenta delle acconciature e del colore che mi propone. La consiglio a chi vuole provare.”</p>
        <div class="who"><img src="https://lh3.googleusercontent.com/a/ACg8ocKN6L6pN2bj1CZRvdxockL13jEwx8y4CPl3pEVtIGcBT3JTbw=s128-c0x00000000-cc-rp-mo-ba2" alt="Daniela"><div><b>Daniela Antonelli</b><span>recensione Google</span></div></div>
      </div>
      <div class="rv">
        <div class="st">★★★★★</div>
        <p>“Il top che si possa desiderare: puntualità, professionalità e simpatia. Consigliatissima!”</p>
        <div class="who"><img src="https://lh3.googleusercontent.com/a-/ALV-UjWPiQ8McN5PaYqxXQ-Fejazqw0CjH3OEIdArzRSY7Zrui8hg5SJSQ=s128-c0x00000000-cc-rp-mo-ba3" alt="Luigia"><div><b>Luigia Caruso</b><span>recensione Google</span></div></div>
      </div>
    </div>'''
A=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>', newrv+"\n  </div>\n</section>", A, count=1, flags=re.S)
# hours list + periods
newhours='''<ul class="hours-list" id="hoursList">
          <li data-day="1"><span class="d">Lunedì</span><span>Chiuso</span></li>
          <li data-day="2"><span class="d">Martedì</span><span>Chiuso</span></li>
          <li data-day="3"><span class="d">Mercoledì</span><span>08:00–12:00 · 15:30–18:00</span></li>
          <li data-day="4"><span class="d">Giovedì</span><span>08:00–12:00 · 15:30–18:00</span></li>
          <li data-day="5"><span class="d">Venerdì</span><span>08:00 – 18:00</span></li>
          <li data-day="6"><span class="d">Sabato</span><span>08:00 – 18:00</span></li>
          <li data-day="0"><span class="d">Domenica</span><span>Chiuso</span></li>
        </ul>'''
A=re.sub(r'<ul class="hours-list" id="hoursList">.*?</ul>', newhours, A, count=1, flags=re.S)
A=rep(A,"const periods={1:[830,1500],2:[900,1800],3:[900,1800],4:[1200,2100],5:[900,1800],6:[800,1600],0:null};","const periods={1:null,2:null,3:[800,1800],4:[800,1800],5:[800,1800],6:[800,1800],0:null};","periods")
# contacts footer
A=rep(A,'<p style="margin-bottom:8px"><a href="tel:+393335037075">333 503 7075</a></p>\n        <p style="margin-bottom:8px"><a href="mailto:deguidisilvia@gmail.com">deguidisilvia@gmail.com</a></p>\n        <p><a href="https://maps.google.com/?cid=3290711706439048689" target="_blank" rel="noopener">Via Golosine 117, 37136 Verona →</a></p>',
 '<p style="margin-bottom:8px"><a href="tel:+393479358389">347 935 8389</a></p>\n        <p><a href="'+ILCID+'" target="_blank" rel="noopener">Via Montanara 24, Strà-Montanara-Pieve, Caldiero (VR) →</a></p>',"footcontacts")
A=rep(A,"<p>Parrucchiere unisex a Verona, zona Golosine. Taglio, colore, acconciature sposa e trattamenti con prodotti di qualità.</p>","<p>Parrucchiera a Caldiero, zona Strà-Montanara. Taglio, colore, piega, acconciature e trattamenti con cura e prezzi onesti.</p>","footdesc")
A=rep(A,"<span>© 2026 Silvia De Guidi Capelli · Verona</span>","<span>© 2026 Parrucchiera Ilaria · Caldiero (VR)</span>","footbot")
# global phone/name cleanup
A=A.replace("tel:+393335037075","tel:+393479358389").replace("333 503 7075","347 935 8389")
A=A.replace("Silvia De Guidi","Parrucchiera Ilaria").replace("SILVIA DE GUIDI","PARRUCCHIERA ILARIA")
open("parrucchiera-ilaria-caldiero.html","w",encoding="utf-8").write(A)
print("A written parrucchiera-ilaria-caldiero.html", len(A))

########## LEAD B: Molinari Ornella — salonkit template ##########
MO_P1="AWCwydhldgmSj3B8IbDT6lr6AXGYjIwFRzufbf4BBfK3bCcdblDGcbDhbVIn6rX6r4qweJUNQ0cZkjBfRccPJiKQxSG7PehWBWmbI3ji3wovRwNYdZPTtCHlv7F9Kj-WWT1aGtI676GqrseFw7lhkAoedTznX8J3ORLhRSrdLWYXg6jBZBGHTDK4AnxkK8jPkDov5S3A_LWZgX3pzbYWZRuFg-A8xFM5CCDffHQbtt0K4eM9ZorH93FQhY6vg0RCxke2KRI4v3VRz7Sm1q9ID8gTB7vMIO1o_7v5bOxh9U-gQN4u9jjp_dMb0Ck8DXdREy3vZT6K6YlcUuifnnRlwdooK2tVq0JXrajoLZQpz_jaqjY1DSkyw7w2CyVe4zhIO_djBtMtwhcJxP9oGFCo__eRai6pfFI3SriBzODIbmRaU2qTlg"
MO_P2="AWCwydjBZ4BxOv8SErVmyrXsBskHZk8UH0UAJM00uJAoPoI8UmKuD1q6um-NRyGEdlM5GGR9BAlSJ3HXtixJxJtjxfX7aePfiTrQHMzYPbQE80UCxJoEEdo74vcNt2GbQ4dzQltEkJkzpjI-PNHE91oavBtkLO31vVyIJDeVsBDeFEHVv614Mi87ooiVnVoykcx7H46JPonKNj6arsHQU8_ZwKd3GwCI2-GQnkb9hfgTqfnJBRZs8XA_OIgZ7MgaBhmN9ltMCuQT8B744O5VXMfoJxgulBSWf2UnUznLkWSskRm3NCFNSlNGibfukWJT1-6fbqhnlb0flA8Du5OBaz5RHCVKZKMpCTLQci6rR6iAVAEVef-1kddSoHBpHAzZmrWtqt7PvsrXkyKAqku0x5CKj0Go9CS0Rp8D8j8OB8hzkeXfsg"
B=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
MOCID="https://maps.google.com/?cid=14581294625844458251"
B=rep(B,"<title>Salone Méta — Parrucchiere a Verona | Prenota</title>","<title>Molinari Ornella — Parrucchiera a Caldiero | Prenota</title>","title")
B=rep(B,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="Parrucchiera Molinari Ornella a Caldiero (Caldierino-Rota): taglio, colore, meches e trattamenti. 4,8★ su Google. Chiama e prenota il tuo appuntamento.">',"desc")
B=rep(B,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiera · Caldiero (VR)</span>',"kick")
B=rep(B,"<h1>Dove l'hairstyling è <em>olistico</em></h1>","<h1>Il tuo look, <em>curato</em> nei dettagli</h1>","h1")
B=rep(B,"<p>Taglio, colore e trattamenti pensati per te e per la salute dei tuoi capelli. Un salone dove bellezza e benessere si incontrano.</p>","<p>Taglio, colore, piega e trattamenti su misura. Ornella ti ascolta, capisce e valorizza il tuo stile, a Caldierino-Rota.</p>","herop")
B=rep(B,'<div class="hero-img"><img src="https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000" alt="Salone di parrucchiere"></div>',f'<div class="hero-img"><img src="{photo(MO_P1)}" alt="Salone Molinari Ornella"></div>',"heroimg")
B=rep(B,'<img src="https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Lavoro 1">',f'<img src="{photo(MO_P2,800)}" alt="Il salone">',"gal1")
# reviews
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Taglio perfetto e colore stupendo. Mi trovo benissimo ogni volta."</p><b>Serena B.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Super soddisfatta di tutti i trattamenti! Taglio perfetto, piega stupenda, colore meraviglioso. Ornella sa ascoltare e valorizzare ogni richiesta."</p><b>Federica B.</b></div>',"rv1")
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente rilassante e staff super professionale. Consigliatissimo."</p><b>Marta L.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Professionalità, gentilezza, cordialità e disponibilità. Un salone dove tornare sempre."</p><b>Angela P.</b></div>',"rv2")
B=rep(B,'<div class="rv"><div class="st">★★★★★</div><p>"Finalmente un salone che cura davvero i capelli. Bravissimi!"</p><b>Chiara V.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Bravissima, da consigliare sicuramente. Un momento di benessere ogni volta."</p><b>Valeria M.</b></div>',"rv3")
# footer contacts + hours
B=rep(B,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>',
 '<div><h4>Contatti</h4><p><a href="'+MOCID+'" target="_blank">Via Caldierino 54, Caldierino-Rota, Caldiero (VR)</a><br><a href="tel:+393886492751">388 649 2751</a><br><a href="https://wa.me/393886492751">WhatsApp</a></p></div>',"footc")
B=rep(B,"<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>","<div><h4>Orari</h4><p>Gio–Ven 8:30–12:30 · 15:00–19:00<br>Sab 8:00–16:00</p></div>","footh")
B=rep(B,"<div><div class=\"brand\" style=\"color:#fff\">Salone Méta</div><p>Parrucchiere olistico nel cuore di Verona.</p></div>","<div><div class=\"brand\" style=\"color:#fff\">Molinari Ornella</div><p>Parrucchiera a Caldiero, zona Caldierino-Rota.</p></div>","footbrand")
B=rep(B,"<div class=\"foot-bot\"><span>© Salone Méta — Verona</span><span>Sito realizzato da HubTec</span></div>","<div class=\"foot-bot\"><span>© Molinari Ornella — Caldiero (VR)</span><span>Sito realizzato da HubTec</span></div>","footbot")
B=B.replace("tel:+390450000000","tel:+393886492751").replace("045 000 0000","388 649 2751").replace("https://wa.me/390450000000","https://wa.me/393886492751")
B=B.replace("Salone Méta","Molinari Ornella")
open("parrucchiera-molinari-ornella-caldiero.html","w",encoding="utf-8").write(B)
print("B written parrucchiera-molinari-ornella-caldiero.html", len(B))

########## LEAD C: Betty Acconciature — revival template (landline / mano) ##########
C=open("parrucchieri-revival-flagship.html",encoding="utf-8").read()
BECID="https://maps.google.com/?cid=17005739071905855816"
C=rep(C,"<title>Revival Hair Studio — Parrucchiere a Verona | Prenota</title>","<title>Betty Acconciature — Parrucchiere a Caldiero (VR) | Chiama</title>","title")
C=rep(C,'content="Revival Hair Studio, parrucchiere a Verona: taglio, colore e styling d\'autore. Un salone dal design minimal ed elegante. 4,9★ su 180 recensioni. Prenota.">','content="Betty Acconciature a Caldiero (Via Strà): taglio, colore, colpi di sole e mesh. 4,8★ su Google. Chiama per il tuo appuntamento.">',"desc")
C=rep(C,'<a href="#top" class="brand">REVIVAL</a>','<a href="#top" class="brand">BETTY</a>',"brand")
C=rep(C,'<span class="kick">Hair Studio · Verona</span>','<span class="kick">Parrucchiere · Caldiero (VR)</span>',"kick")
C=rep(C,"<h1>Revival</h1>","<h1>Betty Acconciature</h1>","h1")
C=rep(C,"<p>Taglio, colore e styling d'autore. Un salone dove l'eleganza incontra la cura del dettaglio.</p>","<p>Taglio, colore, colpi di sole e mesh. Betty e Serena ti mettono a proprio agio e consigliano la soluzione giusta per te.</p>","herop")
C=rep(C,"<h2>Uno studio dedicato allo stile, in ogni dettaglio</h2>","<h2>Professionalità, cordialità e prezzi onesti, nel cuore di Caldiero</h2>","introh2")
C=rep(C,"<p>Un ambiente essenziale ed elegante, pensato per farti vivere un'esperienza di bellezza fuori dal comune. Professionisti attenti, tecniche moderne e ascolto.</p>","<p>Un salone accogliente e pulito, dove ogni cliente è seguito con attenzione. Tecniche di colore, colpi di sole e mesh personalizzate, sempre con il sorriso.</p>","splitp")
C=re.sub(r'<ul class="split-hours">.*?</ul>',
 '<ul class="split-hours">\n        <li><span>Martedì – Sabato</span><span>Su appuntamento</span></li>\n        <li><span>Domenica &amp; Lunedì</span><span>Chiuso</span></li>\n      </ul>', C, count=1, flags=re.S)
# reviews
C=rep(C,"<q>Un salone diverso da tutti. Eleganza, competenza e un taglio impeccabile.</q>","<q>Taglio e colore con mesh spettacolari. Betty e Serena professionali e cordiali, sanno consigliare le migliori soluzioni.</q>","bigq")
C=rep(C,"<b>Beatrice C.</b>","<b>Carmen T.</b>","bigqb")
newarv='''<div class="rv-row">
      <div class="c rv"><div class="st">★★★★★</div><q>"Ottima esperienza, bei colpi di sole e taglio preciso. Grande disponibilità e competenza, oltre a prezzi onesti. Consiglio!"</q><b>Arianna A.</b></div>
      <div class="c rv"><div class="st">★★★★★</div><q>"Bravissime! Sempre gentili e attente. Esco sempre soddisfatta."</q><b>Marta M.</b></div>
    </div>'''
C=re.sub(r'<div class="rv-row">.*?</div>\s*</div>\s*</section>', newarv+"\n  </div>\n</section>", C, count=1, flags=re.S)
# CTA (no whatsapp - landline)
C=rep(C,"<p>Chiamaci o scrivici su WhatsApp: dai forma al tuo nuovo look.</p>","<p>Chiamaci per fissare il tuo appuntamento: ti aspettiamo a Caldiero.</p>","ctap")
C=rep(C,'<a href="tel:+390450000000" class="btn btn-light">045 000 0000</a>\n      <a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>','<a href="tel:+390456151817" class="btn btn-light">Chiama 045 615 1817</a>\n      <a href="'+BECID+'" target="_blank" class="btn btn-ghost">Come raggiungerci</a>',"ctabtns")
# footer contacts
C=rep(C,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@revivalhair.it">info@revivalhair.it</a></p></div>',
 '<div><h4>Contatti</h4><p><a href="'+BECID+'" target="_blank">Via Strà, Caldiero (VR)</a><br><a href="tel:+390456151817">045 615 1817</a></p></div>',"footc")
C=rep(C,"<div><h4>Orari</h4><p>Mar–Ven 9:00–19:00<br>Sab 9:00–18:00</p></div>","<div><h4>Orari</h4><p>Mar–Sab su appuntamento<br>Lun &amp; Dom chiuso</p></div>","footh")
C=rep(C,'<div><div class="brand" style="color:#fff;letter-spacing:.22em">REVIVAL</div><p>Hair studio d\'autore nel cuore di Verona.</p></div>','<div><div class="brand" style="color:#fff;letter-spacing:.22em">BETTY ACCONCIATURE</div><p>Parrucchiere a Caldiero, in Via Strà.</p></div>',"footbrand")
C=rep(C,"<span>© Revival Hair Studio — Verona</span>","<span>© Betty Acconciature — Caldiero (VR)</span>","footbot")
C=C.replace("tel:+390450000000","tel:+390456151817").replace("045 000 0000","045 615 1817")
C=C.replace("Revival Hair Studio","Betty Acconciature").replace(">Revival<",">Betty Acconciature<")
open("betty-acconciature-caldiero.html","w",encoding="utf-8").write(C)
print("C written betty-acconciature-caldiero.html", len(C))

# WA links for CRM/queue
print("ILARIA_WA", walink("393479358389", BASE+"parrucchiera-ilaria-caldiero.html")[:60],"...")
print("MOLINARI_WA", walink("393886492751", BASE+"parrucchiera-molinari-ornella-caldiero.html")[:60],"...")
