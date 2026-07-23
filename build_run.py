# -*- coding: utf-8 -*-
import json, urllib.request, urllib.parse, re, html
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
DATA="2026-07-23"
BASE="https://hubtecit-srl.github.io/website/"

def api(pid):
    f="name,formatted_address,formatted_phone_number,international_phone_number,opening_hours,rating,user_ratings_total,reviews,photos,url"
    u="https://maps.googleapis.com/maps/api/place/details/json?place_id=%s&fields=%s&language=it&key=%s"%(pid,f,KEY)
    return json.load(urllib.request.urlopen(u,timeout=30))["result"]
def ph(ref,w=1200): return "https://maps.googleapis.com/maps/api/place/photo?maxwidth=%d&photo_reference=%s&key=%s"%(w,ref,KEY)
def esc(t): return html.escape(t,quote=False)
def clean_rev(t,maxlen=190):
    t=re.sub(r'\s+',' ',t).strip()
    if len(t)>maxlen:
        cut=t[:maxlen]; m=max(cut.rfind('. '),cut.rfind('! '),cut.rfind('? '))
        cut=cut[:m+1] if m>60 else cut[:cut.rfind(' ')]+'…'
        t=cut
    return esc(t)
DAYABBR={'lunedì':'Lun','martedì':'Mar','mercoledì':'Mer','giovedì':'Gio','venerdì':'Ven','sabato':'Sab','domenica':'Dom'}
def hours_html(d):
    wt=d.get("opening_hours",{}).get("weekday_text")
    if not wt: return "Su appuntamento"
    out=[]
    for line in wt:
        day,_,t=line.partition(': ')
        out.append('%s %s'%(DAYABBR.get(day.strip(),day),t))
    return '<br>'.join(out)
def rep(t,old,new,label):
    if old not in t: print("  !! MISS [%s]"%label)
    return t.replace(old,new,1)
def photos_of(d,n):
    p=[x["photo_reference"] for x in d.get("photos",[])]
    return p if p else None
def cyc(lst,i): return lst[i%len(lst)]
def cid_of(d,fallback):
    u=d.get("url","")
    return u.split("cid=")[1] if "cid=" in u else fallback

WA_TEXT=("""Buongiorno,
Sono Laura di HubTec, azienda di Verona.

Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {URL}

Se vi piace, lo attiviamo con soli 200€.

In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.

Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.

Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!

Laura Borin - HubTec""")
def wa_link(num,url):
    return "https://wa.me/39%s?text=%s"%(num,urllib.parse.quote(WA_TEXT.format(URL=url),safe=''))

results=[]

def build_lorella():
    d=api("ChIJz8F50m5vf0cRhzKPLKH9tGA")
    P=photos_of(d,6); cid=cid_of(d,"")
    tel="+393494225644"; num="3494225644"; telsp="349 422 5644"
    addr="Via Madonna 92, 37051 Bovolone (VR)"
    revs=[r for r in d.get("reviews",[]) if r.get("text")]
    slug="salone-lorella-leielui-bovolone.html"; url=BASE+slug
    t=open("parrucchieri-revival-flagship.html",encoding="utf-8").read()
    t=rep(t,"<title>Revival Hair Studio — Parrucchiere a Verona | Prenota</title>","<title>Salone Lorella LeieLui — Parrucchiere a Bovolone (VR) | Prenota</title>","title")
    t=rep(t,'content="Revival Hair Studio, parrucchiere a Verona: taglio, colore e styling d\'autore. Un salone dal design minimal ed elegante. 4,9★ su 180 recensioni. Prenota.">','content="Salone Lorella LeieLui, parrucchiere per lei e per lui a Bovolone (VR): taglio, colore, piega e trattamenti. 5,0★ su Google. Prenota il tuo appuntamento.">',"desc")
    t=t.replace("© Revival Hair Studio — Verona","© Salone Lorella LeieLui — Bovolone (VR)")
    t=t.replace(">REVIVAL<",">SALONE LORELLA<")
    t=t.replace("Revival Hair Studio","Salone Lorella LeieLui")
    t=rep(t,'<span class="kick">Hair Studio · Verona</span>','<span class="kick">Parrucchiere lei &amp; lui · Bovolone</span>',"kick")
    t=rep(t,"<h1>Revival</h1>","<h1>Salone Lorella</h1>","h1")
    t=rep(t,"<p>Taglio, colore e styling d'autore. Un salone dove l'eleganza incontra la cura del dettaglio.</p>","<p>Taglio, colore e piega per lei e per lui. Un salone accogliente a Bovolone, dove ti prendiamo per mano ad ogni visita.</p>","herop")
    t=rep(t,"<h2>Uno studio dedicato allo stile, in ogni dettaglio</h2>","<h2>Un salone dedicato a te e ai tuoi capelli</h2>","introh2")
    t=rep(t,"<p>Un ambiente essenziale ed elegante, pensato per farti vivere un'esperienza di bellezza fuori dal comune. Professionisti attenti, tecniche moderne e ascolto.</p>","<p>Ambiente curato e accogliente, consigli su misura e cura del dettaglio. Un salone amato dai clienti di Bovolone per gentilezza e professionalità.</p>","splitp")
    hh=hours_html(d)
    li="".join('<li><span>%s</span><span>%s</span></li>'%(DAYABBR.get(l.partition(': ')[0].strip(),l.partition(': ')[0]),l.partition(': ')[2]) for l in d.get("opening_hours",{}).get("weekday_text",[])) or '<li><span>Su appuntamento</span><span>—</span></li>'
    t=re.sub(r'<ul class="split-hours">.*?</ul>','<ul class="split-hours">%s</ul>'%li,t,count=1,flags=re.S)
    t=rep(t,"<p>Mar–Ven 9:00–19:00<br>Sab 9:00–18:00</p>","<p>%s</p>"%hh,"foothours")
    if revs:
        t=re.sub(r'<q>Un salone diverso da tutti\. Eleganza, competenza e un taglio impeccabile\.</q>','<q>%s</q>'%clean_rev(revs[0]["text"],150),t,count=1)
        t=rep(t,"<b>Beatrice C.</b>","<b>%s</b>"%esc(revs[0]["author_name"]),"revauth")
    rr=revs[1:4] if len(revs)>1 else revs
    cards="".join('<div class="c rv"><div class="st">%s</div><q>"%s"</q><b>%s</b></div>'%('★'*int(r.get("rating",5)),clean_rev(r["text"]),esc(r["author_name"])) for r in rr)
    if cards: t=re.sub(r'<div class="rv-row">.*?</div>\s*</section>','<div class="rv-row">%s</div>\n  </div>\n</section>'%cards,t,count=1,flags=re.S)
    t=rep(t,'<a href="tel:+390450000000" class="btn btn-light">045 000 0000</a>','<a href="tel:%s" class="btn btn-light">Chiama %s</a>'%(tel,telsp),"ctatel")
    t=rep(t,'<a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>','<a href="%s" class="btn btn-ghost">WhatsApp</a>'%wa_link(num,url),"ctawa")
    t=rep(t,'<p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@revivalhair.it">info@revivalhair.it</a></p>','<p><a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener">%s</a><br><a href="tel:%s">%s</a></p>'%(cid,addr,tel,telsp),"footcont")
    t=rep(t,"<p>Hair studio d'autore nel cuore di Verona.</p>","<p>Parrucchiere per lei e per lui a Bovolone (VR).</p>","footp")
    t=rep(t,"https://images.pexels.com/photos/3993462/pexels-photo-3993462.jpeg?auto=compress&cs=tinysrgb&w=1600",ph(cyc(P,0),1600),"herobg")
    t=rep(t,"https://images.pexels.com/photos/3992874/pexels-photo-3992874.jpeg?auto=compress&cs=tinysrgb&w=1000",ph(cyc(P,1),1000),"splitbg")
    for i,src in enumerate(["3065209","3738349","3993449","3992855"]):
        t=rep(t,"https://images.pexels.com/photos/%s/pexels-photo-%s.jpeg?auto=compress&cs=tinysrgb&w=800"%(src,src),ph(cyc(P,2+i),800),"folio%d"%i)
    t=t.replace("tel:+390450000000",tel).replace("https://wa.me/390450000000",wa_link(num,url)).replace("045 000 0000",telsp)
    open(slug,"w",encoding="utf-8").write(t)
    results.append(dict(name="Salone Lorella LeieLui",file=slug,tel=telsp,num=num,addr="Via Madonna",cid=cid,tmpl="parrucchieri-revival",channel="whatsapp",rating="5,0 · 7",wa=wa_link(num,url)))
    print("OK lorella",len(t),"photos",len(P) if P else 0)

def build_chinato():
    d=api("ChIJpSgmewBvf0cRIyL0-nAOlF4")
    P=photos_of(d,6); cid=cid_of(d,"")
    tel="+393486703666"; num="3486703666"; telsp="348 670 3666"
    addr="Via San Pierino 107, 37051 Bovolone (VR)"
    revs=[r for r in d.get("reviews",[]) if r.get("text")]
    slug="chinato-federica-bovolone.html"; url=BASE+slug; wl=wa_link(num,url)
    t=open("silvia-de-guidi-capelli-verona.html",encoding="utf-8").read()
    cnt=[0]
    def sub_photo(m):
        w=int(m.group(1))
        if not P: return m.group(0)
        r=cyc(P,cnt[0]); cnt[0]+=1; return ph(r,w)
    t=re.sub(r"https://maps\.googleapis\.com/maps/api/place/photo\?maxwidth=(\d+)&photo_reference=[^&]+&key=[^'\"]+",sub_photo,t)
    t=rep(t,"<title>Silvia De Guidi Capelli — Parrucchiere a Verona (Golosine)</title>","<title>Chinato Federica — Parrucchiere a Bovolone (VR) | Prenota</title>","title")
    t=rep(t,'content="Silvia De Guidi Capelli, parrucchiere a Verona in Via Golosine 117. Taglio, colore, acconciature sposa e trattamenti. 4,9★ su 71 recensioni. Prenota.">','content="Chinato Federica, parrucchiere a Bovolone (VR): taglio, colore, acconciature e trattamenti su misura. 5,0★ su 16 recensioni Google. Prenota il tuo appuntamento.">',"desc")
    t=rep(t,'<span class="mk"></span>SILVIA DE GUIDI','<span class="mk"></span>CHINATO FEDERICA',"brand")
    t=rep(t,'<div class="tag"><b>#01</b> Parrucchiere · Verona Golosine</div>','<div class="tag"><b>★</b> Parrucchiere · Bovolone (VR)</div>',"tag")
    t=rep(t,'<h1 class="display">Silvia<br>De Guidi</h1>','<h1 class="display">Chinato<br>Federica</h1>',"h1")
    t=rep(t,'<p class="sub">Taglio, colore e acconciature su misura — studiati sul tuo viso, sul tuo capello e sullo stile che desideri davvero.</p>','<p class="sub">Taglio, colore e acconciature su misura — studiati sul tuo viso, sul tuo capello e sullo stile che desideri davvero. A Bovolone.</p>',"sub")
    t=rep(t,"<small>4,9 / 5 · 71 recensioni Google</small>","<small>5,0 / 5 · 16 recensioni Google</small>","badge")
    t=rep(t,"<p>4,9 stelle su 71 recensioni Google verificate.</p>","<p>5,0 stelle su 16 recensioni Google verificate.</p>","revp")
    if revs:
        def card(r):
            img=r.get("profile_photo_url","")
            when=esc(r.get("relative_time_description","recensione Google"))
            return '<div class="rv"><div class="st">%s</div><p>“%s”</p><div class="who"><img src="%s" alt="%s"><div><b>%s</b><span>%s</span></div></div></div>'%('★'*int(r.get("rating",5)),clean_rev(r["text"],230),img,esc(r["author_name"]),esc(r["author_name"]),when)
        newcards="\n      ".join(card(r) for r in revs[:3])
        t=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>','<div class="rv-grid">\n      %s\n    </div>\n  </div>\n</section>'%newcards,t,count=1,flags=re.S)
    t=rep(t,'<p style="margin-bottom:8px"><a href="tel:+393335037075">333 503 7075</a></p>','<p style="margin-bottom:8px"><a href="tel:%s">%s</a></p>'%(tel,telsp),"fcont_tel")
    t=rep(t,'<p style="margin-bottom:8px"><a href="mailto:deguidisilvia@gmail.com">deguidisilvia@gmail.com</a></p>','<p style="margin-bottom:8px"><a href="%s" target="_blank" rel="noopener">Scrivici su WhatsApp</a></p>'%wl,"fcont_mail")
    t=rep(t,'<p><a href="https://maps.google.com/?cid=3290711706439048689" target="_blank" rel="noopener">Via Golosine 117, 37136 Verona →</a></p>','<p><a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener">%s →</a></p>'%(cid,addr),"fcont_addr")
    t=rep(t,"<p>Parrucchiere unisex a Verona, zona Golosine. Taglio, colore, acconciature sposa e trattamenti con prodotti di qualità.</p>","<p>Parrucchiere a Bovolone (VR). Taglio, colore, acconciature e trattamenti con prodotti di qualità, su appuntamento.</p>","fsalone")
    t=rep(t,"<span>© 2026 Silvia De Guidi Capelli · Verona</span>","<span>© 2026 Chinato Federica · Bovolone (VR)</span>","copy")
    wt=d.get("opening_hours",{}).get("weekday_text"); per=d.get("opening_hours",{}).get("periods")
    dayname={1:'Lunedì',2:'Martedì',3:'Mercoledì',4:'Giovedì',5:'Venerdì',6:'Sabato',0:'Domenica'}
    order=[1,2,3,4,5,6,0]
    if wt:
        inv={'lunedì':1,'martedì':2,'mercoledì':3,'giovedì':4,'venerdì':5,'sabato':6,'domenica':0}
        mp={}
        for l in wt:
            mp[inv.get(l.partition(': ')[0].strip())]=l.partition(': ')[2]
        lis="\n          ".join('<li data-day="%d"><span class="d">%s</span><span>%s</span></li>'%(dd,dayname[dd],mp.get(dd,'Chiuso')) for dd in order)
        t=re.sub(r'<ul class="hours-list" id="hoursList">.*?</ul>','<ul class="hours-list" id="hoursList">\n          %s\n        </ul>'%lis,t,count=1,flags=re.S)
    else:
        t=re.sub(r'<ul class="hours-list" id="hoursList">.*?</ul>','<ul class="hours-list" id="hoursList">\n          <li><span class="d">Su appuntamento</span><span>Chiama per orari</span></li>\n        </ul>',t,count=1,flags=re.S)
    if per:
        pj={}
        for p in per:
            dd=p.get("open",{}).get("day"); o=p.get("open",{}).get("time"); c=p.get("close",{}).get("time")
            if dd is not None and o and c: pj[dd]=[int(o),int(c)]
        js="{"+",".join("%d:[%d,%d]"%(k,v[0],v[1]) for k,v in sorted(pj.items()))+"}"
    else:
        js="{}"
    t=re.sub(r'const periods=\{[^;]*\};','const periods=%s;'%js,t,count=1)
    t=t.replace("tel:+393335037075",tel)
    t=t.replace('<a href="%s" class="bk">Prenota</a>'%tel,'<a href="%s" class="bk">WhatsApp</a>'%wl)
    open(slug,"w",encoding="utf-8").write(t)
    results.append(dict(name="Chinato Federica",file=slug,tel=telsp,num=num,addr="Via San Pierino",cid=cid,tmpl="silvia-de-guidi",channel="whatsapp",rating="5,0 · 16",wa=wl))
    print("OK chinato",len(t),"photos",len(P) if P else 0,"js",js)

def build_moda():
    d=api("ChIJ5Qh8cRRvf0cRtn0MAQA3K4w")
    P=photos_of(d,5); cid=cid_of(d,"")
    tel="+393484082293"; num="3484082293"; telsp="348 408 2293"
    addr="Via Fosse Ardeatine 1, 37051 Bovolone (VR)"
    revs=[r for r in d.get("reviews",[]) if r.get("text")][:3]
    slug="moda-capelli-giacon-bovolone.html"; url=BASE+slug; wl=wa_link(num,url)
    t=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
    t=rep(t,"<title>Salone Méta — Parrucchiere a Verona | Prenota</title>","<title>Moda Capelli di Giacon Stefano — Parrucchiere a Bovolone (VR) | Prenota</title>","title")
    t=rep(t,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="Moda Capelli di Giacon Stefano, parrucchiere a Bovolone (VR): taglio, colore, trattamenti e acconciature per lui e per lei. 4,7★ su 36 recensioni. Prenota.">',"desc")
    t=rep(t,'<a href="#top" class="brand">Salone Méta</a>','<a href="#top" class="brand">Moda Capelli</a>',"brand")
    t=rep(t,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Bovolone</span>',"kick")
    t=rep(t,"<h1>Dove l'hairstyling è <em>olistico</em></h1>","<h1>Il tuo stile, <em>curato nei dettagli</em></h1>","h1")
    t=rep(t,"<p>Taglio, colore e trattamenti pensati per te e per la salute dei tuoi capelli. Un salone dove bellezza e benessere si incontrano.</p>","<p>Taglio, colore e trattamenti per lui e per lei, curati da Stefano con esperienza e prodotti professionali. Un salone di fiducia nel cuore di Bovolone.</p>","herop")
    t=rep(t,'<div class="sec-h"><span class="kick">Recensioni</span><h2>Le nostre clienti</h2></div>','<div class="sec-h"><span class="kick">Recensioni</span><h2>4,7★ su 36 recensioni Google</h2></div>',"revh")
    cards="\n      ".join('<div class="rv"><div class="st">%s</div><p>"%s"</p><b>%s</b></div>'%('★'*int(r.get("rating",5)),clean_rev(r["text"]),esc(r["author_name"])) for r in revs)
    if cards: t=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>','<div class="rv-grid">\n      %s\n    </div>\n  </div>\n</section>'%cards,t,count=1,flags=re.S)
    t=rep(t,'<a href="tel:+390450000000" class="btn btn-light">📞 045 000 0000</a>','<a href="tel:%s" class="btn btn-light">📞 %s</a>'%(tel,telsp),"ctatel")
    t=rep(t,'<div><div class="brand" style="color:#fff">Salone Méta</div><p>Parrucchiere olistico nel cuore di Verona.</p></div>','<div><div class="brand" style="color:#fff">Moda Capelli</div><p>Parrucchiere per lui e per lei a Bovolone (VR).</p></div>',"fbrand")
    t=rep(t,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>','<div><h4>Contatti</h4><p><a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener">%s</a><br><a href="tel:%s">%s</a></p></div>'%(cid,addr,tel,telsp),"fcont")
    t=rep(t,"<p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p>","<p>%s</p>"%hours_html(d),"fhours")
    t=rep(t,"<span>© Salone Méta — Verona</span>","<span>© Moda Capelli di Giacon Stefano — Bovolone (VR)</span>","copy")
    t=rep(t,"https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000",ph(cyc(P,0),1000),"heroimg")
    for i,src in enumerate(["3993449","3992855","3065209","3738349"]):
        t=rep(t,"https://images.pexels.com/photos/%s/pexels-photo-%s.jpeg?auto=compress&cs=tinysrgb&w=800"%(src,src),ph(cyc(P,1+i),800),"gal%d"%i)
    t=t.replace("tel:+390450000000",tel).replace("https://wa.me/390450000000",wl).replace("045 000 0000",telsp)
    open(slug,"w",encoding="utf-8").write(t)
    results.append(dict(name="Moda Capelli di Giacon Stefano",file=slug,tel=telsp,num=num,addr="Via Fosse Ardeatine",cid=cid,tmpl="parrucchieri-salonkit",channel="whatsapp",rating="4,7 · 36",wa=wl))
    print("OK moda",len(t),"photos",len(P) if P else 0)

def build_spettino():
    d=api("ChIJ0cKHf2Bvf0cRGBer41FIAu4")
    P=photos_of(d,7); cid=cid_of(d,"")
    tel="+390452584021"; telsp="045 258 4021"
    addr="Via Martin Luther King, 37051 Bovolone (VR)"
    revs=[r for r in d.get("reviews",[]) if r.get("text")][:3]
    slug="da-spettino-bovolone.html"
    t=open("parrucchieri-rhazor-flagship.html",encoding="utf-8").read()
    t=rep(t,"<title>Barberia Rasoio — Barbiere a Verona | Prenota</title>","<title>Da Spettino — Parrucchiere &amp; Barbiere a Bovolone (VR)</title>","title")
    t=rep(t,'content="Barberia Rasoio, barbiere a Verona: taglio uomo, rasatura tradizionale, barba e styling. 4,9★ su 200 recensioni. Prenota il tuo appuntamento.">','content="Da Spettino, parrucchiere e barbiere a Bovolone (VR): taglio, barba e styling. 4,9★ su 31 recensioni Google. Chiama per un appuntamento.">',"desc")
    t=rep(t,'<a href="#top" class="brand">Barberia <b>Rasoio</b></a>','<a href="#top" class="brand">Da <b>Spettino</b></a>',"brand")
    t=rep(t,'<span class="kick">Barbiere · Verona</span>','<span class="kick">Parrucchiere &amp; Barbiere · Bovolone</span>',"kick")
    t=rep(t,"<h1>Il miglior <span>barbiere</span> della città</h1>","<h1>Il tuo <span>barbiere</span> a Bovolone</h1>","h1")
    t=rep(t,"<p>Taglio uomo, barba e rasatura tradizionale con panno caldo. Stile, precisione e un'esperienza da veri intenditori.</p>","<p>Taglio, barba e styling curati nei dettagli. Mani esperte e un ambiente accogliente, nel cuore di Bovolone.</p>","herop")
    t=rep(t,'<div class="c"><div><h4>Chiamaci</h4><p><a href="tel:+390450000000">045 000 0000</a></p></div></div>','<div class="c"><div><h4>Chiamaci</h4><p><a href="tel:%s">%s</a></p></div></div>'%(tel,telsp),"ibar_tel")
    t=rep(t,'<div class="c"><div><h4>Dove siamo</h4><p>Via Esempio 12, Verona</p></div></div>','<div class="c"><div><h4>Dove siamo</h4><p><a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener" style="color:inherit">%s</a></p></div></div>'%(cid,addr),"ibar_addr")
    t=rep(t,'<p>Mar–Sab 9:00–19:00</p>','<p>Chiama per gli orari</p>',"ibar_hours")
    t=rep(t,"<p>Da Barberia Rasoio ogni cliente è unico. Mani esperte, strumenti di qualità e la tradizione del barbiere di una volta, in un ambiente curato e maschile.</p>","<p>Da Spettino ogni cliente è unico. Mani esperte, strumenti di qualità e la tradizione del barbiere di una volta, in un ambiente curato e accogliente.</p>","aboutp")
    t=rep(t,'<div class="sec-h"><span class="kick">Recensioni</span><h2>I nostri clienti</h2></div>','<div class="sec-h"><span class="kick">Recensioni</span><h2>4,9★ su 31 recensioni Google</h2></div>',"revh")
    cards="\n      ".join('<div class="rv"><div class="st">%s</div><p>"%s"</p><b>%s</b></div>'%('★'*int(r.get("rating",5)),clean_rev(r["text"]),esc(r["author_name"])) for r in revs)
    if cards: t=re.sub(r'<div class="rv-grid">.*?</div>\s*</div>\s*</section>','<div class="rv-grid">\n      %s\n    </div>\n  </div>\n</section>'%cards,t,count=1,flags=re.S)
    t=rep(t,"<h2>Prenota il tuo taglio</h2>","<h2>Vieni a trovarci</h2>","ctah2")
    t=rep(t,"<p>Chiamaci o scrivici su WhatsApp: ti aspettiamo in poltrona.</p>","<p>Chiamaci per prenotare il tuo taglio: ti aspettiamo in poltrona.</p>","ctap")
    t=rep(t,'<a href="tel:+390450000000" class="btn btn-gold">📞 045 000 0000</a>','<a href="tel:%s" class="btn btn-gold">📞 %s</a>'%(tel,telsp),"cta_tel")
    t=rep(t,'<a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>','<a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener" class="btn btn-ghost">Come raggiungerci</a>'%cid,"cta_wa")
    t=rep(t,'<div><div class="brand">Barberia <b style="color:var(--gold)">Rasoio</b></div><p>Barbiere tradizionale nel cuore di Verona.</p></div>','<div><div class="brand">Da <b style="color:var(--gold)">Spettino</b></div><p>Parrucchiere e barbiere a Bovolone (VR).</p></div>',"fbrand")
    t=rep(t,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@barberiarasoio.it">info@barberiarasoio.it</a></p></div>','<div><h4>Contatti</h4><p><a href="https://maps.google.com/?cid=%s" target="_blank" rel="noopener">%s</a><br><a href="tel:%s">%s</a></p></div>'%(cid,addr,tel,telsp),"fcont")
    t=rep(t,"<p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p>","<p>%s</p>"%hours_html(d),"fhours")
    t=rep(t,"<span>© Barberia Rasoio — Verona</span>","<span>© Da Spettino — Bovolone (VR)</span>","copy")
    if P:
        t=rep(t,"https://images.pexels.com/photos/1319460/pexels-photo-1319460.jpeg?auto=compress&cs=tinysrgb&w=1600",ph(cyc(P,0),1600),"herobg")
        t=rep(t,"https://images.pexels.com/photos/1570807/pexels-photo-1570807.jpeg?auto=compress&cs=tinysrgb&w=1000",ph(cyc(P,1),1000),"aboutimg")
        for i,src in enumerate(["1570806","1805600","2521617","3998429"]):
            t=rep(t,"https://images.pexels.com/photos/%s/pexels-photo-%s.jpeg?auto=compress&cs=tinysrgb&w=800"%(src,src),ph(cyc(P,2+i),800),"gal%d"%i)
        t=rep(t,"https://images.pexels.com/photos/1813272/pexels-photo-1813272.jpeg?auto=compress&cs=tinysrgb&w=1600",ph(cyc(P,6),1600),"ctabg")
    else:
        print("  (spettino: 0 Google photos -> keeping template barber images)")
    t=t.replace("tel:+390450000000",tel).replace("045 000 0000",telsp)
    open(slug,"w",encoding="utf-8").write(t)
    results.append(dict(name="Da Spettino",file=slug,tel=telsp,num="",addr="Via Martin Luther King",cid=cid,tmpl="parrucchieri-rhazor",channel="mano",rating="4,9 · 31",wa=""))
    print("OK spettino",len(t),"photos",len(P) if P else 0)

build_lorella(); build_chinato(); build_moda(); build_spettino()
json.dump(results,open("_run_results.json","w"),ensure_ascii=False)
print("DONE",len(results))
