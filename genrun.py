# -*- coding: utf-8 -*-
import re, urllib.parse
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def photo(ref): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={ref}&key={KEY}"
def rep(html, old, new, label):
    if old not in html:
        print(f"  !! MISS [{label}]")
    return html.replace(old, new, 1)

# ============================================================
# LOVE THE HAIR (parrucchieri-salonkit)  -> love-the-hair-albaredo.html
# ============================================================
LTH_HERO="AWCwydiG7mLirFN14IE-YUKZ52bTGZ0yx0pdhx_qWiAtjP87Us8h3bheQ8KqL-Ti4vMOBW8LNkct1nELY5tbWJIstwrbmMAXvRS7COM6w69ix3TG1dIrgEmTn5MvSpUp9VYm3trs_OBWec4DGHl0O2sy_ceuYu4Yv4-UplzP20tziLaiPIOYL91cCKje4cJsyM2V82W-BK7Blz7qSs8uxv8T3NL1niyhCMVAmbzewK9UOUT4y5hyuXZ6RqR86gmLu__w5ExMXbqs8ATLci4cevhXMyY43Xa9ajoTZfxnC1MEQuSQGXzAKmikrrcQ_KV6lEQ1HmR4YnZvtiAnUQtAgt8PGGaflH_o0sr2wYLqki5KS4tTvRrppyiQIjGIoht7WEXIZsy3967wuznvNrda7yAR2Ww5uyonxqAcebizqWlkLDN3iw"
LTH_G1="AWCwydg1C_xwyLeO9lRmsXuaM490ydEKIrP8IYUAIlP32EtPwDLfgzzfe9snS98cEHKV1TCFyky4OvLnnOF1Qp6Qw9s4BXwQXar1e2qt6VydH5uXTbLNphMEE2Js-W28_WAhvpCfQvT36WE-ujFYgXHstD1g1x7apYJYJQiGBfbrB0OR_0Jqva93wm-VPJ7qbm30p0DBPQNjGn6mtY4dbLX3GSOIsludyaqiMRU86Mor1QfGj0L6tm2MHtZwHdH0OrSl_89F62UHqc_chFQWc0YlfL8QOmFWPVms9t4Dc2cuz6VINGKPcr3s69oMf_-BDe0hxeJYHQla-zjKgRPblGRhbhIh2cRPTnVCakU3bCjQIVhivM1rx8J8FlECE0c2qSRbMh1nwfPTqkim0kTTf0zJVwfZLuYh370yKvWdm50YQPT4qjge"
LTH_G2="AWCwydhm29p4tkSZaUKYmsxxJk6b-18km4kuH_Rvjx3rtnFcfFfDzNiL5-GYmb3zX9Bqfo9airCLQU-beM-bhj44SOl7J54xaObM0gcQgeSUMwqM0VOnJaVbQGzUVxLfmzmd_4jIHL_bWKcho0tcOH_-0f6IfGrBbwzF9BN1K2BnKN0uc85Twyx1fkGM84rz3zTnz4f7tZXEQdibkqMCBO7bu9GM_WQuK1VK_KWmi94nrql8SMCO9-mTOzRPCX9CIo_CUW4IYuTWRtUFZOzZDn2NEzkY_hqDVZWSBa2gfHpoD_wKJmtFCWy6qq65Oz_ZtPFkS0a3a5RQJZPrdZ6kZX4_dyX-l5Ozf3TPHfc5QpmKenaVaDzgVvRT34uYj6EEyMRJTVFWLzPgcV0hz7FB-UZ4GuIiur8GL6GdYV4YEPFrdE5oog"
LTH_G3="AWCwydg-h1F6UbJXQ3-kEUGdTFfR7mb6UXUjgi0K6c5cltJoj7-li39LifkIN7o1denpzdTOJ8C6lz5iNPN6Rumw5zE0Spm_0u-Sf5IicqGXXzf9Hz9BL4_bMsn-xuyehoULqNWTUA7AW4hXS30hberxjGf85GCXhiRT5gAFMSPORygi1J_GGA4mg4TIHiOrXznduR_AI3r-1eUcKtsJOOf_Ygxxsy66DzPaBFT2r2mT6vC3OWV4Ps8wnBQ7hKbjKFi1p1127ygWA6C3FxnbqW6ecRspwEip67Gb2zFqBtI1Kc99NnkNJmvWgPsLFKa8-SOAN-9xpBhsGv8Egf1g6g06lllDT9kWrtQeuwRUJ_w5kDN_G8Q2FVpglWjzalniV_qACXxd6Pggh4eX6zlmu6veIhvzOE4Lw23WKx190nDhi8u6br0P"
LTH_G4="AWCwydg9YlQLa5rFLM7sza9O_yBrQK7ZWZEEX7VmoolT7Bp1pceCDrZwir9pNoDkwe0Tuc0j-xjoIN8-hPivBH3TG7VaRhZaCYC_oJGIQacdg2Rer6ocj4LEK3wMr-h7Jgq9xvmlPDx9RL0lIZvJtCHwySiZx6CY82rgUyeUUEOksSslCB56ENJuoD19UBrx4RxyYVmUMM5ypcynhZhdEvWjdBXIjMmZumZrh1Kbv9mPO_EzpgykF4FfDFvscr6vn5fJPzTEQPEA9ZA-hMOHgRaPYRungnmXMAt3xIFJTOjSL48nszPInoFYRIa7ggmIn-P8JBRXe1O6TlSfXvIEnJGuRJ_oIChMlmgRtmOE1JFgwBuwwWyGYMCCZDvsMfAkyEz99LD3m5_AKnH5lpNBGLoqbSkFgl6hpxfIrbAsa3kVadNteg"
LTH_CID="https://maps.google.com/?cid=6773662699663693242"
LTH_FB="https://www.facebook.com/pages/category/Hair-Salon/Love-The-Hair-di-Rossignoli-Tania-930889770286030/"

H=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
H=rep(H,"<title>Salone Méta — Parrucchiere a Verona | Prenota</title>","<title>Love The Hair — Parrucchiere ad Albaredo d'Adige (VR) | Prenota</title>","title")
H=rep(H,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="Love The Hair di Tania Rossignoli, parrucchiere ad Albaredo d\'Adige (VR): taglio, colore, trattamenti e acconciature. 5,0★ su Google. Prenota.">',"desc")
H=rep(H,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Albaredo d\'Adige</span>',"kick")
H=rep(H,"<h1>Dove l'hairstyling è <em>olistico</em></h1>","<h1>Cura e stile per i tuoi <em>capelli</em></h1>","h1")
H=rep(H,"<p>Taglio, colore e trattamenti pensati per te e per la salute dei tuoi capelli. Un salone dove bellezza e benessere si incontrano.</p>","<p>Taglio, colore e trattamenti con cura e passione. Da Tania e dal suo team, ad Albaredo d'Adige, i tuoi capelli sono in ottime mani.</p>","herop")
H=rep(H,'<div class="hero-img"><img src="https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000" alt="Salone di parrucchiere"></div>',f'<div class="hero-img"><img src="{photo(LTH_HERO)}" alt="Love The Hair — salone ad Albaredo d\'Adige"></div>',"heroimg")
# gallery
H=rep(H,'<img src="https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Lavoro 1">',f'<img src="{photo(LTH_G1)}" alt="Lavoro 1">',"g1")
H=rep(H,'<img src="https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Lavoro 2">',f'<img src="{photo(LTH_G2)}" alt="Lavoro 2">',"g2")
H=rep(H,'<img src="https://images.pexels.com/photos/3065209/pexels-photo-3065209.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Lavoro 3">',f'<img src="{photo(LTH_G3)}" alt="Lavoro 3">',"g3")
H=rep(H,'<img src="https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Lavoro 4">',f'<img src="{photo(LTH_G4)}" alt="Lavoro 4">',"g4")
# reviews (real)
H=rep(H,'"Taglio perfetto e colore stupendo. Mi trovo benissimo ogni volta."','"Ottimo salone dove la cordialità, la professionalità e l\'esperienza la fanno da padroni. Ci tornerò sicuramente."',"rv1")
H=rep(H,"<b>Serena B.</b>","<b>Massimo F.</b>","rv1b")
H=rep(H,'"Ambiente rilassante e staff super professionale. Consigliatissimo."','"L\'ambiente è molto sereno, il personale ha molta cura dei tuoi capelli. Lo consiglio."',"rv2")
H=rep(H,"<b>Marta L.</b>","<b>Damiana F.</b>","rv2b")
H=rep(H,'"Finalmente un salone che cura davvero i capelli. Bravissimi!"','"Parrucchiere molto ma molto simpatiche e brave nelle acconciature."',"rv3")
H=rep(H,"<b>Chiara V.</b>","<b>Giorgia M.</b>","rv3b")
# footer tagline / contacts / hours / copyright
H=rep(H,"<p>Parrucchiere olistico nel cuore di Verona.</p>","<p>Parrucchiere ad Albaredo d'Adige: taglio, colore e cura del capello.</p>","ftag")
H=rep(H,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p>',f'<p>C.so Umberto I, 76 · Albaredo d\'Adige (VR)<br><a href="tel:+390457001883">045 700 1883</a><br><a href="{LTH_FB}" target="_blank">Facebook</a></p>',"fcont")
H=rep(H,"<p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p>","<p>Mer 13:30–21:30 · Gio 9–12:30, 15–19:30<br>Ven 9–19:30 · Sab 9–18:30 · Dom–Mar chiuso</p>","fhours")
H=rep(H,"© Salone Méta — Verona","© Love The Hair — Albaredo d'Adige (VR)","copy")
# brand global
H=H.replace("Salone Méta","Love The Hair")
# phone / whatsapp (Love the hair HAS mobile 345 129 6078 -> WhatsApp ok)
H=H.replace("tel:+390450000000","tel:+390457001883").replace("045 000 0000","045 700 1883").replace("https://wa.me/390450000000","https://wa.me/393451296078")
open("love-the-hair-albaredo.html","w",encoding="utf-8").write(H)
print("love-the-hair-albaredo.html", len(H))

# ============================================================
# PIZZERIA CONGO BAR (ristorante-atlantic) -> pizzeria-congo-bar-albaredo.html
# ============================================================
C1="AWCwydhNkBlpoK-KtpNuKU04Q5Mto_kK3w1KBL_a45xxjPk3VBy2_1oyp47cR-VnD25Xv6wow1iXZtQ5Vf4XL40-rnOkALMxOo4JeyNDqO-d5CyOu00fSpKN8zLL-N3EIq5DrCyxQaqOk5e5PyWpUMPvHP-EuWWD9ziDXmlGhBSq06baGFs7666i9OPyO1I3jk1dnKZcsdV3RPJb9eWPMM6cHhksPVDDU7-nd_TtB4-iWYWgIqJCR_GocPz_sqxuXO1BLn0Q8qVp24Oa6A-QOZIBIUXoFEVWq3hWy4ACKBMUDUl74eYDXYpUEnNiyl9Yz4VxAAopEqvuhrOi-jjgUL0LQraf6bXh_o6YatmDNwNKEsg50tAHYsjkn5BGzJAAf1o4JmOJjxV6Cy5PbYSwf_OnhDr9Teioc2HzwAHESnO2dqJtnlzv"
C2="AWCwydg2nUDTFOcKXnHz9d9EYOSisDM7mOUyFnPNb0v6XsrTYvZlVfhdnpKi7Dn_LDOcNfc1FIH2yoPp5r-yyXbBIeAwTlEjOXicySrZrgjDXj6eL55LQV8zDqlJEmxmTGYE3qAtBYrnHn8HlSN92IZnkSs1LB_3RlY5A8DTQytcBVsY8DbQD2kptGtECz_tsFnODafzWayEKQDnEl5mNZjwsBM6tmT5EIrg_Odo6MSSUu9EeFgjzBlfSYv-wrUiR3g_gwT8_TgEshxsC4xNsXjfW3hAzHdTeXjwpiHdMXOArQBL0TjdSWdDu3Ao1wPDVB6Bgj9VR3uZIG79Wnpo79pTWaL2u2tHSyIOUPPRRcP1nYSJrOF3YOqVoMIQ6iQYZxaDEeSOtKnNRPik-2paJHimRiKd6doNm1uzYbbYkQ-FrHajfpQ"
C3="AWCwydjQWYyYiiIJFySu91wnWNllMpa3f_v5zd4p5D44KPPsP8_M8vT0-4R8anronHDU4y9wWIIh1qVAYHMFCujpAhGcDhB8UmDwg6ZCKW61tDq6-5fStmUcjJo2TQiqLOtMN_BwwLddPAZ-bWwbtKLbKCQxNT7tpYsIXQ0BLN__rgjwa2uzRfVLF-ewgctl_OqJBo_0cWU4uYjmCSIDabjUjUezOV2dqYCP8Ezw8W-Df2OI57zm44KziIT0G93rsqBaWH5SBYBGKnDgzWc18aAqXGoMuN8HpEdVKIzJlanBC_zs5dIwMNFLYv862wESXkOUgkwnULND4n2toeZRAtU-X_ZvzKT5wGARUPjCEiJ-3NNZACSSRhFAFipjAOXuq_CDZV2iDjXU-x3-Hzog_Tn5SDAgJzzjws9i_Wsohn4P-iyeVGaxcKYVhmn0H6U3UTDn"
CONGO_CID="https://maps.google.com/?cid=14721345279856192641"
A=open("ristorante-atlantic-flagship.html",encoding="utf-8").read()
A=rep(A,"<title>Bistrot Contrada — Cucina moderna a Verona | Prenota</title>","<title>Pizzeria Congo Bar — Pizzeria ad Albaredo d'Adige (VR) | Menù</title>","t")
A=rep(A,'content="Bistrot Contrada, cucina moderna nel cuore di Verona. Menù stagionale, cocktail e vini selezionati. 4,8★ su 240 recensioni. Prenota il tuo tavolo.">','content="Pizzeria Congo Bar ad Albaredo d\'Adige (VR): pizza cotta al momento, cucina casalinga e prezzi imbattibili. 4,4★ su 339 recensioni.">',"d")
A=rep(A,'<span class="kick">Cucina moderna · Verona</span>','<span class="kick">Pizzeria & Cucina · Albaredo d\'Adige</span>',"k")
A=rep(A,'<h1 class="display">Sapori di stagione, nel cuore di Verona</h1>','<h1 class="display">La pizza di casa, ad Albaredo</h1>',"h1")
A=rep(A,'<p class="lead">Un bistrot dove la tradizione veneta incontra la cucina contemporanea. Ingredienti locali, cantina selezionata, atmosfera informale.</p>','<p class="lead">Pizza cotta al momento, piatti casalinghi e prezzi onesti. Una pizzeria di paese dove si mangia bene e si torna volentieri.</p>',"lead")
A=rep(A,'<img class="hero-img" src="https://images.pexels.com/photos/958545/pexels-photo-958545.jpeg?auto=compress&cs=tinysrgb&w=1600" alt="Sala del ristorante">',f'<img class="hero-img" src="{photo(C1)}" alt="Pizzeria Congo Bar">',"heroimg")
A=rep(A,"background:var(--paper) url('https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=1200') center/cover",f"background:var(--paper) url('{photo(C2)}') center/cover","storyimg")
A=rep(A,"<h2>Cucina d'autore, ospitalità sincera</h2>","<h2>La nostra pizzeria, dal 1980</h2>","sh2")
A=rep(A,"<p>Bistrot Contrada nasce dalla passione per la materia prima del territorio. Ogni piatto racconta il Veneto con una lettura moderna, curata dallo chef e dalla sua brigata.</p>","<p>Alla Pizzeria Congo Bar impastiamo e cuociamo la pizza al momento, con ingredienti semplici e genuini. Un punto di riferimento per le famiglie di Albaredo d'Adige.</p>","sp1")
A=rep(A,"<p>Una sala accogliente, un servizio attento e una carta dei vini pensata per accompagnare ogni portata: il posto giusto per una cena tra amici o un'occasione speciale.</p>","<p>Ambiente informale, servizio cordiale e prezzi imbattibili: pizza da asporto o al tavolo, pranzo e cena. Vi aspettiamo!</p>","sp2")
A=rep(A,"<p>Via Esempio 12<br>37121 Verona (VR)</p>","<p>Via del Sole, 19<br>37041 Albaredo d'Adige (VR)</p>","addr")
A=rep(A,"<p>Mar–Ven 19:00–23:00<br>Sab–Dom 12:30–14:30 · 19:00–23:30<br>Lunedì chiuso</p>","<p>Mar–Gio 12–14:35 · 18–23<br>Ven 12–14:35 · 18–24 · Sab–Dom 18–24<br>Lunedì chiuso</p>","hrs")
A=rep(A,'<p><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@bistrotcontrada.it">info@bistrotcontrada.it</a></p>',f'<p><a href="tel:+390456600236">045 660 0236</a><br><a href="{CONGO_CID}" target="_blank">Come arrivare →</a></p>',"cont")
# menu head + cols
A=rep(A,"<h2>Cucina di stagione</h2>","<h2>Le nostre pizze</h2>","mh")
A=rep(A,"<p>Una selezione della nostra proposta. La carta cambia con le stagioni e la disponibilità del mercato.</p>","<p>Una selezione dal nostro menù. Pizze classiche e speciali, primi e sfizi. Disponibile anche da asporto.</p>","mhp")
menu_old=re.search(r'<div class="menu-cols">.*?</div>\s*</div>\s*</section>\s*<section id="galleria"', A, re.S).group(0)
menu_new='''<div class="menu-cols">
      <div class="menu-cat">
        <h3>Pizze classiche</h3>
        <div class="dish"><div class="d-main"><h5>Margherita</h5><span>Pomodoro, mozzarella, basilico</span></div><div class="price">5,5 €</div></div>
        <div class="dish"><div class="d-main"><h5>Marinara</h5><span>Pomodoro, aglio, origano</span></div><div class="price">5 €</div></div>
        <div class="dish"><div class="d-main"><h5>Diavola</h5><span>Pomodoro, mozzarella, salame piccante</span></div><div class="price">7 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Pizze speciali</h3>
        <div class="dish"><div class="d-main"><h5>Congo</h5><span>La pizza della casa</span></div><div class="price">8,5 €</div></div>
        <div class="dish"><div class="d-main"><h5>Quattro formaggi</h5><span>Mozzarella e formaggi misti</span></div><div class="price">8 €</div></div>
        <div class="dish"><div class="d-main"><h5>Verdure</h5><span>Ortaggi di stagione grigliati</span></div><div class="price">7,5 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Cucina</h3>
        <div class="dish"><div class="d-main"><h5>Primi del giorno</h5><span>Chiedi la disponibilità</span></div><div class="price">8 €</div></div>
        <div class="dish"><div class="d-main"><h5>Hamburger &amp; patatine</h5><span>Carne, contorno di patatine</span></div><div class="price">9 €</div></div>
        <div class="dish"><div class="d-main"><h5>Insalatona</h5><span>Mista, ricca e fresca</span></div><div class="price">7 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Bibite &amp; Dolci</h3>
        <div class="dish"><div class="d-main"><h5>Bibite</h5><span>Analcoliche e birre</span></div><div class="price">2,5 €</div></div>
        <div class="dish"><div class="d-main"><h5>Birra alla spina</h5><span>Media</span></div><div class="price">4 €</div></div>
        <div class="dish"><div class="d-main"><h5>Dolce della casa</h5><span>Chiedi al banco</span></div><div class="price">4 €</div></div>
      </div>
    </div>
  </div>
</section>

<section id="galleria"'''
A=A.replace(menu_old, menu_new, 1)
# gallery imgs
A=rep(A,'<img src="https://images.pexels.com/photos/1279330/pexels-photo-1279330.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Piatto 1">',f'<img src="{photo(C3)}" alt="Pizza 1">',"gg1")
A=rep(A,'<img src="https://images.pexels.com/photos/262918/pexels-photo-262918.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Sala">',f'<img src="{photo(C1)}" alt="Locale">',"gg2")
A=rep(A,'<img src="https://images.pexels.com/photos/1058277/pexels-photo-1058277.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Piatto 2">',f'<img src="{photo(C2)}" alt="Pizza 2">',"gg3")
# reviews
A=rep(A,"<h2>4,8 su 240 recensioni</h2>","<h2>4,4 su 339 recensioni</h2>","rvh")
A=rep(A,'"Cena eccezionale, piatti curati e servizio impeccabile. Torneremo di sicuro."','"Ottima pizzeria, cibo ottimo, prezzi assolutamente imbattibili, personale gentile. Complimenti!"',"rv1")
A=rep(A,"<b>Giulia M.</b>","<b>Antonio</b>","rv1b")
A=rep(A,'"Ambiente elegante ma informale. Il risotto all\'Amarone è da provare."','"Molto buona la pizza! Super qualità-prezzo!"',"rv2")
A=rep(A,"<b>Marco T.</b>","<b>Viorel C.</b>","rv2b")
A=rep(A,'"Ottima carta dei vini e personale gentilissimo. Consigliatissimo."','"Pizza davvero buona, nel complesso abbiamo mangiato bene."',"rv3")
A=rep(A,"<b>Elena R.</b>","<b>Alice C.</b>","rv3b")
# reserve
A=rep(A,"<p>Siamo aperti dal martedì alla domenica. Per gruppi o eventi speciali, chiamaci: troveremo la soluzione migliore per voi.</p>","<p>Siamo aperti dal martedì alla domenica. Per prenotazioni o ordini d'asporto, chiamaci: ti aspettiamo!</p>","resp")
A=rep(A,'<a href="https://wa.me/390450000000" class="btn btn-out">WhatsApp</a>',f'<a href="{CONGO_CID}" target="_blank" class="btn btn-out">Come arrivare</a>',"resbtn")
A=rep(A,"<p>Cucina moderna e ospitalità nel cuore di Verona.</p>","<p>Pizzeria e cucina casalinga ad Albaredo d'Adige.</p>","ftag")
A=rep(A,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@bistrotcontrada.it">info@bistrotcontrada.it</a></p>',f'<p>Via del Sole 19, Albaredo d\'Adige (VR)<br><a href="tel:+390456600236">045 660 0236</a><br><a href="{CONGO_CID}" target="_blank">Indicazioni</a></p>',"fcont")
A=rep(A,"<p>Mar–Ven 19–23<br>Sab–Dom 12:30–14:30 · 19–23:30<br>Lun chiuso</p>","<p>Mar–Dom 12–14:35 · 18–24<br>Lunedì chiuso</p>","fhrs")
A=rep(A,"© Bistrot Contrada — Verona","© Pizzeria Congo Bar — Albaredo d'Adige (VR)","copy")
A=rep(A,'<a href="https://wa.me/390450000000" class="wa">WhatsApp</a>',f'<a href="{CONGO_CID}" target="_blank" class="wa">Mappa</a>',"mbarwa")
A=A.replace("Bistrot Contrada","Pizzeria Congo Bar")
A=A.replace("tel:+390450000000","tel:+390456600236").replace("045 000 0000","045 660 0236")
open("pizzeria-congo-bar-albaredo.html","w",encoding="utf-8").write(A)
print("pizzeria-congo-bar-albaredo.html", len(A))

# ============================================================
# BAR TRATTORIA ISOLANI (ristorante-juniper) -> bar-trattoria-isolani-albaredo.html
# ============================================================
I1="AWCwydgE6Tvs5oaMiPsDPKDM5C-bNJJVCS7Ct0h_O2siGBdR5MyQe6NyxoQ9xv9QGRcvRXzHUDAiuK8b6SX1LCN2Wc0dqksu92-WTDEedACsZiXfsDBkwOMJH4glBhJWPFlePjPawVuXgpLDb0xOD8iNncHE5w3wysNbMUFkPuAiC50ifYvVZ9qxRPcH-DpwrEzDJZfKmoyg2NUByaErK0bs3-JfGdjqFa_3PQRNlzl1p8PFJ5xkbTruam3zxhJ5F9lhXXN_8OStLuFgb4I50XNL28UmzChEGpYew2J8iJxOsTN4__5CBTK3uatfkhYXwlPJWuinqmDJG0ilTGrPWCzfMwF-UkmPlK7v7jqdztkJat7yxJ0jBDopos48HsRul9MSEgSv-U-bo0M-a_I6rysa0pSd363fjjqCLWDyeAGe-mCod571qtSwfedoiqroNNO3"
I2="AWCwydh8HdPwquZHQeFia1SaGrpBoPPkumbj2IBEkUSertXdnqe59v2uqSTpZfwOevtUzyOiDA7C-4AKgofD993LfhPwn67KiOS2mg5Wgx1g41cDyuOC3R3g00pjUZuiozAgdH7Q8Z7oKPrA9w7t0ovQnNCGitiwZCnNbufn_QMRkXY3OEQGvJpd-sUC7LH_C2gco7Ct4YNIZFvdXdLvryizdDNW90HWEfOe8eUYdsb9e7zryHpkmm1vGLkyDYUAwRQoJjXSf8V77t7ZJ5e7uTjMzPAligC8ljA35lCXa-zey-FvIMX2xy2W84bsI3vz0MrW14dUmW7vaDH_0c5Sl792Eg0la-1xxbG7SO_s5TcFcNR2_Wc2_FWzh7ApYIBjmUoRwo4OZ4YgsfPUay-glKx3K9Chk8GBhsHo-zgGDOyCGZwoT7k"
I3="AWCwydjoKBpw7JLhN3RAaFZSH8sziO8HxdNuVBgdg9s5Cp7JxTYHLo7xSizA6vlOZEJwEIjaCSbVdWnWuH8iFyH6G0jwMvprpG-OrwzsMdDAqobUNSOUbcNPd2cAW5YzcuE0HADPkMdx7sOfrBUmAFrC_yqA-4OMXvtEC-cK9da7XmW_3Wo__Uf8-GD_M6JcaW1zJYFXrY4fJJav2aBQDrx7a4CkeG1nhi2UXPfmDN2C3ESGN-SzU-tZNmEKltMxwhIezg-EkUn0YQfDpN-9798ZF6oaREZYNyHtn8kWzn00SGuUl4RuOBFhThJmEfP2yksPBkb_9HXG1cXf7CJX_FoAJm0g2HQWIK5bwAEgpNqDwAvZRcdANSkt606RFnzXhNIC03vqhZroIK370K-8PI5CLCGblOIaBJo6-NEujHprBr9ctdECc4WVAeClPAZttg"
ISO_CID="https://maps.google.com/?cid=17857696104779878211"
J=open("ristorante-juniper-flagship.html",encoding="utf-8").read()
J=rep(J,"<title>Ristorante Ginepro — Fine dining a Verona | Prenota</title>","<title>Bar Trattoria Isolani — Trattoria ad Albaredo d'Adige (VR)</title>","t")
J=rep(J,'content="Ristorante Ginepro, cucina raffinata e stagionale a Verona. Percorsi degustazione, cantina d\'autore, sala elegante. 4,9★ su 210 recensioni. Prenota.">','content="Bar Trattoria Isolani ad Albaredo d\'Adige (VR): colazione, pranzo di lavoro e cucina casalinga. Aperti dalle 6 a mezzanotte. 4,2★ su 43 recensioni.">',"d")
J=rep(J,'<span class="kick">Fine dining · Verona</span>','<span class="kick">Bar & Trattoria · Albaredo d\'Adige</span>',"k")
J=rep(J,"<h1>L'arte della tavola</h1>","<h1>La tua trattoria di paese</h1>","h1")
J=rep(J,"<p>Cucina raffinata e stagionale, in una sala elegante nel cuore di Verona. Un'esperienza da vivere con calma.</p>","<p>Colazione al bancone, pranzo di lavoro e cucina casalinga. Un punto d'incontro ad Albaredo d'Adige, dal mattino fino a sera.</p>","herop")
J=rep(J,"url('https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1600')",f"url('{photo(I1)}')","herobg")
J=rep(J,"<h2>Dove ogni piatto è un piccolo racconto</h2>","<h2>Cucina semplice, fatta in casa</h2>","ih2")
J=rep(J,"<p>Al Ristorante Ginepro celebriamo la materia prima con tecnica e misura. Percorsi degustazione che cambiano con le stagioni, una cantina curata e un servizio discreto e attento.</p>","<p>Al Bar Trattoria Isolani trovi la cucina di casa: primi e secondi della tradizione, un menù di lavoro a pranzo e l'accoglienza di sempre. Il bar è aperto dalle 6 del mattino.</p>","ip")
J=rep(J,'<img class="split-img" src="https://images.pexels.com/photos/2696064/pexels-photo-2696064.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Piatto d\'autore">',f'<img class="split-img" src="{photo(I2)}" alt="La trattoria">',"splitimg")
J=rep(J,"<h3>Stagionalità, territorio, eleganza</h3>","<h3>Genuinità e porzioni giuste</h3>","sh3")
J=rep(J,"<p>Lavoriamo con piccoli produttori locali per portare in tavola solo il meglio di ogni stagione. Ogni dettaglio, dalla mise en place al calice, è pensato per l'ospite.</p>","<p>Piatti casalinghi preparati ogni giorno, primi e secondi di una volta. Ideale per la pausa pranzo di chi lavora in zona.</p>","sp1")
J=rep(J,"<p>Un luogo intimo, ideale per cene speciali, anniversari e occasioni da ricordare.</p>","<p>Un locale alla mano, dove fermarsi per un caffè, un pranzo veloce o una cena in compagnia.</p>","sp2")
# menu
menu_old2=re.search(r'<div class="menu-cols">.*?</div>\s*</div>\s*</section>\s*<section id="galleria"', J, re.S).group(0)
menu_new2='''<div class="menu-cols">
      <div class="menu-cat">
        <h3>Colazione &amp; Bar</h3>
        <div class="dish"><h5>Caffè &amp; brioche</h5><span>Al bancone, dalle 6:00</span><div class="price">2 €</div></div>
        <div class="dish"><h5>Cappuccino</h5><span>Con pasticceria fresca</span><div class="price">1,5 €</div></div>
        <div class="dish"><h5>Aperitivo</h5><span>Con stuzzichini</span><div class="price">5 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Primi</h3>
        <div class="dish"><h5>Pasta al ragù</h5><span>Fatta in casa</span><div class="price">7 €</div></div>
        <div class="dish"><h5>Risotto del giorno</h5><span>Secondo disponibilità</span><div class="price">8 €</div></div>
        <div class="dish"><h5>Minestra / zuppa</h5><span>Della tradizione</span><div class="price">6 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Secondi</h3>
        <div class="dish"><h5>Carne del giorno</h5><span>Con contorno</span><div class="price">10 €</div></div>
        <div class="dish"><h5>Scaloppine</h5><span>Al limone o funghi</span><div class="price">9 €</div></div>
        <div class="dish"><h5>Contorni di stagione</h5><span>Verdure fresche</span><div class="price">3,5 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Menù pranzo</h3>
        <div class="dish"><h5>Menù di lavoro</h5><span>Primo, secondo, contorno</span><div class="price">12 €</div></div>
        <div class="dish"><h5>Primo + contorno</h5><span>Pausa veloce</span><div class="price">9 €</div></div>
        <div class="dish"><h5>Caffè incluso</h5><span>Con il menù pranzo</span><div class="price">—</div></div>
      </div>
    </div>
  </div>
</section>

<section id="galleria"'''
J=J.replace(menu_old2, menu_new2, 1)
# gallery
J=rep(J,'<img src="https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Piatto">',f'<img src="{photo(I3)}" alt="Piatto">',"gg1")
J=rep(J,'<img src="https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Sala">',f'<img src="{photo(I1)}" alt="Locale">',"gg2")
J=rep(J,'<img src="https://images.pexels.com/photos/3184183/pexels-photo-3184183.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Dettaglio">',f'<img src="{photo(I2)}" alt="Dettaglio">',"gg3")
# reviews
J=rep(J,"<h2>4,9 su 210 recensioni</h2>","<h2>4,2 su 43 recensioni</h2>","rvh")
J=rep(J,'"Un\'esperienza raffinata dall\'inizio alla fine. Ogni piatto un\'emozione."','"Cucina tradizionale, molto buoni sia i primi che i secondi."',"rv1")
J=rep(J,"<b>Chiara F.</b>","<b>Agostino R.</b>","rv1b")
J=rep(J,'"Servizio impeccabile e cantina straordinaria. Il posto per le occasioni."','"Quando sono in zona mi fermo sempre e sono sempre soddisfatta."',"rv2")
J=rep(J,"<b>Davide N.</b>","<b>Rosa Maria G.</b>","rv2b")
J=rep(J,'"Cucina elegante e mai banale. Il percorso degustazione vale il viaggio."','"Cucina semplice ma di qualità, ottimo per la pausa pranzo."',"rv3")
J=rep(J,"<b>Francesca L.</b>","<b>Stefano O.</b>","rv3b")
# visit
J=rep(J,"<p>Consigliamo la prenotazione. Per menù degustazione ed eventi privati, contattaci.</p>","<p>Passa a trovarci per colazione, pranzo o cena. Per il menù di lavoro e informazioni, chiamaci pure.</p>","visp")
J=rep(J,"<div class=\"hours\">Via Esempio 12, Verona · Mar–Dom 19:00–23:00 · Lunedì chiuso</div>","<div class=\"hours\">Via Motta, Albaredo d'Adige (VR) · Lun–Sab 6:00–24:00 · Domenica chiuso</div>","vishrs")
J=rep(J,"url('https://images.pexels.com/photos/1307698/pexels-photo-1307698.jpeg?auto=compress&cs=tinysrgb&w=1600')",f"url('{photo(I3)}')","visbg")
J=rep(J,'<a href="https://wa.me/390450000000" class="btn btn-light">WhatsApp</a>',f'<a href="{ISO_CID}" target="_blank" class="btn btn-light">Come arrivare</a>',"visbtn")
# footer
J=rep(J,"<p>Cucina raffinata e stagionale nel cuore di Verona.</p>","<p>Bar e trattoria casalinga ad Albaredo d'Adige.</p>","ftag")
J=rep(J,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@ristoranteginepro.it">info@ristoranteginepro.it</a></p>',f'<p>Via Motta, Albaredo d\'Adige (VR)<br><a href="tel:+390457000069">045 700 0069</a><br><a href="{ISO_CID}" target="_blank">Indicazioni</a></p>',"fcont")
J=rep(J,"<p>Mar–Dom 19:00–23:00<br>Lunedì chiuso</p>","<p>Lun–Sab 6:00–24:00<br>Domenica chiuso</p>","fhrs")
J=rep(J,'<a href="https://wa.me/390450000000" class="wa">WhatsApp</a>',f'<a href="{ISO_CID}" target="_blank" class="wa">Mappa</a>',"mbarwa")
J=rep(J,"© Ristorante Ginepro — Verona","© Bar Trattoria Isolani — Albaredo d'Adige (VR)","copy")
J=J.replace("Percorso Ginepro","Piatto della casa").replace("Ristorante Ginepro","Bar Trattoria Isolani").replace(">Ginepro<",">Trattoria Isolani<")
J=J.replace("tel:+390450000000","tel:+390457000069").replace("045 000 0000","045 700 0069")
open("bar-trattoria-isolani-albaredo.html","w",encoding="utf-8").write(J)
print("bar-trattoria-isolani-albaredo.html", len(J))

# WhatsApp link for Love the hair (Laura template, section 9b)
SITO="https://hubtecit-srl.github.io/website/love-the-hair-albaredo.html"
msg=("Buongiorno,\nSono Laura di HubTec, azienda di Verona.\n\n"
"Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: "+SITO+"\n\n"
"Se vi piace, lo attiviamo con soli 200€.\n\n"
"In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
"Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
"Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n"
"Laura Borin - HubTec")
walink="https://wa.me/393451296078?text="+urllib.parse.quote(msg)
open("/tmp/lth_wa.txt","w").write(walink)
print("WA_LINK_OK", len(walink))
print("DONE")
