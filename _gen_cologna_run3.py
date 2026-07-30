# -*- coding: utf-8 -*-
import json, urllib.parse, os
os.chdir("/tmp/hub_1785369714")
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
TODAY="2026-07-30"
BASE="https://hubtecit-srl.github.io/website/"
WARN=[]
def R(html, old, new, req=True):
    if old not in html:
        if req: WARN.append((old[:60]))
        return html
    return html.replace(old,new)
def ph(ref,w): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={KEY}"
WA_TMPL=("Buongiorno,\n""Sono Laura di HubTec, azienda di Verona.\n\n"
"Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
"Se vi piace, lo attiviamo con soli 200€.\n\n"
"In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
"Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
"Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n""Laura Borin - HubTec")
def wa_link(intl,url): return "https://wa.me/"+intl+"?text="+urllib.parse.quote(WA_TMPL.format(url=url),safe='')

# photo refs
FHG=["AWCwydhAhQbLVj4eknuZeRPc7k_jYU7DwORH_q_tCw3QbQwlZFIpiI0gmWN4xm8oMVDfn9uFG3W8PF26MnKO8-maCVvvBVLW4-eheO_M4ZT8Y5BpugdYcSaq5Ait5Er0TmBv1cBGM46HuC0De-EsEfSlc46UM5G-5ELFP9sEZg2Felnbg7OTdcmFGEGoETwbhda-Jg0Vb8MSeVBMgDoklFltp7XYpOrcd1iPGadjhppqnOPE99ILFLlRPP6Q3dBljAuDzgRy9KO0g_2NNOorLmJSRNtXxqgxUZ3GuN0bx0qcQ0JThodPxWGZEAyk4VVLkFmNa6DN-KWsg-0ELHdfl-7s4J8sf11mYyXmF8scPa4hcGrSWyGDDZLUAUhkZob8kYjSUTta_motfQWP5EPcE9t2teAY5N8StquRnAItcm5JdOMVvvhSEwafDrd8uQ8oCbwo",
"AWCwydiyS9w4wBFCq67U-RslrHZoveQskomrxfCNXMNJbD0VU6U5paoSypDvIP4vkxpYmfPsiPX8-ZTyGbnO5rA1y_marriKRZ-PA1Z3u5OWYWekOWilUp1id4xw_Es9tbDVk-IDyrXPxSX5o1kHUpOjqJkNXMo3e--Qd8DO8_VdMeCpOquqhtzeQ49Ie6GaDldv-HnEkNfF1j85Zl_J8H3bPy8uk-jjurBwMWLFiKx73pEkilL73lgwEk-AwcpHSsVpubbFoq8P9DHMBggKJllqacvNbS9OxI1b4ou1g8HRkbF00yptgNQYWm7v9qqdHTDlUCr0I_G_OXGSwnyfkyvFotQrid66hCNYlhM2QaSKRzuvGRtbQK_n2z8Cd64pyyxevHkosqrO5B0j58EeffYQup4cVjlmn_u2dmoybh0n3yIf4Jld"]
BAR=["AWCwydiHfU8NTEyJo7VM6Cquo_V1fNE0Bsr0hjTrhUwz05AR1LBpWzcAkCZwuYtqN0ovWBujdcus6dfNI0zO6FDm7uUDRKRS0O38QccgNoVYQ4YAd6kyvxF-yNLvlvh8NAGTG5S3uaPEPMYfa-jovm-4cMA087zjYyIX1ox5Qg6th5C3IqQEn3QYw6zkLMa9IoCL7pR8C4Twj8NkfCwINAAmdGexZ55BWmzhLW5_niLB-j8mGYudyRMu0UGnCrxz2YLAIhk2hvXzxdnmh7B66zTg0A81GAP5N7DH0KKNcUdioKK9PPHNc6Nuan1u4uysVSCZ-6ntYSQHAOy0vhwLYxkyiH0Lw28K8ASJJtl8y5qJAsdJQXZNa1cUdTCK7ECh_NLotpuUWUiropHVhDa8D_-X2EGJxLdbG_fgSzpRRr20chGMW5oHWQEe6QuEiXhNJpaV",
"AWCwydhwtczpWzmarPOBJ7M5YzRGyIVjN9D88BZ580ZN9HHcVMKZo-CZkEJusyXmbF_H2NSAmV006aINLRxtzBdIoPhfzPSYvxHqVaCkon4E9J6AXOrkoTYb8nNHQFcYZR7d0OZ4Ybxjql0i39To0QJwm1kyr4l81uNPW9xnECTf_b_l6A7owwrQxF_BESRKsRl9Oy4JjiziRUwpYN00VLltOIcVzO2C4KhEINqhzi8jHJyP7vc2y3f14h-WFux5XIUVQXhL6VUppE4VbO181m_y2xaZrJwJKd-LtpLvrukYsTKVVB-Yx3J2wLFtX4MSOBWEJ9MYlSlpxxEkGsv0vUmmEOJ61R5X6in-lAT5w_X8Oqr6SUoucIhwPkc45Oq5hKcUEAXF9k-Z7x6nl0PSLfc-C-XLhTlc5pjtul7ec3ghwVYaUIjh8NCo-VG0rN84ww",
"AWCwydgo-1j15PYGjOtCP-qyJRRF5myRk12fB9dqmMx6qLVfTtxu2aEqrLRLnx3wlec2F95WHeuoyJglbElgcg34AZAZYYIZUUVs9tL6NSJKmkZA6k2MvmtUWRG_zVncvJfj0lUDqSFOmuBCSTXbCjToaVSmMZ939RRQNP-pcye0ILCr5MN7PdXBO7IgV3k1rkxFJHXOSpTddthSWQvwfvADjdCGc6CijidqzRT58ctMR8ReVXf4XVsQPdR-y_T9mblXnEyguZSWFjjsjAaDRL4BErBkD0vz2cpif1pcxWP0J64Lr8eqq_ixM39PYC84xHaM6fC76tBs7M5iI-naIllh4ORGOy4xVpmjkezFR_fcrfU8D_f5pUT2Er-2Pgn4jXNH29qQ0pQLjnTL3GbqbqazpMrOsIE3825u40Eii2sT-xGPQSO4KovxoLp0wGw52Q"]

# ============ LEAD 1: FHG-Federica Hair Gallery -> revival (v3) ============
h=open("parrucchieri-revival-flagship.html",encoding="utf-8").read()
h=R(h,'<title>Revival Hair Studio — Parrucchiere a Verona | Prenota</title>','<title>Federica Hair Gallery — Parrucchiere a Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Revival Hair Studio, parrucchiere a Verona: taglio, colore e styling d\'autore. Un salone dal design minimal ed elegante. 4,9★ su 180 recensioni. Prenota.">','content="Federica Hair Gallery (FHG), parrucchiere a Cologna Veneta (VR) in Viale del Lavoro 1. Taglio, colore, piega e trattamenti. Oltre 40 recensioni su Google. Prenota.">')
h=R(h,'<a href="#top" class="brand">REVIVAL</a>','<a href="#top" class="brand">FHG</a>')
h=R(h,'<span class="kick">Hair Studio · Verona</span>','<span class="kick">Hair Gallery · Cologna Veneta</span>')
h=R(h,'<h1>Revival</h1>','<h1>Federica</h1>')
h=R(h,'<p>Taglio, colore e styling d\'autore. Un salone dove l\'eleganza incontra la cura del dettaglio.</p>','<p>Federica Hair Gallery: taglio, colore, piega e trattamenti con cura del dettaglio, nel cuore di Cologna Veneta.</p>')
# portfolio imgs: replace first 2 with real, keep 2 atmosphere
h=R(h,'https://images.pexels.com/photos/3065209/pexels-photo-3065209.jpeg?auto=compress&cs=tinysrgb&w=800',ph(FHG[0],800))
h=R(h,'https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800',ph(FHG[1],800))
# reviews (real)
h=R(h,'<q>Un salone diverso da tutti. Eleganza, competenza e un taglio impeccabile.</q>','<q>Personale sempre disponibile, professionale e cordiale. Piega eccezionale e consigli ottimi.</q>')
h=R(h,'<b>Beatrice C.</b>','<b>Anna B. · Google</b>')
h=R(h,'<div class="c rv"><div class="st">★★★★★</div><q>"Colore perfetto e consulenza vera. Mi sento sempre valorizzata."</q><b>Elena V.</b></div>','<div class="c rv"><div class="st">★★★★★</div><q>"Molto bravi, prodotti ottimi e squadra vincente. Meravigliosi!"</q><b>Anna Baschirotto · Google</b></div>')
h=R(h,'<div class="c rv"><div class="st">★★★★★</div><q>"Ambiente raffinato e staff attentissimo. Consigliato."</q><b>Giulia F.</b></div>','<div class="c rv"><div class="st">★★★★★</div><q>"Shampoo scrub, taglio e piega: mezz\'ora di totale relax. Grazie Federica."</q><b>Sonia Bogoni · Google</b></div>')
h=R(h,'<div class="c rv"><div class="st">★★★★★</div><q>"Il miglior taglio che abbia mai avuto. Tornerò sicuramente."</q><b>Sofia R.</b></div>','<div class="c rv"><div class="st">★★★★★</div><q>Oltre 40 recensioni verificate dei clienti su Google.</q><b>Recensioni Google</b></div>')
# hours: Lun-Sab 09-19, Dom 09-12:30
h=R(h,'<li><span>Martedì – Venerdì</span><span>9:00 – 19:00</span></li>','<li><span>Lunedì – Venerdì</span><span>9:00 – 19:00</span></li>')
h=R(h,'<li><span>Sabato</span><span>9:00 – 18:00</span></li>','<li><span>Sabato</span><span>9:00 – 18:00</span></li>')
h=R(h,'<li><span>Domenica &amp; Lunedì</span><span>Chiuso</span></li>','<li><span>Domenica</span><span>9:00 – 12:30</span></li>')
# cta tel/wa
h=R(h,'<a href="tel:+390450000000" class="btn btn-light">045 000 0000</a>','<a href="tel:+390442172380" class="btn btn-light">📞 0442 172 3805</a>')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>','<a href="https://wa.me/393716910078" class="btn btn-ghost">WhatsApp</a>')
# footer
h=R(h,'<div class="brand" style="color:#fff;letter-spacing:.22em">REVIVAL</div><p>Hair studio d\'autore nel cuore di Verona.</p>','<div class="brand" style="color:#fff;letter-spacing:.22em">FHG</div><p>Federica Hair Gallery — parrucchiere a Cologna Veneta (VR).</p>')
h=R(h,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@revivalhair.it">info@revivalhair.it</a></p></div>','<div><h4>Contatti</h4><p>Viale del Lavoro 1, 37044 Cologna Veneta (VR)<br><a href="tel:+390442172380">0442 172 3805</a><br><a href="https://maps.google.com/?cid=3626886260224841483" target="_blank" rel="noopener">Come arrivare →</a></p></div>')
h=R(h,'<div><h4>Orari</h4><p>Mar–Ven 9:00–19:00<br>Sab 9:00–18:00</p></div>','<div><h4>Orari</h4><p>Lun–Ven 9:00–19:00<br>Sab 9:00–18:00 · Dom 9:00–12:30</p></div>')
h=R(h,'<span>© Revival Hair Studio — Verona</span>','<span>© 2026 Federica Hair Gallery · Cologna Veneta (VR)</span>')
h=R(h,'<a href="#prenota" class="book">Prenota</a>','<a href="https://wa.me/393716910078" class="book">WhatsApp</a>')
h=h.replace('tel:+390450000000','tel:+390442172380')
open("fhg-federica-hair-gallery-cologna-veneta.html","w",encoding="utf-8").write(h)
print("FHG done | pexels_left",h.count("images.pexels.com"),"| verona_left",h.count("Verona"),"| revival_left",h.lower().count("revival"),"| placeholders",h.count("045 000 0000"))

# ============ LEAD 2: Barberoshop Bayrout -> rhazor (v2) ============
h=open("parrucchieri-rhazor-flagship.html",encoding="utf-8").read()
h=R(h,'<title>Barberia Rasoio — Barbiere a Verona | Prenota</title>','<title>Barberoshop Bayrout — Barbiere a Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Barberia Rasoio, barbiere a Verona: taglio uomo, rasatura tradizionale, barba e styling. 4,9★ su 200 recensioni. Prenota il tuo appuntamento.">','content="Barberoshop Bayrout, barbiere a Cologna Veneta (VR) in Via de Bernardino Anti 14. Taglio uomo, barba e rasatura. 5,0★ su Google. Prenota il tuo appuntamento.">')
h=R(h,'<a href="#top" class="brand">Barberia <b>Rasoio</b></a>','<a href="#top" class="brand">Barberoshop <b>Bayrout</b></a>')
h=R(h,'<span class="kick">Barbiere · Verona</span>','<span class="kick">Barbiere · Cologna Veneta</span>')
# ibar
h=R(h,'<div class="c"><div><h4>Chiamaci</h4><p><a href="tel:+390450000000">045 000 0000</a></p></div></div>','<div class="c"><div><h4>Chiamaci</h4><p><a href="tel:+393773747221">377 374 7221</a></p></div></div>')
h=R(h,'<div class="c"><div><h4>Dove siamo</h4><p>Via Esempio 12, Verona</p></div></div>','<div class="c"><div><h4>Dove siamo</h4><p>Via de Bernardino Anti 14, Cologna Veneta (VR)</p></div></div>')
h=R(h,'<div class="c"><div><h4>Orari</h4><p>Mar–Sab 9:00–19:00</p></div></div>','<div class="c"><div><h4>Orari</h4><p>Lun–Sab 9:00–21:00 · Dom chiuso</p></div></div>')
# about
h=R(h,'<p>Da Barberia Rasoio ogni cliente è unico. Mani esperte, strumenti di qualità e la tradizione del barbiere di una volta, in un ambiente curato e maschile.</p>','<p>Da Barberoshop Bayrout ogni cliente è unico. Mani esperte, strumenti di qualità e la cura del barbiere di una volta, in un ambiente curato e accogliente.</p>')
# gallery: 3 real + keep 1
h=R(h,'https://images.pexels.com/photos/1570806/pexels-photo-1570806.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BAR[0],800))
h=R(h,'https://images.pexels.com/photos/1805600/pexels-photo-1805600.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BAR[1],800))
h=R(h,'https://images.pexels.com/photos/2521617/pexels-photo-2521617.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BAR[2],800))
# reviews real
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Miglior barbiere di Verona. Taglio sempre perfetto e ambiente top."</p><b>Luca M.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Ragazzo gentile ed educato. Veloce, bravo ed offre un ottimo prezzo."</p><b>Umberto Leardi · Google</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"La rasatura col panno caldo è un\'altra cosa. Bravissimi e simpatici."</p><b>Andrea P.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"È bravissimo, venite sempre da lui!"</p><b>Marwan Tamym · Google</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Professionali, veloci e curati. Ci porto anche mio figlio."</p><b>Stefano R.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Valutazione 5,0★ su Google dai clienti del quartiere.</p><b>Recensioni Google</b></div>')
# cta tel/wa
h=R(h,'<a href="tel:+390450000000" class="btn btn-gold">📞 045 000 0000</a>','<a href="tel:+393773747221" class="btn btn-gold">📞 377 374 7221</a>')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>','<a href="https://wa.me/393773747221" class="btn btn-ghost">WhatsApp</a>')
# footer
h=R(h,'<div><div class="brand">Barberia <b style="color:var(--gold)">Rasoio</b></div><p>Barbiere tradizionale nel cuore di Verona.</p></div>','<div><div class="brand">Barberoshop <b style="color:var(--gold)">Bayrout</b></div><p>Barbiere a Cologna Veneta (VR).</p></div>')
h=R(h,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@barberiarasoio.it">info@barberiarasoio.it</a></p></div>','<div><h4>Contatti</h4><p>Via de Bernardino Anti 14, 37044 Cologna Veneta (VR)<br><a href="tel:+393773747221">377 374 7221</a><br><a href="https://maps.google.com/?cid=18011962456166187664" target="_blank" rel="noopener">Come arrivare →</a></p></div>')
h=R(h,'<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>','<div><h4>Orari</h4><p>Lun–Sab 9:00–21:00<br>Domenica chiuso</p></div>')
h=R(h,'<span>© Barberia Rasoio — Verona</span>','<span>© 2026 Barberoshop Bayrout · Cologna Veneta (VR)</span>')
h=R(h,'<a href="#prenota" class="book">Prenota</a>','<a href="https://wa.me/393773747221" class="book">WhatsApp</a>')
h=h.replace('tel:+390450000000','tel:+393773747221')
open("barberoshop-bayrout-cologna-veneta.html","w",encoding="utf-8").write(h)
print("BAR done | pexels_left",h.count("images.pexels.com"),"| verona_left",h.count("Verona"),"| rasoio_left",h.lower().count("rasoio"),"| placeholders",h.count("045 000 0000"))

# ============ LEAD 3: Parrucchiera Ricci e Capricci -> salonkit (v1) ============
h=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
h=R(h,'<title>Salone Méta — Parrucchiere a Verona | Prenota</title>','<title>Ricci e Capricci — Parrucchiere a Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="Parrucchiera Ricci e Capricci a Cologna Veneta (VR), Via Indipendenza 11. Taglio, colore, trattamenti e acconciature. 5,0★ su Google. Prenota.">')
h=R(h,'<a href="#top" class="brand">Salone Méta</a>','<a href="#top" class="brand">Ricci e Capricci</a>')
h=R(h,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Cologna Veneta</span>')
h=R(h,'<h1>Dove l\'hairstyling è <em>olistico</em></h1>','<h1>Il tuo stile, <em>su misura</em></h1>')
h=R(h,'<p>Taglio, colore e trattamenti pensati per te e per la salute dei tuoi capelli. Un salone dove bellezza e benessere si incontrano.</p>','<p>Da Ricci e Capricci: taglio, colore, trattamenti e acconciature curati nel dettaglio, nel cuore di Cologna Veneta.</p>')
# reviews (no real text -> generic, no fake names)
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Taglio perfetto e colore stupendo. Mi trovo benissimo ogni volta."</p><b>Serena B.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Valutazione 5,0★ su Google dalle clienti del salone.</p><b>Recensioni Google</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente rilassante e staff super professionale. Consigliatissimo."</p><b>Marta L.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Taglio, colore e cura dei capelli con passione e attenzione.</p><b>Ricci e Capricci</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Finalmente un salone che cura davvero i capelli. Bravissimi!"</p><b>Chiara V.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Un punto di riferimento per la bellezza a Cologna Veneta.</p><b>Ricci e Capricci</b></div>')
# cta tel/wa
h=R(h,'<a href="tel:+390450000000" class="btn btn-light">📞 045 000 0000</a>','<a href="tel:+393520489198" class="btn btn-light">📞 352 048 9198</a>')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>','<a href="https://wa.me/393520489198" class="btn btn-glass">WhatsApp</a>')
# footer
h=R(h,'<div class="brand" style="color:#fff">Salone Méta</div><p>Parrucchiere olistico nel cuore di Verona.</p>','<div class="brand" style="color:#fff">Ricci e Capricci</div><p>Parrucchiere a Cologna Veneta (VR).</p>')
h=R(h,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>','<div><h4>Contatti</h4><p>Via Indipendenza 11, 37044 Cologna Veneta (VR)<br><a href="tel:+393520489198">352 048 9198</a><br><a href="https://maps.google.com/?cid=9958794653962710783" target="_blank" rel="noopener">Come arrivare →</a></p></div>')
h=R(h,'<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>','<div><h4>Orari</h4><p>Mar–Ven 9:30–12:00 · 15:30–18:30<br>Sab 8:30–18:00 · Lun e Dom chiuso</p></div>')
h=R(h,'<span>© Salone Méta — Verona</span>','<span>© 2026 Parrucchiera Ricci e Capricci · Cologna Veneta (VR)</span>')
h=R(h,'<a href="#prenota" class="book">Prenota</a>','<a href="https://wa.me/393520489198" class="book">WhatsApp</a>')
h=h.replace('tel:+390450000000','tel:+393520489198')
open("ricci-e-capricci-cologna-veneta.html","w",encoding="utf-8").write(h)
print("RICCI done | pexels_left",h.count("images.pexels.com"),"| verona_left",h.count("Verona"),"| meta_left",h.count("Salone Méta")+h.count("salonemeta"),"| placeholders",h.count("045 000 0000"))

print("WARN(missing anchors):",WARN)
