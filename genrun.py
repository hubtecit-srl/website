# -*- coding: utf-8 -*-
import re
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"

def R(html, old, new, req=True):
    if old not in html:
        if req: print("!! NOT FOUND:", repr(old[:70]))
        return html
    return html.replace(old, new)

# ---------- SITE 1: L'incanto -> estetica-anna ----------
h=open("estetica-anna-verona.html",encoding="utf-8").read()
p1="AWCwydjVEDCg2UOATSs_7-KaVEG42PYctG9kM-ZJqB-I-03tQlaljf0xZVftmgLkhp-tPAlkIlxozvbAjcC8VPjuC3xjtJ70bYYZN0RT3FSeqYrmUjJAIBw3ZGkpMreiE_rkgWmMvcFsimnxmyegY9KnPtfRyMC1oeLkhARvYgtZ1bzsxZ7j5yG6O467fXXuA7S2f_90Hy766LQh49ENwn0N8iFMcN5IAAmmwhHoKBSZneBRrChND9LbbpngvOqZsl_qYEETx1_Vse8FmeuxUkbjWr0dDK7Xa2N3g4aIoEB3aTISxGI2ddd1EvtorlNeODhV5sTuW7XIIVNVJJbMZGmUh8s4fAfGld2STkYAaZF-ne96DT7TFNlZTt70kcMvrBxqXthX-rjftihZOYYIrdbeY5ulpggf5z50U6dZ-pJqYMxkXD31"
p2="AWCwydgmhfDxyR9sDeBoZ_RBiXiUz6STUGGRt4o03kJZPN4nhOI_S1aQuYg56fMWK83-DwNUDHClOEUNn-5NyzfXMofqOeuFX70FaxPfZq0kqA9lqQBFC1NQKGQzxG61vsWs9talbRQlFJjca2e6CYyZKMvIsOIMT14-5iuMFuVeTYKSSaYAh5zgR6UIT8XvYyWtcH5Jh4AUHyuLwgq7e2-X7CYnDsjmsTxvZYejQKd4RZbtfrj8mwfFDZb2UmONbsnQ-pZEEO3mBJbujBOLzsUrhctQ1uruMl4SFQGdtMbXX2mWVjBOYALj6v7uGzR8Z9QiGFVZx75pdj6L5reR6JpOH2n_kL3WLXkkhXH5Ia7NxOw-MVbr37hHwGZHBOVtVOvLSHciCO6w_NeA-SGjE3Tq3OIQwIPiIFM5xV3MdwHMduA5UA"
p3="AWCwydhQbHXWeibFDgTMNQQJKsLmFaFgAok1sEBiti7ctDSPtViAjhr6V_9pFNvtC_Qxioc5GpFcn63eFBHtV6wPWKPn8f7NiUFX_tZATI4Xr7Eoj0cPzKMHNHZSptZj1BayLH2nrRdK7G6oXmFQRUXWrwkPSqusgEhAXeIHxLqz7ls7ejUWhO5jkBfnhMSwv9oY3RD0aDvusyamAiu1GchAf8E9DYfYBWlPv9ZiPeWQoW1HagGTlYM36Ff2e2Z7gqS7ZQcxPJP_ALsAxfmOsmzbtK7xLXzMFBETjX-zHT3al5yYR8EaYlqARvt4q_AD4eiNg2j9JOPMS6fF-R313qbreL0G_z4xFFRdcUalOvZbwOqSmyd7K5T8IgAM5EP-ZuITHyCK11h_bL9_gzFq-lDmESTKl1l9NXk4webR1MqYm_w"
refs=[p1,p2,p3]; cnt=[0]
def sub(m):
    r=refs[cnt[0]] if cnt[0]<len(refs) else refs[-1]; cnt[0]+=1
    return "photo_reference="+r
h=re.sub(r'photo_reference=[^&]+', sub, h)
print("photos replaced (anna):",cnt[0])
h=R(h,'<title>Estetica Anna — Centro estetico a Verona</title>','<title>L\'incanto Centro Estetico — Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Estetica Anna, centro estetico a Verona in Via Ghetto 63B. Trattamenti viso, corpo, sopracciglia e abbronzatura con prodotti naturali. 4,9★ su 109 recensioni."','content="L\'incanto Centro Estetico a Cologna Veneta (VR), Via Dante 5/G. Trattamenti viso, corpo, unghie ed epilazione. 4,7★ su 62 recensioni Google. Prenota il tuo appuntamento."')
h=R(h,'📞 045 862 1514','📞 340 825 5024')
h=R(h,'<div class="label">Centro estetico · Verona</div>','<div class="label">Centro estetico · Cologna Veneta</div>')
h=R(h,'Un angolo di benessere in Via Ghetto, dove','Un angolo di benessere in Via Dante, dove')
h=R(h,'<div class="c">4,9<small>★ 109 REC.</small></div>','<div class="c">4,7<small>★ 62 REC.</small></div>')
h=R(h,'· RECENSIONI GOOGLE · ESTETICA ANNA VERONA ','· RECENSIONI GOOGLE · L\'INCANTO CENTRO ESTETICO ')
h=R(h,'<h2>Un ambiente accogliente e curato, dove Anna e Maria mettono passione, gentilezza e prodotti naturali in ogni gesto.</h2>','<h2>Un ambiente accogliente e curato, dove Jessica ti accoglie con passione, professionalità e prodotti di qualità in ogni trattamento.</h2>')
h=R(h,'Da Estetica Anna troverai molto più di un trattamento: un ambiente rilassante e curato, dove ci si sente davvero a casa. Anna e Maria ti accolgono sempre con un sorriso e tanta competenza.','Da L\'incanto troverai molto più di un trattamento: un ambiente rilassante e curato, dove ci si sente davvero a casa. Jessica ti accoglie sempre con un sorriso e tanta competenza.')
h=R(h,'<div class="svc"><div class="n">iv</div><h3>Abbronzatura</h3><p>Lampada solare professionale Ergoline per un colorito sano e uniforme tutto l\'anno.</p></div>','<div class="svc"><div class="n">iv</div><h3>Epilazione</h3><p>Ceretta e trattamenti delicati per una pelle liscia e curata a lungo.</p></div>')
# testimonial
h=R(h,'Trattamento viso purificante e idratante, poi una maschera per borse e occhiaie. Tutti prodotti naturali, si sente la differenza sulla pelle sensibile. Anna ti fa sentire a tuo agio: consiglio a tutti!','Un luogo stupendo, in senso estetico e professionale: i massaggi di Jessica, la titolare, e della sua collaboratrice sono rilassanti e rigeneranti come non avevo mai provato. Accoglienza gentile e prezzo concorrenziale. Davvero complimenti!')
h=R(h,'https://lh3.googleusercontent.com/a-/ALV-UjVJN_yK6gvCMXEIgctNxEtCPSJdUPO1sgeQqBx10D0E9P6EmhQ=s128-c0x00000000-cc-rp-mo','https://lh3.googleusercontent.com/a-/ALV-UjVFGK96V9HYUucFy6Mruhev8RR_tDme2xXSZtMdV2ZmoyPQwI7h=s128-c0x00000000-cc-rp-mo-ba3')
h=R(h,'alt="Vittoria"','alt="Emanuela"')
h=R(h,'<b>Vittoria Toffalini</b>','<b>Emanuela Bellini</b>')
h=R(h,'“Bravissima e super precisa! Prezzi molto onesti, sincera nei consigli e ti mette a tuo agio. Ambiente super accogliente: ci si sente a casa!”','“Professionalità e cortesia. Mi sono trovata molto bene.”')
h=R(h,'<b>Stefania Morabito</b>','<b>Fabiola Soga</b>')
h=R(h,'“Centro estetico eccellente: gentilezza e professionalità di alto livello. Personale sempre accogliente. Ottima la lampada solare Ergoline!”','“Negozio accogliente con personale gentile e preparato. La titolare sa coccolare i suoi clienti facendoli sentire come a casa propria.”')
h=R(h,'<b>Davide Moletta</b>','<b>Andrea Pavanati</b>')
h=R(h,'Tutte le 109 recensioni su Google','Tutte le 62 recensioni su Google')
# hours
h=R(h,'<li data-day="1"><span class="d">Lunedì</span><span>09:00 – 18:30</span></li>','<li data-day="1"><span class="d">Lunedì</span><span>09:30 – 12:30</span></li>')
h=R(h,'<li data-day="2"><span class="d">Martedì</span><span>09:00 – 18:30</span></li>','<li data-day="2"><span class="d">Martedì</span><span>08:45 – 19:30</span></li>')
h=R(h,'<li data-day="3"><span class="d">Mercoledì</span><span>09:00 – 18:30</span></li>','<li data-day="3"><span class="d">Mercoledì</span><span>08:45 – 19:30</span></li>')
h=R(h,'<li data-day="4"><span class="d">Giovedì</span><span>09:00 – 18:30</span></li>','<li data-day="4"><span class="d">Giovedì</span><span>08:45 – 19:30</span></li>')
h=R(h,'<li data-day="5"><span class="d">Venerdì</span><span>09:00 – 18:30</span></li>','<li data-day="5"><span class="d">Venerdì</span><span>08:45 – 19:30</span></li>')
h=R(h,'<li data-day="6"><span class="d">Sabato</span><span>Chiuso</span></li>','<li data-day="6"><span class="d">Sabato</span><span>08:00 – 15:00</span></li>')
h=R(h,'const periods={1:[900,1830],2:[900,1830],3:[900,1830],4:[900,1830],5:[900,1830],6:null,0:null};','const periods={1:[930,1230],2:[845,1930],3:[845,1930],4:[845,1930],5:[845,1930],6:[800,1500],0:null};')
# email crow insert (before global tel replace)
h=R(h,'<div class="crow"><div class="ic">☎</div><div><h4>Telefono</h4><a href="tel:+390458621514">045 862 1514</a></div></div>','<div class="crow"><div class="ic">☎</div><div><h4>Telefono</h4><a href="tel:+390458621514">045 862 1514</a></div></div>\n        <div class="crow"><div class="ic">✉</div><div><h4>Email</h4><a href="mailto:jessica@incantoestetica.it">jessica@incantoestetica.it</a></div></div>')
h=R(h,'Via Ghetto 63 B, 37137 Verona (VR)','Via Dante 5/G, 37044 Cologna Veneta (VR)')
h=R(h,'src="https://www.google.com/maps?q=Via+Ghetto+63B,+37137+Verona&output=embed"','src="https://www.google.com/maps?q=Via+Dante+5G,+37044+Cologna+Veneta&output=embed"')
h=R(h,'<div class="foot-line">© 2026 Estetica Anna · Via Ghetto 63B, 37137 Verona · P.IVA da inserire</div>','<div class="foot-line">© 2026 L\'incanto Centro Estetico · Via Dante 5/G, 37044 Cologna Veneta (VR)</div>')
# globals
h=h.replace('4526940053737465846','14224630564653140029')
h=h.replace('tel:+390458621514','tel:+393408255024')
h=h.replace('045 862 1514','340 825 5024')
h=h.replace('✿</span>Estetica Anna','✿</span>L\'incanto')
open("lincanto-centro-estetico-cologna-veneta.html","w",encoding="utf-8").write(h)
print("wrote site1, remaining 'Estetica Anna':", h.count('Estetica Anna'), " 'Verona':", h.count('Verona'), " Ghetto:", h.count('Ghetto'))

# ---------- SITE 2: Zorzi Emanuela -> beautispa ----------
h=open("estetiste-beautispa-flagship.html",encoding="utf-8").read()
h=h.replace('3757942/pexels-photo-3757942','3852204/pexels-photo-3852204')
h=h.replace('3865676/pexels-photo-3865676','3979134/pexels-photo-3979134')
h=h.replace('3997989/pexels-photo-3997989','3973089/pexels-photo-3973089')
h=R(h,'<title>Bellessere Spa — Centro estetico &amp; SPA a Verona | Prenota</title>','<title>Zorzi Emanuela — Centro estetico a Cologna Veneta | Prenota</title>')
h=R(h,'content="Bellessere Spa a Verona: trattamenti viso, massaggi, corpo e percorsi benessere. 4,9★ su 160 recensioni. Prenota il tuo momento di relax."','content="Zorzi Emanuela, centro estetico a Cologna Veneta (VR): trattamenti viso e corpo, manicure e riflessologia. 4,9★ su 12 recensioni Google."')
h=R(h,'<a href="#top" class="brand">Bellessere Spa</a>','<a href="#top" class="brand">Zorzi Emanuela</a>')
h=R(h,'<span class="kick">Centro estetico &amp; Spa · Verona</span>','<span class="kick">Centro estetico · Cologna Veneta</span>')
h=R(h,'<p>Trattamenti viso e corpo, massaggi e percorsi benessere in un\'oasi di relax nel cuore di Verona.</p>','<p>Trattamenti viso e corpo, manicure e riflessologia in un ambiente accogliente a Cologna Veneta.</p>')
h=R(h,'Da Bellessere Spa ci prendiamo cura di te con trattamenti personalizzati, prodotti selezionati e mani esperte. Un luogo pensato per rigenerare corpo e mente.','Da Zorzi Emanuela ci prendiamo cura di te con trattamenti personalizzati, prodotti selezionati e mani esperte. Un luogo pensato per rigenerare corpo e mente.')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Un\'oasi di pace. Massaggio fantastico e personale attentissimo."</p><b>Valentina R.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Per me la migliore della zona: ti senti a casa quando entri. Prodotti validi, sempre aggiornata e professionale. Le sedute di riflessologia le consiglio a tutti."</p><b>Nicolò M.</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Trattamento viso eccezionale, pelle rinata. Tornerò di sicuro."</p><b>Chiara D.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Professionalità ed esperienza!!"</p><b>Rossana C.</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente curato e rilassante, professioniste vere. Consigliato!"</p><b>Federica M.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Valutazione media 4,9★ su 12 recensioni Google.</p><b>★★★★★ · Google</b></div>')
h=R(h,'📞 045 000 0000','📞 0442 84288')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>','<a href="https://maps.google.com/?cid=4148120007295442704" target="_blank" rel="noopener" class="btn btn-glass">Come arrivare</a>')
h=R(h,'<div class="brand" style="color:#fff">Bellessere Spa</div>','<div class="brand" style="color:#fff">Zorzi Emanuela</div>')
h=R(h,'<p>Centro estetico e spa nel cuore di Verona.</p>','<p>Centro estetico a Cologna Veneta.</p>')
h=R(h,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@bellesserespa.it">info@bellesserespa.it</a></p>','<p><a href="https://maps.google.com/?cid=4148120007295442704" target="_blank" rel="noopener">Piazzale Vittorio Veneto 5, 37044 Cologna Veneta (VR)</a><br><a href="tel:+39044284288">0442 84288</a></p>')
h=R(h,'Mar–Sab 9:00–19:00<br>Lun e Dom chiuso','Mar 8:30–16:30 · Mer–Ven 8:30–12:30 / 15–19:30<br>Sab 8:30–16:00 · Lun e Dom chiuso')
h=R(h,'<span>© Bellessere Spa — Verona</span>','<span>© Zorzi Emanuela — Cologna Veneta (VR)</span>')
h=h.replace('tel:+390450000000','tel:+39044284288')
open("zorzi-emanuela-cologna-veneta.html","w",encoding="utf-8").write(h)
print("wrote site2, remaining 'Bellessere':", h.count('Bellessere'), " Verona:", h.count('Verona'), " 045 000:", h.count('045 000 0000'))

# ---------- SITE 3: Centro salute ed estetica -> spamagic ----------
h=open("estetiste-spamagic-flagship.html",encoding="utf-8").read()
h=h.replace('3997385/pexels-photo-3997385','3768926/pexels-photo-3768926')
h=h.replace('3762879/pexels-photo-3762879','9146381/pexels-photo-9146381')
h=h.replace('3985329/pexels-photo-3985329','5240818/pexels-photo-5240818')
h=R(h,'<title>Centro Estetico Iris — Beauty &amp; Spa a Verona | Prenota</title>','<title>Centro Salute ed Estetica — Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Centro Estetico Iris a Verona: trattamenti viso, corpo, epilazione, unghie e make-up. 4,9★ su 175 recensioni. Prenota il tuo appuntamento di bellezza."','content="Centro Salute ed Estetica a Cologna Veneta (VR), Piazza Duomo: trattamenti viso, corpo, unghie ed epilazione. Valutazione 5★ su Google. Prenota il tuo appuntamento."')
h=R(h,'<a href="#top" class="brand">Centro Estetico <b>Iris</b></a>','<a href="#top" class="brand">Centro Salute <b>ed Estetica</b></a>')
h=R(h,'<h2>Il tuo angolo di bellezza a Verona</h2>','<h2>Il tuo angolo di bellezza a Cologna Veneta</h2>')
h=R(h,'Al Centro Estetico Iris uniamo competenza, prodotti di qualità e tanta cura per farti sentire bella e a tuo agio, ad ogni visita.','Al Centro Salute ed Estetica uniamo competenza, prodotti di qualità e tanta cura per farti sentire bella e a tuo agio, ad ogni visita.')
h=R(h,'<div class="sec-h"><span class="script">Recensioni</span><h2>Cosa dicono le clienti</h2></div>','<div class="sec-h"><span class="script">Perché noi</span><h2>Il nostro centro</h2></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Coccolata dall\'inizio alla fine. Trattamento viso meraviglioso!"</p><b>Martina P.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Valutazione 5,0 su 5 su Google.</p><b>Recensioni Google</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Unghie sempre perfette e ambiente super curato. La mia estetista di fiducia."</p><b>Giada R.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Trattamenti viso e corpo personalizzati.</p><b>I nostri servizi</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Professionali e simpatiche. Il pacchetto sposa è stato perfetto!"</p><b>Elisa M.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Accoglienza cordiale e cura in ogni dettaglio.</p><b>Il centro</b></div>')
h=R(h,'📞 045 000 0000','📞 0442 84855')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>','<a href="https://maps.google.com/?cid=5243097979145901372" target="_blank" rel="noopener" class="btn btn-glass">Come arrivare</a>')
h=R(h,'<div class="brand" style="color:#fff">Centro Estetico Iris</div>','<div class="brand" style="color:#fff">Centro Salute ed Estetica</div>')
h=R(h,'<p>Il tuo angolo di bellezza e benessere a Verona.</p>','<p>Il tuo centro benessere a Cologna Veneta.</p>')
h=R(h,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@centroiris.it">info@centroiris.it</a></p>','<p><a href="https://maps.google.com/?cid=5243097979145901372" target="_blank" rel="noopener">Piazza Duomo, 37044 Cologna Veneta (VR)</a><br><a href="tel:+39044284855">0442 84855</a></p>')
h=R(h,'Mar–Sab 9:00–19:00<br>Lun e Dom chiuso','Su appuntamento<br>Chiamaci per gli orari')
h=R(h,'<span>© Centro Estetico Iris — Verona</span>','<span>© Centro Salute ed Estetica — Cologna Veneta (VR)</span>')
h=h.replace('tel:+390450000000','tel:+39044284855')
open("centro-salute-estetica-cologna-veneta.html","w",encoding="utf-8").write(h)
print("wrote site3, remaining 'Iris':", h.count('Iris'), " Verona:", h.count('Verona'), " 045 000:", h.count('045 000 0000'))
print("DONE")
