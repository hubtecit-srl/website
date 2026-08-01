# -*- coding: utf-8 -*-
import json, html, datetime
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def photo(ref): return "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference="+ref+"&key="+KEY
def esc(s): return html.escape(s, quote=True)

def hours_html(rows):
    out=[]
    for day,val in rows:
        cls=' class="closed"' if val.strip().lower()=="chiuso" else ""
        out.append(f'<div class="hrow"><span>{day}</span><span{cls}>{esc(val)}</span></div>')
    return "".join(out)

def menu_html(cols):
    out=[]
    for title,items in cols:
        lis="".join(f'<li><span>{esc(n)}</span><b>{esc(p)}</b></li>' for n,p in items)
        out.append(f'<div class="mcol"><h3>{esc(title)}</h3><ul>{lis}</ul></div>')
    return "".join(out)

def reviews_html(revs):
    out=[]
    for stars,text,author in revs:
        s="★"*stars
        out.append(f'<figure class="rev"><div class="rstars">{s}</div><blockquote>{esc(text)}</blockquote><figcaption>— {esc(author)}</figcaption></figure>')
    return "".join(out)

def gallery_html(name, refs):
    out=[]
    for i,r in enumerate(refs,1):
        u=photo(r)
        out.append(f'<a class="gitem" href="{u}" target="_blank" rel="noopener"><img loading="lazy" src="{u}" alt="{esc(name)} foto {i}"></a>')
    return "".join(out)

TPL="""<!DOCTYPE html>
<html lang="it"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<meta property="og:title" content="{name} — {comune}">
<meta property="og:description" content="{tagline} {rating}★ su {reviews_total} recensioni.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--ink:{ink};--accent:{accent};--accent2:{accent2};--cream:{cream};--band:{band};--line:#e7ded1;--sub:#7d7266;--white:#fff;--h:'Archivo',Georgia,serif;--b:'Inter',system-ui,sans-serif}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--b);color:var(--ink);background:var(--cream);line-height:1.65;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
img{{display:block;max-width:100%}}
a{{color:inherit;text-decoration:none}}
.wrap{{max-width:1160px;margin:0 auto;padding:0 22px}}
.kick{{font-family:var(--b);font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:.72rem;color:var(--accent)}}
h1,h2,h3{{font-family:var(--h);font-weight:700;line-height:1.1}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:700;font-size:.95rem;padding:14px 26px;border-radius:6px;cursor:pointer;transition:.2s;border:2px solid transparent}}
.btn-fill{{background:var(--accent);color:#fff}}.btn-fill:hover{{filter:brightness(1.1)}}
.btn-wa{{background:#25d366;color:#0b3d1e}}.btn-wa:hover{{filter:brightness(1.05)}}
.btn-line{{background:transparent;color:#fff;border-color:rgba(255,255,255,.6)}}.btn-line:hover{{background:#fff;color:var(--ink)}}
header{{position:fixed;top:0;left:0;right:0;z-index:60;transition:.3s}}
header .bar{{display:flex;align-items:center;justify-content:space-between;height:70px}}
.brand{{font-family:var(--h);font-weight:800;font-size:1.3rem;color:#fff;letter-spacing:.02em}}
header.solid{{background:var(--band);box-shadow:0 2px 18px rgba(0,0,0,.18)}}
nav.main{{display:flex;gap:26px}}
nav.main a{{color:rgba(255,255,255,.9);font-weight:600;font-size:.9rem;transition:.2s}}
nav.main a:hover{{color:#fff}}
.navcta{{background:var(--accent);color:#fff;padding:9px 18px;border-radius:6px;font-weight:700;font-size:.85rem}}
.hero{{position:relative;min-height:92vh;display:flex;align-items:flex-end;color:#fff}}
.hero::before{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,.72)),url('{hero_img}') center/cover;z-index:-1}}
.hero .wrap{{padding-bottom:66px;padding-top:110px}}
.hero h1{{font-size:clamp(2.5rem,7vw,4.6rem);margin:.35em 0 .25em;max-width:14ch}}
.hero .kick{{display:block;margin-bottom:6px}}
.hero p.lead{{font-size:1.15rem;max-width:44ch;color:rgba(255,255,255,.92)}}
.rate{{display:inline-flex;align-items:center;gap:10px;background:rgba(255,255,255,.14);backdrop-filter:blur(4px);padding:8px 15px;border-radius:40px;font-weight:600;font-size:.95rem;margin-bottom:8px}}
.rate .s{{color:#ffc94d;letter-spacing:2px}}
.hero .cta{{display:flex;gap:14px;flex-wrap:wrap;margin-top:26px}}
section{{padding:76px 0}}
.sec-head{{max-width:620px;margin-bottom:40px}}
.sec-head h2{{font-size:clamp(1.9rem,4vw,2.9rem);margin:.25em 0}}
.about{{display:grid;grid-template-columns:1.1fr .9fr;gap:52px;align-items:center}}
.about img{{border-radius:12px;aspect-ratio:4/5;object-fit:cover;width:100%}}
.about p{{font-size:1.06rem;margin-bottom:16px;color:#3a3128}}
.menu{{background:var(--band);color:#fff}}
.menu .kick{{color:var(--accent2)}}
.menu .grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:44px}}
.mcol h3{{font-size:1.4rem;color:var(--accent2);margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,.18)}}
.mcol ul{{list-style:none}}
.mcol li{{display:flex;justify-content:space-between;gap:14px;padding:9px 0;border-bottom:1px dotted rgba(255,255,255,.14);font-size:1rem}}
.mcol li b{{color:var(--accent2);white-space:nowrap}}
.mnote{{text-align:center;margin-top:34px;color:rgba(255,255,255,.6);font-size:.9rem}}
.gal{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}
.gitem img{{width:100%;height:230px;object-fit:cover;border-radius:10px;transition:.3s}}
.gitem:hover img{{transform:scale(1.03)}}
.reviews{{background:var(--white)}}
.revgrid{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.rev{{background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:26px}}
.rstars{{color:#f0a91c;letter-spacing:2px;margin-bottom:12px}}
.rev blockquote{{font-size:1rem;color:#3a3128;margin-bottom:14px}}
.rev figcaption{{font-weight:600;font-size:.9rem;color:var(--sub)}}
.contact{{background:var(--band);color:#fff}}
.cgrid{{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:start}}
.cinfo h2{{color:#fff}}
.cinfo .kick{{color:var(--accent2)}}
.cline{{display:flex;gap:12px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.14);font-size:1.02rem}}
.cline b{{min-width:96px;color:var(--accent2)}}
.hrow{{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px dotted rgba(255,255,255,.14);font-size:.97rem}}
.hrow .closed{{color:#e08a8a}}
.map{{border-radius:12px;overflow:hidden;min-height:340px;border:0;width:100%}}
.contact .cta{{margin-top:24px;display:flex;gap:14px;flex-wrap:wrap}}
footer{{background:var(--ink);color:rgba(255,255,255,.7);text-align:center;padding:40px 22px}}
footer .fbrand{{font-family:var(--h);font-weight:800;font-size:1.4rem;color:#fff;margin-bottom:8px}}
footer a{{color:var(--accent2)}}
.hubcredit{{margin-top:14px;font-size:.82rem;color:rgba(255,255,255,.4)}}
.mbar{{display:none;position:fixed;bottom:0;left:0;right:0;z-index:70;background:var(--band);padding:9px;gap:9px;box-shadow:0 -2px 16px rgba(0,0,0,.28)}}
.mbar a{{flex:1;text-align:center;padding:14px 0;border-radius:8px;font-weight:700;font-size:1rem;color:#fff}}
.mbar .call{{background:var(--accent)}}
.mbar .book{{background:var(--accent2)}}
.mbar .wa{{background:#25d366;color:#0b3d1e}}
@media(max-width:900px){{
 nav.main,.navcta{{display:none}}
 .about,.cgrid{{grid-template-columns:1fr;gap:30px}}
 .menu .grid{{grid-template-columns:1fr;gap:30px}}
 .gal{{grid-template-columns:repeat(2,1fr)}}
 .revgrid{{grid-template-columns:1fr}}
 .mbar{{display:flex}}
 body{{padding-bottom:70px}}
 section{{padding:52px 0}}
}}
@media(max-width:560px){{
 .hero h1{{font-size:2.1rem}}
 .hero .cta .btn{{width:100%}}
 .sec-head h2,.about h2{{font-size:1.7rem}}
 .gal{{grid-template-columns:1fr 1fr}}
 .gitem img{{height:150px}}
 body{{font-size:15.5px}}
}}
</style></head>
<body>
<header id="hd"><div class="wrap bar">
 <a href="#top" class="brand">{name}</a>
 <nav class="main">
   <a href="#chi-siamo">Chi siamo</a>
   <a href="#menu">Menù</a>
   <a href="#galleria">Galleria</a>
   <a href="#recensioni">Recensioni</a>
   <a href="#contatti">Contatti</a>
 </nav>
 <a href="tel:{tel_raw}" class="navcta">Chiama: {phone}</a>
</div></header>

<a id="top"></a>
<section class="hero"><div class="wrap">
 <div class="rate"><span class="s">★★★★★</span> {rating} · {reviews_total} recensioni Google</div>
 <span class="kick">{comune} · Verona</span>
 <h1>{name}</h1>
 <p class="lead">{tagline}</p>
 <div class="cta">
   <a href="tel:{tel_raw}" class="btn btn-fill">Chiama e prenota</a>
   {hero_secondary}
 </div>
</div></section>

<section id="chi-siamo"><div class="wrap about">
 <div>
   <span class="kick">La nostra cucina</span>
   <h2>Benvenuti da {name}</h2>
   {about_paras}
   <a href="#contatti" class="btn btn-fill" style="margin-top:8px">Vieni a trovarci</a>
 </div>
 <img loading="lazy" src="{about_img}" alt="Ambiente di {name}">
</div></section>

<section id="menu" class="menu"><div class="wrap">
 <div class="sec-head"><span class="kick">La proposta</span><h2>Il nostro menù</h2></div>
 <div class="grid">{menu}</div>
 <p class="mnote">Il menù può variare in base alla stagione e alla disponibilità del mercato. Chiama per conoscere i piatti del giorno.</p>
</div></section>

<section id="galleria"><div class="wrap">
 <div class="sec-head"><span class="kick">Galleria</span><h2>Uno sguardo da noi</h2></div>
 <div class="gal">{gallery}</div>
</div></section>

<section id="recensioni" class="reviews"><div class="wrap">
 <div class="sec-head"><span class="kick">Dicono di noi</span><h2>{rating}★ su {reviews_total} recensioni</h2></div>
 <div class="revgrid">{reviews}</div>
</div></section>

<section id="contatti" class="contact"><div class="wrap cgrid">
 <div class="cinfo">
   <span class="kick">Dove siamo</span>
   <h2>Contatti &amp; orari</h2>
   <div class="cline"><b>Indirizzo</b><span>{address}</span></div>
   <div class="cline"><b>Telefono</b><a href="tel:{tel_raw}">{phone}</a></div>
   {social_line}
   <div class="cline"><b>Mappa</b><a href="{cid_url}" target="_blank" rel="noopener">Apri su Google Maps</a></div>
   <div style="margin-top:18px">{hours}</div>
   <div class="cta"><a href="tel:{tel_raw}" class="btn btn-fill">Chiama e prenota</a>{contact_secondary}</div>
 </div>
 <iframe class="map" src="https://maps.google.com/maps?q={lat},{lng}&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mappa {name}"></iframe>
</div></section>

<footer>
 <div class="fbrand">{name}</div>
 <div>{address} · <a href="tel:{tel_raw}">{phone}</a></div>
 <div class="hubcredit">Sito realizzato da HubTec · Verona</div>
</footer>

<div class="mbar">
 <a class="call" href="tel:{tel_raw}">Chiama</a>
 {mbar_secondary}
</div>
<script>
document.addEventListener('scroll',function(){{document.getElementById('hd').classList.toggle('solid',window.scrollY>60)}});
</script>
</body></html>"""

SITES=[]

# ---- 1. Ristorante Corte Peretti (palette: verde bosco + oro) ----
SITES.append(dict(
 slug="ristorante-corte-peretti-dossobuono",
 name="Ristorante Corte Peretti",
 comune="Dossobuono",
 title="Ristorante Corte Peretti — Dossobuono | Cucina di mare e carne alla brace",
 tagline="Cucina di mare e carne alla brace nel cuore di Madonna di Dossobuono: pasta fatta in casa, bolliti veronesi e ambiente curato.",
 meta_desc="Ristorante Corte Peretti a Dossobuono (Verona): cucina di mare e carne alla brace, pasta fatta in casa, carrello dei bolliti. 4.3 stelle su 393 recensioni. Prenota chiamando 045 950134.",
 rating="4.3", reviews_total="393",
 phone="045 950134", tel_raw="045950134",
 address="Via Mantovana, 112/B, 37137 Madonna di Dossobuono VR",
 cid_url="https://maps.google.com/?cid=1085521879438930120",
 lat="45.409982", lng="10.9311059",
 ink="#1a1f1b", accent="#1f6f5c", accent2="#c39b4e", cream="#f3f1ea", band="#14231f",
 social_kind=None, social_url="", wa=None,
 about=["Ristorante Corte Peretti è un'osteria di charme immersa nel verde a Madonna di Dossobuono: un ambiente curato in ogni dettaglio, con giardino e sale accoglienti, dove la tradizione veronese incontra il gusto per la brace e il pesce.",
        "La nostra forza è la pasta fatta a mano, servita con una scelta di sughi, insieme alla carne alla brace, ai bolliti con la pearà e ai piatti di mare. Un servizio attento e un rapporto qualità-prezzo che i nostri ospiti apprezzano da anni."],
 menu=[("Antipasti",[("Antipasto di mare","16"),("Carne salada con rucola e grana","12"),("Tagliere di salumi e formaggi","11")]),
       ("Primi · pasta fatta in casa",[("Pasta fatta a mano con scelta di sughi","12"),("Bigoli con ragù d'anatra","11"),("Risotto del giorno","12")]),
       ("Dalla brace & bolliti",[("Costata alla brace","con supplemento"),("Carrello dei bolliti con pearà","16"),("Grigliata mista di carne","18")]),
       ("Pesce & dolci",[("Grigliata di pesce","20"),("Spaghetti allo scoglio","15"),("Dolci della casa","6")])],
 reviews=[(5,"Se cercate un'esperienza culinaria autentica, la carne alla brace è da provare: succulenta, tenera e cucinata alla perfezione. Il bollito, altra prelibatezza veronese, è un trionfo di sapori. Ottima anche la pasta fatta in casa.","Davide Prosperino"),
          (5,"Splendida esperienza. Tutta la location è curata anche nei particolari, giardino compreso. Piatti ottimamente cucinati, servizio impeccabile e staff efficiente. Il rapporto qualità-prezzo è più che soddisfacente!","Franco Stropeni"),
          (4,"Trattoria che promette molto bene, famosa per la pasta fatta a mano dove ti portano quattro sughi con cui condire a piacere. Ma anche carne e pesce di qualità. Da provare.","Luca Enrico Spedo")],
 hours=[("Lunedì","12:00–14:30"),("Martedì","Chiuso"),("Mercoledì","12:00–14:30"),("Giovedì","12:00–14:30"),("Venerdì","12:00–14:30"),("Sabato","Chiuso"),("Domenica","Chiuso")],
 refs=["AWCwydgHfBpWG398Ao2RYn1QY2vAE1wFx7aAFTw3waZM7in5BVxzple5aEtT-1pahSt4jIm3gxyibnrQlUGYcC5a0v9dws17tDSNA67gdthA5rZVWfVhLPlhC_BwU-387b1iHFI4GOMUL1mXRcJdp2NiNc44TrwF9I9xEYFPTzelX_DN__PJKcEpFamsZ8kgmTU6aiu_8r5o2FGIhdUV4pxicXSYTsAl_7DkGe1jS3_22fYvHl-w-uzQ_HtNjitidfRi4GgYZiA3398FXLNVzOVNVjQSdUF4Drt_UR8ToXejmUn2Tlsl7Kfp8f0yHjQwtH1E4cR4LLKT4keAEYc34xDG9lWkciMHfq8HGjCrBcOh7eAWKJu3doNqJEex2XTfDIjnsAFtLzZSCFHJ1msurDcCWEgvKz9JchrRNsJsFCfDQrvPE9qi",
       "AWCwydip4DagzTAxJ70d8GGnbjTQ13kqJ-Vxau-yIe4cn6WE0sEPnz9kRrZO-bv7U4xCSG1n2G0ukh5uWWDLqhqHhARJgA73YR3QbVowOSNrApx62kIF-jC8kHguz95iu994bIbpzhVtRAfHKKB2TrSbhyivYB8zUZqmvl3XMUcijw-yXMdIZOADNZP_-Xiu6vpmauAUo0lpxiRcvtd4SgVHG3NytxISsjU20UUbnpQ2uSK5bBdzpike327ebJdOSCOBT-jBHG-eWCSpC3YiQFVis2k7mWy54lOuMZXpHbt6L2P-zqI_swDGnp5kK7ZrNu8ioY1j279XJdiWiWI8p7z0jfaEWI081Y6dJlWH2jJdLpsFQJN0YKAClJnVrrCCJmbd_OmBuhWZu1pnB-3lg2HFP1vFyPXNUI4PKL4uREou0Khiqk5mj1qUb6WPJQyQUdcf",
       "AWCwydgrMZjzv5wZmg6U9ADFOOnxSbjjkAf6w0buqZHmFfsfSgfWqgwiTJW0Ia9pJMZ88T8mZI_T5zQjZ1MX3FDU2z9OBfeVkCTCrCveY_qXAJpaMwaIQfaRzTexIDt2QiuM7_4iWqMKL6w6qB-4VJ_u33H40JRo4WGHukikn_c91Xxe1CARVSyI5E8fPFyUIMCmCOac-LUDq6oFBufCNsEv3xZVD5kGzmqkXhXrK_4aF0Rw1CGRIFi0MyGHnwIgcbgRYO1fAehfIFoeWOfki6xnkj8pLmE-tAXAVvwVihWWyquUQfHyAgjP0nvcf2-H3IPsiTJ3ZcCvHAE2li6Zg9f2j6wuLJwBKISmh3JJ0YzMQF4_SiDp6zefam8iehaMjpn6RHbIAmMShYq9hFaLSZeU1qWx9Niy_bBDZSlu44qEOzSs2-qHMU_5yL2JPk40yRtb",
       "AWCwydgvwPBohNFQyA5W9-EYvE5ZHnLADpvAebsad2m1k5jLbVWcsuOyyTIIYsFgdazJQLJh3Lc57ZsCBKNDd8fEdBYO4E2xAYMyjSQEKbRR019aqREAdhpIGByu2h4mfkZ9yZ6nnyKrXpLzNACQeporcSnLiOSWM19nV-XSdejZJqVvz8LuQkPbq0FzUNFMUOnKC0yDGw11o4pC-DjEjYFaMPCy2crN3T8hqR_kjX0gOYdS5umGzjiJAnCk40HbAYbji7n288C3J50TS1qRz_axz9qmj1B1k8JMjelKlTLxoFpMt8jflhiFFRCtmvQ0jH8F4Po0_AExqfZSDCfc8TiiUgLQ_gSP1GDVcHTjd0mCQyGzzb9NqSzcTMaZT_vJlPS6NfwyuYCnh3gONuALLMRGAIW0OkjWoxIbnM3GCyfj8cPrZFU"],
))

# ---- 2. Trattoria Da Emy (palette: blu mare + arancio) ----
SITES.append(dict(
 slug="trattoria-da-emy-dossobuono",
 name="Trattoria Da Emy",
 comune="Dossobuono",
 title="Trattoria Da Emy — Dossobuono | Pesce fresco e cucina casereccia",
 tagline="Trattoria di pesce e cucina casereccia a Dossobuono: antipasti di mare, spaghetti allo scoglio e menù di lavoro a prezzi onesti.",
 meta_desc="Trattoria Da Emy a Dossobuono (Verona): pesce fresco, spaghetti allo scoglio, piatti caserecci di terra e di mare e menù di lavoro. 4.3 stelle su 575 recensioni. Prenota al 045 468 6197.",
 rating="4.3", reviews_total="575",
 phone="045 468 6197", tel_raw="0454686197",
 address="Via Brigate Alpine, 64, 37069 Dossobuono VR",
 cid_url="https://maps.google.com/?cid=18310711355188873876",
 lat="45.3917007", lng="10.9091234",
 ink="#141b21", accent="#1c5a86", accent2="#d98b3a", cream="#f4f1ea", band="#132a3a",
 social_kind=None, social_url="", wa=None,
 about=["Trattoria Da Emy è un indirizzo genuino a Dossobuono, dove si mangia pesce fresco e cucina casereccia in un ambiente semplice e conviviale. Ampia sala pranzo, piccolo dehor esterno e la cordialità di uno staff giovane e attento.",
        "Antipasti di mare, spaghetti allo scoglio, fritture e piatti di terra: porzioni abbondanti e sapori curati. A pranzo il menù di lavoro a prezzo modico, la sera l'atmosfera si fa allegra con serate a tema."],
 menu=[("Antipasti di mare",[("Antipasto misto di mare","14"),("Cozze alla marinara","10"),("Insalata di mare","12")]),
       ("Primi",[("Spaghetti allo scoglio","13"),("Risotto di pesce","13"),("Pasta al ragù della casa","9")]),
       ("Secondi",[("Frittura di paranza","15"),("Grigliata mista di pesce","18"),("Secondo di carne del giorno","12")]),
       ("Pranzo & dolci",[("Menù di lavoro","da 12"),("Dolce della casa","5"),("Caffè","1,5")])],
 reviews=[(5,"Ottima trattoria con scelta sia di terra che di mare. Servizio giovane e affabile. Luogo conviviale e allegro. Ottimo rapporto qualità/prezzo. Raccomando.","Marco Marinopiccoli"),
          (5,"Pranzato e cenato in diversi ristoranti della zona: la Trattoria da Emy si è aggiudicata il primo posto. Ambiente semplice e accogliente, personale professionale, cucina abbondante dai sapori curati. Grandi!","Chiara Costa"),
          (4,"Ristorante di pesce. Il menù è limitato ma le preparazioni caserecce sono abbondanti e gustose. Molti piatti unici e menù di lavoro a prezzo modico. Il rapporto qualità/prezzo regge bene.","Antonino De Marines")],
 hours=[("Lunedì","Chiuso"),("Martedì","12:00–14:30, 19:00–22:30"),("Mercoledì","12:00–14:30, 19:00–22:30"),("Giovedì","12:00–14:30, 19:00–22:30"),("Venerdì","12:00–14:30, 19:00–22:30"),("Sabato","12:00–14:30, 19:00–22:30"),("Domenica","12:00–14:30")],
 refs=["AWCwydhgXYG77_XW8zGlmJzIrH9m9Wlwb2c4OG2JfyGKAULg1fJEFx-XO8Tz62cViV9NPOTOOWv3Wqh-xplBf0bdHDIetwMXRmswezhUQGFoY80Bp-Io8HIWRlaR4HiI_1GAtFcLRGqwKUTJLYqhRntM2EJkjJ_Jvi4bZ39HYvrE_Et8M-_k8LID3VQK5rB5K7Lp5Q3ykXQxjf4ja2xf0RoeU-wAMiiyYU8XMj6izPnNFAs_CGDOKULXXDYnHEqwdDczNGkwjuvwp6CgR3OQcKsUZ5mpvxYvWcvuwR7Bvuoo56MybXy0qX9sLGacs6-_-NGFjurKXA1ub-82tpSa2siX09D3gP5y5Ea0LaPAl0EuUGTDGWLz7_H4aT2F9NFiFnyZfoX3FYSG4sgUJx8eEeX3JM05TxvZFf2pVck-4qULNgdBAg",
       "AWCwydjIESC4DhzylDt089hzy_8qpppfWB98Dkdfrg0dKWS2He0sQ8Jg571sFcjG_l8h9aTXR5wWZ2KMQY0a4VuH3V1Da3G5j8mpkr6MBBIrCuJy1c7mMsQfGnF8SrQ7cChcjs0RGKCqg-_T3NBCi8GnVhcsZZpF74vFt8XQYCGzgzKkqLglnzBtG-H6fsMO9kV0UmGT7Z8F1tdwoDmx1PiVB8nSvnLJLjzbQeboMQm7G3_i64lEBjuVSt1DvPjX9KHfCg4oSHw6koJm6n1-2npb8cx2DXCH-uh2ErxviwRe6RrG_6fW5pSXVT2FWmC8ec64n34TiFYhfNsx4_JvUs2nNb5T0C3rSDk79olBdz2Q5DdZQcgBc29yHDiK6n1dxlnMyDqtenBD4EI6Jy_bQwYidPYGahCkG9WmeeC7jyzd0U4JcvAT",
       "AWCwydhWVaJmuC1kebaAP3PDbjndUMZXeM5FVTOd6feLl1op92sMMnGS8ktWUfGH_RS-ZfwQpuA58dTjamjXYTMNf5jbXjxFqmM0qC3ZQr-UouMES8n9B01y0v6TTFF-oArRrCpQ_OTnKnnykFojJbcJb5kVqqtzNpMhjF9l00i8QXNdKYAYklAKvNOfm3nlTQcgzz8_u-LdigAInBD_fGOxQd6-REJZk8deH59yLJDoaZZ3e7GNiGsaTBxru08xPwpaNjXKegr1v1l8a9-d6-RSGz0pYG-h18cEcy6NPIxD1nl1f-nrx0FmPjyJkuyfRU-g7Z0IVeNnic1nEVa43QM_ECfvqKnInn6RR1dAX_-Y8zVx65dGoQUva12efL7fOtjytjq0ux84D3TWNUsvA5tar5jbCKz5PAmh0PDG-Zlf9NnQPZIQIMxairJB3i45TSWT",
       "AWCwydgEQKHMkTGHKkGOO2gvoO2QHblZWVHL1JX8Vs7GTMd5gerGYE8HVCiOMu-PYPb42iIIZRF7EEtPiMMW0mjOoTJc2njiJp6YHZ-ZH07sS9mQPU_u8hsnSUZ4Xd1sEhRqEmY5rpFn1f-gzOfX-X5igEcI28qmJjL0k99I8bFESL8_VWaHcFNSwvrnm2QlCe27wpAy0DDZz4w5JHr7NCWpPiAo97vOily8qTgNoONIi9nqsOhHLm3Ebqy_n3CMIM9QksrZXXJvpF2eGPQdwohJzuAdgjqgmpmqU0Ps0QKsVEdsmBUWKuDVtvlFZECFovB9hwe4TQR5H13RNjw-v6fpvSL4_MCzreqwtJUqPEwee_NYAUogeup3V9tFV1_NFku4CIXNe-gPXM6nmQ3e9cD2eVe2uyugbrcyC6eFq_7r86xDx-wM"],
))

# ---- 3. Borgo Bello Bistrot (palette: verde oliva bistrot) ----
SITES.append(dict(
 slug="borgo-bello-bistrot-dossobuono",
 name="Borgo Bello Bistrot",
 comune="Dossobuono",
 title="Borgo Bello Bistrot — Dossobuono | Colazioni, pause pranzo e aperitivi",
 tagline="Il bistrot di Dossobuono per colazioni, pause pranzo e aperitivi: menù del giorno che cambia ogni giorno, piatti freschi e tanta cordialità.",
 meta_desc="Borgo Bello Bistrot a Dossobuono (Verona): colazioni, pause pranzo con menù del giorno e aperitivi. Locale accogliente e moderno. 4.9 stelle su 64 recensioni. Info e prenotazioni 351 646 9168.",
 rating="4.9", reviews_total="64",
 phone="351 646 9168", tel_raw="3516469168",
 address="Via Staffali, 44C, 37062 Dossobuono VR",
 cid_url="https://maps.google.com/?cid=16675559475256100294",
 lat="45.389795", lng="10.9040641",
 ink="#20241a", accent="#7a8450", accent2="#c98a3c", cream="#f7f2e8", band="#2a2418",
 social_kind="Instagram", social_url="https://www.instagram.com/borgo_bello_bistrot", wa="393516469168",
 about=["Borgo Bello Bistrot è il punto di riferimento di Dossobuono per iniziare la giornata con una buona colazione, fermarsi per una pausa pranzo veloce e genuina o ritrovarsi all'ora dell'aperitivo. Un locale accogliente e moderno, con dehor fronte strada.",
        "Ogni giorno proponiamo un menù che cambia, con tre primi diversi e i grandi classici. Ingredienti freschi, presentazioni curate e un servizio rapido e sorridente: qui si mangia bene, in fretta e a un prezzo onesto."],
 menu=[("Colazioni",[("Cappuccino e brioche","2,5"),("Toast farcito","4"),("Centrifughe e spremute","4")]),
       ("Primi del giorno",[("Risotto zucca e parmigiano","8,50"),("Pasta al pesto di rucola e noci","8,50"),("Carbonara (una volta a settimana)","8,50")]),
       ("Secondi",[("Secondo del giorno con contorno","10"),("Piatto unico","9"),("Insalatona ricca","8")]),
       ("Aperitivi & bar",[("Spritz","6"),("Americano","7"),("Tagliere con calice di vino","10")])],
 reviews=[(5,"Frequento il Borgo Bello quasi ogni giorno per il pranzo. Ogni giorno un menù che varia con tre primi diversi. La qualità del cibo è costantemente alta, ingredienti freschi. Personale gentile e rapidissimo. Rapporto qualità-prezzo imbattibile.","Luca Piraino"),
          (5,"Locale accogliente e moderno, il migliore a Dossobuono per pranzi di lavoro. Ragazze sempre gentili e precise. Ingredienti di qualità e piatti buoni con ottime presentazioni. Possibilità di aperitivo dal pomeriggio alla sera. Consigliatissimo!","Mattia Boscaro"),
          (5,"Locale per pranzi veloci. Il servizio è svelto e a prezzi modici. La professionalità del personale è degna di nota, estremamente gentili e celeri. Stra consigliato per un pranzo al volo.","Michele Canalia")],
 hours=[("Lunedì","07:00–20:00"),("Martedì","07:00–20:00"),("Mercoledì","07:00–20:00"),("Giovedì","07:00–20:00"),("Venerdì","07:00–20:00"),("Sabato","Chiuso"),("Domenica","Chiuso")],
 refs=["AWCwydgIO5Xyw6p9qs99yrqVetJVhRvByizOTiPUvYDDBINyyeCk4UUmaGWEDj0rnx3v7diMa39o1E1fC-yj2BUhMIm7V-hyFs__Zyok4Ry1uXcVkndM9J8y3ByGnoJizvDK2CKrLf2fNaCAz3NV5V-O8uGMEM_AkO8ai78DlbWBeBWEkhxIZMVoh5Lh82EiB0gWeAQ9l2qSkFmR0RnPAAlatmclbrsIMgit2hqdo7rvT3ddzmE-Qv4dSN_VchlhLMdV2f8jinl9Mc0dMedDOMc1cS1Bf256jwKqOic8p1HVCiHb6qg_tHdghxqqIdmojHsLp0qCQjVyrBhFAK8rt2yK_Z61H1wkfSsnu51xZgq5zi1sLaj1NXooOHNbNO_kU9u-uodracuvwE7kUppdVAlDbWnD28CytW5F3mw7C1K46L30dbr1",
       "AWCwydjbCl4dFYMhch9oMtGSrJ8B-FT9nb_bLWboesbBYyNJmwHBthtocXwQEoKYeYuji3AHjHRM9J66as-E9-MQ38v-jGmWIYDC4EBuS9JV3adGDozGtcmhQDlzrHnPdsehGauT2Ug9ohxDo9CXVW7VjSFTiJLoU71u6P9wXyDA4nhh4b08z_ZtU0i9AX-75mOIk6DjltcQOuo9nYjjoTW3WXK1pEvHy2uYPNfYd4s936hhtuIE0R7dhdFlkXGua9nKKhRJkr7F9xElAC5-x6QKAffh-KUH8c72lPFcI9rubruRZ7FM0-I2QRE6coumRXBgnLq0OV-z1A67yQ1UJNXKbCDcKyWxwdXf3VmrGSeNJkLLtRwpTb4FriypvmEHF1jSe1dKoI8GpeIIhFvEMQ4-BjPwl59w2rKCMsAu0E2wTykWzuStXucTp_EFKn4D_Q",
       "AWCwydh5f4sAMWE73zhBGshmJzv_x5oUqbshKx38RrVAU2NKnm2OCciNVpkY6cmCYCfNTtu92SoVcnmTCXDdEkfrsdySyrgiZtdfb3OW0EV8YknlMSMU3LMlUbTnP8-gw2Nq169cUA5yPkJSWDouZceYa0Lw99l8NANmS-WsBeEXsKUDa-GvuWeuvwc75aTFl6YE6tpMgVZtr9ktzDME4qFM_kBXyA1MErsrRdbzOVacPJJzBqkix99Ch5sCYaBJcLTIFig72Ma_uyDBoP6M4uTnl2Wxs5waZC1-nOxEDpdqo8GmI4lS491L6cSA4AkjRfPgR5RIdS0L2csbIwY8qrpF86nKvvsFT9yiiJdm6W87W3tB6xL6HkJB1tcl11-onjvsOunCA6xCbtwXJJbm6VChmkBuOwS6e9XLrdkY5yNqlLDv8Qp6xJRux-_xJ71NOA",
       "AWCwydi4RyHZ75wqtpVQZ4hq37QTEuGOqgWtzT5byIBmwm6jSc0P4KxdFJjAjSLup77l8fVZVzYdRD43UgXsTZxGa-iXqqOIb4r-27eCQUMN-I95L-49nh0R-4NbKj_mVAcIuZiqin-mHcOm2mDIezX3ay4T3eSvIJ3y36fONbGHceD2gxdNghzVS7LgG0eSMcP0VJvtE_MJYNl1V1j4zTTSybu68w30S_5bsJW0a6McqjWKQjks4Xzu8bnmXR2okRbAsIAcQTPXdi1kGpVA1Ovso9K_Gms4zNsVoDYynpFpedrtZn30AIWIeUeoY-l5R8aBhW9CjfWkEdMy_Fp-nJkorV5tyN1O3hQGFhOlN4xfHbBOipuCPdIjuRwoqEPebO3BAnC2_rQ9rIG87xC5II_hAAad9gUBLOjLq9YMPEDdSe8"],
))

for s in SITES:
    hero_secondary='<a href="#menu" class="btn btn-line">Scopri il menù</a>'
    contact_secondary=""
    mbar_secondary='<a class="book" href="#contatti">Prenota</a>'
    social_line=""
    if s.get("wa"):
        wa_url="https://wa.me/"+s["wa"]
        hero_secondary='<a href="'+wa_url+'" class="btn btn-wa" target="_blank" rel="noopener">Scrivici su WhatsApp</a>'
        contact_secondary='<a href="'+wa_url+'" class="btn btn-wa" target="_blank" rel="noopener">WhatsApp</a>'
        mbar_secondary='<a class="wa" href="'+wa_url+'" target="_blank" rel="noopener">WhatsApp</a>'
    if s.get("social_kind"):
        social_line='<div class="cline"><b>'+s["social_kind"]+'</b><a href="'+s["social_url"]+'" target="_blank" rel="noopener">Seguici su '+s["social_kind"]+'</a></div>'
    about_paras="".join("<p>"+esc(p)+"</p>" for p in s["about"])
    out=TPL.format(
        title=esc(s["title"]), meta_desc=esc(s["meta_desc"]), name=esc(s["name"]), comune=esc(s["comune"]),
        tagline=esc(s["tagline"]), rating=s["rating"], reviews_total=s["reviews_total"],
        phone=esc(s["phone"]), tel_raw=s["tel_raw"], address=esc(s["address"]), cid_url=s["cid_url"],
        lat=s["lat"], lng=s["lng"], ink=s["ink"], accent=s["accent"], accent2=s["accent2"], cream=s["cream"], band=s["band"],
        hero_img=photo(s["refs"][0]), about_img=photo(s["refs"][1]),
        about_paras=about_paras, menu=menu_html(s["menu"]), gallery=gallery_html(s["name"], s["refs"]),
        reviews=reviews_html(s["reviews"]), hours=hours_html(s["hours"]),
        hero_secondary=hero_secondary, contact_secondary=contact_secondary, mbar_secondary=mbar_secondary,
        social_line=social_line,
    )
    open(s["slug"]+".html","w",encoding="utf-8").write(out)
    print("WROTE",s["slug"]+".html",len(out),"bytes")

# ---- update index.html ----
idx=open("index.html","r",encoding="utf-8").read()
block='<h2>Nuovi siti — Dossobuono (2026-08-01 · ristoranti)</h2>\n<ul>\n'
block+='<li><a href="./ristorante-corte-peretti-dossobuono.html">Ristorante Corte Peretti — Ristorante — Dossobuono</a></li>\n'
block+='<li><a href="./trattoria-da-emy-dossobuono.html">Trattoria Da Emy — Trattoria di pesce — Dossobuono</a></li>\n'
block+='<li><a href="./borgo-bello-bistrot-dossobuono.html">Borgo Bello Bistrot — Bistrot — Dossobuono</a></li>\n'
block+='</ul>\n'
marker='<h2>Nuovi siti — Caprino Veronese (2026-07-31 · parrucchieri)</h2>'
idx=idx.replace(marker, block+marker, 1)
open("index.html","w",encoding="utf-8").write(idx)
print("INDEX updated")
