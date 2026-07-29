# -*- coding: utf-8 -*-
import re
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def photo(ref,w=1200): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={KEY}"
def rep(html, old, new, label):
    if old not in html:
        print(f"  !! MISS [{label}]")
    return html.replace(old, new, 1)

# ================= CASA POMARI -> auburn -> casa-pomari-cerea.html =================
P1="AWCwydjhFuD0Ny6XvhhjaHE0sRTWu1b_DkTKec9_kjlfa57WKaoVitknrV7KYQGdOXSE4bLfehu0lIibav-KvNa5pw3tZ28n7zYOKPjiTY7pLVDfyRk5_KGgErC5CfIDtXI3l5w_nOQG5iE8ktVlRuOYzdZAHWguSFyC-NUj3pB_Qaed0cTXaAxZvpRkrF_2TBynANOcAtkXyDDZyxpZUm2jCUG1K94bPZV9WoIAyDcGszW5d_D88j3KyHVHwYFrN6Qh9sSdaaAl4GPdGXvXfrzyOMKg8v2fINL80GzZsz-DOhVf9nY9SaTVMJIu9jTSJNObgYjRwcL4sM8XI-Wy98tayuNU4OWzIiVjynisqq2KdUstRbIqUzIFirwX0p-vJ0iCW7edwvCPlJptJTu6geGbx_Y_bRGCEB8Wnj6JngrNz1AA6n5ujWv_z9cmumo092xw"
P2="AWCwydjFWm9Chc0M98w4hZ720FdWt-ggrm0saHZLBZbp8LMv7Gv64zS4B2WTIqP2OSrdx4LGRZhUJFrGpaoaSH9GROA3U9LA_Q4TwuiX1fthUpr_MbGvACr6hwps8F5wLsH2pqzlXAuHvc6P-9ol_2y5ucnXta5_P79S7GXldMFvuB5rmuMM9-sddPTn58b1lUTDpu-8LBmXkMs7Wx1U2hlFIoiVm0gkArSu0wJeJGMJjlrgpLJH9J5WuTfBg0N3cFjrUooPz1Bdxq8kvQiW0m5ZxlkVvzGOT9s5e5wOsorMrQYkDT6bbyYIz2SUKN7JmBeeYQ1XtBIkzwotb-yv3XENHM2ChUYNHdMn8u4rZwj_nQKS-MIBQTreWl3jJn_oKWTdFqDl1YFetCuBWiA4V0jtk6E8Ljqs-dKb0GlrHvPT0ALzRpQM_Xlc04jwn3wnRSCl"
P3="AWCwydiQrdvp_gdXQStJwcgqUKl3GX9YanTw6vpDD2L63C3fYmx_qWhn5i0Q5wDuOCOMsHiRpjGiOu33Y2ft6-Mo93g4EpLrR2xL-IULoJPVklAR7hJ1AAQzLscJIt1ip5ZlVQFrmNzy8K9JL4g91begDtA51FTeiMxOuZzO68QWr3QdGf6Pp5uBT5YRoDkkNnPfijKVjy9q1nvpMfx3zgsSaob-S6VdKrjOe5zkfPEpMKkHmJ85ot18pj8wRCdOyfxnpfu4qW59YnJrNTdjoed6qMejoM02rV9R8WQlZ2U-l83a9jQBOnfL-7Nadp0gVCjpC_1TbBVWnzNfIRP-I1_LaLWeGQGqWj3TR1X65ZjBSG1TADoAb_BvvWyOTazPWX0x6PQx5NKk9pY6YVHRjz5Bx5No5uIR21cRXENgzHgL6dKZIH4TyR5euqpQbubdHwB_"
P4="AWCwydh8RUaod6lLJJ4gsFTrJkJgKK8JfhIrk43agni3PrgzOLzBxRGeqlaLYiDz_hX9RiXXJtiGzQ-xlIeIGqOMjEl_IOp3IOyjKtYa5UyI3PVW1OtY9PbvisfRuKBXA45vT0yd3vx1G8qNt7O44Ly-6Ols6NE6sWUIUwrX4FR5711ZEwXVdHl8zR12I2u6BHigzTcw-6aDzMHTN2L0mgq5fgw2nbtkRln2AlTO5FE4L7fP2uLMcHM5c8KqjZfe8I6bUmrylr5qr4u-c6nZ-cxjOXW-jJ5H8w6X8MbjcQ_ESHowsyT_w1SCdVdwpwvImfYDPFot-9CISukmiAntQkudw_JjhF7dLpmBiFBMom3gwsHa4uFObEDm7yDo4FumCdBXSEQHFBUVbfdJd0fa1AGZAupKGoxRL-OLz-e5K_q-DGNwhpkV9yyBOtXgf7QvzfOk"
h=open("ristorante-auburn-flagship.html",encoding="utf-8").read()
h=rep(h,"<title>Osteria del Fuoco — Cucina di brace a Verona | Prenota</title>","<title>Casa Pomari — Ristorante & Lounge Bar a Cerea (VR) | Prenota</title>","t")
h=rep(h,'content="Osteria del Fuoco, cucina di brace e sapori decisi a Verona. Carni, primi della tradizione, cantina locale. 4,7★ su 180 recensioni. Prenota il tuo tavolo.">','content="Casa Pomari, ristorante & lounge bar a Cerea (VR). Cucina curata, risotti della tradizione, carrello dei dolci e ambiente elegante. 4,8 stelle su Google. Prenota il tuo tavolo.">',"d")
h=rep(h,'<span class="kick">Cucina di brace · Verona</span>','<span class="kick">Ristorante & Lounge Bar · Cerea</span>',"k")
h=rep(h,"<h1>Il gusto del fuoco</h1>","<h1>Casa Pomari</h1>","h1")
h=rep(h,"<p>Carni alla brace, primi della tradizione e una cantina che racconta il territorio. Nel cuore di Verona.</p>","<p>Cucina curata in un ambiente elegante e accogliente. Risotti della tradizione, carrello dei bolliti e dei dolci, ampia scelta di vini. A Cerea.</p>","herop")
h=rep(h,"<h2>Sapori decisi, materie prime scelte</h2>","<h2>Un mix di vintage e modernità</h2>","exph2")
h=rep(h,"<p>All'Osteria del Fuoco la cucina parte dalla brace e dalla stagionalità. Piatti generosi, servizio caloroso e un ambiente rustico ed elegante insieme.</p>","<p>Da Casa Pomari ci si sente subito a casa: un ristorante curato nei minimi dettagli, con un'atmosfera calda e familiare, piatti ottimi e un servizio attento e sorridente.</p>","expp")
h=rep(h,'<img src="https://images.pexels.com/photos/2233729/pexels-photo-2233729.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Brace">',f'<img src="{photo(P2,800)}" alt="Sala Casa Pomari">',"ei1")
h=rep(h,'<img src="https://images.pexels.com/photos/1279330/pexels-photo-1279330.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Piatto">',f'<img src="{photo(P3,800)}" alt="Ambiente Casa Pomari">',"ei2")
h=rep(h,'<img src="https://images.pexels.com/photos/941861/pexels-photo-941861.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Sala">',f'<img src="{photo(P4,800)}" alt="Dettaglio Casa Pomari">',"ei3")
# menu tweaks (personalizzo alcuni piatti citati nelle recensioni reali)
h=rep(h,"<h5>Pastissada de caval</h5><span>Con gnocchi fatti in casa</span>","<h5>Risotto all'isolana</h5><span>Il classico della casa, saporito</span>","m1")
h=rep(h,"<h5>Costata di scottona</h5><span>Alla griglia, 500g</span>","<h5>Carrello dei bolliti</h5><span>Selezione di carni con salse</span>","m2")
h=rep(h,"<h5>Costine glassate</h5><span>Marinate e cotte lentamente</span>","<h5>Pollo con patate al forno</h5><span>Tenerissimo, si scioglie in bocca</span>","m3")
h=rep(h,"<h5>Sbrisolona</h5><span>Con zabaione</span>","<h5>Carrello dei dolci</h5><span>Uno più buono dell'altro</span>","m4")
# address / hours / contacts
h=rep(h,"<p>Via Esempio 12, 37121 Verona (VR)</p>","<p>Via Mantova, 18, 37053 Cerea (VR)</p>","addr1")
h=rep(h,"<p>Mar–Dom 12:00–14:30 · 19:00–23:00<br>Lunedì chiuso</p>","<p>Mer–Dom 10:30–15:00 · 17:00–23:30<br>Lunedì e Martedì chiuso</p>","hrs1")
h=rep(h,'<p><a href="tel:+390450000000">045 000 0000</a> · <a href="mailto:info@osteriadelfuoco.it">info@osteriadelfuoco.it</a></p>','<p><a href="tel:+393391833334">339 183 3334</a> · <a href="https://maps.google.com/?cid=3356799635808851068" target="_blank">Come arrivare →</a></p>',"cont1")
# reviews
h=rep(h,"<h2>4,7 su 180 recensioni</h2>","<h2>4,8 su Google — 60 recensioni</h2>","rvh")
h=rep(h,'"Carne alla brace strepitosa e porzioni generose. Tornerò presto!"','"L\'atmosfera è calda e accogliente, ti fa sentire subito come a casa. Risotto all\'isolana saporito e pollo tenerissimo. Consiglio davvero!"',"rv1")
h=rep(h,"<b>Andrea B.</b>","<b>Anna B.</b>","rv1b")
h=rep(h,'"Atmosfera calda e piatti della tradizione fatti come si deve."','"Ristorante con un tocco vintage ed elegante, personale squisito e attento ai dettagli. Da assaggiare il carrello dei dolci!"',"rv2")
h=rep(h,"<b>Sara P.</b>","<b>Edda M.</b>","rv2b")
h=rep(h,'"Ottimo rapporto qualità-prezzo, personale gentilissimo."','"Bel posto per una serata tranquilla. Il carrello dei bolliti e quello dei dolci fanno la loro bella figura. Personale gentile."',"rv3")
h=rep(h,"<b>Luca V.</b>","<b>Eleonora F.</b>","rv3b")
# reserve
h=rep(h,"<p>Per gruppi, eventi o serate speciali chiamaci: ti aspettiamo attorno al fuoco.</p>","<p>Per pranzi, cene, gruppi ed eventi chiamaci o scrivici su WhatsApp: ti aspettiamo da Casa Pomari.</p>","resp")
# footer
h=rep(h,"<p>Cucina di brace e sapori del territorio, a Verona.</p>","<p>Ristorante & lounge bar: cucina curata e ambiente elegante, a Cerea.</p>","ftag")
h=rep(h,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@osteriadelfuoco.it">info@osteriadelfuoco.it</a></p>','<p>Via Mantova, 18, Cerea<br><a href="tel:+393391833334">339 183 3334</a><br><a href="https://maps.google.com/?cid=3356799635808851068" target="_blank">Come arrivare →</a></p>',"fcont")
h=rep(h,"<p>Mar–Dom 12–14:30<br>19–23<br>Lun chiuso</p>","<p>Mer–Dom 10:30–15<br>17–23:30<br>Lun–Mar chiuso</p>","fhrs")
h=rep(h,"© Osteria del Fuoco — Verona","© Casa Pomari — Cerea (VR)","copy")
# css bg
h=rep(h,"https://images.pexels.com/photos/1633578/pexels-photo-1633578.jpeg?auto=compress&cs=tinysrgb&w=1600",photo(P1,1600),"hero-bg")
# global brand + phone/wa
h=h.replace("Osteria del Fuoco","Casa Pomari")
h=h.replace("tel:+390450000000","tel:+393391833334").replace("045 000 0000","339 183 3334").replace("https://wa.me/390450000000","https://wa.me/393391833334")
open("casa-pomari-cerea.html","w",encoding="utf-8").write(h)
print("casa-pomari-cerea.html",len(h))

# ================= BUFFOOSTERIA -> juniper -> buffoosteria-cerea.html =================
B1="AWCwydjKPZvYgJuvZfLbjTqArkrFkast_3jYW3DBvMqeKfSSQRcDKo2NAToonLQs4j7LngIVe0NERXkNEAYA2D0ThyS-Shej7FDWKTD34phWJP-UX5BC-Uq9B1HgBgR4uudkILQrseQ7mV8dFsmdw_OWNA7dpvpotujdWPkHv9DyFRzU614JKlmQuW5VcHdOJXi4tVHHe9Pt2x3dUtgc_hPptEmsWxOdlkn8EofmxGkPW339td_8bRpMzwNzxvPUzerwPT4JomOKmapq-4aBnLhrzOD8D5QaGh_oI59ZvacgXVMpaMw4zvU_4V6CmVQDChkG99r5j8rBZLyXU3B1UrvHELu1bWfc5WfdBw0YSAZJPiOWmh3LQOHgqn60Opq4rnzc1UNNhbOJeG4UPSp6YCaFc3fEg5fwYtElQh_mNzftpidw_yy5"
B2="AWCwydgGlNYPP303BBFUvX7KKju-KBr0YV5JA6AXyrlueNr644TPTLtzE84jRqBkUtyjmhLXKkiDqU7yiGSo3JmpKLV9AWQFggBXxdHRT94yLwJFJaS-ZtkooY7lwlVQXsQnULVRNSVyriFRV1vcemCyo5jhw6MFXgUA20KexrcBPg82KMLuS83ybJYxDQrx6Odd94ppJAPVqQ_coEcm4bO2TOyKHhRyLhKoB89bnlz2hje2umF3GQTlbw5g5F-6EJpRpey4HtcnCNhjpX49vprnaSTIqBox9TikCShF6jmYeuuowEcfcoRtWqC6kuS4cQU5iVT6T-8yjvdovwG2ik6Ydl3gQcvLOFCz4qY85EvKUyv-MdIY4BhFEQlnLTu01FubNXP5mBV-S9LHMBMlRqxZGmX9uaRCFqyALTfZiMSAbbR-MyBY"
B3="AWCwydjKvMOz6vmDCTHQyoOEhJJPAMmlYGx7VWGN7-Z71cR5aq-nWvvY_cK8Y1osiiwhDqrSwCaOcLeWsoty9kpw8FhEvqa2Q4yBFkWQQKuYQh6Rdx3dqIAUlH7LpCvS3de9LBv-aXfDGH24rsfwRHYbtEVh1vZvWU0Y7CUyL5rie7Cc4GdtwmdAXKTbhPSVfo-Ca3f3fNaRkCunHKQMHJGce9UNR0495IQMA1AaNrtfzv1S-79GjyozTxXjrOCw82Re4RHXH8e7h9V2WQD4i0GQhWvK6HhjuKUIPEHAqzYyOavAIKBCh014x0m2lug-iyE7dCAzueJusrLfXOYuZOiMMTA5-kyP_uKZdMyK2hhYd5PxicHFyjQl6o4EcGUlcm07Z1zpkM7p1qT7_z-Oi6RZgPmy3upl9lOfaaJIeG32VHrmtg"
B4="AWCwydjuq1-QpV8070R1RGNlQ1rj8eeQD0jEfXPwOkuIpA6Ndt49nc_X0T7WCHCtTJP2gx79O57EmGI0Jpuj3RMQcAuxaxfiRe5YAA95wjik0DBvKhhK-WVhmjJixBGCi-VxhV1hPxA2BqBhQazQGf2lv54Lt7fL9C95EOFDhTtemqotKxAEeLGSQYfsXlbNQW1lhlP8-UW9ep8ezFteQq1PR0ZscAWhTdimMs4EgKIclYlcWRtGWqCjCcXr1SxDMA2LlaNHJB7Lhf0opkU3sQUL--QchhT59lsp99JKOvfKX7NOiPfEmO_RpzNfoZwltrKTPFVbV7Ka1-4nHAmMqN-kiZX8fUpPcr4c6nBnaoCJMvEu7UZ8XeeErUUa5SQ8QsoCm2wVFPH2KiRrsK17gG_e9EXXJ7NPfsXIjLrHb8p6rke5EkKqLBnL0PA1nrYSIQrW"
j=open("ristorante-juniper-flagship.html",encoding="utf-8").read()
j=rep(j,"<title>Ristorante Ginepro — Fine dining a Verona | Prenota</title>","<title>BuffoOsteria — Osteria & Cucina veronese a Cerea (VR) | Prenota</title>","t")
j=rep(j,'content="Ristorante Ginepro, cucina raffinata e stagionale a Verona. Percorsi degustazione, cantina d\'autore, sala elegante. 4,9★ su 210 recensioni. Prenota.">','content="BuffoOsteria a Cerea (VR): osteria dal clima familiare, cucina veronese, bigoli al ragù, pizze e piatti abbondanti. 4,2 stelle su 630 recensioni. Prenota.">',"d")
j=rep(j,'<span class="kick">Fine dining · Verona</span>','<span class="kick">Osteria & Cucina · Cerea</span>',"k")
j=rep(j,"<h1>L'arte della tavola</h1>","<h1>Come a casa, a Cerea</h1>","h1")
j=rep(j,"<p>Cucina raffinata e stagionale, in una sala elegante nel cuore di Verona. Un'esperienza da vivere con calma.</p>","<p>Un'osteria dal clima familiare in centro a Cerea: cucina veronese, piatti abbondanti, pizze e un'accoglienza sincera.</p>","herop")
j=rep(j,"<h2>Dove ogni piatto è un piccolo racconto</h2>","<h2>Un'osteria dove ci si sente in famiglia</h2>","ih2")
j=rep(j,"<p>Al Ristorante Ginepro celebriamo la materia prima con tecnica e misura. Percorsi degustazione che cambiano con le stagioni, una cantina curata e un servizio discreto e attento.</p>","<p>Alla BuffoOsteria, nel cuore di Cerea, la cucina è quella veronese di sempre: bigoli al ragù, tortelli, carni e pizze. Ambiente accogliente, personale gentile e prezzi nella norma.</p>","ip")
j=rep(j,'<img class="split-img" src="https://images.pexels.com/photos/2696064/pexels-photo-2696064.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Piatto d\'autore">',f'<img class="split-img" src="{photo(B2)}" alt="Piatto BuffoOsteria">',"split")
j=rep(j,"<h3>Stagionalità, territorio, eleganza</h3>","<h3>Tradizione, gusto e ospitalità</h3>","sh3")
j=rep(j,"<p>Lavoriamo con piccoli produttori locali per portare in tavola solo il meglio di ogni stagione. Ogni dettaglio, dalla mise en place al calice, è pensato per l'ospite.</p>","<p>Piatti genuini e generosi, dai primi della tradizione alle pizze. Una location rustica e curata, ricca di piccoli cimeli, dove il cliente è al centro.</p>","sp1")
j=rep(j,"<p>Un luogo intimo, ideale per cene speciali, anniversari e occasioni da ricordare.</p>","<p>Perfetta per un pranzo di lavoro veloce o una cena in compagnia, con laurea, feste ed eventi su richiesta.</p>","sp2")
# menu (osteria) - riscrivo prezzi/piatti
j=rep(j,"<h5>Capasanta scottata</h5><span>Topinambur, nocciola, agrumi</span><div class=\"price\">18 €</div>","<h5>Antipasti veronesi</h5><span>Salumi e sfizi del territorio</span><div class=\"price\">10 €</div>","m1")
j=rep(j,"<h5>Uovo &amp; tartufo</h5><span>Fonduta leggera, tartufo nero</span><div class=\"price\">16 €</div>","<h5>Bruschette della casa</h5><span>Pane, pomodoro e condimenti</span><div class=\"price\">7 €</div>","m2")
j=rep(j,"<h5>Tartare di manzo</h5><span>Senape antica, capperi, tuorlo</span><div class=\"price\">17 €</div>","<h5>Tagliere misto</h5><span>Da condividere</span><div class=\"price\">12 €</div>","m3")
j=rep(j,"<h5>Risotto agli agrumi</h5><span>Mantecato, gambero rosso</span><div class=\"price\">20 €</div>","<h5>Bigoli al ragù di cinghiale</h5><span>Saporiti e abbondanti</span><div class=\"price\">11 €</div>","m4")
j=rep(j,"<h5>Raviolo di zucca</h5><span>Burro nocciola, amaretto</span><div class=\"price\">18 €</div>","<h5>Tortelli di zucca</h5><span>Burro e salvia</span><div class=\"price\">10 €</div>","m5")
j=rep(j,"<h5>Tagliolino al tartufo</h5><span>Fatto in casa, tartufo nero</span><div class=\"price\">22 €</div>","<h5>Lasagne della casa</h5><span>Al forno, come una volta</span><div class=\"price\">9 €</div>","m6")
j=rep(j,"<h5>Filetto di manzo</h5><span>Jus al vino rosso, sedano rapa</span><div class=\"price\">28 €</div>","<h5>Tagliata di pollo</h5><span>Rucola e grana</span><div class=\"price\">13 €</div>","m7")
j=rep(j,"<h5>Branzino in crosta</h5><span>Verdure di stagione, beurre blanc</span><div class=\"price\">26 €</div>","<h5>Stracotto alla veronese</h5><span>Al vino rosso, con polenta</span><div class=\"price\">14 €</div>","m8")
j=rep(j,"<h5>Piccione arrosto</h5><span>Frutti rossi, patata affumicata</span><div class=\"price\">30 €</div>","<h5>Pizze classiche</h5><span>Cotte al momento</span><div class=\"price\">7 €</div>","m9")
j=rep(j,"<h5>Percorso Ginepro</h5><span>5 portate a sorpresa dello chef</span><div class=\"price\">65 €</div>","<h5>Menù pranzo di lavoro</h5><span>Primo, secondo, contorno</span><div class=\"price\">13 €</div>","m10")
j=rep(j,"<h5>Abbinamento vini</h5><span>Calici in accompagnamento</span><div class=\"price\">35 €</div>","<h5>Contorni</h5><span>Patate al forno, verdure</span><div class=\"price\">4 €</div>","m11")
j=rep(j,"<h5>Dessert del giorno</h5><span>Creazione del pasticcere</span><div class=\"price\">10 €</div>","<h5>Dolci della casa</h5><span>Chiedi in sala</span><div class=\"price\">5 €</div>","m12")
j=rep(j,'<div class="menu-cat">\n        <h3>Degustazione &amp; Dolci</h3>','<div class="menu-cat">\n        <h3>Pizze &amp; Menù &amp; Dolci</h3>',"mcat")
# gallery
j=rep(j,'<img src="https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Piatto">',f'<img src="{photo(B3,800)}" alt="Piatto BuffoOsteria">',"g1")
j=rep(j,'<img src="https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Sala">',f'<img src="{photo(B1,800)}" alt="Locale BuffoOsteria">',"g2")
j=rep(j,'<img src="https://images.pexels.com/photos/3184183/pexels-photo-3184183.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Dettaglio">',f'<img src="{photo(B4,800)}" alt="Dettaglio BuffoOsteria">',"g3")
# reviews
j=rep(j,"<h2>4,9 su 210 recensioni</h2>","<h2>4,2 su Google — 630 recensioni</h2>","rvh")
j=rep(j,'"Un\'esperienza raffinata dall\'inizio alla fine. Ogni piatto un\'emozione."','"Staff molto gentile, cibo veramente ottimo: tortelli burro e salvia e tagliata di pollo eccezionali. Ambiente carino e arredato con stile!"',"rv1")
j=rep(j,"<b>Chiara F.</b>","<b>Manuel S.</b>","rv1b")
j=rep(j,'"Servizio impeccabile e cantina straordinaria. Il posto per le occasioni."','"Bigoli al ragù di cinghiale saporiti e abbondanti. Nel centro di Cerea, comodo da raggiungere, servizio rapido e cortese."',"rv2")
j=rep(j,"<b>Davide N.</b>","<b>Anna G.</b>","rv2b")
j=rep(j,'"Cucina elegante e mai banale. Il percorso degustazione vale il viaggio."','"Pranzo di lavoro: atmosfera tranquilla, personale gentile, cucina abbondante ma non unta, piatti semplici ma efficaci. Prezzi onesti."',"rv3")
j=rep(j,"<b>Francesca L.</b>","<b>Walter L.</b>","rv3b")
# visit block
j=rep(j,"<p>Consigliamo la prenotazione. Per menù degustazione ed eventi privati, contattaci.</p>","<p>Consigliamo la prenotazione per gruppi e serate. Per info ed eventi scrivici o chiamaci.</p>","visp")
j=rep(j,'<div class="hours">Via Esempio 12, Verona · Mar–Dom 19:00–23:00 · Lunedì chiuso</div>','<div class="hours">Via Roma 5, Cerea · Lun–Dom 9:00–14:30 · Mer–Sab anche 18:00–22:30</div>',"vhours")
# footer
j=rep(j,"<p>Cucina raffinata e stagionale nel cuore di Verona.</p>","<p>Osteria dal clima familiare e cucina veronese, a Cerea.</p>","ftag")
j=rep(j,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@ristoranteginepro.it">info@ristoranteginepro.it</a></p>','<p>Via Roma 5, Cerea<br><a href="tel:+393381677420">338 167 7420</a><br><a href="https://maps.google.com/?cid=16739140940002306136" target="_blank">Come arrivare →</a></p>',"fcont")
j=rep(j,"<p>Mar–Dom 19:00–23:00<br>Lunedì chiuso</p>","<p>Lun–Dom 9:00–14:30<br>Mer–Sab anche 18–22:30</p>","fhrs")
j=rep(j,"© Ristorante Ginepro — Verona","© BuffoOsteria — Cerea (VR)","copy")
# css bg hero
j=rep(j,"https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1600",photo(B1,1600),"hero-bg")
# global brand + phone/wa
j=j.replace(">Ginepro<",">BuffoOsteria<").replace("Ristorante Ginepro","BuffoOsteria")
j=j.replace("tel:+390450000000","tel:+393381677420").replace("045 000 0000","338 167 7420").replace("https://wa.me/390450000000","https://wa.me/393381677420")
open("buffoosteria-cerea.html","w",encoding="utf-8").write(j)
print("buffoosteria-cerea.html",len(j))
print("DONE 2")
