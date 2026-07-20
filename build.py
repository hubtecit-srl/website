# -*- coding: utf-8 -*-
import json, urllib.request, urllib.parse, re, html
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def api(pid):
    f="name,formatted_address,formatted_phone_number,international_phone_number,opening_hours,rating,user_ratings_total,reviews,photos,url"
    u="https://maps.googleapis.com/maps/api/place/details/json?place_id=%s&fields=%s&language=it&key=%s"%(pid,f,KEY)
    return json.load(urllib.request.urlopen(u,timeout=30))["result"]
def ph(ref,w=1200): return "https://maps.googleapis.com/maps/api/place/photo?maxwidth=%d&photo_reference=%s&key=%s"%(w,ref,KEY)
def clean_rev(t,maxlen=190):
    t=re.sub(r'\s+',' ',t).strip()
    if len(t)>maxlen:
        cut=t[:maxlen]
        # cut at last sentence end or space
        m=max(cut.rfind('. '),cut.rfind('! '),cut.rfind('? '))
        if m>60: cut=cut[:m+1]
        else: cut=cut[:cut.rfind(' ')]+'…'
        t=cut
    return html.escape(t,quote=False)
stock=json.load(open('stock-library.json'))

leads=[]

# ============ 1) OSTERIA DOGANA (ristorante-atlantic) ============
d=api("ChIJOf_vBPhqf0cRMKp3JvI-Pfg")
photos=[p["photo_reference"] for p in d.get("photos",[])]
revs=[r for r in d.get("reviews",[]) if r.get("text")][:3]
cid=(d.get("url","").split("cid=")[1] if "cid=" in d.get("url","") else "17887522504733862448")
t=open("ristorante-atlantic-flagship.html",encoding="utf-8").read()
P0=ph(photos[0],1600); P1=ph(photos[1],1200); Pg=[ph(x,800) for x in photos[2:5]]
# head
t=t.replace("<title>Bistrot Contrada — Cucina moderna a Verona | Prenota</title>",
            "<title>Osteria Dogana dal 1969 — Trattoria &amp; Pizzeria ad Albaredo d'Adige | Prenota</title>")
t=t.replace('content="Bistrot Contrada, cucina moderna nel cuore di Verona. Menù stagionale, cocktail e vini selezionati. 4,8★ su 240 recensioni. Prenota il tuo tavolo.">',
            'content="Osteria Dogana dal 1969: trattoria e pizzeria nella piazza di Albaredo d\'Adige (VR). Cucina tipica veronese, pizza e accoglienza di famiglia. 4,6★ su 590 recensioni. Prenota il tuo tavolo.">')
# brand / hero
t=t.replace('<a href="#top" class="brand">Bistrot Contrada</a>','<a href="#top" class="brand">Osteria Dogana</a>')
t=t.replace('<span class="kick">Cucina moderna · Verona</span>','<span class="kick">Trattoria &amp; Pizzeria · Albaredo d\'Adige</span>')
t=t.replace('<h1 class="display">Sapori di stagione, nel cuore di Verona</h1>','<h1 class="display">Cucina veronese e pizza dal 1969</h1>')
t=t.replace("<p class=\"lead\">Un bistrot dove la tradizione veneta incontra la cucina contemporanea. Ingredienti locali, cantina selezionata, atmosfera informale.</p>",
            "<p class=\"lead\">Dal 1969 una trattoria di famiglia nella piazza di Albaredo d'Adige: cucina tipica della bassa veronese, pizza cotta come si deve e accoglienza sincera.</p>")
# story
t=t.replace('<h2>Cucina d\'autore, ospitalità sincera</h2>','<h2>Una storia di famiglia dal 1969</h2>')
t=t.replace("<p>Bistrot Contrada nasce dalla passione per la materia prima del territorio. Ogni piatto racconta il Veneto con una lettura moderna, curata dallo chef e dalla sua brigata.</p>",
            "<p>L'Osteria Dogana accoglie da oltre cinquant'anni chi cerca i sapori veri della bassa veronese: piatti della tradizione, pizze fragranti e prodotti scelti con cura.</p>")
t=t.replace("<p>Una sala accogliente, un servizio attento e una carta dei vini pensata per accompagnare ogni portata: il posto giusto per una cena tra amici o un'occasione speciale.</p>",
            "<p>Una sala curata, personale cortese e prezzi onesti: il posto giusto per un pranzo di lavoro, una cena tra amici o un'occasione speciale in famiglia.</p>")
# info band
t=t.replace('<p>Via Esempio 12<br>37121 Verona (VR)</p>','<p>Piazza Vittorio Emanuele, 6<br>37041 Albaredo d\'Adige (VR)</p>')
t=t.replace('<p><a href="#prenota">Indicazioni →</a></p>','<p><a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener">Indicazioni →</a></p>'%cid)
t=t.replace('<p>Mar–Ven 19:00–23:00<br>Sab–Dom 12:30–14:30 · 19:00–23:30<br>Lunedì chiuso</p>',
            '<p>Lun 11:00–15:00<br>Mer–Ven 11:00–15:00 · 18:00–23:00<br>Sab–Dom 18:00–23:00 · Mar chiuso</p>')
t=t.replace('<p><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@bistrotcontrada.it">info@bistrotcontrada.it</a></p>',
            '<p><a href="tel:+393382179295">338 217 9295</a></p>')
# menu head
t=t.replace('<p>Una selezione della nostra proposta. La carta cambia con le stagioni e la disponibilità del mercato.</p>',
            '<p>Una selezione indicativa della nostra proposta tra cucina veronese e pizzeria. Chiedi la carta completa in sala.</p>')
# menu categories -> adapt (Antipasti/Primi/Secondi/Pizze&Dolci)
t=t.replace('<h3>Vini &amp; Dolci</h3>','<h3>Pizze &amp; Dolci</h3>')
t=t.replace('<div class="dish"><div class="d-main"><h5>Calice Valpolicella</h5><span>Selezione della casa</span></div><div class="price">6 €</div></div>',
            '<div class="dish"><div class="d-main"><h5>Pizza Margherita</h5><span>Pomodoro, mozzarella, basilico</span></div><div class="price">7 €</div></div>')
t=t.replace('<div class="dish"><div class="d-main"><h5>Calice Soave</h5><span>Selezione della casa</span></div><div class="price">6 €</div></div>',
            '<div class="dish"><div class="d-main"><h5>Pala alla Romana</h5><span>La nostra specialità, farcita a scelta</span></div><div class="price">9 €</div></div>')
# gallery
gal=['<img src="%s" alt="Osteria Dogana - foto %d">'%(Pg[i],i+1) for i in range(len(Pg))]
t=re.sub(r'<div class="wrap gal-grid">.*?</div>\s*</section>',
         '<div class="wrap gal-grid">\n    %s\n  </div>\n</section>'%("\n    ".join(gal)),t,flags=re.S)
# reviews
t=t.replace('<h2>4,8 su 240 recensioni</h2>','<h2>4,6★ su 590 recensioni Google</h2>')
rvcards="\n      ".join('<div class="rv"><div class="st">%s</div><p>"%s"</p><b>%s</b></div>'%('★'*int(r.get("rating",5)),clean_rev(r["text"]),html.escape(r["author_name"])) for r in revs)
t=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>',
         '<div class="rv-grid">\n      %s\n    </div>\n  </div>\n</section>'%rvcards,t,flags=re.S,count=1)
# reserve
t=t.replace('<p>Siamo aperti dal martedì alla domenica. Per gruppi o eventi speciali, chiamaci: troveremo la soluzione migliore per voi.</p>',
            '<p>Siamo aperti tutta la settimana (martedì chiuso). Per gruppi, cerimonie o eventi speciali chiamaci: troveremo la soluzione migliore per voi.</p>')
t=t.replace('<a href="tel:+390450000000" class="btn btn-dark">Chiama 045 000 0000</a>','<a href="tel:+393382179295" class="btn btn-dark">Chiama 338 217 9295</a>')
# footer
t=t.replace('<div class="brand">Bistrot Contrada</div>','<div class="brand">Osteria Dogana</div>')
t=t.replace('<p>Cucina moderna e ospitalità nel cuore di Verona.</p>','<p>Trattoria e pizzeria di famiglia dal 1969, ad Albaredo d\'Adige (VR).</p>')
t=t.replace('<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@bistrotcontrada.it">info@bistrotcontrada.it</a></p>',
            '<p>Piazza Vittorio Emanuele 6, Albaredo d\'Adige<br><a href="tel:+393382179295">338 217 9295</a></p>')
t=t.replace('<p>Mar–Ven 19–23<br>Sab–Dom 12:30–14:30 · 19–23:30<br>Lun chiuso</p>',
            '<p>Lun 11–15<br>Mer–Ven 11–15 · 18–23<br>Sab–Dom 18–23 · Mar chiuso</p>')
t=t.replace('<span>© Bistrot Contrada — Verona</span>','<span>© Osteria Dogana dal 1969 — Albaredo d\'Adige</span>')
# images (hero+story backgrounds and hero img)
t=t.replace("https://images.pexels.com/photos/958545/pexels-photo-958545.jpeg?auto=compress&cs=tinysrgb&w=1600",P0)
t=t.replace("https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=1200",P1)
# global tel/wa cleanup
t=t.replace('tel:+390450000000','tel:+393382179295').replace('https://wa.me/390450000000','https://wa.me/393382179295')
t=t.replace('045 000 0000','338 217 9295')
open("osteria-dogana-albaredo.html","w",encoding="utf-8").write(t)
leads.append(("Osteria Dogana dal 1969","osteria-dogana-albaredo.html","338 217 9295","393382179295","Albaredo d'Adige",cid,"ristorante-atlantic",photos[:5],"No"))
print("OK osteria", len(t), "photos_used",min(5,len(photos)))

# ============ 2) ESTETICA RACHELE (estetiste-spamagic) ============
d=api("ChIJ7e6pcMNrf0cRVPqroIRmO0E")
photos=[p["photo_reference"] for p in d.get("photos",[])]
revs=[r for r in d.get("reviews",[]) if r.get("text")][:3]
cid=(d.get("url","").split("cid=")[1] if "cid=" in d.get("url","") else "4700463355908586068")
t=open("estetiste-spamagic-flagship.html",encoding="utf-8").read()
hero=ph(photos[0],1600) if photos else stock["estetiste"][0]
split=stock["estetiste"][1]; ctaimg=stock["estetiste"][2]
t=t.replace("<title>Centro Estetico Iris — Beauty &amp; Spa a Verona | Prenota</title>",
            "<title>Estetica Rachele — Centro estetico ad Albaredo d'Adige | Prenota</title>")
t=t.replace('content="Centro Estetico Iris a Verona: trattamenti viso, corpo, epilazione, unghie e make-up. 4,9★ su 175 recensioni. Prenota il tuo appuntamento di bellezza.">',
            'content="Estetica Rachele ad Albaredo d\'Adige (VR): trattamenti viso e corpo, unghie, epilazione e make-up. 5★ su 14 recensioni. Prenota il tuo appuntamento di bellezza.">')
t=t.replace('<a href="#top" class="brand">Centro Estetico <b>Iris</b></a>','<a href="#top" class="brand">Estetica <b>Rachele</b></a>')
t=t.replace('<h2>Il tuo angolo di bellezza a Verona</h2>','<h2>Il tuo angolo di bellezza ad Albaredo d\'Adige</h2>')
t=t.replace('<p>Al Centro Estetico Iris uniamo competenza, prodotti di qualità e tanta cura per farti sentire bella e a tuo agio, ad ogni visita.</p>',
            '<p>Da Estetica Rachele uniamo competenza, prodotti di qualità e tanta cura per farti sentire bella e a tuo agio, ad ogni visita. Un centro pulito e curato dove staccare la spina.</p>')
# reviews
rvcards="\n      ".join('<div class="rv"><div class="st">%s</div><p>"%s"</p><b>%s</b></div>'%('★'*int(r.get("rating",5)),clean_rev(r["text"]),html.escape(r["author_name"])) for r in revs)
t=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>',
         '<div class="rv-grid">\n      %s\n    </div>\n  </div>\n</section>'%rvcards,t,flags=re.S,count=1)
t=t.replace('<div class="sec-h"><span class="script">Recensioni</span><h2>Cosa dicono le clienti</h2></div>',
            '<div class="sec-h"><span class="script">Recensioni</span><h2>5★ su Google · le nostre clienti</h2></div>')
# cta buttons
t=t.replace('<a href="tel:+390450000000" class="btn btn-light">📞 045 000 0000</a>','<a href="tel:+393473598935" class="btn btn-light">📞 347 359 8935</a>')
# footer
t=t.replace('<div><div class="brand" style="color:#fff">Centro Estetico Iris</div><p>Il tuo angolo di bellezza e benessere a Verona.</p></div>',
            '<div><div class="brand" style="color:#fff">Estetica Rachele</div><p>Il tuo angolo di bellezza e benessere ad Albaredo d\'Adige (VR).</p></div>')
t=t.replace('<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@centroiris.it">info@centroiris.it</a></p></div>',
            '<div><h4>Contatti</h4><p><a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener">Via Roma 24, Albaredo d\'Adige</a><br><a href="tel:+393473598935">347 359 8935</a></p></div>'%cid)
t=t.replace('<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>',
            '<div><h4>Orari</h4><p>Lun 13:00–20:00<br>Mar–Ven 9:00–19:00<br>Sab e Dom chiuso</p></div>')
t=t.replace('<span>© Centro Estetico Iris — Verona</span>','<span>© Estetica Rachele — Albaredo d\'Adige</span>')
# images (CSS backgrounds)
t=t.replace("https://images.pexels.com/photos/3997385/pexels-photo-3997385.jpeg?auto=compress&cs=tinysrgb&w=1600",hero)
t=t.replace("https://images.pexels.com/photos/3762879/pexels-photo-3762879.jpeg?auto=compress&cs=tinysrgb&w=1000",split)
t=t.replace("https://images.pexels.com/photos/3985329/pexels-photo-3985329.jpeg?auto=compress&cs=tinysrgb&w=1600",ctaimg)
t=t.replace('tel:+390450000000','tel:+393473598935').replace('https://wa.me/390450000000','https://wa.me/393473598935')
t=t.replace('045 000 0000','347 359 8935')
open("estetica-rachele-albaredo.html","w",encoding="utf-8").write(t)
leads.append(("Estetica Rachele di Menin Rachele","estetica-rachele-albaredo.html","347 359 8935","393473598935","Albaredo d'Adige",cid,"estetiste-spamagic",photos[:1],"No"))
print("OK rachele", len(t), "realphotos",len(photos))

# ============ 3) SALONE ANDREA (parrucchieri-salonkit) ============
d=api("ChIJRxEXMfdqf0cR8FFkOEJFc8A")
photos=[p["photo_reference"] for p in d.get("photos",[])]
revs=[r for r in d.get("reviews",[]) if r.get("text")][:3]
cid=(d.get("url","").split("cid=")[1] if "cid=" in d.get("url","") else "13867503828320145904")
t=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
hero=ph(photos[0],1000) if photos else stock["parrucchieri"][0]
gal=[ph(x,800) for x in photos[1:5]]
while len(gal)<4: gal.append(stock["parrucchieri"][len(gal)%len(stock["parrucchieri"])])
t=t.replace("<title>Salone Méta — Parrucchiere a Verona | Prenota</title>",
            "<title>Salone Andrea — Parrucchiere ad Albaredo d'Adige | Prenota</title>")
t=t.replace('content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">',
            'content="Salone Andrea di Soffiati Andrea, parrucchiere ad Albaredo d\'Adige (VR): taglio, colore, trattamenti e acconciature per lui e per lei. 4,8★ su 34 recensioni. Prenota.">')
t=t.replace('<a href="#top" class="brand">Salone Méta</a>','<a href="#top" class="brand">Salone Andrea</a>')
t=t.replace('<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Albaredo d\'Adige</span>')
t=t.replace('<h1>Dove l\'hairstyling è <em>olistico</em></h1>','<h1>Il tuo stile, <em>curato nei dettagli</em></h1>')
t=t.replace("<p>Taglio, colore e trattamenti pensati per te e per la salute dei tuoi capelli. Un salone dove bellezza e benessere si incontrano.</p>",
            "<p>Taglio, colore e trattamenti per lui e per lei, curati da Andrea con attenzione e prodotti professionali. Un salone dove ti senti a casa, nel cuore di Albaredo d'Adige.</p>")
# reviews
rvcards="\n      ".join('<div class="rv"><div class="st">%s</div><p>"%s"</p><b>%s</b></div>'%('★'*int(r.get("rating",5)),clean_rev(r["text"]),html.escape(r["author_name"])) for r in revs)
t=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>',
         '<div class="rv-grid">\n      %s\n    </div>\n  </div>\n</section>'%rvcards,t,flags=re.S,count=1)
t=t.replace('<div class="sec-h"><span class="kick">Recensioni</span><h2>Le nostre clienti</h2></div>',
            '<div class="sec-h"><span class="kick">Recensioni</span><h2>4,8★ su 34 recensioni Google</h2></div>')
# cta
t=t.replace('<a href="tel:+390450000000" class="btn btn-light">📞 045 000 0000</a>','<a href="tel:+393913005001" class="btn btn-light">📞 391 300 5001</a>')
# footer
t=t.replace('<div><div class="brand" style="color:#fff">Salone Méta</div><p>Parrucchiere olistico nel cuore di Verona.</p></div>',
            '<div><div class="brand" style="color:#fff">Salone Andrea</div><p>Parrucchiere per lui e per lei ad Albaredo d\'Adige (VR).</p></div>')
t=t.replace('<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>',
            '<div><h4>Contatti</h4><p><a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener">Via Chiesa 6, Albaredo d\'Adige</a><br><a href="tel:+393913005001">391 300 5001</a></p></div>'%cid)
t=t.replace('<span>© Salone Méta — Verona</span>','<span>© Salone Andrea — Albaredo d\'Adige</span>')
# images: hero (CSS bg line47 + img line158) and gallery(4)
t=t.replace("https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000",hero)
galsrc=["https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/3065209/pexels-photo-3065209.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800"]
for i,src in enumerate(galsrc): t=t.replace(src,gal[i])
t=t.replace('tel:+390450000000','tel:+393913005001').replace('https://wa.me/390450000000','https://wa.me/393913005001')
t=t.replace('045 000 0000','391 300 5001')
open("salone-andrea-albaredo.html","w",encoding="utf-8").write(t)
leads.append(("Salone Andrea Di Soffiati Andrea","salone-andrea-albaredo.html","391 300 5001","393913005001","Albaredo d'Adige",cid,"parrucchieri-salonkit",photos[:5],"No"))
print("OK salone", len(t), "realphotos",len(photos))

json.dump(leads,open("/tmp/hubsite/_leads.json","w"))
print("DONE", len(leads),"siti")
