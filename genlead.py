# -*- coding: utf-8 -*-
import re
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def photo(ref): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={ref}&key={KEY}"

def rep(html, old, new, label):
    if old not in html:
        print(f"  !! MISS [{label}]")
    return html.replace(old, new)

# ============ HAMBURGERIA (auburn) ============
H = open("ristorante-auburn-flagship.html", encoding="utf-8").read()
hp = ["AWCwydjySxP-fu1jkxqr6YXGW-L0FGeOzy_tR5SngGBAynCmy8fw66ihx3Bal3ssuZ6G6D4-LPTbisD7cyQPKHCXJBnGu3wFRU6lbHNwKYpOhuUl5UnRLUdo2POs3wN4WqnG5i2ztw-ZDvNZURFJdmvQ4QH36JDqykTnXNHZNPuRwC0pcpyM4tbLrExc282sMTmk6kti1_N1J9QyM7JIDoGcZWdFmASVRhgFGl6krFINlpwgqEadSf5dzO1hag7uWyNJlp-wfldETizS1B88xgtoRPSCVUlKZCGHerY0aNZT0Eo1ZWuUptJir4pCnf3S1W6pjU7F5oJ13XavLe_Zq6VwQRXeBaBiVI_TUR6F9_e3FkUGE70akBXHiJ8EJ9qvuZn4gvIDpO8T9WQSOYSgCPuTriEafv_0JK-EJXeniFkzcxC1os0tVbOfuwj88BkyhA",
"AWCwydiy9gBIvO8aosa641ObdEokFHAlU7FEP6rJuIour_lMfugtKBY1eYm-swcUTw-IwzbFNseyi9po_1dvQ3sc_M4Bk-HPC8s4SkNxiViAh05Fwy_YPXlSBhIOwIM1zKqM2rwsieBhBSChLdF7wCnrJE1XHQQ7S62Di1YGV0_vuNUXkGTO5-vHF1REErHLnexnz4Zab3P1e2fUjxfbjY-fzINnQsr8Bn1oZbDTZ5-Uwoe-4PMBYqlenJh-E9r5GmTzqeDHyo3-OiZtxmhdF8EPSoBhAmQH6uv_oPHxLsabbdj90eRvxOFRR2Ihr89Y07BcjltyRoOtN9NLN79G1G0RY2ZtCpYwHHqbXO-RQwA9v9SsRlENqgJ9cwvreTUyHhpP4jvHovL9Kr3mS_qVmoFVEP7gcXxo9AWswOEZQk9qDz0rAfg3",
"AWCwydgmXuEeE2YezeDu-8SDc8TOlRiJhoyvLsil3i8Cks9_M7cuqWVY4NAN8noNN_GencoL6MsI2vd1RDt7SfuOezJzCspiAVaA5aMc40mnCL1fbVqb_62N2DNAacR5Dz3X8yfh8FB_ISgEuTxt6-CKq95aJJb3EOBBfrrbN0dRZ3LGhLgdiQz0kIPC7Q42filkn1lIYnwKFGsYl5rQL9hGOVEPgGaarQnvblcEK0a3jzEIJikq8dv4i3m2XEr1S9W0pUoA-X9f1GgZYhJTv-20cp9AL56QnwopMsXgwzuSXzYdsDdiwoqQnqW31SW42UzHBjKUFaTVWrRunTn_bWhyQVy7BikbOUZ3dmQOAj5HSLOrl71txqWjYr71rO-CJd_DSt3H05FsHY6ubV2Wbe_nrptTy1iI8L7TFBRmWCyO1vFTPHLUmFpxIOA7Kwgh3a3M",
"AWCwydiBriqd-uyabY4JKCFdTyAKQIbPZyJLxQ0GlSksPq7PjHeYVarfXmEh9cXVWuDlA6LaJYLl3dBMfHKn4XvsJeTv9XTyfBnVqowI6lUp7dMAcl0-6g1l-iJ9PNjhRPujvKOXR8E9DBd-zBSx79Rq1gD7YTJ8LUlKcn1QuJQSRraAx1j9HaUHgkkEt504hEvdhsJKfnsBbsrQdkE046fsXSxyuvq5ObYECzPDaODg4G4Lt6SWcZYsnC7SvwvuBMJs_xPEr8SqJ9bWsv8aJnR7faePMXIzG-UlhPmnynharlm2BUu9mlH1vWCW9U2Z06L8wyE6x__nj3jRBDiblwqJzntwbIgVNnw2tI7XKbREJLwGUXhe_PijSoXbFI5q1HB_y4ZKtwDE9QL9dpSWNU2rLrEynEJ1LoLjY3ioBUMQ3lXCrmvi",
"AWCwydhldrGRVR7DyzqE6gr-miwgvD8Bs-tc1B50Fa2WOQ3KcxmrOy0Ea8goQT_2rltZbpZf56yGdzr4n50h3--uPFBYvrtQBYHf2SwQhb2UrRvHP-Z5igzRLvdEkU8bDANVzGXIwD5McaBWBxJhQ_ewlKxcYrLicDrsOQJTw2gx8viKmw-zNOyr8C5RYIzYGjLTrRNp2xO66vcNJgSzUaN-9LIC5Ppmm4dY3LsBJw2JNoHzIMatFlksMlNZUaMGJvF4in-fo6sBScWZXGbhlVE6c5bPAnpMKvaGkCbJ4l5ObVp5RLoyUvO0VHLkDVyoA_eughrfo4w4OEzmtZuLUYiDAn1CjqmpaUuJofFt_IlSOiduuvS8fo8nQ064SPkTo3YCyTvOzT1H5XFGSVGTtn9AqKujZvpCXHy25U6R6UxeoRXnVj-rNqXyoqhF0FRd7VTi",
"AWCwydhevBkR6kJR-2Z85JnSacHxDyioCsV114DY5bI0I0yIEXadRbGOAH9v7SFHTcRw310BsYemyfa-cKDggxmMi2MXX00T2c13VXAQxEKIjAJIITi-fDoUO98v7yAT5-hRn-kFKv9ddUCH-3daAFA_TaegHw9CORNFNKb50HpkEFfeQniFmcYZYTnEziyNPBjW_Z6XFTL-hRdvDnRNoKeIyQ4dydevyKS2WAzyyVVxLWveIfCzmmpuJx9p3B8qGXkClFUK94hxZEJ4pXzQLYwIjHKaZu2cHdvu4fvajIwVO2oXbCTkkrEQ_HheKB_RUuPuT7_h_2bwU35wr_5olll_lLwlSSsr2sj1SSdftExAZfg2H3tPr7_-13ev_C8yUCoXkTOFdlr9vzc2Q14iP1ps-xRR82q2YhxrqYqC-_WLhIUq9K1V"]
CID="https://maps.google.com/?cid=1396137290374075571"
H=rep(H,"<title>Osteria del Fuoco — Cucina di brace a Verona | Prenota</title>","<title>Hamburgeria — Hamburger artigianali ad Affi (Grand'Affi) | Menù</title>","title")
H=rep(H,'content="Osteria del Fuoco, cucina di brace e sapori decisi a Verona. Carni, primi della tradizione, cantina locale. 4,7★ su 180 recensioni. Prenota il tuo tavolo.">','content="Hamburgeria ad Affi, dentro il Grand\'Affi Shopping Center: hamburger artigianali, carne cotta su piastra al momento, patatine e sfizi. 4,7★ su 352 recensioni.">',"desc")
H=H.replace("Osteria del Fuoco","Hamburgeria")
H=rep(H,"<span class=\"kick\">Cucina di brace · Verona</span>","<span class=\"kick\">Hamburger artigianali · Grand'Affi, Affi</span>","hkick")
H=rep(H,"<h1>Il gusto del fuoco</h1>","<h1>Hamburgeria</h1>","h1")
H=rep(H,"<p>Carni alla brace, primi della tradizione e una cantina che racconta il territorio. Nel cuore di Verona.</p>","<p>Hamburger artigianali con carne cotta su piastra al momento, ingredienti freschi e patatine croccanti. Al Grand'Affi Shopping Center di Affi.</p>","hp")
H=rep(H,"https://images.pexels.com/photos/1633578/pexels-photo-1633578.jpeg?auto=compress&cs=tinysrgb&w=1600",photo(hp[0]),"herobg")
H=rep(H,"<span class=\"kick\">Un'esperienza unica</span>","<span class=\"kick\">La nostra cucina</span>","expk")
H=rep(H,"<h2>Sapori decisi, materie prime scelte</h2>","<h2>Hamburger fatti come si deve</h2>","exph2")
H=rep(H,"<p>All'Osteria del Fuoco la cucina parte dalla brace e dalla stagionalità. Piatti generosi, servizio caloroso e un ambiente rustico ed elegante insieme.</p>","<p>Panini generosi e ben conditi, carne alla piastra al momento, proposte anche vegetariane. Ambiente pulito e servizio veloce e cordiale.</p>","expp")
H=rep(H,'<img src="https://images.pexels.com/photos/2233729/pexels-photo-2233729.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Brace">',f'<img src="{photo(hp[1])}" alt="Hamburger">',"ei1")
H=rep(H,'<img src="https://images.pexels.com/photos/1279330/pexels-photo-1279330.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Piatto">',f'<img src="{photo(hp[2])}" alt="Piatto">',"ei2")
H=rep(H,'<img src="https://images.pexels.com/photos/941861/pexels-photo-941861.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Sala">',f'<img src="{photo(hp[3])}" alt="Locale">',"ei3")
# menu -> burger
newmenu='''<div class="menu-cols">
      <div class="menu-cat">
        <h3>Gli hamburger</h3>
        <div class="dish"><div><h5>Classic</h5><span>Manzo, insalata, pomodoro, salse della casa</span></div><div class="price">8,5 €</div></div>
        <div class="dish"><div><h5>Cheeseburger</h5><span>Manzo e formaggio fuso</span></div><div class="price">9 €</div></div>
        <div class="dish"><div><h5>Bacon burger</h5><span>Manzo, bacon croccante, cheddar</span></div><div class="price">10,5 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Specialità</h3>
        <div class="dish"><div><h5>Burger della casa</h5><span>Ricetta dello chef, condimenti freschi</span></div><div class="price">11 €</div></div>
        <div class="dish"><div><h5>Veggie burger</h5><span>Proposta vegetariana</span></div><div class="price">9,5 €</div></div>
        <div class="dish"><div><h5>Menù completo</h5><span>Burger + patatine + bibita</span></div><div class="price">13 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Fritti &amp; sfizi</h3>
        <div class="dish"><div><h5>Patatine fritte</h5><span>Croccanti e poco unte</span></div><div class="price">4 €</div></div>
        <div class="dish"><div><h5>Scamorza fritta</h5><span>Il nostro cavallo di battaglia</span></div><div class="price">5 €</div></div>
        <div class="dish"><div><h5>Anelli di cipolla</h5><span>In pastella</span></div><div class="price">4,5 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Bibite &amp; dolci</h3>
        <div class="dish"><div><h5>Bibite</h5><span>Analcoliche e birre</span></div><div class="price">3 €</div></div>
        <div class="dish"><div><h5>Birra artigianale</h5><span>Selezione alla spina</span></div><div class="price">5 €</div></div>
        <div class="dish"><div><h5>Dolce del giorno</h5><span>Chiedi al banco</span></div><div class="price">4 €</div></div>
      </div>
    </div>
  </div>
</section>'''
H=re.sub(r'<div class="menu-cols">.*?</section>', lambda m: newmenu, H, count=1, flags=re.S)
H=rep(H,'<div class="addr-img" role="img" aria-label="Ingresso dell\'osteria"></div>',f'<div class="addr-img" role="img" aria-label="Il locale" style="background:url(\'{photo(hp[4])}\') center/cover"></div>',"addrimg")
H=rep(H,"<p>Via Esempio 12, 37121 Verona (VR)</p>",f'<p><a href="{CID}" target="_blank">Località Canove — Grand\'Affi Shopping Center, Affi (VR)</a></p>',"addr")
H=rep(H,"<p>Mar–Dom 12:00–14:30 · 19:00–23:00<br>Lunedì chiuso</p>","<p>Tutti i giorni 11:30–15:00 · 17:00–22:00</p>","hours")
H=rep(H,'<div class="addr-row"><h4>Contatti</h4><p><a href="tel:+390450000000">045 000 0000</a> · <a href="mailto:info@osteriadelfuoco.it">info@osteriadelfuoco.it</a></p></div>','<div class="addr-row"><h4>Contatti</h4><p><a href="tel:+393701508787">370 150 8787</a> · <a href="https://wa.me/393701508787">WhatsApp</a></p></div>',"contacts")
H=rep(H,"<h2>4,7 su 180 recensioni</h2>","<h2>4,7 su 352 recensioni</h2>","revh2")
newrv='''<div class="rv-grid">
      <div class="rv"><div class="st">★★★★★</div><p>"Ottimo hamburger, con ottimi ingredienti e le patatine veramente buone e poco unte. La scamorza fritta eccellente. Consiglio vivamente."</p><b>eros miotto</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Personale davvero cordiale, si lavora con passione. Cibo molto buono, porzioni abbondanti e ottimo rapporto qualità-prezzo."</p><b>Fiona R.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Locale curato e ordinato, panini super, fatti a dovere. Servizio ottimo e veloce. Ci torniamo sicuramente."</p><b>Michael B.</b></div>
    </div>'''
H=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>', newrv+"\n  </div>\n</section>", H, count=1, flags=re.S)
H=rep(H,"https://images.pexels.com/photos/262047/pexels-photo-262047.jpeg?auto=compress&cs=tinysrgb&w=1600",photo(hp[5]),"resbg")
H=rep(H,"<h2>Prenota il tuo tavolo</h2>","<h2>Vieni a trovarci</h2>","resh2")
H=rep(H,"<p>Per gruppi, eventi o serate speciali chiamaci: ti aspettiamo attorno al fuoco.</p>","<p>Passa al Grand'Affi o scrivici su WhatsApp: ti aspettiamo con un buon hamburger.</p>","resp")
H=H.replace("tel:+390450000000","tel:+393701508787").replace("045 000 0000","370 150 8787").replace("https://wa.me/390450000000","https://wa.me/393701508787")
H=rep(H,"<p>Cucina di brace e sapori del territorio, a Verona.</p>","<p>Hamburger artigianali al Grand'Affi Shopping Center di Affi.</p>","fp")
H=rep(H,"<p>Via Esempio 12, Verona<br><a href=\"tel:+393701508787\">370 150 8787</a><br><a href=\"mailto:info@osteriadelfuoco.it\">info@osteriadelfuoco.it</a></p>",f'<p>Grand\'Affi, Affi (VR)<br><a href="tel:+393701508787">370 150 8787</a><br><a href="{CID}" target="_blank">Indicazioni</a></p>',"fcontacts")
H=rep(H,"<p>Mar–Dom 12–14:30<br>19–23<br>Lun chiuso</p>","<p>Tutti i giorni<br>11:30–15:00<br>17:00–22:00</p>","fhours")
open("hamburgeria-affi.html","w",encoding="utf-8").write(H)
print("hamburgeria-affi.html written", len(H))

# ============ ANNA ACCONCIATURE (revival) ============
A=open("parrucchieri-revival-flagship.html",encoding="utf-8").read()
ap="AWCwydivApioSRr_Anworz9Ryr3noFmifDBkR4-bmlSXWsfeE3cNyHNnEOdx2v04T2xm39R0tFlYotr70zZ8P2-4xxYavUL9yMMx2FdkFNWr0ht3sIgFZDDDURXnWbWrfTyzUx_DTfMcbfbrWCJ6FWpWra4PYdSI5fLKE1jMNVM5udBwVuJVGihLB2cpsVBLF6r4m5xZBnYrTEKshfeCrf266osVDX9khV3jyAb7mDdPxsgJuorUnQtMDRx-GROiMvwSZ4u8VZ0Bawz77M2aUXD71Zu32I-8dM3cV3LXmzX1LSUdkcVV8dA6kruLbGYEO2pmKhERwKc8vDkkpm2BdOK7icjeR5mtr53p13rz22MPGFtXUhYWPdhwzFB0sePRptGjFvuFF-TKRBTomPcHcgEtu1b_C7WCh1X7KNRckoGR_bk"
ACID="https://maps.google.com/?cid=428085637304607855"
A=rep(A,"<title>Revival Hair Studio — Parrucchiere a Verona | Prenota</title>","<title>Anna Acconciature — Parrucchiere ad Affi (VR) | Prenota</title>","atitle")
A=rep(A,'content="Revival Hair Studio, parrucchiere a Verona: taglio, colore e styling d\'autore. Un salone dal design minimal ed elegante. 4,9★ su 180 recensioni. Prenota.">','content="Anna Acconciature, parrucchiere ad Affi (VR): taglio, colore, piega e cura del capello con prodotti naturali. 5,0★ su Google. Prenota il tuo appuntamento.">',"adesc")
A=A.replace("© Revival Hair Studio — Verona","© Anna Acconciature — Affi (VR)")
A=A.replace("Revival Hair Studio","Anna Acconciature")
A=A.replace(">REVIVAL<",">ANNA ACCONCIATURE<")
A=rep(A,"<span class=\"kick\">Hair Studio · Verona</span>","<span class=\"kick\">Parrucchiere · Affi (VR)</span>","ak")
A=rep(A,"<h1>Revival</h1>","<h1>Anna Acconciature</h1>","ah1")
A=rep(A,"<p>Taglio, colore e styling d'autore. Un salone dove l'eleganza incontra la cura del dettaglio.</p>","<p>Taglio, colore e piega con cura e prodotti naturali. Un salone accogliente ad Affi, dove ti senti a casa.</p>","ahp")
A=rep(A,"https://images.pexels.com/photos/3993462/pexels-photo-3993462.jpeg?auto=compress&cs=tinysrgb&w=1600",photo(ap),"aherobg")
A=rep(A,"<h2>Uno studio dedicato allo stile, in ogni dettaglio</h2>","<h2>Un salone dedicato a te e alla cura dei tuoi capelli</h2>","aintro")
A=rep(A,"background:#ddd url('https://images.pexels.com/photos/3992874/pexels-photo-3992874.jpeg?auto=compress&cs=tinysrgb&w=1000') center/cover",f"background:#ddd url('{photo(ap)}') center/cover","asplit")
A=rep(A,"<p>Un ambiente essenziale ed elegante, pensato per farti vivere un'esperienza di bellezza fuori dal comune. Professionisti attenti, tecniche moderne e ascolto.</p>","<p>Ambiente accogliente e servizio flessibile. Consigli su misura e prodotti naturali per la cura del capello. Disponibilità e gentilezza al primo posto.</p>","asplitp")
A=rep(A,'''<ul class="split-hours">
        <li><span>Martedì – Venerdì</span><span>9:00 – 19:00</span></li>
        <li><span>Sabato</span><span>9:00 – 18:00</span></li>
        <li><span>Domenica &amp; Lunedì</span><span>Chiuso</span></li>
      </ul>''','''<ul class="split-hours">
        <li><span>Martedì – Sabato</span><span>8:00 – 18:00</span></li>
        <li><span>Domenica &amp; Lunedì</span><span>Chiuso</span></li>
      </ul>''',"ahours")
# reviews
A=rep(A,"<q>Un salone diverso da tutti. Eleganza, competenza e un taglio impeccabile.</q>","<q>Speciale… super competente e bravissima. Consigliatissima!</q>","aq")
A=rep(A,"<b>Beatrice C.</b>","<b>Denise D.</b>","aqb")
newarv='''<div class="rv-row">
      <div class="c rv"><div class="st">★★★★★</div><q>"Disponibile e gentile. Offre un ottimo servizio, con orario flessibile. Ottimi consigli e prodotti per capelli naturali."</q><b>Baita G.</b></div>
      <div class="c rv"><div class="st">★★★★★</div><q>"Speciale, super competente e bravissima. Consigliatissima!"</q><b>Denise D.</b></div>
    </div>'''
A=re.sub(r'<div class="rv-row">.*?</div>\s*</div>\s*</section>', newarv+"\n  </div>\n</section>", A, count=1, flags=re.S)
# CTA + contacts (landline only, no email/whatsapp)
A=rep(A,"<p>Chiamaci o scrivici su WhatsApp: dai forma al tuo nuovo look.</p>","<p>Chiamaci per fissare il tuo appuntamento: ti aspettiamo ad Affi.</p>","actap")
A=rep(A,'<a href="tel:+390450000000" class="btn btn-light">045 000 0000</a>\n      <a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>','<a href="tel:+390456260145" class="btn btn-light">Chiama 045 626 0145</a>\n      <a href="'+ACID+'" target="_blank" class="btn btn-ghost">Come raggiungerci</a>',"actabtns")
A=rep(A,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@revivalhair.it">info@revivalhair.it</a></p>','<p>Via Pozzo dell\'Amore 49, Affi (VR)<br><a href="tel:+390456260145">045 626 0145</a><br><a href="https://www.instagram.com/annacconciature____/" target="_blank">Instagram</a></p>',"afcontacts")
A=rep(A,"<p>Mar–Ven 9:00–19:00<br>Sab 9:00–18:00</p>","<p>Mar–Sab 8:00–18:00<br>Lun &amp; Dom chiuso</p>","afhours")
A=rep(A,"<p>Hair studio d'autore nel cuore di Verona.</p>","<p>Parrucchiere ad Affi: taglio, colore e cura del capello.</p>","afp")
A=A.replace("tel:+390450000000","tel:+390456260145")
open("anna-acconciature-affi.html","w",encoding="utf-8").write(A)
print("anna-acconciature-affi.html written", len(A))
