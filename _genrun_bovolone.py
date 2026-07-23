# -*- coding: utf-8 -*-
import re
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def photo(ref): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={ref}&key={KEY}"
def rep(html, old, new, label):
    if old not in html: print(f"  !! MISS [{label}]")
    return html.replace(old,new)

# ---------- photo refs ----------
MAR=["AWCwydgn7NPPOLV_Slsoyoof9pYLRR1pKwMjApSC1xbJzAzkmd23Hc2PeCfuKEMCtVBxPs0ECPzvZGiWNPUqX2Ulm1sM91hqbn-JfS4SyT7tfFVEA8m8G8fNQ3lKcrJnLXB-0yJoB0E4Bqt2L3HVhYIALK1k7w48Rv1tFWvhBgX2DdHfWKLzYR-rCxFoMzCWJMt9C0bQazP1X1IGytdAVkT6jSqqfrRZ_yQFWPkuDPdbeNQTipFW3rNzVCZfNNXJFGUfkztJ0Jea6OOkesWpLSXbHstLxaeAbdENOGG0cD1KpEIekxLLEUyCGeOCvUseJar0tFrKIVPFXD7tDVp-Ha7A6MXpMHiCgLvvtgk3Og5E65FHLs51LARqjX3YPWoYdWziMivWHw2LPBBEJYJtbNHfffaVEPb1_--6dXYud3F4a2rb0If9fRwjbe5Em6RChEdB",
"AWCwydiy2C4DEzJPAIj7Y3HOsUGGDrlFATF6S2Yfg8ZY98ux-yEJSqBMH7drLisA7uZAiaPAiDt2oSS2gA0HrP_d_RM0idqkJyS80_ecJPF1OzITKEYwSZETn0XbUfJ0s_cCq1xNJkoDnlp53T40fxMVuJ6pSDqLK3cql8VNAgeXgPQ9SJIE9JeWnQ9V9hbxRMGTACyN4ci0gaKUpX1DkrB3d7Ns1RtFUgcEzj5FV8gM__pPmli-paDlbjZk5VJRbSKFR0lzSX0wAL1kdfZkpou66-u47QRuHGqR1_b4jYaiKweHZSmFlJ7Vkh8wli4fCtYlYpLBy6cXYnCPMvndDHFnfAhOW-ipunBq5UCj-TH1uI27VbfFiwH6Kc-j2mRwNwjUk_lp_oJV4ABxQ6x6YTlghGUCkD8D8XtxTYBXw8LJS7zruDTVp5SBzw-yOQdz6g"]
LUX=["AWCwydjEpuExgO5_U_w4QMHFEIMFqw0aCfUptOMLO0B7zdDHV8U915CDQx-l_balJiBQPqsv7alJ6EptD_REeWnsM4IGIZiQxMf7MfLMYnHS3PnrHH5U-tjRXpfJWVjkZQUvBtUtmZE070kcx5Zn7IqIXeNqu7Ge82DNq6PcRFEceoBRa7kJjpToe67wI7Nz8EMP787Q5q0VXpykmkFWOof5FhRfO7Z6c806wub4StH1Kiso6L4xMwsdOH4Vhdg_owE1SN3j-fQ_pXsj4ytCHx9i3qVnsJre23prl6rck4Wp4UW3lE7YU_uK6Pfuy50Xq_sdsUf5Yyydfqdd4TtNuF9Ogrsj1wWy0PUhPTUva01g_-hKHPGt1G1XOYpzebQFkfuieEoiqJmsG3PXobxacvf_5HESW0NI9HeGjzbhxVbllnJYsJe0ahSX356X9VXixtjA",
"AWCwydiIzGv2E2DkWXccgpoO4DMkEGYBNnpO4tihtBapZjZePvnJNvDLapdNOfm16fPIJS9A1dlMIJ1IdeU51CniwvQUEWpYb717eyD5D8t8quWW8wuxhp8RCe0is8uQD9a-J6EzlmXorKlLWj0T-Uc5e4zJVNzFf81afmZJ23Eg-r97DBKO1zhplj16no2J86QBgtqa9CQuSXI5t_o609xpUdb81xcW48EE9-vNjMurKXPIcneX_PDqmkXQBMAvRFZi_XFvlDR-FTK6_rcRSp18it4UdE3ZNNtHbrJYmIThqaAEL9TkhXJwPZNJqFQMimkrPhxn0kyP1ObN4r04G3Su-9lG6MrEcOZhejVyfWt7tw6H-eRuv2NODCPme4VBewmVL07a2QCEOPhSGUvdWwXDj8zHPSzNFjZ4hA1T7XVa26-So0ZBKVxoWsQXmLv5k40Z"]
GIN=["AWCwydhxdYGqZKCH6p2AlJGSMnt-xW6fvj-woinoS97l56wcgj0YRAhUXEgCQic6pxS8nrCoiAuVdS_MMJfpAOvEv9MiNBq_jj9bz6HRq8DKCz0UEt3oqWsoL3dkIbbjoPhuxcSb8XGVidyMj24UatMwk-DM1vv3doaLLJPGz8WylgqbOPpinP8386VFGUVxrJphXkTxs_ceTSrQ6-aYOl-jkciQJwwPFtXBsDnpTRoKAsqauSYX_y1B-b9h6PGTv5eZVUXsjg90DSPr0TE7V7TuZaT5UjuVIawAVTt3piXcqJ2O5DQNpSQxD4mfUcF6IuTinr_wm57H0NZXB8OkCrl4meP3LOni6aAuMR6cQ-qjLNk1RtqKnu5Bz8z9LQSop4-4iKD7370RyGYWfd8vieTcjSsLsCmmzl0icIktZfrj95xsTbl6"]

# ================= MARINA -> revival =================
M=open("parrucchieri-revival-flagship.html",encoding="utf-8").read()
CID="https://maps.google.com/?cid=7696412374868271140"
M=rep(M,"<title>Revival Hair Studio — Parrucchiere a Verona | Prenota</title>","<title>Marina élite image — Parrucchiere a Bovolone (VR) | Prenota</title>","t")
M=rep(M,'content="Revival Hair Studio, parrucchiere a Verona: taglio, colore e styling d\'autore. Un salone dal design minimal ed elegante. 4,9★ su 180 recensioni. Prenota.">','content="Marina élite image, parrucchiere a Bovolone (VR): taglio, colore, piega e cura del capello. 5,0★ su Google. Prenota il tuo appuntamento.">',"d")
M=rep(M,"© Revival Hair Studio — Verona","© Marina élite image — Bovolone (VR)","cp")
M=M.replace(">REVIVAL<",">Marina élite image<")
M=rep(M,"<span class=\"kick\">Hair Studio · Verona</span>","<span class=\"kick\">Parrucchiere · Bovolone (VR)</span>","k")
M=rep(M,"<h1>Revival</h1>","<h1>Marina élite image</h1>","h1")
M=rep(M,"https://images.pexels.com/photos/3993462/pexels-photo-3993462.jpeg?auto=compress&cs=tinysrgb&w=1600",photo(MAR[0]),"hero")
M=rep(M,"background:#ddd url('https://images.pexels.com/photos/3992874/pexels-photo-3992874.jpeg?auto=compress&cs=tinysrgb&w=1000') center/cover",f"background:#ddd url('{photo(MAR[1])}') center/cover","split")
M=rep(M,"<h2>Uno studio dedicato allo stile, in ogni dettaglio</h2>","<h2>Un salone dedicato a te e alla cura dei tuoi capelli</h2>","i2")
M=rep(M,'''<ul class="split-hours">
        <li><span>Martedì – Venerdì</span><span>9:00 – 19:00</span></li>
        <li><span>Sabato</span><span>9:00 – 18:00</span></li>
        <li><span>Domenica &amp; Lunedì</span><span>Chiuso</span></li>
      </ul>''','''<ul class="split-hours">
        <li><span>Martedì</span><span>9:30 – 16:30</span></li>
        <li><span>Mercoledì</span><span>13:00 – 21:00</span></li>
        <li><span>Giovedì</span><span>12:00 – 20:00</span></li>
        <li><span>Venerdì</span><span>9:00 – 18:30</span></li>
        <li><span>Sabato</span><span>8:30 – 16:30</span></li>
        <li><span>Domenica &amp; Lunedì</span><span>Chiuso</span></li>
      </ul>''',"hrs")
M=rep(M,"<q>Un salone diverso da tutti. Eleganza, competenza e un taglio impeccabile.</q>","<q>Negozio molto bello, accogliente e ben curato. Marina ti fa sentire protagonista, i suoi consigli sono preziosi.</q>","fq")
M=rep(M,"<b>Beatrice C.</b>","<b>Laura B.</b>","fb")
M=re.sub(r'<div class="rv-row">.*?</div>\s*</div>\s*</section>', '''<div class="rv-row">
      <div class="c rv"><div class="st">★★★★★</div><q>"Estremamente soddisfatta. Marina ha trattato il mio capello riccio con competenza. Colore su misura per me!"</q><b>Lisa T.</b></div>
      <div class="c rv"><div class="st">★★★★★</div><q>"Ambiente curato ed elegante, Marina ti sa sempre mettere a tuo agio. Professionalità e tanto relax."</q><b>Anna C.</b></div>
      <div class="c rv"><div class="st">★★★★★</div><q>"Marina è proprio professionale, brava a tagliare i capelli. Soddisfatta del taglio."</q><b>Franca B.</b></div>
    </div>
  </div>
</section>''', M, count=1, flags=re.S)
M=rep(M,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@revivalhair.it">info@revivalhair.it</a></p>',f'<p>Via Giuseppe Garibaldi 34, Bovolone (VR)<br><a href="tel:+393489361845">348 936 1845</a><br><a href="{CID}" target="_blank">Indicazioni</a></p>',"fc")
M=rep(M,"<p>Mar–Ven 9:00–19:00<br>Sab 9:00–18:00</p>","<p>Mar–Sab (vedi orari)<br>Lun &amp; Dom chiuso</p>","fh")
M=rep(M,"<p>Hair studio d'autore nel cuore di Verona.</p>","<p>Parrucchiere a Bovolone: taglio, colore e cura del capello.</p>","fp")
M=M.replace("+390450000000","+393489361845").replace("390450000000","393489361845").replace("045 000 0000","348 936 1845")
open("marina-elite-image-bovolone.html","w",encoding="utf-8").write(M)
print("marina-elite-image-bovolone.html",len(M))

# ================= LUXURY -> rhazor =================
L=open("parrucchieri-rhazor-flagship.html",encoding="utf-8").read()
CID="https://maps.google.com/?cid=1293378063526137771"
L=rep(L,"<title>Barberia Rasoio — Barbiere a Verona | Prenota</title>","<title>Luxury Barbershop — Barbiere a Bovolone (VR) | Prenota</title>","t")
L=rep(L,'content="Barberia Rasoio, barbiere a Verona: taglio uomo, rasatura tradizionale, barba e styling. 4,9★ su 200 recensioni. Prenota il tuo appuntamento.">','content="Luxury Barbershop, barbiere a Bovolone (VR): taglio uomo, barba, rasatura e styling. Prenota il tuo appuntamento.">',"d")
L=rep(L,'<a href="#top" class="brand">Barberia <b>Rasoio</b></a>','<a href="#top" class="brand">Luxury <b>Barbershop</b></a>',"navb")
L=rep(L,'<div class="brand">Barberia <b style="color:var(--gold)">Rasoio</b></div>','<div class="brand">Luxury <b style="color:var(--gold)">Barbershop</b></div>',"fb")
L=rep(L,"© Barberia Rasoio — Verona","© Luxury Barbershop — Bovolone (VR)","cp")
L=L.replace("Barberia Rasoio","Luxury Barbershop")
L=rep(L,'<span class="kick">Barbiere · Verona</span>','<span class="kick">Barbiere · Bovolone (VR)</span>',"k")
L=rep(L,"https://images.pexels.com/photos/1319460/pexels-photo-1319460.jpeg?auto=compress&cs=tinysrgb&w=1600",photo(LUX[0]),"hero")
L=rep(L,"https://images.pexels.com/photos/1570807/pexels-photo-1570807.jpeg?auto=compress&cs=tinysrgb&w=1000",photo(LUX[1]),"about")
L=rep(L,"<p>Via Esempio 12, Verona</p>","<p>Via Madonna 256, Bovolone (VR)</p>","ibaraddr")
L=rep(L,"<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>","<div><h4>Orari</h4><p>Lun 8:00–20:00<br>Mar–Ven 9:00–20:00<br>Sab e Dom chiuso</p></div>","foothrs")
L=rep(L,'<div class="c"><div><h4>Orari</h4><p>Mar–Sab 9:00–19:00</p></div></div>','<div class="c"><div><h4>Orari</h4><p>Lun–Ven · Sab e Dom chiuso</p></div></div>',"ibarhrs")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"Miglior barbiere di Verona. Taglio sempre perfetto e ambiente top."</p><b>Luca M.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Taglio uomo, barba e rasatura tradizionale in un ambiente curato e maschile."</p><b>Luxury Barbershop</b></div>',"rv1")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"La rasatura col panno caldo è un\'altra cosa. Bravissimi e simpatici."</p><b>Andrea P.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Servizio veloce e professionale, con cura del dettaglio. Anche senza appuntamento."</p><b>Luxury Barbershop</b></div>',"rv2")
L=rep(L,'<div class="rv"><div class="st">★★★★★</div><p>"Professionali, veloci e curati. Ci porto anche mio figlio."</p><b>Stefano R.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Prodotti professionali per capelli e barba. Aperto anche il lunedì."</p><b>Luxury Barbershop</b></div>',"rv3")
L=rep(L,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@barberiarasoio.it">info@barberiarasoio.it</a></p></div>',f'<div><h4>Contatti</h4><p>Via Madonna 256, Bovolone (VR)<br><a href="tel:+393791873762">379 187 3762</a><br><a href="{CID}" target="_blank">Indicazioni</a></p></div>',"fc")
L=L.replace("+390450000000","+393791873762").replace("390450000000","393791873762").replace("045 000 0000","379 187 3762")
open("luxury-barbershop-bovolone.html","w",encoding="utf-8").write(L)
print("luxury-barbershop-bovolone.html",len(L))

# ================= GINETTO -> salonkit =================
G=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
CID="https://maps.google.com/?cid=6623153073563273119"
G=rep(G,"<title>Salone Méta — Parrucchiere a Verona | Prenota</title>","<title>Parrucchiere Ginetto — Parrucchiere a Bovolone (VR) | Prenota</title>","t")
G=rep(G,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="Parrucchiere Ginetto, parrucchiere storico a Bovolone (VR): taglio donna e uomo (barber), colore e styling. 4,9★ su Google. Prenota.">',"d")
G=G.replace("Salone Méta","Parrucchiere Ginetto")
G=rep(G,"© Parrucchiere Ginetto — Verona","© Parrucchiere Ginetto — Bovolone (VR)","cp")
G=rep(G,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Bovolone (VR)</span>',"k")
G=rep(G,"<h1>Dove l'hairstyling è <em>olistico</em></h1>","<h1>Il tuo <em>parrucchiere</em> a Bovolone</h1>","h1")
G=rep(G,"<p>Parrucchiere olistico nel cuore di Verona.</p>","<p>Parrucchiere storico a Bovolone (VR): donna &amp; barber.</p>","fp")
G=G.replace("https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000",photo(GIN[0]))
G=rep(G,'<div class="rv"><div class="st">★★★★★</div><p>"Taglio perfetto e colore stupendo. Mi trovo benissimo ogni volta."</p><b>Serena B.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Parrucchiere storico di Bovolone, uno dei migliori. Ginetto sa essere molto umano e farti sentire a tuo agio."</p><b>Matteo C.</b></div>',"rv1")
G=rep(G,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente rilassante e staff super professionale. Consigliatissimo."</p><b>Marta L.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Parrucchiere bravissimo ed esperto, ci vado da 14 anni."</p><b>Brian G.</b></div>',"rv2")
G=rep(G,'<div class="rv"><div class="st">★★★★★</div><p>"Finalmente un salone che cura davvero i capelli. Bravissimi!"</p><b>Chiara V.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Un parrucchiere eccellente. Tagli sempre eccellenti e tanta cordialità."</p><b>Jacopo B.</b></div>',"rv3")
G=rep(G,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>',f'<div><h4>Contatti</h4><p>Via Giuseppe Garibaldi 79, Bovolone (VR)<br><a href="tel:+393495273243">349 527 3243</a><br><a href="{CID}" target="_blank">Indicazioni</a></p></div>',"fc")
G=rep(G,"<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>","<div><h4>Orari</h4><p>Mar–Ven 9:00–12:30 · 15:30–19:30<br>Sab 8:00–18:00 · Lun e Dom chiuso</p></div>","fh")
G=G.replace("+390450000000","+393495273243").replace("390450000000","393495273243").replace("045 000 0000","349 527 3243")
open("parrucchiere-ginetto-bovolone.html","w",encoding="utf-8").write(G)
print("parrucchiere-ginetto-bovolone.html",len(G))
