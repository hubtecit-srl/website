# -*- coding: utf-8 -*-
import re, json, urllib.parse, itertools, datetime
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
DATA="2026-07-24"
BASE="https://hubtecit-srl.github.io/website/"
def ph(ref,w): return "https://maps.googleapis.com/maps/api/place/photo?maxwidth=%d&photo_reference=%s&key=%s"%(w,ref,KEY)

def sub_places_photos(html, refs):
    cyc=itertools.cycle(refs)
    def rep(m):
        return "maxwidth=%s&photo_reference=%s&key=%s"%(m.group(1), next(cyc), KEY)
    return re.sub(r"maxwidth=(\d+)&photo_reference=[^&\"']+&key="+re.escape(KEY), rep, html)

def sub_pexels(html, refs, w=1200):
    cyc=itertools.cycle(refs)
    def rep(m): return ph(next(cyc), w)
    return re.sub(r"https://images\.pexels\.com/photos/[^\s'\")]+", rep, html)

def wa_link(num_digits, site_url):
    txt=("Buongiorno,\nSono Laura di HubTec, azienda di Verona.\n\n"
         "Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: "+site_url+"\n\n"
         "Se vi piace, lo attiviamo con soli 200€.\n\n"
         "In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
         "Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
         "Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n"
         "Laura Borin - HubTec")
    return "https://wa.me/39"+num_digits+"?text="+urllib.parse.quote(txt)

crm=[]
def add_crm(**k): crm.append(k)

# ============================================================
# LEAD 1: Trattoria da Pasinato  (template il-vicoletto)  -> WhatsApp NO (fisso). Canale "Da contattare a mano"
# ============================================================
PAS=[
"AWCwydi2JuQLh1zen_AdNE1trfGJq1luhv4uCtfgVwE_iS5_3p4A9Lo4xR9FeH_SI_wKdX_1fwVLbNNuHBYjpc5JdUKrW6WO4mx8hlwlCblZeTQ6OBaPrSBMAZzsYats0mh7fwJTmtfkCBgBzgrPshtopOWMoTNfTtw1pQzFJ0zRMGnGT10p1iYsXDdw7fgNubEwlFGKaT6ZssoNK6_hXNFyEV6F-RdrDmWzIYBw90AA1j3lWBb4z9Y9E6ppVoPTpxTuvmKaScIH3Yan5dsjEkxEYXGrmi6xgb2u4PUKtRflFg2o9VbPEphdJyJuXmy6kQIWMNAJ9jWvciYAjtOiFAJke_YDQzmlEDw_ToBRXf0_jkVqnEzLb6pJB9Kh8fBzdvn_q2QxupTvj_v93AYwPU91-jMJ92t3pYfqNLeoQSUurlwzzGHV",
"AWCwydimS4WFayTZ-rV1xeGfkuE-Dix9vpAwF6FGr69uYdirrmx6Vk-ylWURSkip1UhQNxxrWiFjmmlX_SLXGvb_EcoZZiWCM7VM4KIqRLp8s30cVrHRHvq2jQrQnmFoDiDJlAYNP_mbI1QXOMiwKJ4thQu7mDf4lZ4TI6dLTeBgH3cEsbj88swYCUktXDOhlaTCJwwEwgsrb7-uIkHx1wNHYH1WammJ0awPv87PobuF7ApLPPQB3Xd_Ha04_cy0A6oX-urGpoyPOHY_2-tmAN5vwAgf8Nz2-cnKYw6V43st45HHu-JulZwvTvRzVU2L_EDIvS6RlQ0le1VzwTmhEcv5K_ri6MEcFNN2w3eZ5uQV6hh_LqjlAZrVrJZpwIVHGxtQLXg_Ltg48VKQDRjlupIMKhCjr96gAfjkxiMFOY-_tvVhFQxz",
"AWCwydiXe7vS0GuJTPnhurEap9x1RApOwop49GDtSQWkboxQLqgZzfbkcL6ZJln0IZ8VD_eM3eGSx1Z1lwaemkLzYGysBIPRj43I1NCDv9DBC8lVLVieV32yPkNdPwTJWZa9W3QusDtk0k5TEIg-gnNMynkhUX4sDn8fHcvzc__ktXNB1LqVVuRBoGn-HDFQZFhSLkT_4QQdS8qo3DM2Y3wFjvFlsrRsZKBceV3CV_pADaYiJqGZiH9p8bgUosy4ykbmOvVPU9MPcPsXo_y_dBMxN_CH1zBVrVGD5wYYqYAAQBpx4bXLvb309GXIq74x7hcp8e3ngtiyBjfQj2G8YkU39XedzIblr8KQ_dLlKdmNyx8iniLhtOjI62PSXpDoO8roOKIsb2FFeDu7F69X-RAvTuA-qZYiymCssNFS44inSOg",
"AWCwydj-pC5wlK6QqDt4eA0n56qkTXFdpPmGau3A8AH4t1azyjER4Z2ACS6SlzAquAsoIsHQPd_HywcIFuA0wmw6mhU4d7d76K34F0RBmcrv7PT--tARqd3IMFbnxyrd4CAAC7pGVxicqEFrXTtZ4zb5crMOQav_vjFYXiHo7w3Oolc5RYVJiw0NujWfwsXKyJRj9KZIIhl-twr9T6ZwZQFvneefie2lYP4owZAspB78j_W5UFhbEZI0wsztu-J8mZ5HYuQCL-MLCkAjUiUy9AmEsZkANIX8gLZGrE3C6f1gsjJXNTcc5zufyEI3lg_RPhI2UBANQFj3G-_mD4udlkHIr6I4J2eiA1NmmRAE7P8spclewPDU7S__jmIk6i4qMz8h_DIelWqqPa4gunab1beisDiMkoN1tE77UR0LQpskkTyOkQ",
"AWCwydgmDLWOuNJzrxETmWx0xlU3mRmw5Js2dleqO7bbr68rHx15aFSK_2Iw0M9sYDW5JFLwd_einho7tacUBMvP6wcu4gUh7-lynT6wO1hD4hewmZDRPdPELimJQY-ozV0-h2OPPS04S_mPHkKKb4kTtuua3YuFapPERVtgGpz5dQB5FhXAKeVGcvkxv5cIGi3hMPXfMCxt24Q5e0a3-DQPjuoBgkqFEZHedQUIHUOzsCnT35pam-GOPcUu4rucF4-CRW5tpFKI4LoDGxqPz8BCEjX5j0EC1YlxNEFVqrUhKxzz6Dep_3BNUoU5WJgFlmU6fmuZNzZeyikrLxgEZk8uPm_Ygbc0tNuQUEHIE3VKAKU6goH1G2A3bm6qmy6fDz97EqeMFWyDik9ovf19iblu1p-k2IFfkMgMnb4_lO99twGxAxnD",
"AWCwydg-yk8hlF5RCyfl3A7eYvT-hRXGZXuRQOZ5vfALKwhPAWtdSvhmNjvRaosFSmj7l6h5OuAj82SlreeyiDHaN_9D1LH6EMqJgbXQVdoaWb-G5VwfcuqqjccXF27apk2CqEf2jXc2yZqv65NA3mAFbRCcYVY_pJfcrhBUJvbMu605EDmzT4rjYJd-YZPXnHWbw1bh7CdlsvW8M4OoAxEfbVoCDVfVAWDJpEbAdQ-ii54s4jaNusXJ8UaDtQdoOOUII_Fmcsch6ZbWHTKgdAjEvvoTUIFIr_pqKbZddojMdOVVGLFKOkgi4oY7A4R-0HIKAtSh5tlaabVVFpeddmVtQZWLQZxhcyDsiBQG50yMbls1G87_SKGnGahWT4rZdHwdrh3-F5fIlyEolp1Ui8S4y0xC4g_BngWUOKM2luXCgG4eGQ",
"AWCwydjTGycDo-85anP4KGJC-xHwqGOB7SGvbdaBZAue8uOSDFJlgou8-GPiJ1RxL41rlJaELhv2pYgZlnF77fNkmu020a74aqHEemkNv15PyPN1b3QCTccrlcZ42QnnRzgS6y-kqfS-GIH3Siqw06r--sdNIXhgTupVIvj6wtuBWOOqjG8YkBds49eqxoz8G6cbBn5vr1Hi64CvpZIIwyoKxuFxN2qR28wgCE4kgktkv0c4ElqFQCW_LcOSg-D0H_I0OCFNwDLbB2D9CS4nsaadQVDh6f3SD_iYnFNhOKpVOi9uu9bQCL4DpdnMK8eMedsKsD6fGPm1OW3WmB4JMofBI8_FPvc3-6fWWTtYHva_sDtB0xPJkG05t72aqP9vfZo3OUx5FVPbLabwfvyw_pq4irtrqnB8SQURaeBTzRvtGAC5PE8",
"AWCwydjnG8nLBb_gARyYT4SjIDDh-ivXA9LASVoXK_Rv6rY-N3AA7UAAEzi6MEAr-0PLURECvc0bAcbDwJnvSMFHNVhX2CiOTmS9NS8u-3U5MEPwaYwezBQBBfeuX528YWDG8q9CK8Dh6nT0JYKcrPx9LNdgHa064ZwcpevjgiyywG_8T_MA-OpL-ycaH39LZe0EPScLDDz3aNLpmb4VeMqtuSZbwcqYZkglLAFuKQfWa-8dbg4kJ4wgRgyjnM7Au8V_G-P19Wd4Glz6lYDzOhnA2kedta7XVslPEpTtAuS-VUzI328mnhP-wi-Nndz0ytAiKw7PxaAQdsOr-j1SpxlRgUCBa8bu8b4Ci-e9zNr2ola-mlSgfXOUL4kaBB4mQovUJ6yDB3yvtbmNK_mYNix0NxayR5mjAlsf_3YyEl9H7pC-rQ",
]
h=open("il-vicoletto-trattoria-verona.html",encoding="utf-8").read()
r=[
("<title>Il Vicoletto Trattoria — Cucina tradizionale veronese | Verona</title>",
 "<title>Trattoria da Pasinato — Cucina veronese a Buttapietra (VR)</title>"),
('<meta name="description" content="Il Vicoletto Trattoria, cucina tradizionale veronese nel centro di Verona. Bigoli all\'anatra, pastissada de caval, fegato alla veneta. 4,8★ su 1.842 recensioni. Prenota un tavolo.">',
 '<meta name="description" content="Trattoria da Pasinato a Buttapietra (VR): cucina veronese casalinga e menu fisso a pranzo, atmosfera di famiglia. 4,3★ su 207 recensioni. Chiama e prenota.">'),
('<a href="#" class="brand">Il Vicoletto<span>.</span></a>',
 '<a href="#" class="brand">Trattoria da Pasinato<span>.</span></a>'),
('<div class="kicker">Trattoria · Verona centro</div>',
 '<div class="kicker">Trattoria di famiglia · Buttapietra</div>'),
('<p class="sub">Nel cuore del centro storico, tra vicoli e pietra viva. Piatti della tradizione, materie prime scelte, accoglienza sincera.</p>',
 '<p class="sub">A Buttapietra, una trattoria di famiglia dove si mangia bene e ci si sente a casa. Menu fisso a pranzo con buona scelta e cucina veronese abbondante.</p>'),
('<div><span class="stars">★★★★★</span> <b>4,8</b></div>',
 '<div><span class="stars">★★★★☆</span> <b>4,3</b></div>'),
('<div>1.842 recensioni Google</div>','<div>207 recensioni Google</div>'),
('<div>Via Santa Maria in Chiavica 5</div>','<div>Strada Provinciale 51 Ovest 38, Buttapietra</div>'),
('<h2>Un vicolo, una tavola, una tradizione</h2>','<h2>Una tavola di famiglia, dal pranzo di lavoro alle feste</h2>'),
('<p>Il Vicoletto è un tempio della cucina tradizionale veronese, quella vera. Un locale intimo ed elegante, curato nei dettagli, dove ogni piatto racconta il territorio.</p>',
 '<p>La Trattoria da Pasinato è un locale caratteristico di Buttapietra: semplicità, sobrietà e una buona cucina abbondante, con un costo davvero abbordabile per tutti.</p>'),
('<p>Materie prime di altissima qualità, lavorate con maestria e passione: dai bigoli all\'anatra alla pastissada de caval, ogni portata è una carezza per il palato. In sala, un servizio attento, gentile e preciso che mette l\'ospite al centro.</p>',
 '<p>Ideale per un pranzo di lavoro o in compagnia, con menu fisso e varia scelta. Per le occasioni speciali abbiamo anche una saletta riservata: il proprietario Zeno e il personale vi faranno sentire in famiglia.</p>'),
('<div class="sign">— dove si mangia bene e ci si sente a casa</div>',
 '<div class="sign">— dove si mangia bene e ci si sente a casa</div>'),
('<p class="menu-note">Il menù cambia con la stagione — chiedi in sala i piatti del giorno e la carta dei vini.</p>',
 '<p class="menu-note">A pranzo trovi il nostro menu fisso con varia scelta — chiedi in sala i piatti del giorno.</p>'),
('<h2>4,8 su 1.842 recensioni</h2>','<h2>4,3 su 207 recensioni</h2>'),
('Leggi tutte le 1.842 recensioni su Google →','Leggi tutte le 207 recensioni su Google →'),
('<a href="https://maps.google.com/?cid=8374942607263514723" target="_blank" rel="noopener">Via Santa Maria in Chiavica 5, 37121 Verona</a>',
 '<a href="https://maps.google.com/?cid=13648034815617291636" target="_blank" rel="noopener">Strada Provinciale 51 Ovest 38, 37060 Buttapietra (VR)</a>'),
('class="btn btn-out">Facebook</a>','class="btn btn-out">Come arrivare</a>'),
('src="https://www.google.com/maps?q=Via+Santa+Maria+in+Chiavica+5,+37121+Verona&output=embed"',
 'src="https://www.google.com/maps?q=Trattoria+da+Pasinato+Strada+Provinciale+51+Buttapietra+VR&output=embed"'),
('<div class="foot-line">Trattoria · Cucina tradizionale veronese</div>',
 '<div class="foot-line">Trattoria · Cucina veronese casalinga · Buttapietra</div>'),
('<div class="foot-line">© 2026 Il Vicoletto Trattoria · Via Santa Maria in Chiavica 5, Verona · P.IVA da inserire</div>',
 '<div class="foot-line">© 2026 Trattoria da Pasinato · Strada Provinciale 51 Ovest 38, Buttapietra (VR) · P.IVA da inserire</div>'),
('const periods={0:[[1200,1500],[1900,2230]],1:[[1200,1430],[1900,2230]],2:[[1200,1430],[1900,2230]],3:[[1200,1430],[1900,2230]],4:[[1200,1430],[1900,2230]],5:[[1200,1430],[1900,2300]],6:[[1200,1500],[1900,2300]]};',
 'const periods={0:[[1200,1400]],1:[[1200,1400]],2:[[1200,1400]],3:[[1200,1400]],4:[[1200,1400]],5:[[1200,1400]],6:[[1200,1400]]};'),
]
for a,b in r:
    assert a in h, "MISS PAS: "+a[:60]
    h=h.replace(a,b)
# hours list
newhours=('<ul class="hours-list" id="hoursList">\n'
 '          <li data-day="1"><span class="d">Lunedì</span><span>12:00–14:00</span></li>\n'
 '          <li data-day="2"><span class="d">Martedì</span><span>12:00–14:00</span></li>\n'
 '          <li data-day="3"><span class="d">Mercoledì</span><span>12:00–14:00</span></li>\n'
 '          <li data-day="4"><span class="d">Giovedì</span><span>12:00–14:00</span></li>\n'
 '          <li data-day="5"><span class="d">Venerdì</span><span>12:00–14:00</span></li>\n'
 '          <li data-day="6"><span class="d">Sabato</span><span>12:00–14:00</span></li>\n'
 '          <li data-day="0"><span class="d">Domenica</span><span>12:00–14:00</span></li>\n'
 '        </ul>')
h=re.sub(r'<ul class="hours-list" id="hoursList">.*?</ul>', lambda m:newhours, h, flags=re.S)
# reviews grid
def vic_rev(text,name,when,stars):
    s='★'*stars+'☆'*(5-stars)
    return ('      <div class="rev">\n'
            '        <div class="stars">%s</div>\n'
            '        <p>“%s”</p>\n'
            '        <div class="who"><div><b>%s</b><span>%s</span></div></div>\n'
            '      </div>'%(s,text,name,when))
revs=[
 vic_rev("Sono stata per i 90 anni di mia mamma in una stanza tutta per noi: abbiamo mangiato bene, con atmosfera di casa. Molto gentile il proprietario Zeno e anche la cameriera.","Marisa Ferlini","5 mesi fa",5),
 vic_rev("Locale caratteristico ed in linea con quello che mi aspettavo. Semplicità, sobrietà e buona cucina abbondante. Il costo è veramente abbordabile da tutti. Consigliato.","Mauro Rocchi","un anno fa",5),
 vic_rev("Il posto ideale per un buon pranzo di lavoro o in compagnia, a menù fisso ma con varia scelta. Personale che ti fa sentire in famiglia.","Albiza Bm","un anno fa",4),
]
newgrid='<div class="rev-grid">\n'+"\n".join(revs)+"\n    </div>"
h=re.sub(r'<div class="rev-grid">.*?</div>\s*(?=<div class="rev-foot">)', lambda m:newgrid+"\n    ", h, flags=re.S)
# global
h=h.replace("+390458769827","+390456660966")
h=h.replace("8374942607263514723","13648034815617291636")
h=h.replace("https://www.facebook.com/profile.php?id=100078507787681","https://maps.google.com/?cid=13648034815617291636")
h=h.replace("Il Vicoletto","Trattoria da Pasinato")
h=sub_places_photos(h,PAS)
open("trattoria-da-pasinato-buttapietra.html","w",encoding="utf-8").write(h)
add_crm(name="Trattoria da Pasinato",file="trattoria-da-pasinato-buttapietra.html",phone="045 666 0966",intl="390456660966",comune="Buttapietra",cid="13648034815617291636",tmpl="ristorante-vicoletto",url=BASE+"trattoria-da-pasinato-buttapietra.html",wa="")
print("OK pasinato", len(h))

# ============================================================
# LEAD 2: Turkish Pizza Kebab (template atlantic) -> WhatsApp (389)
# ============================================================
KEB=[
"AWCwydig96Mht-RfS6KNXOGkRgYrxyzFUvwWijm19GeKHYhkx91dIO3FZwBvpDs5_1DAPeR_HmLjrXNMgrvnQpZBTV2KYvx2G4zNNc9y7cpsBnvzbtYpcmnjIaXOKmORohNuSXdkSXxi6c7HXdJeNGI7spBArCfi1T5RSn_V2lqmV8CqTuY4zVNHAbqMykaT4QB6U7QRYvUgcwhpig38ApIBdg46jRinvcLcVnE_2ZjQ6WQxsEXPpLlUdz1wzGg8DUGDRJrLiNCq--H_MgS3_Sax2zRvn5tE9MOd7YDN_gXFXQl2DBiGeM2nsmlQSZlHOfjze_MyzgUdZOsbAi8E9lvDja-jF_AMrHzNtJD664cEAYkNW0hkoGEDSo2GXSAr00Tn-C_2jmQrmB6S2JbYm5jrhryHugIGxIRhCDB8PlUeozAHVVU9MFoWEc8dPGi_kTG7",
"AWCwydhI6bj1rMKJwgKOW7OVeyZ-aXcTXJllnRa0EEU0KJnofJ6Ro6uTGi7BX23xxpoOWYNr_ivTcMsWr6HDe8slQdz7hExdr0ZIJwPn1orPwKKbQkibhwBy5FCm_M-1cVwogcnfAbIH0CUO-L71WJvZWt1ZKEpyGlpFutGrGkxepQR7xeWl_ArDtDWVLUg45z7_7BkomPHRcdYy6-8lHyxuT2TRpRG7WSWORDe9-lLKE-ipQBBmth8g1UY3GVq3R3JvNwJEtmJtphhjHNFcOegcZbPraa5hWodahSWmFuqrx33zjEyqqitat822_ABt3_m4NU7uww13545-2Q-yydusZnyp5CBvyeEm5myHfSezKN0jn8928mOeXB0EqRifUqyNXDg-Omw3lToz-MfBedMDtC9ZeXVVqVt90GsA_Vv5DywM9njGbSfHuYgSxPS7s5A0",
"AWCwydilXVHOC2vJQBGa7aYKuD9ZKm4UUXSbc8Kd1pmHx68ln5bbGgBspkH6vdmU5R-CyA9KZcCauKODTZRNdeDlW5i-7DctuJosGnoCQBFmUA1gDSFMYOEISOv4ZeKvMX9nD5DK0IYhN-zR01xd23ofMFbZ_XgC4DeX9WHuxLLVllsjRL-_kKTYpIe06TC7NuNz6QPl7uGiV2XOcZfucCyNj3x-gJIvi15ITjMIjjrqzeXUGlOC90GZlKUz2cSlb13OsLwPUU3CJKe0QW9TJkjGoi8ADZpSDyTNXVhIdGvZvpX4WNhswf_n87GcWN3ImgkYgnKZ_CppqJ_lnQpdunbEDMra78QFFVrjylclGpHA-fZPjQAoRt0i2WgySkO7J_TMLl1mV6m9Ve6R-KqnOS1FTzUOXMdgq05LMMaDBhQwCYhvpYGDtJVUq3xTdrewjA",
"AWCwydi4pJN62KEn0wRSjI_rrgr6zd4aMc92cp426np6XlwBmo4mEfmYJf_v0v7tLLaLx0ouAUz60Hj9qASaXhGQf6C5ACmFRIlqnWrcacqvx5ssmhpF_gAxoXQOpjDG0YY-GH6oPgPSNbiXqDxBntWwF25PpcM6ZUQgyPnV1ejOwZMbMLZdLBfHfrjsgBf5FOl77j4J8FZk5-zhwjMhKCCdUovph2Y0f6F5vSpagsC9H6yXR49_Y3SC9UXC4h48RiBxmeI3PEzdDwz5z4nbvoUJf4ZQuQvemrSYGoeoWD6iwxNwA1LSVpXbUsWmlgnoVKkU161b48-skZlyd94rR4T6-KM2u8Om1o3CrSFMnxs3EDw4DUdOpVorMTEaTKcB4Z5djYxPfJso8uEQkuCQ-SE18fYNuHVLiX32Xni6cwGZkY7t4bdq",
"AWCwydgTqCCSegsifpA4NA-Vwhwi78HI3Xoeg7WnXCE8KLzQcAA5DxrVv9h-oZ2us7BlXZpM_gimHub4jSZCOjRkr4SPClRQfsbSXBKgbYG1_lEzszlW4OBScFE7P96sqbnvCp6hfR6Mddc05LOSzs5ImbHMBzkYnMvDcOZ6rGi5YG86Ichz7D2X0R0fwe1S4x5WX51vHkqlamcVQhIXsFZVlWv0-CGemNFP850rZpQTwLQjAqSXpv6L3_PddQkYBXdYh-iY4R5DpK8nFZVNFkszza4fUQh27_hwcXsz--DO0RD1BsEguNxq-DKkYeHuaPUN56IcUEhp65oljWL-deCrCEpgtj8i3QJ44O1RcOyzPWPRhcW4Y5k0naOcs_lHSOcVFKKOhrN6Tcda0AGeTAI5Qq_kGj26xa0coEIPDy8E2JDr6w",
"AWCwydhz8dFc2lCwRtOFPurdo7xUY6o4aoPhxPyrDx7U04V8nYFYFZKx-nyvxi_Ij58eoR4FNr_2hFx_8AD_ijWvzB2JXhR_IeVci7tTl_21alPzbVw43vhccWemW6JiF5nqAudyNsHySNRr7QgwnAIhOlBtMMzkmNGSTb4lhY4Y1AG_ZQxHs9qc6AhK2U_aXXOsZED-Qm-2kuvb_SSSEjcHv8wDEJbIoJsrV3q0R8YBNHresRT180DGR5UXXaumLyzNwUjx9QQeLuj3YJ6NjmQEe_qxqULlntlJpCKTyu-kfnTz3pqr53paCky06xHSqhZ5hDz970KGfFytdEN_cLLIUjXmMsfj77wWKyIypy46YbKLFediB3UqdP_FMLd6NExMEHl0GmlO5QZ8mblygNn2C7-Q-canQrScy41NwiGxUGmdTlyZ",
]
def rebuild(html, sec_regex, new): return re.sub(sec_regex, lambda m:new, html, flags=re.S)
tel="+393891953784"; wanum="3891953784"; site="turkish-pizza-kebab-buttapietra.html"; url=BASE+site
h=open("ristorante-atlantic-flagship.html",encoding="utf-8").read()
h=h.replace("Bistrot Contrada","Turkish Pizza Kebab")
h=h.replace("+390450000000",tel).replace("390450000000",wanum)
h=h.replace("045 000 0000","389 195 3784")
h=h.replace('<title>Turkish Pizza Kebab — Cucina moderna a Verona | Prenota</title>',
            '<title>Turkish Pizza Kebab Buttapietra — Kebab &amp; Pizza | Ordina</title>')
h=h.replace('content="Turkish Pizza Kebab, cucina moderna nel cuore di Verona. Menù stagionale, cocktail e vini selezionati. 4,8★ su 240 recensioni. Prenota il tuo tavolo.">',
            'content="Turkish Pizza Kebab a Buttapietra (VR): kebab con carne fantastica e impasto tirato a mano, pizze e menù vasto. 4,5★ su 120 recensioni. Chiama o scrivi su WhatsApp.">')
# hero
h=rebuild(h, r'<section id="top" class="hero">.*?</section>',
'''<section id="top" class="hero">
  <div class="wrap">
    <span class="kick">Kebab &amp; Pizza · Buttapietra</span>
    <h1 class="display">Kebab e pizza, fatti come si deve</h1>
    <p class="lead">Carne fantastica, impasto tirato a mano e un menù vasto. Da anni uno dei kebab più apprezzati della zona, sulla statale a Buttapietra. Asporto e da mangiare qui.</p>
    <div class="hero-cta">
      <a href="https://wa.me/3891953784" class="btn btn-dark">Ordina su WhatsApp</a>
      <a href="#menu" class="btn btn-out">Vedi il menù</a>
    </div>
  </div>
  <img class="hero-img" src="''' + ph(KEB[0],1600) + '''" alt="Kebab e pizza Turkish Pizza Kebab Buttapietra">
</section>''')
# story
h=rebuild(h, r'<section id="storia" class="story">.*?</section>',
'''<section id="storia" class="story">
  <div class="wrap story-grid">
    <div class="story-img" role="img" aria-label="Kebab appena preparato" style="background:url('''+ph(KEB[1],1200)+''') center/cover"></div>
    <div class="story-txt">
      <span class="kick">Chi siamo</span>
      <h2>Il gusto vero del kebab</h2>
      <p>Da Turkish Pizza Kebab la carne è una garanzia: kebab preparato al momento con impasto tirato a mano e ingredienti scelti. Un menù ampio tra panini, piadine, piatti e pizze.</p>
      <p>Un locale semplice e accogliente, sulla statale a Buttapietra in un punto comodo. Proprietario gentile e disponibile: passa a trovarci o ordina d'asporto.</p>
    </div>
  </div>
</section>''')
# info band
h=rebuild(h, r'<section class="info">.*?</section>',
'''<section class="info">
  <div class="wrap info-grid">
    <div class="info-col">
      <h4>Dove siamo</h4>
      <p>Via Isola della Scala 3<br>37060 Buttapietra (VR)</p>
      <p><a href="https://maps.google.com/?cid=15710783198979579878" target="_blank" rel="noopener">Indicazioni →</a></p>
    </div>
    <div class="info-col">
      <h4>Orari</h4>
      <p>Lun–Gio 10:30–23:55<br>Ven–Sab 10:30–01:00<br>Domenica 10:30–23:55</p>
    </div>
    <div class="info-col">
      <h4>Contatti</h4>
      <p><a href="tel:+393891953784">389 195 3784</a><br><a href="https://wa.me/3891953784">Scrivici su WhatsApp</a></p>
    </div>
  </div>
</section>''')
# menu
h=rebuild(h, r'<section id="menu" class="menu">.*?</section>',
'''<section id="menu" class="menu">
  <div class="wrap">
    <div class="menu-head">
      <span class="kick">Il menù</span>
      <h2>Kebab, pizza e non solo</h2>
      <p>Una selezione della nostra proposta. Menù ampio, prezzi onesti — chiedi anche i piatti del giorno.</p>
    </div>
    <div class="menu-cols">
      <div class="menu-cat">
        <h3>Kebab</h3>
        <div class="dish"><div class="d-main"><h5>Kebab nel panino</h5><span>Carne, insalata, salse a scelta</span></div><div class="price">5 €</div></div>
        <div class="dish"><div class="d-main"><h5>Kebab in piadina</h5><span>Farcito e arrotolato</span></div><div class="price">5,50 €</div></div>
        <div class="dish"><div class="d-main"><h5>Kebab nel piatto</h5><span>Con patatine e insalata</span></div><div class="price">7 €</div></div>
        <div class="dish"><div class="d-main"><h5>Menù kebab</h5><span>Kebab + patatine + bibita</span></div><div class="price">8,50 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Pizze</h3>
        <div class="dish"><div class="d-main"><h5>Margherita</h5><span>Pomodoro e mozzarella</span></div><div class="price">5 €</div></div>
        <div class="dish"><div class="d-main"><h5>Diavola</h5><span>Salame piccante</span></div><div class="price">6,50 €</div></div>
        <div class="dish"><div class="d-main"><h5>Pizza kebab</h5><span>Con carne di kebab e salse</span></div><div class="price">7,50 €</div></div>
        <div class="dish"><div class="d-main"><h5>Capricciosa</h5><span>Prosciutto, funghi, carciofi</span></div><div class="price">7 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Panini &amp; Fritti</h3>
        <div class="dish"><div class="d-main"><h5>Hamburger</h5><span>Con patatine</span></div><div class="price">5 €</div></div>
        <div class="dish"><div class="d-main"><h5>Patatine fritte</h5><span>Porzione abbondante</span></div><div class="price">3 €</div></div>
        <div class="dish"><div class="d-main"><h5>Alette di pollo</h5><span>Croccanti</span></div><div class="price">5 €</div></div>
        <div class="dish"><div class="d-main"><h5>Falafel</h5><span>Di ceci, con salsa</span></div><div class="price">4,50 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Bibite</h3>
        <div class="dish"><div class="d-main"><h5>Bibita in lattina</h5><span>Cola, aranciata, tè</span></div><div class="price">2 €</div></div>
        <div class="dish"><div class="d-main"><h5>Acqua</h5><span>Naturale o frizzante</span></div><div class="price">1 €</div></div>
        <div class="dish"><div class="d-main"><h5>Ayran</h5><span>Bevanda allo yogurt</span></div><div class="price">2 €</div></div>
        <div class="dish"><div class="d-main"><h5>Dolce turco</h5><span>Baklava</span></div><div class="price">2,50 €</div></div>
      </div>
    </div>
  </div>
</section>''')
# gallery
h=rebuild(h, r'<section id="galleria" class="gallery">.*?</section>',
'''<section id="galleria" class="gallery">
  <div class="wrap gal-grid">
    <img src="'''+ph(KEB[2],800)+'''" alt="Kebab">
    <img src="'''+ph(KEB[3],800)+'''" alt="Piatto">
    <img src="'''+ph(KEB[4],800)+'''" alt="Locale">
  </div>
</section>''')
# reviews
h=rebuild(h, r'<section class="reviews">.*?</section>',
'''<section class="reviews">
  <div class="wrap">
    <div class="stars">★★★★★</div>
    <h2>4,5 su 120 recensioni</h2>
    <div class="rv-grid">
      <div class="rv"><div class="st">★★★★★</div><p>"La pizza kebab qui è una garanzia! Carne fantastica, impasto tirato a mano eccezionale, uno dei migliori kebab della zona. Menù molto vasto e proprietario gentile."</p><b>Giuseppe De Rosa</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Miglior kebab di Verona, staff come fratelli. Andateci, sono onestissimi."</p><b>Oscar Castello</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Kebab più buono di Verona e staff simpaticissimo."</p><b>Geremia Castello</b></div>
    </div>
  </div>
</section>''')
# reserve
h=rebuild(h, r'<section id="prenota" class="reserve">.*?</section>',
'''<section id="prenota" class="reserve">
  <div class="wrap">
    <span class="kick">Ordina</span>
    <h2>Vieni a trovarci o ordina d'asporto</h2>
    <p>Siamo aperti tutti i giorni, fino a tardi nel weekend. Chiamaci o scrivici su WhatsApp: prepariamo tutto al momento.</p>
    <div class="btns">
      <a href="tel:+393891953784" class="btn btn-dark">Chiama 389 195 3784</a>
      <a href="https://wa.me/3891953784" class="btn btn-out">WhatsApp</a>
    </div>
  </div>
</section>''')
# footer
h=rebuild(h, r'<footer>.*?</footer>',
'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="brand">Turkish Pizza Kebab</div>
        <p>Kebab, pizza e sfizi d'asporto a Buttapietra (VR).</p>
      </div>
      <div>
        <h4>Contatti</h4>
        <p>Via Isola della Scala 3, Buttapietra<br><a href="tel:+393891953784">389 195 3784</a><br><a href="https://wa.me/3891953784">WhatsApp</a></p>
      </div>
      <div>
        <h4>Orari</h4>
        <p>Lun–Gio 10:30–23:55<br>Ven–Sab fino 01:00<br>Dom 10:30–23:55</p>
      </div>
    </div>
    <div class="foot-bot">
      <span>© Turkish Pizza Kebab — Buttapietra (VR)</span>
      <span>Sito realizzato da HubTec</span>
    </div>
  </div>
</footer>''')
# nav label Prenota->Ordina
h=h.replace('<a href="#prenota">Prenota</a>','<a href="#prenota">Ordina</a>')
h=h.replace('<a href="#prenota" class="btn btn-dark">Prenota</a>','<a href="#prenota" class="btn btn-dark">Ordina</a>')
h=sub_pexels(h,KEB,1400)
assert "pexels" not in h, "pexels leftover atlantic"
open(site,"w",encoding="utf-8").write(h)
add_crm(name="Turkish Pizza Kebab",file=site,phone="389 195 3784",intl="393891953784",comune="Buttapietra",cid="15710783198979579878",tmpl="ristorante-atlantic",url=url,wa=wa_link(wanum,url))
print("OK kebab", len(h))

# ============================================================
# LEAD 3: Bonus Food (template auburn) -> WhatsApp (388)
# ============================================================
BON=[
"AWCwydikV1y2LfhbBmwK51zTj80L2F2DNVqF1jcAPvTrapGbXfeC41DrnAq_M_LhEDgPuqhnpRjlxmvtEH4dWCzUmmziaVHViPgNtbOvFqlxpXott2uUBU68ncsOPhBd4J6W33yLfkBCke1-CJ9tug1i8HHr2z8wjHMdumgxjJ2ppAUx97n4TmSn7TZEGWigezn9x12hQ7-aLLuf-UH9r4PRFB74UpMhzG9_aE14DkhFz5FBTkfnUBMyHRQK0Ey72AGQfAerXUsSzVMxY-WCMSuFKqeffU-9B2wpa9ljSVTtVvfG49SO0cfi6AWJu1_n8VhTVdOp911-myupC35Y3XaGbgXp01tH1MZS7ouUzofswvofJr3KoNUrv7_Qu-FEeNRIeQSCKewC_NvMpGpWzOzAqlrVQy23eXIvdfVjYMXm-tHDVyb2ontdxx42nUY9vA",
"AWCwydgnkxTE2GwQjlKC6JZOn_mEJUqlv0eUizLPMsc-0XIquXTih1dXguMsqt_VgsAS1_mePlUK5zZr4wa5YJVBKV7rqMumWFRNRmouTrwYIle9Bz_cneu52TDoLAlNdHe9dy5g_BuV0Dte1Jjwc1JtqVCs0Hb3b2NBsrzBzNQO1HGHCmVlQfPjSBTqLyfz9kgUDee8MTRvfdx2yEOdENP8xOnclvMMfN4HofHZTv5mv2bbpeLKjyH_Czx4fOWC1dKzY4oFrn9x118_xH88HnCD7nHYawv5NZpxZOgHb_eauCDOopJugjvzzy7woBX1xK2hf0oDn6DXoTBviuNSAPq7C1Gh_XnBtTNkZqjkbog5Q1Dwb0Uc1a8wI30lLoaq09u6kytFo7rMi-vcOVC_cgQBT9PKX-Re3kV1LhHBqWQO2ASLi5S1-Kr8UoS4UUkcZdgo",
"AWCwydiyc_g7TpTGHwIhBNgU3PGGxkv-mPRsNnJE3MDZoM6MNNGd-TCoCe8khUvInGcRh4nVIqXITpx55_rueUY1hMJ_8Gff6NfJFN8BEBBY_LR0DwaGcF25yd5lO_ZKcLmEmoUGKctQOG3EZNtfTAJOMiKtRmZcQ7aJg2qtk11pYIgP-Q9Tx30wpL0HoTvlJW-v64Oo3hLgDZWwME5ZPHJnJHu2DC0MmAxa27-NcUSLDWruv6Qhmf2jitxZiy6s8S3bxI0lER8tT_27WhXad1Ur89lCWVJ0CUu1DxljIiSWLoQk_nlTlBXEKmirYSDGeOufHms_Cw2-OoMoXuKU7H28mthg4QLRgdi8LsZYXsnDVj_mXiu4qsTRzI2JNVQnaw5fh3Ap_5OA1npmtYYVQkRECgsew4FmvbbvbzH9c2q9R1rituLAGvFDfxueOa7yOQt8",
"AWCwydiFmOXVTJO83onNZHbX0I7R3O1KOy9uMsmM9ad621wDNWPG7r-yYetMomhFQuBu7HwgUM0TGzTfx6pVVA88sLtom78mVg5q9hQ5wJnGG7M_4p21vBPg6czA7fLJwxHZbfy4OdZ56IbhTXp8xSZrsS-v3gSBSFEB2Geg-CRFgla8rIyveNI4c7xEWUX1U2jhD6OZzhNNHQ62SIgjHbmUZs8oQ7JfOH2kCZzLTzq4RyNuEeR7zy553tp6soqzUNNnmuSKfVxk4MdxnqU_VjSdQogEcon8U0goQgpCtS0JfxqF5qVWQAEa8zphsGThqv7zz8J59Z10xZuRpWk-yHLtXJ7EstidcsqYR6au11yZdBmncVonizWCpk_0vGjUDssFnpjC71CCEeaWEeElFgUQbnKyBk41kVo2-ktDiJ8b8IaT83MlmBSjXEp_m-neQEub",
"AWCwydgJV3Ijb1v8poZpLHynAoCs89jbfKvgZBJuuTbI2tdOSUyfjbbIoQywk2nOnQMSDtFKXhzHhFl4QOrzBfWlT_MSzcWGCPWI9rdJnQQKDDakcKZBobAQNxdxVfGitqNEAK9KsvI5q2EMQ5fMlRBg-Fd_Ar0D-urItlKbeHENE24PbGe9AWoTrHJ27glCPhyAqvAtuqw9Jh3IIQBHBZ9hO4q9ArSsOOY4EC1wK08Ok49yKK-6dN59a3kvN4mdvs5X2OOl8e_okFfbdknWe56dQCENKOdEW5FwKIS3Cef5ioj6zKdnTaCWyK8_V6fnWOBHf_Dn745cYrB_sOQePdBLPnMys4GVeausufxHhiJKxut-Uc59pAHqN3bjsy9TpSSC74VEi0-q1Y6xfpy9eJO5asok0f3kGrKWETXy_uHejXz5jO7pXkq_G6oGW5LiZVU4",
"AWCwydhfN_2JcB1o2GlC90-uE1KeYUGSTCT9bFvIbHwKIdy68cGCltTtNH9BaAAw11pGXoJqXAPTGdPwYr8Mpsc4JS82oQikuA-Ku3QMf3_fcSKp1jbgW29xpk7tIq14RUDX8gy3ndKxiyiE_V8PoUbvTC0MHrOePsAlexuj3mWAFYJInF-A3-aemZ5d6LnjECoQELb41vK1yIrS8eP7WduD0aMClmGA9USApLuOmIRW5Ek6BVudP1LzomIBgd9DgTFRRHL-l351D5dzfmOp4GRdd26QIEcWVdbjd6Bu-2Sg4YXZ92x_c9FjrF8a009Osx-UInu67ZrVl3ZXfbo3kfDHDCwutlcN6VXwfP08hyz-1sADD0BRAmFn_YqlaEy6QdjUnzMzzHnyze7KHUVW3vd_qo4sxEaZUjOofRTcLJXZ7ZTZMaC67SdOD2b6rFaIHQu_",
]
tel="+393884537698"; wanum="3884537698"; site="bonus-food-buttapietra.html"; url=BASE+site
h=open("ristorante-auburn-flagship.html",encoding="utf-8").read()
h=h.replace("Osteria del Fuoco","Bonus Food")
h=h.replace("+390450000000",tel).replace("390450000000",wanum)
h=h.replace("045 000 0000","388 453 7698")
h=h.replace('<title>Bonus Food — Cucina di brace a Verona | Prenota</title>',
            '<title>Bonus Food Buttapietra — Pizza, kebab e consegna a domicilio | Ordina</title>')
h=h.replace('content="Bonus Food, cucina di brace e sapori decisi a Verona. Carni, primi della tradizione, cantina locale. 4,7★ su 180 recensioni. Prenota il tuo tavolo.">',
            'content="Bonus Food a Buttapietra (VR): pizza, kebab, panini e fritti con consegna a domicilio. Servizio veloce e gentile. Ordina al 388 453 7698 o su WhatsApp.">')
h=h.replace('<a href="mailto:info@bonus food.it">info@bonus food.it</a>','')  # safety noop
h=h.replace('<a href="mailto:info@osteriadelfuoco.it">info@osteriadelfuoco.it</a>','<a href="https://wa.me/3884537698">WhatsApp</a>')
# hero
h=rebuild(h, r'<section id="top" class="hero">.*?</section>',
'''<section id="top" class="hero">
  <div class="hero-bg"></div>
  <div class="hero-inner">
    <span class="kick">Pizza · Kebab · Domicilio · Buttapietra</span>
    <h1>Fame? Ci pensa Bonus Food</h1>
    <p>Pizza, kebab, panini e fritti preparati al momento. Ambiente pulito, servizio veloce e consegna a domicilio a Buttapietra e dintorni.</p>
    <div class="hero-cta">
      <a href="https://wa.me/3884537698" class="btn btn-fill">Ordina su WhatsApp</a>
      <a href="#menu" class="btn btn-line">Scopri il menù</a>
    </div>
  </div>
</section>''')
# exp
h=rebuild(h, r'<section id="exp" class="exp">.*?</section>',
'''<section id="exp" class="exp">
  <div class="wrap">
    <span class="kick">Chi siamo</span>
    <h2>Veloci, buoni e a domicilio</h2>
    <p>Da Bonus Food trovi pizza, kebab e tanti sfizi da asporto, con un occhio all'ordine e alla pulizia. Consegniamo a casa tua e ti teniamo aggiornato sullo stato dell'ordine.</p>
    <div class="exp-imgs">
      <img src="'''+ph(BON[0],800)+'''" alt="Piatto Bonus Food">
      <img src="'''+ph(BON[1],800)+'''" alt="Pizza">
      <img src="'''+ph(BON[2],800)+'''" alt="Locale">
    </div>
  </div>
</section>''')
# menu
h=rebuild(h, r'<section id="menu" class="menu">.*?</section>',
'''<section id="menu" class="menu">
  <div class="wrap">
    <div class="menu-head">
      <span class="kick">La cucina</span>
      <h2>Il nostro menù</h2>
    </div>
    <div class="menu-cols">
      <div class="menu-cat">
        <h3>Pizze</h3>
        <div class="dish"><div><h5>Margherita</h5><span>Pomodoro e mozzarella</span></div><div class="price">5 €</div></div>
        <div class="dish"><div><h5>Diavola</h5><span>Salame piccante</span></div><div class="price">6,50 €</div></div>
        <div class="dish"><div><h5>Quattro formaggi</h5><span>Mix di formaggi</span></div><div class="price">7 €</div></div>
        <div class="dish"><div><h5>Bufala</h5><span>Mozzarella di bufala e basilico</span></div><div class="price">7,50 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Kebab &amp; Panini</h3>
        <div class="dish"><div><h5>Kebab nel panino</h5><span>Carne, insalata, salse</span></div><div class="price">5,50 €</div></div>
        <div class="dish"><div><h5>Hamburger</h5><span>Con patatine</span></div><div class="price">5 €</div></div>
        <div class="dish"><div><h5>Panino di pollo</h5><span>Croccante, con salse</span></div><div class="price">6 €</div></div>
        <div class="dish"><div><h5>Piadina farcita</h5><span>A scelta</span></div><div class="price">5 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Fritti</h3>
        <div class="dish"><div><h5>Patatine fritte</h5><span>Porzione abbondante</span></div><div class="price">3 €</div></div>
        <div class="dish"><div><h5>Nuggets di pollo</h5><span>6 pezzi</span></div><div class="price">5 €</div></div>
        <div class="dish"><div><h5>Mozzarelline</h5><span>Fritte, croccanti</span></div><div class="price">4 €</div></div>
        <div class="dish"><div><h5>Onion rings</h5><span>Anelli di cipolla</span></div><div class="price">4 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Bibite &amp; Dolci</h3>
        <div class="dish"><div><h5>Bibita in lattina</h5><span>Cola, aranciata, tè</span></div><div class="price">2 €</div></div>
        <div class="dish"><div><h5>Acqua</h5><span>Naturale o frizzante</span></div><div class="price">1 €</div></div>
        <div class="dish"><div><h5>Birra</h5><span>In bottiglia</span></div><div class="price">3,50 €</div></div>
        <div class="dish"><div><h5>Tiramisù</h5><span>Fatto in casa</span></div><div class="price">3,50 €</div></div>
      </div>
    </div>
  </div>
</section>''')
# addr
h=rebuild(h, r'<section id="adresse" class="addr">.*?</section>',
'''<section id="adresse" class="addr">
  <div class="wrap addr-grid">
    <div class="addr-img" role="img" aria-label="Bonus Food Buttapietra"></div>
    <div class="addr-txt">
      <span class="kick">Dove siamo</span>
      <h2>Vieni a trovarci</h2>
      <div class="addr-row"><h4>Indirizzo</h4><p><a href="https://maps.google.com/?cid=7732589089538638128" target="_blank" rel="noopener">Piazza 4 Novembre 21, 37060 Buttapietra (VR)</a></p></div>
      <div class="addr-row"><h4>Orari</h4><p>Tutti i giorni 10:00–01:30</p></div>
      <div class="addr-row"><h4>Contatti</h4><p><a href="tel:+393884537698">388 453 7698</a> · <a href="https://wa.me/3884537698">WhatsApp</a></p></div>
      <a href="https://wa.me/3884537698" class="btn btn-dark" style="margin-top:8px">Ordina ora</a>
    </div>
  </div>
</section>''')
# reviews
h=rebuild(h, r'<section class="reviews">.*?</section>',
'''<section class="reviews">
  <div class="wrap">
    <div class="stars">★★★★☆</div>
    <h2>Dicono di noi</h2>
    <div class="rv-grid">
      <div class="rv"><div class="st">★★★★★</div><p>"Ho ordinato in orario di chiusura per 5 persone e sono stati gentili e disponibili: rispondono al telefono e ti aggiornano sull'ordine. Fattorino super gentile. Servizio stupendo!"</p><b>Lucia Pisciotta</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Ambiente molto pulito, servizio veloce e cibo buono! In più consegnano anche a domicilio. Assolutamente consigliato!"</p><b>Lavinia Scapini</b></div>
      <div class="rv"><div class="st">★★★★☆</div><p>"Cibo e servizio buoni."</p><b>Filippo Stornati</b></div>
    </div>
  </div>
</section>''')
# reserve
h=rebuild(h, r'<section id="prenota" class="reserve">.*?</section>',
'''<section id="prenota" class="reserve">
  <div class="reserve-bg"></div>
  <div class="wrap">
    <h2>Ordina adesso</h2>
    <p>Chiamaci o scrivici su WhatsApp: prepariamo tutto al momento e, se vuoi, consegniamo a casa tua.</p>
    <div class="btns">
      <a href="tel:+393884537698" class="btn btn-fill">Chiama 388 453 7698</a>
      <a href="https://wa.me/3884537698" class="btn btn-line">WhatsApp</a>
    </div>
  </div>
</section>''')
# footer
h=rebuild(h, r'<footer>.*?</footer>',
'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="brand">Bonus Food</div>
        <p>Pizza, kebab e sfizi con consegna a domicilio, a Buttapietra (VR).</p>
      </div>
      <div>
        <h4>Contatti</h4>
        <p>Piazza 4 Novembre 21, Buttapietra<br><a href="tel:+393884537698">388 453 7698</a><br><a href="https://wa.me/3884537698">WhatsApp</a></p>
      </div>
      <div>
        <h4>Orari</h4>
        <p>Tutti i giorni<br>10:00–01:30</p>
      </div>
    </div>
    <div class="foot-bot">
      <span>© Bonus Food — Buttapietra (VR)</span>
      <span>Sito realizzato da HubTec</span>
    </div>
  </div>
</footer>''')
h=sub_pexels(h,BON,1400)
assert "pexels" not in h, "pexels leftover auburn"
open(site,"w",encoding="utf-8").write(h)
add_crm(name="Bonus Food",file=site,phone="388 453 7698",intl="393884537698",comune="Buttapietra",cid="7732589089538638128",tmpl="ristorante-auburn",url=url,wa=wa_link(wanum,url))
print("OK bonusfood", len(h))

# ============================================================
# REPO UPDATES
# ============================================================
# 1) index.html insert block
idx=open("index.html",encoding="utf-8").read()
block=('<h2>Nuovi siti — Buttapietra (2026-07-24 · ristoranti)</h2>\n<ul>\n'
 '<li><a href="./trattoria-da-pasinato-buttapietra.html">Trattoria da Pasinato — Buttapietra</a></li>\n'
 '<li><a href="./turkish-pizza-kebab-buttapietra.html">Turkish Pizza Kebab — Buttapietra</a></li>\n'
 '<li><a href="./bonus-food-buttapietra.html">Bonus Food — Buttapietra</a></li>\n'
 '</ul>\n\n')
anchor='<body><h1>Anteprime siti — HubTec</h1><p>Siti dimostrativi generati per attività locali senza sito. Pagina interna.</p>\n'
assert anchor in idx, "index anchor miss"
idx=idx.replace(anchor, anchor+block, 1)
open("index.html","w",encoding="utf-8").write(idx)
print("index updated")

# 2) whatsapp-queue.csv append (kebab + bonus food; pasinato NO)
wq=open("whatsapp-queue.csv",encoding="utf-8").read()
def wq_row(name,phone,link,siteurl,comune):
    return "%s;%s;%s;%s;%s;%s\n"%(name,phone,link,siteurl,comune,DATA)
added=[]
kb_url=BASE+"turkish-pizza-kebab-buttapietra.html"
bf_url=BASE+"bonus-food-buttapietra.html"
if "389 195 3784" not in wq:
    wq+=wq_row("Turkish Pizza Kebab","389 195 3784",wa_link("3891953784",kb_url),kb_url,"Buttapietra"); added.append("kebab")
if "388 453 7698" not in wq:
    wq+=wq_row("Bonus Food","388 453 7698",wa_link("3884537698",bf_url),bf_url,"Buttapietra"); added.append("bonusfood")
open("whatsapp-queue.csv","w",encoding="utf-8").write(wq)
print("whatsapp-queue added:",added)

# 3) progress.json advance (Buttapietra ristoranti exhausted -> next comune Caldiero, cat 0)
pj=json.load(open("progress.json"))
pj["comuneIndex"]=8
pj["categoryIndex"]=0
json.dump(pj,open("progress.json","w"),ensure_ascii=False,indent=2)
print("progress ->",pj["comuneIndex"],pj["categoryIndex"])

# 4) _crm.json append
allcrm=json.load(open("_crm.json"))
allcrm+=crm
json.dump(allcrm,open("_crm.json","w"),ensure_ascii=False,indent=1)
print("crm total",len(allcrm))

# 5) run summary
json.dump({"run":DATA,"comune":"Buttapietra","categoria":"ristoranti","leads":crm},open("_run_buttapietra_rist.json","w"),ensure_ascii=False,indent=1)
print("DONE")
