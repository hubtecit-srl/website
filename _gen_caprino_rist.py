import json,re,html
K="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def L(pid): return json.load(open(f"_leaddata/{pid}.json"))["result"]
def photo_url(ref,w): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={K}"
def refs(r): return [p["photo_reference"] for p in r.get("photos",[])]
def clean(t):
    t=" ".join(t.split())
    if len(t)>230:
        t=t[:230].rsplit(" ",1)[0]+"…"
    return t
def reviews(r,n=3):
    out=[]
    for rv in r.get("reviews",[])[:n]:
        out.append((clean(rv.get("text","")),rv.get("author_name","Cliente"),rv.get("relative_time_description",""),rv.get("profile_photo_url",""),int(rv.get("rating",5))))
    return out

# ---------- LEAD 1: Al Frantoio -> il-vicoletto ----------
r=L("ChIJW7WOrGnxgUcRkzrULYgDcXU"); rf=refs(r)
s=open("il-vicoletto-trattoria-verona.html").read()
# photos: replace each photo_reference sequentially
it=iter(rf*3)
s=re.sub(r'photo_reference=[^&]+', lambda m:'photo_reference='+next(it), s)
# scalars
s=s.replace("Il Vicoletto Trattoria — Cucina tradizionale veronese | Verona","Trattoria Al Frantoio — Cucina tradizionale · Caprino Veronese")
s=s.replace('Il Vicoletto Trattoria, cucina tradizionale veronese nel centro di Verona. Bigoli all\'anatra, pastissada de caval, fegato alla veneta. 4,8★ su 1.842 recensioni. Prenota un tavolo.',
            'Trattoria Al Frantoio a Caprino Veronese: cucina tradizionale in un contesto naturale e rilassante. 4,8★ su 235 recensioni Google. Prenota un tavolo.')
s=s.replace(">Il Vicoletto<",">Al Frantoio<")
s=s.replace("Il Vicoletto Trattoria","Trattoria Al Frantoio")
s=s.replace("+390458769827","+390459232145")
s=s.replace("045 876 9827","045 923 2145")
s=s.replace("8374942607263514723","8462549058225191571")
s=s.replace("Via Santa Maria in Chiavica 5, 37121 Verona","Via Canal 115, 37013 Caprino Veronese (VR)")
s=s.replace("Via Santa Maria in Chiavica 5","Via Canal 115")
s=s.replace("Via+Santa+Maria+in+Chiavica+5,+37121+Verona","Via+Canal+115,+37013+Caprino+Veronese+VR")
s=s.replace("Trattoria · Verona centro","Trattoria · Caprino Veronese")
s=s.replace("1.842","235")
s=s.replace("https://www.facebook.com/profile.php?id=100078507787681","https://www.facebook.com/p/Trattoria-Al-Frantoio-100041611247648/")
# hours list
hl='''<li data-day="1"><span class="d">Lunedì</span><span>12:00–14:00 · 19:00–21:00</span></li>
          <li data-day="2"><span class="d">Martedì</span><span>12:00–14:00 · 19:00–21:00</span></li>
          <li data-day="3"><span class="d">Mercoledì</span><span>Chiuso</span></li>
          <li data-day="4"><span class="d">Giovedì</span><span>12:00–14:00 · 19:00–21:00</span></li>
          <li data-day="5"><span class="d">Venerdì</span><span>12:00–14:00 · 19:00–21:00</span></li>
          <li data-day="6"><span class="d">Sabato</span><span>12:00–14:00 · 19:00–21:00</span></li>
          <li data-day="0"><span class="d">Domenica</span><span>12:00–14:00 · 19:00–21:00</span></li>'''
s=re.sub(r'<li data-day="1">.*?<li data-day="0">.*?</li>', hl, s, flags=re.S)
s=s.replace('const periods={0:[[1200,1500],[1900,2230]],1:[[1200,1430],[1900,2230]],2:[[1200,1430],[1900,2230]],3:[[1200,1430],[1900,2230]],4:[[1200,1430],[1900,2230]],5:[[1200,1430],[1900,2300]],6:[[1200,1500],[1900,2300]]};',
            'const periods={0:[[1200,1400],[1900,2100]],1:[[1200,1400],[1900,2100]],2:[[1200,1400],[1900,2100]],3:[],4:[[1200,1400],[1900,2100]],5:[[1200,1400],[1900,2100]],6:[[1200,1400],[1900,2100]]};')
# reviews
rv=reviews(r)
blocks=[]
for t,n,tm,av,st in rv:
    av=av or "https://lh3.googleusercontent.com/a/default-user=s128"
    blocks.append(f'''<div class="rev">
        <div class="stars">{"★"*st}{"☆"*(5-st)}</div>
        <p>“{html.escape(t)}”</p>
        <div class="who"><img src="{av}" alt="{html.escape(n)}"><div><b>{html.escape(n)}</b><span>{html.escape(tm)}</span></div></div>
      </div>''')
newgrid='<div class="rev-grid">\n      '+"\n      ".join(blocks)+"\n    </div>"
s=re.sub(r'<div class="rev-grid">.*?</div>\s*</div>\s*<div class="rev-foot">',
         newgrid+'\n    <div class="rev-foot">', s, flags=re.S)
open("al-frantoio-caprino.html","w").write(s)
print("al-frantoio-caprino.html", len(s), "photos:",len(rf),"revs:",len(rv))

# ---------- helper for flagship templates ----------
def flagship(tpl,out,r,repl,pex_ok=True):
    s=open(tpl).read()
    rf=refs(r)
    # replace pexels images with real Places photos
    it=iter((rf*4))
    s=re.sub(r'https://images\.pexels\.com/[^\s"\')]+', lambda m:photo_url(next(it),1600), s)
    for a,b in repl: s=s.replace(a,b)
    # reviews (flagship style)
    rv=reviews(r)
    blocks=[]
    for t,n,tm,av,st in rv:
        blocks.append(f'<div class="rv"><div class="st">{"★"*st}{"☆"*(5-st)}</div><p>"{html.escape(t)}"</p><b>{html.escape(n)}</b></div>')
    s=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>',
             '<div class="rv-grid">\n      '+"\n      ".join(blocks)+'\n    </div>\n  </div>\n</section>', s, count=1, flags=re.S)
    open(out,"w").write(s)
    print(out,len(s),"photos:",len(rf),"revs:",len(rv))

# ---------- LEAD 2: Cima 11 -> atlantic (no email, no wa) ----------
r=L("ChIJ98hH3CDxgUcRmz7E3eXjxyg")
repl=[
 ("Bistrot Contrada — Cucina moderna a Verona | Prenota","Ristorante Cima 11 — Cucina di montagna · Caprino Veronese | Prenota"),
 ('Bistrot Contrada, cucina moderna nel cuore di Verona. Menù stagionale, cocktail e vini selezionati. 4,8★ su 240 recensioni. Prenota il tuo tavolo.',
  'Ristorante Cima 11 a Caprino Veronese (Porcino): cucina del territorio, funghi e specialità di montagna in una location suggestiva. 4,6★ su 1.425 recensioni. Prenota.'),
 ("Bistrot Contrada","Ristorante Cima 11"),
 ("Cucina moderna · Verona","Cucina di montagna · Caprino Veronese"),
 ("Sapori di stagione, nel cuore di Verona","La cucina del territorio, tra i boschi del Baldo"),
 ("Via Esempio 12<br>37121 Verona (VR)","Località Porcino<br>37013 Caprino Veronese (VR)"),
 ("Via Esempio 12, Verona","Località Porcino, Caprino Veronese"),
 ("Mar–Ven 19:00–23:00<br>Sab–Dom 12:30–14:30 · 19:00–23:30<br>Lunedì chiuso","Lun chiuso<br>Mar 19:30–21:30<br>Mer–Dom 12:30–13:45 · 19:30–21:30"),
 ("Mar–Ven 19–23<br>Sab–Dom 12:30–14:30 · 19–23:30<br>Lun chiuso","Mer–Dom 12:30–13:45<br>19:30–21:30<br>Lun chiuso"),
 ("+390450000000","+390457265061"),
 ("045 000 0000","045 726 5061"),
 ("4,8 su 240 recensioni","4,6 su 1.425 recensioni"),
 # remove email
 ('<br><a href="mailto:info@bistrotcontrada.it">info@bistrotcontrada.it</a>',''),
 ('<a href="mailto:info@bistrotcontrada.it">info@bistrotcontrada.it</a>',''),
 # remove whatsapp (landline)
 ('<a href="https://wa.me/390450000000" class="btn btn-out">WhatsApp</a>',''),
 ('<a href="https://wa.me/390450000000" class="wa">WhatsApp</a>',''),
 ("Siamo aperti dal martedì alla domenica. Per gruppi o eventi speciali, chiamaci: troveremo la soluzione migliore per voi.",
  "Aperto da mercoledì a domenica (martedì solo cena). Per gruppi ed eventi chiamaci: troveremo la soluzione migliore per voi."),
]
flagship("ristorante-atlantic-flagship.html","ristorante-cima-11-caprino.html",r,repl)

# ---------- LEAD 3: Ostaria de Cavrin -> auburn (no email, no wa) ----------
r=L("ChIJo--PayHxgUcReaPlAEcbPk0")
repl=[
 ("Osteria del Fuoco — Cucina di brace a Verona | Prenota","Ostaria de Cavrin — Cucina veneta · Caprino Veronese | Prenota"),
 ('Osteria del Fuoco, cucina di brace e sapori decisi a Verona. Carni, primi della tradizione, cantina locale. 4,7★ su 180 recensioni. Prenota il tuo tavolo.',
  'Ostaria de Cavrin nel centro di Caprino Veronese: tradizione veneta e cura dei dettagli, cortile accogliente e ottima cantina. 4,8★ su 70 recensioni. Prenota.'),
 ("Osteria del Fuoco","Ostaria de Cavrin"),
 ("Cucina di brace · Verona","Cucina veneta · Caprino Veronese"),
 ("Il gusto del fuoco","Tradizione veneta, nel cuore di Caprino"),
 ("Carni alla brace, primi della tradizione e una cantina che racconta il territorio. Nel cuore di Verona.",
  "Faraona, selezione di formaggi, petto d'anatra e sbrisolona: la cucina veneta curata nei dettagli, in un cortile accogliente nel centro di Caprino."),
 ("Via Esempio 12, 37121 Verona (VR)","Via G. Mazzini 29, 37013 Caprino Veronese (VR)"),
 ("Via Esempio 12, Verona","Via G. Mazzini 29, Caprino Veronese"),
 ("Mar–Dom 12:00–14:30 · 19:00–23:00<br>Lunedì chiuso","Lun–Ven 19:00–22:00<br>Sab 19:00–22:30 · Dom 19:00–22:00"),
 ("Mar–Dom 12–14:30<br>19–23<br>Lun chiuso","Tutti i giorni<br>19:00–22:00<br>(Sab fino 22:30)"),
 ("+390450000000","+390456230016"),
 ("045 000 0000","045 623 0016"),
 ("4,7 su 180 recensioni","4,8 su 70 recensioni"),
 ('<br><a href="mailto:info@osteriadelfuoco.it">info@osteriadelfuoco.it</a>',''),
 (' · <a href="mailto:info@osteriadelfuoco.it">info@osteriadelfuoco.it</a>',''),
 ('<a href="https://wa.me/390450000000" class="btn btn-line">WhatsApp</a>',''),
 ('<a href="https://wa.me/390450000000" class="wa">WhatsApp</a>',''),
]
flagship("ristorante-auburn-flagship.html","ostaria-de-cavrin-caprino.html",r,repl)

# ---------- LEAD 4: Al Vicolo -> juniper (email + mobile => keep WA) ----------
r=L("ChIJeck3ue_xgUcRHiALMTTtqoo")
repl=[
 ("Ristorante Ginepro — Fine dining a Verona | Prenota","Ristorante Al Vicolo — Cucina tipica · Caprino Veronese | Prenota"),
 ('Ristorante Ginepro, cucina raffinata e stagionale a Verona. Percorsi degustazione, cantina d\'autore, sala elegante. 4,9★ su 210 recensioni. Prenota.',
  'Ristorante Al Vicolo a Caprino Veronese: piatti tipici e cucina gustosa in un ambiente rustico e familiare, tra sasso e camino. 4,7★ su 185 recensioni. Prenota.'),
 (">Ginepro<",">Al Vicolo<"),
 ("Ristorante Ginepro","Ristorante Al Vicolo"),
 ("Fine dining · Verona","Cucina tipica · Caprino Veronese"),
 ("L'arte della tavola","Come a casa, tra sasso e camino"),
 ("Cucina raffinata e stagionale, in una sala elegante nel cuore di Verona. Un'esperienza da vivere con calma.",
  "Ambiente rustico con soffitto a volta, pareti in sasso e camino. Piatti tipici, cucina gustosa e una gestione familiare che ti fa sentire a casa."),
 ("Via Esempio 12, Verona","Via Vicolo Cieco 3/A, Caprino Veronese"),
 ("Mar–Dom 19:00–23:00 · Lunedì chiuso","Lun–Sab 11:00–14:00 · 19:00–21:00 · Domenica chiuso"),
 ("Mar–Dom 19:00–23:00<br>Lunedì chiuso","Lun–Sab 11:00–14:00<br>19:00–21:00<br>Domenica chiuso"),
 ("+390450000000","+393288595197"),
 ("045 000 0000","328 859 5197"),
 ("390450000000","393288595197"),
 ("info@ristoranteginepro.it","alvicolo.caprino@gmail.com"),
 ("4,9 su 210 recensioni","4,7 su 185 recensioni"),
]
flagship("ristorante-juniper-flagship.html","al-vicolo-caprino.html",r,repl)
print("DONE")
