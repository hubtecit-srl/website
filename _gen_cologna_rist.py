# -*- coding: utf-8 -*-
import re, urllib.parse
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
WARN=[]
def R(h,old,new,req=True):
    if old not in h:
        if req: WARN.append(old[:70])
        return h
    return h.replace(old,new)
def cyc(urls):
    i={'n':0}
    def f(_m):
        u=urls[i['n']%len(urls)]; i['n']+=1; return u
    return f

BAR=["https://lh3.googleusercontent.com/place-photos/AG9NLjDpMHk0qG1-E6G25YNj9Re_jknChLhHypoSVvHuMTXrMimA_lLA2za5-Lo3fbhIkPEfyipP2Ackw0u8iINc0l9bXaEelFtBcX5Czb5e3RCnYPJINB4TyuW0t3ILxWeOLxsrESS_Rrdrof65=s1600-w800",
"https://lh3.googleusercontent.com/place-photos/AG9NLjBRzWNKh6RvBc5SPovfyOW0K9MFRTtvjYKTA5akL1fVJYrULFC8_nJDcbDJG47uD0yUvbX1BC7GkTj1l-sKZ24Vibrs5N-A6yyGBZAq6jVyK0K1Hll7L7B1B8AD2ZoPy4-KA-ZIgY0K8CdVAg=s1600-w960",
"https://lh3.googleusercontent.com/place-photos/AG9NLjA3YgP9o9czN_vmIkqepXq1XIdrhteU0Lq4qVkQ6oEGv_H3dKhO99h-fbaf8x0W0euqFeTvTVarffdLWM6ZfHAH29MoXxQLI9FL_tSi24EDTREI6gVQqZre4LCFaiIC81J0b3-z-hQLTZ1IIGY=s1600-w1200",
"https://lh3.googleusercontent.com/place-photos/AG9NLjCLeLoUCKKygP5A8QRoKANdUDgQXtmuFB7gBlEwXUi_0f5XTrM4N3YBzAnDbzM3MkoVz4J0UGlYTMiuIqFvs_deTvV8wpD5zpQe0p--41ZQjWG5SuRDrGjEwy_3VxioYc2Gn0-iPpjSa95neb5SE5VXpQ=s1600-w1200"]
LAN=["https://lh3.googleusercontent.com/place-photos/AG9NLjB9p8boRHCQlnaC6oHeqpkUETHj8payb9VAwmVizFJmqLwA1eKyp6BznFwQJU7H5do6f0pJLpyN5ez1uygJqwAgs5pC0rfz-L9eVmpImPZ1_QkdiYOEWUEBgKPPj7m7823gM0stmSYMiWHrXg=s1600-w847",
"https://lh3.googleusercontent.com/place-photos/AG9NLjBxIb9tbCDOt8KdL6T6plfyH8aBcExy1wyTbYAz2PKyX0Iw-vaQ0ZwqMFLMn1JgK_Tk-tbTVBkLp541CYxOiV4chrYS4u8gKtMy0fyaTJzy4v1MzvqqoxPF9W-_80PCk9WJhj40URY16ZIGSA=s1600-w848",
"https://lh3.googleusercontent.com/place-photos/AG9NLjDPGWD6vhjJaQBKQCY9h9Uxk6Bid-q6NJ7v5ylq0tOsYUd_FXoEzFA_d9pn25-HKWLvoLMT0sVTwfauvsmgOEwlR6YeABitduaMJQ0AAAuKCyKno5he0GFz3YjoxJlmafxL2Qhzj30n2aXzzpkabbilLA=s1600-w1200",
"https://lh3.googleusercontent.com/place-photos/AG9NLjBYo1O233qUijhKSPpf4iPpgfHBrNBRSwD-Eafmdn43J7UfhP5RUq37LGG4br_R6T9R4TNntXK0Uf0g5kJXujzpu0aunAvL9VcnajrzhoWMWpVQTI2EMQl36v2z0nZ0eGFLTC3MoUlKQiY=s1600-w1200"]
GAR=["https://lh3.googleusercontent.com/place-photos/AG9NLjC-O7KcL7r4BVnyvYt7FwMEjlh2TTT0xmo6eC06vfZp53QUHrtWY2w9g32fm0fS5zH9pvrczLzPFRXw2lhCFerOKvQcV0Nk8k-joNIFbtF8ZjGRtXNvVgMdMkkuGcqbCoqKKFuxmoJc8XNK6w=s1600-w1024",
"https://lh3.googleusercontent.com/place-photos/AG9NLjDwzInTveIO9k_j8g7de3u1aTcrFS7QxHJTxHbIqp5k1kHNuaSBOFLZtQyfzJuTNzHvqJ71SFqTS1ts_I2COjWuc7YKVF8qlp4umF1wSAKgXWe59xDNofU4wx8CVGHS0qRehdIKuLF5L9slU9jfD7dKTw=s1600-w1200",
"https://lh3.googleusercontent.com/place-photos/AG9NLjAw5gs2j1gWylnrXRSndgtLE6JTbmMSFmhkj2lI6aapBFLbjbup0ZLxDvwdQlCJUbQXUwBblNAXVVncTb5yZC1WFb4mpAnly9nf9jtTv3s4zrBB0OMHzExcxatZq0328zNwLe8_2-aW4s4bCV8=s1600-w1200",
"https://lh3.googleusercontent.com/place-photos/AG9NLjB8WWyzMmfDowEZE7F1VrLTau43BEBtGXZAuPkN24-qjBjtppUyN8g8JbHVHTUQthBLXHQjVUI_Kwhdsm3kkwgVqMzG2n522Behy_DNWPnOEFwiHcpooO-GKscD91XlKPPRM3aa_ltFTvQuU8A=s1600-w1200"]

RX_MAPS=re.compile(r"https://maps\.googleapis\.com/maps/api/place/photo\?[^'\"]+")
RX_PEX=re.compile(r"https://images\.pexels\.com/photos/[^'\"]+")

# ================= LEAD 1: Osteria dal Barbesin -> il-vicoletto (idx0) MANUAL =================
h=open("il-vicoletto-trattoria-verona.html",encoding="utf-8").read()
h=RX_MAPS.sub(cyc(BAR),h)
FB="https://www.facebook.com/OsteriadalBarbesin"
h=R(h,'<title>Il Vicoletto Trattoria — Cucina tradizionale veronese | Verona</title>','<title>Osteria dal Barbesin — Cucina tradizionale a Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Il Vicoletto Trattoria, cucina tradizionale veronese nel centro di Verona. Bigoli all\'anatra, pastissada de caval, fegato alla veneta. 4,8★ su 1.842 recensioni. Prenota un tavolo.">','content="Osteria dal Barbesin, cucina tradizionale veronese a Cologna Veneta (VR), Via Cavour 54. Bigoli al ragù d\'anatra, gnocchi, carni e vini del territorio. 4,4★ su 325 recensioni Google. Prenota un tavolo.">')
h=R(h,'<a href="#" class="brand">Il Vicoletto<span>.</span></a>','<a href="#" class="brand">Osteria dal Barbesin</a>')
h=R(h,'<div class="kicker">Trattoria · Verona centro</div>','<div class="kicker">Osteria · Cologna Veneta</div>')
h=R(h,'<h1>La cucina veronese,<br><em>come una volta</em></h1>','<h1>La cucina veronese,<br><em>come una volta</em></h1>')
h=R(h,'<p class="sub">Nel cuore del centro storico, tra vicoli e pietra viva. Piatti della tradizione, materie prime scelte, accoglienza sincera.</p>','<p class="sub">Nel cuore di Cologna Veneta, in Via Cavour. Piatti della tradizione veronese, materie prime scelte e accoglienza sincera dal 1900.</p>')
h=R(h,'<div><span class="stars">★★★★★</span> <b>4,8</b></div>','<div><span class="stars">★★★★★</span> <b>4,4</b></div>')
h=R(h,'<div>1.842 recensioni Google</div>','<div>325 recensioni Google</div>')
h=R(h,'<div>Via Santa Maria in Chiavica 5</div>','<div>Via Cavour 54, Cologna Veneta</div>')
h=R(h,'<p>Il Vicoletto è un tempio della cucina tradizionale veronese, quella vera. Un locale intimo ed elegante, curato nei dettagli, dove ogni piatto racconta il territorio.</p>','<p>L\'Osteria dal Barbesin è un punto di riferimento della cucina tradizionale veronese a Cologna Veneta. Un locale accogliente e curato, dove ogni piatto racconta il territorio.</p>')
h=R(h,'<h2>4,8 su 1.842 recensioni</h2>','<h2>4,4 su 325 recensioni</h2>')
# reviews text + names (3)
h=R(h,'“Il prosciutto era divino e i bigoli al sugo d\'anatra meravigliosi. I camerieri gentilissimi, il posto intimo ed elegante. Un meraviglioso posto per mangiare bene e rilassarsi.”','“Siamo passati per caso: ambiente bello, ci hanno fatto accomodare in veranda ed è stato piacevole pranzare. Cibo molto buono e di ottima qualità!”')
h=R(h,'<b>Genny</b><span>un mese fa</span>','<b>Valentina De Maio</b><span>su Google</span>')
h=R(h,'“Ottima esperienza. Abbiamo assaggiato i bigoli all\'anatra e gli gnocchi alla pastissada de caval: entrambi ottimi, la pastissada in particolare era superlativa. Personale eccezionale.”','“Ottimi i bigoli al ragù d\'anatra, delicati gli gnocchi. Ottimo l\'antipasto misto e il semifreddo mandorlato. Ottima carta dei vini. Consigliato.”')
h=R(h,'<b>Laura Sigona</b><span>un mese fa</span>','<b>Davide Fustini</b><span>su Google</span>')
h=R(h,'“Locale ben curato, frequentato da molti turisti che il personale gestisce con velocità e gentilezza. Buoni i piatti, attenti alla tradizione locale. Consigliato.”','“Da Barbara, Ivano e la loro famiglia ci si sente a casa: cucina tradizionale ben fatta e accoglienza calorosa.”')
h=R(h,'<b>Enzo Valentini</b><span>2 mesi fa</span>','<b>Mario Rossi</b><span>su Google</span>')
h=R(h,'<a href="https://maps.google.com/?cid=8374942607263514723" target="_blank" rel="noopener">Leggi tutte le 1.842 recensioni su Google →</a>','<a href="https://maps.google.com/?cid=14391494700058488378" target="_blank" rel="noopener">Leggi tutte le 325 recensioni su Google →</a>')
# hours block
h=R(h,'''<ul class="hours-list" id="hoursList">
          <li data-day="1"><span class="d">Lunedì</span><span>12:00–14:30 · 19:00–22:30</span></li>
          <li data-day="2"><span class="d">Martedì</span><span>12:00–14:30 · 19:00–22:30</span></li>
          <li data-day="3"><span class="d">Mercoledì</span><span>12:00–14:30 · 19:00–22:30</span></li>
          <li data-day="4"><span class="d">Giovedì</span><span>12:00–14:30 · 19:00–22:30</span></li>
          <li data-day="5"><span class="d">Venerdì</span><span>12:00–14:30 · 19:00–23:00</span></li>
          <li data-day="6"><span class="d">Sabato</span><span>12:00–15:00 · 19:00–23:00</span></li>
          <li data-day="0"><span class="d">Domenica</span><span>12:00–15:00 · 19:00–22:30</span></li>
        </ul>''','''<ul class="hours-list" id="hoursList">
          <li data-day="1"><span class="d">Lunedì</span><span>11:00–15:00 · 19:00–24:00</span></li>
          <li data-day="2"><span class="d">Martedì</span><span>11:00–15:00 · 19:00–24:00</span></li>
          <li data-day="3"><span class="d">Mercoledì</span><span>11:00–15:00 · 19:00–24:00</span></li>
          <li data-day="4"><span class="d">Giovedì</span><span>11:00–15:00 · 19:00–24:00</span></li>
          <li data-day="5"><span class="d">Venerdì</span><span>11:00–15:00 · 19:00–24:00</span></li>
          <li data-day="6"><span class="d">Sabato</span><span>11:00–15:00 · 19:00–24:00</span></li>
          <li data-day="0"><span class="d">Domenica</span><span>11:00–15:00 · 19:00–24:00</span></li>
        </ul>''')
h=R(h,'<a href="https://maps.google.com/?cid=8374942607263514723" target="_blank" rel="noopener">Via Santa Maria in Chiavica 5, 37121 Verona</a>','<a href="https://maps.google.com/?cid=14391494700058488378" target="_blank" rel="noopener">Via Cavour 54, 37044 Cologna Veneta (VR)</a>')
h=R(h,'<h4>Telefono / Prenotazioni</h4><a href="tel:+390458769827">045 876 9827</a>','<h4>Telefono / Prenotazioni</h4><a href="tel:+390442411040">0442 411040</a>')
h=R(h,'src="https://www.google.com/maps?q=Via+Santa+Maria+in+Chiavica+5,+37121+Verona&output=embed"','src="https://www.google.com/maps?q=Via+Cavour+54,+37044+Cologna+Veneta+VR&output=embed"')
h=R(h,'<div class="brand">Il Vicoletto<span style="color:var(--gold)">.</span></div>','<div class="brand">Osteria dal Barbesin</div>')
h=R(h,'<div class="foot-line">© 2026 Il Vicoletto Trattoria · Via Santa Maria in Chiavica 5, Verona · P.IVA da inserire</div>','<div class="foot-line">© 2026 Osteria dal Barbesin · Via Cavour 54, Cologna Veneta (VR)</div>')
h=h.replace('https://www.facebook.com/profile.php?id=100078507787681',FB)
h=h.replace('https://maps.google.com/?cid=8374942607263514723','https://maps.google.com/?cid=14391494700058488378')
h=h.replace('tel:+390458769827','tel:+390442411040')
open("osteria-dal-barbesin-cologna-veneta.html","w",encoding="utf-8").write(h)
print("BARBESIN | maps_left",len(RX_MAPS.findall(h)),"| verona_left",h.count("Verona")-h.count("Cologna Veneta"),"| vicoletto_left",h.count("Vicoletto"),"| placeholder_tel",h.count("390458769827"))

print("WARN:",WARN)
