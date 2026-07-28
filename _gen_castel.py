# -*- coding: utf-8 -*-
import html
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def ph(ref,w=1400): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={KEY}"
STOCK=[
"https://images.pexels.com/photos/36436447/pexels-photo-36436447.jpeg?auto=compress&cs=tinysrgb&w=1600",
"https://images.pexels.com/photos/3852204/pexels-photo-3852204.jpeg?auto=compress&cs=tinysrgb&w=1600",
"https://images.pexels.com/photos/3979134/pexels-photo-3979134.jpeg?auto=compress&cs=tinysrgb&w=1600",
"https://images.pexels.com/photos/3768926/pexels-photo-3768926.jpeg?auto=compress&cs=tinysrgb&w=1600",
"https://images.pexels.com/photos/5240818/pexels-photo-5240818.jpeg?auto=compress&cs=tinysrgb&w=1600",
]
def e(s): return html.escape(s,quote=True)

def build(d):
    p=d["pal"]
    css_vars=f"--teal:{p['teal']}; --teal-d:{p['teald']}; --dark:{p['dark']}; --gold:{p['gold']}; --ink:#20302d; --ink2:#556661; --sub:#8a978f; --line:#e4e6df; --cream:{p['cream']}; --soft:{p['soft']}; --white:#fff; --green:#25d366;"
    # services
    serv="".join(f'<div class="serv-c"><div class="ic">{s[0]}</div><h3>{e(s[1])}</h3><p>{e(s[2])}</p></div>' for s in d["services"])
    # pricing
    price=""
    for i,pc in enumerate(d["pricing"]):
        feat=" feat" if i==1 else ""
        bcls="btn-light" if i==1 else "btn-out"
        lis="".join(f"<li>{e(x)}</li>" for x in pc[2])
        price+=f'<div class="price-c{feat}"><h3>{e(pc[0])}</h3><div class="amt">{e(pc[1])}</div><ul>{lis}</ul><a href="#prenota" class="btn {bcls}">Prenota</a></div>'
    # reviews
    revsec=""
    if d["reviews"]:
        cards="".join(f'<div class="rv"><div class="st">★★★★★</div><p>"{e(r[1])}"</p><b>{e(r[0])}</b></div>' for r in d["reviews"])
        revsec=f'''<section class="reviews">
  <div class="wrap">
    <div class="sec-h"><span class="kick">Recensioni</span><h2>Cosa dicono di noi · {d["rating"]}★ su Google</h2></div>
    <div class="rv-grid">{cards}</div>
    <p style="text-align:center;color:var(--sub);margin-top:22px;font-size:.9rem">Valutazione media {d["rating"]}/5 su {d["nrev"]} recensioni Google verificate.</p>
  </div>
</section>'''
    # hours
    hrows="".join(f'<tr><td>{e(h[0])}</td><td>{e(h[1])}</td></tr>' for h in d["hours"])
    # wa button/bar
    wa=d.get("wa")
    watext=("Buongiorno, ho visto il vostro sito e vorrei maggiori informazioni.")
    wa_link=f"https://wa.me/{wa}?text={watext.replace(' ','%20')}" if wa else None
    hero_cta_wa=f'<a href="{wa_link}" class="btn btn-glass">💬 WhatsApp</a>' if wa_link else ''
    cta_wa=f'<a href="{wa_link}" class="btn btn-glass">💬 WhatsApp</a>' if wa_link else ''
    mbar_wa=f'<a href="{wa_link}" class="book">WhatsApp</a>' if wa_link else f'<a href="#prenota" class="book">Prenota</a>'
    email_line=f'<br><a href="mailto:{d["email"]}">{e(d["email"])}</a>' if d.get("email") else ''
    intro_extra=(" "+d["introextra"]) if d.get("introextra") else ""
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(d["name"])} — {e(d["cat"])} a Castel d'Azzano (VR)</title>
<meta name="description" content="{e(d["metadesc"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Antic+Didone&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{ {css_vars}
  --h:'Antic Didone',Georgia,serif; --b:'Public Sans',system-ui,sans-serif; }}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--b);color:var(--ink);background:var(--white);line-height:1.75;font-weight:400;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
a{{text-decoration:none;color:inherit}}
img{{display:block;max-width:100%}}
.wrap{{max-width:1160px;margin:0 auto;padding:0 30px}}
.kick{{letter-spacing:.26em;text-transform:uppercase;font-size:.72rem;color:var(--teal);font-weight:600}}
.serif{{font-family:var(--h)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-family:var(--b);font-weight:600;font-size:.86rem;letter-spacing:.04em;padding:14px 28px;border-radius:4px;cursor:pointer;transition:.2s;border:1px solid var(--teal)}}
.btn-teal{{background:var(--teal);color:#fff}}
.btn-out{{background:transparent;color:var(--teal)}}
.btn-out:hover{{background:var(--teal);color:#fff}}
.btn-light{{background:#fff;color:var(--teal);border-color:#fff}}
.btn-glass{{background:rgba(255,255,255,.15);color:#fff;border-color:rgba(255,255,255,.5)}}
header{{position:fixed;top:0;left:0;right:0;z-index:50;background:rgba(255,255,255,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}}
header .bar{{display:flex;align-items:center;justify-content:space-between;height:76px}}
.brand{{font-family:var(--h);font-size:1.5rem;letter-spacing:.02em}}
header nav{{display:flex;gap:30px}}
header nav a{{font-weight:500;font-size:.9rem;color:var(--ink2);transition:.2s}}
header nav a:hover{{color:var(--teal)}}
.hero{{position:relative;min-height:100svh;display:flex;align-items:center;color:#fff}}
.hero-bg{{position:absolute;inset:0;background:url('{d["hero"]}') center/cover;z-index:0}}
.hero-bg::after{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,{p['ov1']},{p['ov2']})}}
.hero-inner{{position:relative;z-index:2;max-width:640px;padding-top:60px}}
.hero .kick{{color:{p['heroκick'] if False else p['herokick']};display:block;margin-bottom:20px}}
.hero h1{{font-family:var(--h);font-size:clamp(2.4rem,7vw,5.4rem);line-height:1.04;margin-bottom:22px}}
.hero p{{font-size:1.12rem;color:rgba(255,255,255,.9);max-width:500px;margin-bottom:32px}}
.hero-cta{{display:flex;gap:12px;flex-wrap:wrap}}
.badge{{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.4);padding:7px 15px;border-radius:40px;font-size:.82rem;margin-bottom:20px}}
.intro{{padding:100px 0;text-align:center;background:var(--cream)}}
.intro .kick{{display:block;margin-bottom:16px}}
.intro h2{{font-family:var(--h);font-size:clamp(2rem,4.4vw,3.2rem);line-height:1.2;max-width:22ch;margin:0 auto 18px}}
.intro p{{color:var(--ink2);max-width:640px;margin:0 auto}}
.serv{{padding:100px 0}}
.sec-h{{text-align:center;max-width:640px;margin:0 auto 54px}}
.sec-h .kick{{display:block;margin-bottom:12px}}
.sec-h h2{{font-family:var(--h);font-size:clamp(2rem,4.4vw,3.2rem);line-height:1.15}}
.serv-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}}
.serv-c{{text-align:center;padding:34px 22px;border:1px solid var(--line);border-radius:6px;transition:.25s}}
.serv-c:hover{{border-color:var(--teal);box-shadow:0 18px 40px rgba(0,0,0,.08);transform:translateY(-5px)}}
.serv-c .ic{{width:64px;height:64px;margin:0 auto 16px;background:var(--soft);color:var(--teal);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.7rem}}
.serv-c h3{{font-family:var(--h);font-size:1.3rem;margin-bottom:8px}}
.serv-c p{{color:var(--ink2);font-size:.92rem}}
.split{{padding:0 0 100px}}
.split-grid{{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}}
.split-img{{width:100%;height:520px;object-fit:cover;border-radius:6px;background:var(--soft) url('{d["split"]}') center/cover}}
.split-txt .kick{{display:block;margin-bottom:14px}}
.split-txt h2{{font-family:var(--h);font-size:clamp(1.9rem,3.8vw,2.8rem);margin-bottom:18px;line-height:1.2}}
.split-txt p{{color:var(--ink2);margin-bottom:14px}}
.split-list{{list-style:none;margin-top:14px}}
.split-list li{{display:flex;gap:12px;align-items:center;margin-bottom:11px;font-weight:500}}
.split-list .ck{{width:26px;height:26px;flex:0 0 26px;background:var(--teal);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.8rem}}
.pricing{{padding:100px 0;background:var(--cream)}}
.price-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.price-c{{background:#fff;border:1px solid var(--line);border-radius:8px;padding:40px 30px;text-align:center;transition:.25s}}
.price-c.feat{{background:var(--dark);color:#fff;border-color:var(--dark)}}
.price-c:hover{{transform:translateY(-6px);box-shadow:0 22px 48px rgba(0,0,0,.12)}}
.price-c h3{{font-family:var(--h);font-size:1.5rem;margin-bottom:6px}}
.price-c .amt{{font-family:var(--h);font-size:2.6rem;color:var(--teal);margin:10px 0}}
.price-c.feat .amt{{color:var(--gold)}}
.price-c ul{{list-style:none;margin:18px 0 26px;text-align:left}}
.price-c li{{padding:8px 0;border-bottom:1px solid var(--line);font-size:.92rem;color:var(--ink2)}}
.price-c.feat li{{border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.82)}}
.reviews{{padding:100px 0}}
.rv-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.rv{{background:var(--soft);border-radius:8px;padding:32px}}
.rv .st{{color:var(--gold);letter-spacing:2px;margin-bottom:12px}}
.rv p{{font-family:var(--h);font-size:1.08rem;color:var(--ink);margin-bottom:16px;line-height:1.5}}
.rv b{{font-weight:600;font-size:.9rem}}
.contact{{padding:100px 0;background:var(--cream)}}
.contact-grid{{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}}
.contact-info p{{margin-bottom:10px;color:var(--ink2)}}
.hours-t{{width:100%;border-collapse:collapse;margin-top:10px}}
.hours-t td{{padding:9px 0;border-bottom:1px solid var(--line);font-size:.94rem}}
.hours-t td:last-child{{text-align:right;color:var(--ink2)}}
.map-embed{{width:100%;height:340px;border:0;border-radius:8px}}
.cta{{position:relative;padding:120px 0;text-align:center;color:#fff}}
.cta-bg{{position:absolute;inset:0;background:url('{d["cta"]}') center/cover;z-index:0}}
.cta-bg::after{{content:"";position:absolute;inset:0;background:{p['ctaov']}}}
.cta .wrap{{position:relative;z-index:2}}
.cta h2{{font-family:var(--h);font-size:clamp(2.2rem,5vw,3.6rem);margin-bottom:14px}}
.cta p{{max-width:520px;margin:0 auto 28px;color:rgba(255,255,255,.9)}}
.cta .btns{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}}
footer{{background:var(--dark);color:rgba(255,255,255,.75);padding:60px 0 36px}}
.foot-grid{{display:grid;grid-template-columns:2fr 1fr 1fr;gap:40px;margin-bottom:38px}}
.foot-grid .brand{{color:#fff;margin-bottom:12px}}
.foot-grid h4{{font-family:var(--b);font-weight:600;letter-spacing:.12em;text-transform:uppercase;font-size:.74rem;color:{p['herokick']};margin-bottom:12px}}
.foot-grid p,.foot-grid a{{font-size:.92rem;line-height:1.9;color:rgba(255,255,255,.75)}}
.foot-bot{{border-top:1px solid rgba(255,255,255,.14);padding-top:22px;font-size:.82rem;color:rgba(255,255,255,.5);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}}
.mbar{{display:none}}
@media(max-width:920px){{
  .serv-grid{{grid-template-columns:1fr 1fr}}
  .split-grid,.contact-grid{{grid-template-columns:1fr;gap:30px}}
  .split-img{{height:340px}}
  .price-grid,.rv-grid{{grid-template-columns:1fr}}
}}
@media(max-width:560px){{
  html,body{{max-width:100vw;overflow-x:hidden}}
  header nav{{display:none}}
  .wrap{{padding:0 20px}}
  .serv-grid{{grid-template-columns:1fr}}
  .hero h1{{font-size:2.2rem}}
  .sec-h h2,.intro h2{{font-size:1.9rem}}
  body{{padding-bottom:66px}}
  .btn{{font-size:.9rem;padding:14px 20px}}
  .hero-cta .btn{{flex:1}}
  .mbar{{display:flex;position:fixed;bottom:0;left:0;right:0;z-index:60;background:#fff;border-top:1px solid var(--line)}}
  .mbar a{{flex:1;text-align:center;padding:15px 8px;font-weight:600;font-size:.95rem}}
  .mbar .call{{color:var(--teal)}}
  .mbar .book{{background:var(--green);color:#fff}}
}}
</style>
</head>
<body>
<header>
  <div class="wrap bar">
    <a href="#top" class="brand">{e(d["brand"])}</a>
    <nav>
      <a href="#servizi">Servizi</a>
      <a href="#centro">Chi siamo</a>
      <a href="#prezzi">Listino</a>
      <a href="#contatti">Contatti</a>
    </nav>
    <a href="#contatti" class="btn btn-out">Contattaci</a>
  </div>
</header>
<section id="top" class="hero">
  <div class="hero-bg"></div>
  <div class="wrap"><div class="hero-inner">
    <span class="badge">★ {d["rating"]} · {d["nrev"]} recensioni Google</span>
    <h1>{e(d["h1"])}</h1>
    <p>{e(d["herop"])}</p>
    <div class="hero-cta">
      <a href="tel:{d["tel"]}" class="btn btn-light">📞 {e(d["phone"])}</a>
      {hero_cta_wa}
    </div>
  </div></div>
</section>
<section class="intro">
  <div class="wrap">
    <span class="kick">Benvenuti</span>
    <h2>{e(d["introh"])}</h2>
    <p>{e(d["introp"])}{intro_extra}</p>
  </div>
</section>
<section id="servizi" class="serv">
  <div class="wrap">
    <div class="sec-h"><span class="kick">I nostri servizi</span><h2>{e(d["servh"])}</h2></div>
    <div class="serv-grid">{serv}</div>
  </div>
</section>
<section id="centro" class="split">
  <div class="wrap split-grid">
    <div class="split-img" role="img" aria-label="{e(d['name'])}"></div>
    <div class="split-txt">
      <span class="kick">Chi siamo</span>
      <h2>{e(d["splith"])}</h2>
      <p>{e(d["splitp"])}</p>
      <ul class="split-list">
        {"".join(f'<li><span class="ck">✓</span> {e(x)}</li>' for x in d["splitlist"])}
      </ul>
    </div>
  </div>
</section>
<section id="prezzi" class="pricing">
  <div class="wrap">
    <div class="sec-h"><span class="kick">Listino</span><h2>Trattamenti e prezzi</h2></div>
    <div class="price-grid">{price}</div>
    <p style="text-align:center;color:var(--sub);margin-top:22px;font-size:.9rem">Prezzi indicativi. Contattaci per un preventivo personalizzato.</p>
  </div>
</section>
{revsec}
<section id="contatti" class="contact">
  <div class="wrap">
    <div class="sec-h"><span class="kick">Dove siamo</span><h2>Vieni a trovarci</h2></div>
    <div class="contact-grid">
      <div class="contact-info">
        <p><strong>{e(d["name"])}</strong></p>
        <p>📍 {e(d["address"])}</p>
        <p>📞 <a href="tel:{d["tel"]}">{e(d["phone"])}</a></p>
        {"<p>💬 <a href='"+wa_link+"'>Scrivici su WhatsApp</a></p>" if wa_link else ""}
        {"<p>✉️ <a href='mailto:"+d['email']+"'>"+e(d['email'])+"</a></p>" if d.get("email") else ""}
        <p style="margin-top:16px"><a href="https://maps.google.com/?cid={d['cid']}" target="_blank" class="btn btn-out">Apri in Google Maps</a></p>
        <table class="hours-t">{hrows}</table>
      </div>
      <div>
        <iframe class="map-embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={d['maps_q']}&output=embed"></iframe>
      </div>
    </div>
  </div>
</section>
<section class="cta">
  <div class="cta-bg"></div>
  <div class="wrap">
    <h2>Prenota il tuo appuntamento</h2>
    <p>Chiamaci o scrivici: saremo felici di accoglierti.</p>
    <div class="btns">
      <a href="tel:{d["tel"]}" class="btn btn-light">📞 {e(d["phone"])}</a>
      {cta_wa}
    </div>
  </div>
</section>
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div><div class="brand" style="color:#fff">{e(d["brand"])}</div><p>{e(d["cat"])} a Castel d'Azzano (VR).</p></div>
      <div><h4>Contatti</h4><p>{e(d["address"])}<br><a href="tel:{d["tel"]}">{e(d["phone"])}</a>{email_line}</p></div>
      <div><h4>Orari</h4><p>{"<br>".join(e(h[0])+": "+e(h[1]) for h in d["hours"])}</p></div>
    </div>
    <div class="foot-bot"><span>© {e(d["name"])} — Castel d'Azzano (VR)</span><span>Sito realizzato da HubTec</span></div>
  </div>
</footer>
<div class="mbar">
  <a href="tel:{d["tel"]}" class="call">📞 Chiama</a>
  {mbar_wa}
</div>
</body>
</html>'''
print("gen loaded ok")
