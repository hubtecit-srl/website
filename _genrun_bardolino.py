# -*- coding: utf-8 -*-
import json
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
BASE="https://hubtecit-srl.github.io/website/"
def photo(ref,w=1400):
    return "https://maps.googleapis.com/maps/api/place/photo?maxwidth=%d&photo_reference=%s&key=%s"%(w,ref,KEY)

stock=json.load(open("/tmp/hub_1784637408/stock-library.json"))["estetiste"]

PAL={
 "v0":dict(cream="#f7f1ec",cream2="#f2e9e1",blush="#f4e7e2",blush2="#efdcd6",tan="#a5825a",tand="#876a41",brown="#2b2320",sub="#7c7067",line="#e6dcd2",fl="✿"),
 "v1":dict(cream="#f7f0f2",cream2="#f1e6ea",blush="#f0e0e6",blush2="#e8d2da",tan="#b07a88",tand="#8f5f6b",brown="#2c2226",sub="#7d6a70",line="#ecdae0",fl="✦"),
 "v2":dict(cream="#f1f4ef",cream2="#e8ede4",blush="#e4ece1",blush2="#d6e0d1",tan="#7d9471",tand="#5f7355",brown="#232a22",sub="#68746331"[:7],line="#dce6d6",fl="❀"),
}
PAL["v2"]["sub"]="#687463"

def stars(n): return "★"*int(round(n))

def hours_html(hours):
    out=[]
    for d,lab,txt in hours:
        out.append('<li data-day="%d"><span class="d">%s</span><span>%s</span></li>'%(d,lab,txt))
    return "\n          ".join(out)

def periods_js(hours_ranges):
    # hours_ranges: dict day-> list of [start,end] or None
    return json.dumps(hours_ranges)

def svc_html(svcs):
    rom=["i","ii","iii","iv","v","vi"]
    out=[]
    for i,(t,d) in enumerate(svcs):
        out.append('<div class="svc"><div class="n">%s</div><h3>%s</h3><p>%s</p></div>'%(rom[i],t,d))
    return "\n      ".join(out)

def mini_html(revs):
    out=[]
    for txt,who in revs:
        out.append('<div class="mini"><div class="stars">★★★★★</div><p>“%s”</p><b>%s</b></div>'%(txt,who))
    return "\n      ".join(out)

def build(c):
    p=PAL[c["pal"]]
    heroimg=c["hero"]; bandimg=c["band"]; aboutimg=c["about"]
    badge = ""
    if c.get("rating") and c["rating"]>=4.2:
        badge='<div class="badge"><svg viewBox="0 0 200 200"><defs><path id="cp" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/></defs><text font-family="Jost" font-size="12" letter-spacing="3" fill="%s"><textPath href="#cp" startOffset="0%%">· RECENSIONI GOOGLE · %s · </textPath></text></svg><div class="c">%s<small>★ %d REC.</small></div></div>'%(p["tan"],c["name"].upper(),str(c["rating"]).replace(".",","),c["reviews_total"])
        badge_h2='Un ambiente accogliente e curato, dove ogni trattamento nasce da passione, gentilezza e prodotti di qualità.'
    else:
        badge='<div class="badge2">'+p["fl"]+'</div>'
        badge_h2='Un ambiente accogliente e curato, dove ci si sente subito a casa: gentilezza, pulizia e trattamenti fatti con passione.'
    tel=c["tel"]; telhref="tel:+39"+tel.replace(" ","")
    mobbtns=c["mobile_bar"]
    socials=c.get("socials","")
    reviews_link='<div style="text-align:center;margin-top:26px"><a href="%s" target="_blank" rel="noopener" style="color:%s;border-bottom:1px solid %s;padding-bottom:2px;font-size:.92rem">Tutte le recensioni su Google →</a></div>'%(c["cid"],p["tan"],p["line"])
    html=f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{c["name"]} — Centro estetico a {c["comune"]}</title>
<meta name="description" content="{c["name"]}, centro estetico a {c["comune"]} (VR) in {c["address_short"]}. Trattamenti viso, corpo e benessere. Prenota il tuo momento di relax.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root{{
  --cream:{p["cream"]}; --cream2:{p["cream2"]}; --blush:{p["blush"]}; --blush2:{p["blush2"]}; --tan:{p["tan"]};
  --tan-d:{p["tand"]}; --brown:{p["brown"]}; --sub:{p["sub"]}; --line:{p["line"]}; --white:#fff;
  --serif:'Playfair Display',Georgia,serif; --sans:'Jost',system-ui,sans-serif;
  --sh:0 24px 60px rgba(0,0,0,.12);
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--sans);color:var(--brown);background:var(--cream);line-height:1.75;font-weight:300;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
a{{text-decoration:none;color:inherit}}
img{{display:block;max-width:100%}}
.wrap{{max-width:1200px;margin:0 auto;padding:0 30px}}
.label{{font-family:var(--sans);font-weight:400;letter-spacing:.34em;text-transform:uppercase;font-size:.72rem;color:var(--tan)}}
header{{position:fixed;top:18px;left:0;right:0;z-index:60}}
.navpill{{max-width:1180px;margin:0 auto;background:rgba(255,255,255,.88);backdrop-filter:blur(12px);border-radius:60px;display:flex;align-items:center;justify-content:space-between;padding:12px 14px 12px 30px;box-shadow:0 10px 34px rgba(0,0,0,.08);border:1px solid rgba(255,255,255,.6)}}
.navpill nav{{display:flex;gap:26px}}
.navpill nav a{{font-size:.9rem;color:var(--brown);transition:.2s}}
.navpill nav a:hover{{color:var(--tan)}}
.brand{{position:absolute;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:8px;font-family:var(--serif);font-size:1.4rem;color:var(--brown)}}
.brand .fl{{color:var(--tan);font-size:1.05rem}}
.nav-right{{display:flex;align-items:center;gap:18px}}
.nav-tel{{font-size:.88rem;color:var(--brown);display:flex;align-items:center;gap:6px}}
.pill-cta{{background:var(--tan);color:#fff;padding:12px 24px;border-radius:50px;font-size:.85rem;display:inline-flex;align-items:center;gap:8px;transition:.25s}}
.pill-cta:hover{{background:var(--tan-d)}}
.menu-toggle{{display:none;background:none;border:0;font-size:1.4rem;color:var(--brown);cursor:pointer}}
.hero{{position:relative;height:100vh;height:100svh;min-height:600px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;overflow:hidden}}
.hero-bg{{position:absolute;inset:0;background:url('{heroimg}') center/cover no-repeat}}
.hero-bg::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,15,15,.42),rgba(20,15,15,.4))}}
.hero-inner{{position:relative;z-index:2;padding:0 20px}}
.hero .label{{color:rgba(255,255,255,.9);margin-bottom:20px}}
.hero h1{{font-family:var(--serif);font-weight:500;font-size:clamp(2.6rem,7vw,5.4rem);line-height:1.05;margin-bottom:20px}}
.hero h1 em{{font-style:italic}}
.hero p{{font-size:1.12rem;max-width:520px;margin:0 auto 30px;color:rgba(255,255,255,.92);font-weight:300}}
.hero .pill-cta{{background:#fff;color:var(--brown)}}
.badge-sec{{background:var(--blush);text-align:center;padding:90px 0}}
.badge{{width:170px;height:170px;margin:0 auto 34px;position:relative;display:flex;align-items:center;justify-content:center}}
.badge svg{{position:absolute;inset:0;width:100%;height:100%;animation:spin 22s linear infinite}}
.badge2{{font-family:var(--serif);font-size:3rem;color:var(--tan);margin:0 auto 30px;width:96px;height:96px;border-radius:50%;background:var(--white);display:flex;align-items:center;justify-content:center;box-shadow:var(--sh)}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.badge .c{{font-family:var(--serif);font-size:2.6rem;color:var(--brown);position:relative;z-index:2}}
.badge .c small{{display:block;font-family:var(--sans);font-size:.7rem;letter-spacing:.2em;color:var(--tan);margin-top:-4px}}
.badge-sec h2{{font-family:var(--serif);font-weight:500;font-size:clamp(1.8rem,3.6vw,2.7rem);max-width:760px;margin:0 auto;line-height:1.25;color:var(--brown)}}
.band{{position:relative;height:70vh;min-height:460px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff}}
.band-bg{{position:absolute;inset:0;background:url('{bandimg}') center/cover no-repeat}}
.band-bg::after{{content:"";position:absolute;inset:0;background:rgba(20,15,15,.46)}}
.band p{{position:relative;z-index:2;font-family:var(--serif);font-weight:400;font-style:italic;font-size:clamp(1.5rem,3vw,2.3rem);max-width:820px;padding:0 24px;line-height:1.4}}
.about{{background:var(--cream);padding:110px 0}}
.about-grid{{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}}
.about-img img{{width:100%;height:560px;object-fit:cover;border-radius:26px}}
.about-txt .label{{margin-bottom:16px;display:block}}
.about-txt h2{{font-family:var(--serif);font-weight:500;font-size:clamp(2rem,4vw,3rem);line-height:1.15;margin-bottom:20px}}
.about-txt p{{color:var(--sub);margin-bottom:16px}}
.about-txt .sign{{font-family:var(--serif);font-style:italic;font-size:1.4rem;color:var(--tan);margin-top:6px}}
.services{{background:var(--cream2);padding:110px 0}}
.sec-h{{text-align:center;max-width:600px;margin:0 auto 56px}}
.sec-h h2{{font-family:var(--serif);font-weight:500;font-size:clamp(2rem,4vw,2.9rem);margin:12px 0;color:var(--brown)}}
.sec-h p{{color:var(--sub)}}
.svc-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.svc{{background:var(--white);border-radius:24px;padding:38px 32px;transition:.3s;border:1px solid var(--line)}}
.svc:hover{{transform:translateY(-6px);box-shadow:var(--sh)}}
.svc .n{{font-family:var(--serif);font-style:italic;font-size:1.3rem;color:var(--tan);margin-bottom:14px}}
.svc h3{{font-family:var(--serif);font-weight:500;font-size:1.4rem;margin-bottom:8px;color:var(--brown)}}
.svc p{{color:var(--sub);font-size:.95rem}}
.svc-note{{text-align:center;margin-top:30px;color:var(--sub);font-style:italic;font-family:var(--serif);font-size:1.2rem}}
.testi{{background:var(--cream);padding:110px 0}}
.testi-card{{background:var(--blush);border-radius:34px;padding:64px;max-width:1000px;margin:0 auto;position:relative}}
.testi-card .q{{font-family:var(--serif);font-size:5rem;color:var(--tan);line-height:.6;margin-bottom:10px}}
.testi-card blockquote{{font-family:var(--serif);font-weight:400;font-size:clamp(1.4rem,2.6vw,2rem);line-height:1.4;color:var(--brown);margin-bottom:26px}}
.testi-card .who b{{font-family:var(--sans);font-weight:500;color:var(--brown)}}
.testi-card .who span{{display:block;font-size:.82rem;color:var(--tan)}}
.mini-rev{{display:grid;grid-template-columns:1fr 1fr;gap:22px;max-width:1000px;margin:24px auto 0}}
.mini{{background:var(--white);border:1px solid var(--line);border-radius:22px;padding:26px}}
.mini .stars{{color:var(--tan);letter-spacing:2px;margin-bottom:8px;font-size:.9rem}}
.mini p{{color:var(--sub);font-size:.94rem;margin-bottom:10px}}
.mini b{{font-family:var(--sans);font-weight:500;font-size:.88rem}}
.contact{{background:var(--cream2);padding:110px 0}}
.contact-grid{{display:grid;grid-template-columns:1fr 1.1fr;gap:50px;align-items:stretch}}
.cinfo{{background:var(--white);border:1px solid var(--line);border-radius:26px;padding:40px}}
.cinfo h3{{font-family:var(--serif);font-weight:500;font-size:1.7rem;color:var(--brown);margin-bottom:6px}}
.open-badge{{display:inline-flex;align-items:center;gap:8px;font-size:.78rem;letter-spacing:.06em;padding:6px 14px;border-radius:40px;margin:12px 0 20px}}
.open-badge.open{{background:#e7f0e3;color:#5c7a4e}}
.open-badge.closed{{background:#f4e2dc;color:#a5674b}}
.open-badge .dot{{width:8px;height:8px;border-radius:50%;background:currentColor}}
.hours-list{{list-style:none}}
.hours-list li{{display:flex;justify-content:space-between;padding:11px 2px;border-bottom:1px solid var(--line);font-size:.95rem;color:var(--sub)}}
.hours-list li:last-child{{border-bottom:0}}
.hours-list li.today{{color:var(--brown);font-weight:500}}
.hours-list li.today .d{{color:var(--tan)}}
.crow{{display:flex;gap:14px;align-items:flex-start;padding:14px 0;border-top:1px solid var(--line)}}
.crow .ic{{width:40px;height:40px;flex:0 0 40px;background:var(--blush);color:var(--tan);border-radius:50%;display:flex;align-items:center;justify-content:center}}
.crow h4{{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--tan);font-weight:500;margin-bottom:2px}}
.crow a,.crow p{{color:var(--brown);font-size:1rem}}
.cinfo .pill-cta{{margin-top:22px}}
.map-wrap{{border-radius:26px;overflow:hidden;min-height:460px;box-shadow:var(--sh)}}
.map-wrap iframe{{width:100%;height:100%;min-height:460px;border:0}}
footer{{background:var(--brown);color:rgba(255,255,255,.75);padding:56px 0 26px;text-align:center}}
footer .brand{{position:static;transform:none;justify-content:center;color:#fff;margin-bottom:10px}}
.socials{{display:flex;gap:14px;justify-content:center;margin:18px 0}}
.socials a{{width:42px;height:42px;border-radius:50%;border:1px solid rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;color:#fff;transition:.25s}}
.socials a:hover{{background:var(--tan);border-color:var(--tan)}}
.foot-line{{border-top:1px solid rgba(255,255,255,.12);margin-top:22px;padding-top:18px;font-size:.82rem;opacity:.6}}
.foot-note{{font-size:.72rem;opacity:.45;margin-top:6px}}
.mobile-bar{{display:none}}
@media(max-width:960px){{
  .about-grid,.contact-grid{{grid-template-columns:1fr;gap:40px}}
  .svc-grid{{grid-template-columns:1fr 1fr}}
  .mini-rev{{grid-template-columns:1fr}}
  .navpill nav,.nav-tel{{display:none}}
  .menu-toggle{{display:block}}
  .brand{{position:static;transform:none}}
}}
@media(max-width:560px){{
  .wrap{{padding:0 18px}}
  section,.about,.services,.testi,.contact,.badge-sec{{padding:64px 0}}
  .svc-grid{{grid-template-columns:1fr}}
  .testi-card{{padding:34px 22px}}
  .hero{{min-height:86svh}}
  .hero h1{{font-size:2.4rem}}
  .hero p{{font-size:1rem}}
  .hero .pill-cta{{width:100%;justify-content:center}}
  .about-img img{{height:340px}}
  .cinfo .pill-cta{{width:100%;justify-content:center}}
  .map-wrap,.map-wrap iframe{{min-height:320px}}
  .badge{{width:150px;height:150px}}
  .band{{min-height:380px}}
  .mobile-bar{{display:flex;position:fixed;bottom:0;left:0;right:0;z-index:70}}
  .mobile-bar a{{flex:1;text-align:center;padding:15px 6px;font-size:.9rem;color:#fff;letter-spacing:.02em}}
  .mobile-bar .mb-call{{background:var(--tan-d)}}
  .mobile-bar .mb-alt{{background:var(--tan)}}
  body{{padding-bottom:54px}}
}}
</style>
</head>
<body>
<header>
  <div class="navpill">
    <nav>
      <a href="#chi">Chi siamo</a>
      <a href="#trattamenti">Trattamenti</a>
      <a href="#recensioni">Recensioni</a>
      <a href="#contatti">Contatti</a>
    </nav>
    <a href="#" class="brand"><span class="fl">{p["fl"]}</span>{c["name"]}</a>
    <div class="nav-right">
      <span class="nav-tel">\U0001F4DE {tel}</span>
      <a href="{telhref}" class="pill-cta">Prenota ›</a>
      <button class="menu-toggle" onclick="document.querySelector('.navpill nav').scrollIntoView()">☰</button>
    </div>
  </div>
</header>
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-inner">
    <div class="label">Centro estetico · {c["comune"]}</div>
    <h1>{c["hero_h1"]}</h1>
    <p>{c["hero_p"]}</p>
    <a href="{telhref}" class="pill-cta">Prenota il tuo trattamento ›</a>
  </div>
</section>
<section class="badge-sec">
  <div class="wrap">
    {badge}
    <h2>{badge_h2}</h2>
  </div>
</section>
<section class="band">
  <div class="band-bg"></div>
  <p>“{c["band"]==bandimg and c["band_quote"] or c["band_quote"]}”</p>
</section>
<section class="about" id="chi">
  <div class="wrap about-grid">
    <div class="about-img"><img loading="lazy" src="{aboutimg}" alt="{c["name"]}"></div>
    <div class="about-txt">
      <span class="label">Chi siamo</span>
      <h2>{c["about_h2"]}</h2>
      {c["about_p"]}
      <div class="sign">— {c["about_sign"]}</div>
    </div>
  </div>
</section>
<section class="services" id="trattamenti">
  <div class="wrap">
    <div class="sec-h">
      <span class="label">I trattamenti</span>
      <h2>{c["svc_h2"]}</h2>
      <p>{c["svc_p"]}</p>
    </div>
    <div class="svc-grid">
      {svc_html(c["svcs"])}
    </div>
    <p class="svc-note">Prezzi onesti e trasparenti — chiamaci per il listino completo.</p>
  </div>
</section>
<section class="testi" id="recensioni">
  <div class="wrap">
    <div class="testi-card">
      <div class="q">&ldquo;</div>
      <blockquote>{c["hero_review"][0]}</blockquote>
      <div class="who"><div><b>{c["hero_review"][1]}</b><span>Recensione Google · ★★★★★</span></div></div>
    </div>
    <div class="mini-rev">
      {mini_html(c["mini_reviews"])}
    </div>
    {reviews_link}
  </div>
</section>
<section class="contact" id="contatti">
  <div class="wrap">
    <div class="sec-h"><span class="label">Dove siamo</span><h2>Orari &amp; Contatti</h2></div>
    <div class="contact-grid">
      <div class="cinfo">
        <h3>Orari di apertura</h3>
        <div id="openBadge" class="open-badge closed"><span class="dot"></span><span id="openText">—</span></div>
        <ul class="hours-list" id="hoursList">
          {hours_html(c["hours"])}
        </ul>
        <div class="crow"><div class="ic">◍</div><div><h4>Indirizzo</h4><a href="{c["cid"]}" target="_blank" rel="noopener">{c["address_full"]}</a></div></div>
        <div class="crow"><div class="ic">☎</div><div><h4>Telefono</h4><a href="{telhref}">{tel}</a></div></div>
        <a href="{telhref}" class="pill-cta">Prenota il tuo trattamento ›</a>
      </div>
      <div class="map-wrap"><iframe loading="lazy" allowfullscreen src="https://www.google.com/maps?q={c["map_q"]}&output=embed"></iframe></div>
    </div>
  </div>
</section>
<footer>
  <div class="wrap">
    <div class="brand"><span class="fl">{p["fl"]}</span>{c["name"]}</div>
    <div class="socials">
      <a href="{telhref}" title="Telefono">☎</a>
      <a href="{c["cid"]}" target="_blank" rel="noopener" title="Mappa">◍</a>
      {socials}
    </div>
    <div class="foot-line">© 2026 {c["name"]} · {c["address_full"]} · P.IVA da inserire</div>
    <div class="foot-note">Sito dimostrativo realizzato da HubTec — bozza a scopo di proposta commerciale.</div>
  </div>
</footer>
<div class="mobile-bar">{mobbtns}</div>
<script>
document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{{const t=document.querySelector(a.getAttribute('href'));if(t){{e.preventDefault();t.scrollIntoView({{behavior:'smooth'}})}}}}));
const periods={periods_js(c["periods"])};
const now=new Date(),day=now.getDay(),hm=now.getHours()*100+now.getMinutes();
document.querySelectorAll('#hoursList li').forEach(li=>{{if(+li.dataset.day===day)li.classList.add('today')}});
const pr=periods[day],badge=document.getElementById('openBadge'),txt=document.getElementById('openText');
let open=false;if(pr){{for(const r of pr){{if(hm>=r[0]&&hm<r[1])open=true;}}}}
if(open){{badge.className='open-badge open';txt.textContent='Aperto ora';}}else{{badge.className='open-badge closed';txt.textContent='Chiuso ora';}}
</script>
</body>
</html>'''
    return html

# ---------- LEAD CONFIGS ----------
L_laura=[stock[3],stock[5],stock[7],stock[9]]  # fallback (unused, has real)
laura_photos=[
 "AWCwydilekRirouelWRBhJXUfxnLYnivarISOxuFAqdmelwOvENHwrasPAveviNiWaz2CF6iASy8M3_JX9xfOAwTqCurhJhe_Ol5lB0OuPqLq9wUbURC0OKfh7DlpYfS-lycGpBunUsZaKvdg7HgZhncrEbbMOPvjMrQSO6dfw5aTPLm20HFunhraolTEkZstdjE8FZY8eWrB2tevILXzWcHZsoH5cMNRh34kGFTLOf_0ZUBxv3hQEX6h4C-0ObS3_QiuaLZkdyag92q3QNfau9JTwqHhtaAbDaPMFNqmfx1D1g-bXE_qXik_G5EsqjLbuy0yST3_m3eCKsyh4zLeOU12zO_yMFaeYTJv99ZQH8X809cBWwayhNICOs8HdT1UxVYohLlbHIHmQOa3SDZYHD--8p5XX3fgICgdl20bynHDISrOmaS",
 "AWCwydiYT5dfKqF7MMivdcR8tBDqJD6Ax3LtxoSrBWIVNjY27dUqrDBbGVsUTBXmW22TE9Bsza-3S2_oyq_onfaIJpBEkdmqyLspK4kPqMSG2aX7fuPIzVHzAvXEqJI0vgI4im9Zq9ViOcNrL47Z2oK4yUBXXsMLdMegSPkMjLKM3zHrp4UOH6l-aOdcaBPJQvvoeNPI0XDRo1tNhuHeleUpbwEKhwlnRqJ8iYCk-z89GZYTeWLQN4t7Tlc0h9KASDOHGQFDJu-ZDaLOAhrwoubsfJijqJC5DHkPR7s_oB_gqqZvxdLm9ypTd1DjphXWklaQ_gREzvsywJ_dlQVjQ5G_GB1nwGsDTT_Rtul0-ciGnheQVtMhPwCDE96btSuM-krNl-iEOQe85e7Lo0lrlD9hRmNbJt10PpkNg-pRC7bGJUt7VAf0",
 "AWCwydj1I2NV2gNjkM-xdeue_nUzpmdL31_SPUas70dNFs9nNJEfwq6pRT86I0mgxT17apLwLNbIgl7mptdqcLjeQ3dSzVmXDvqOP3EtobcJwtbvIqUGqG9agTHifFX5noaK6-8tLE6j5Z-JDciJ5f5hgyrI5W7J5JXa9E1q_wmCtv3-nzxHxhRoz5XGZQ85FxjKdwbJzBFnYN-NPx0P33G9Y-X_eJZl_KF3Mr5fD6abRAt5ei2LVjB8ako9qF2P9cMuX1qBvP35BIS9Ws7H9cJYgg3fFK0tB7Nvj7Cl5GUt2pV0blb_UhKWMGml8nkjSANO2CKGAlwAOGWoEdtWqyQlTje8Vk3aPPm8ueEHbJ1tMVYKvFI3E4FNeMLng1LeRg00ohiX4QUoipNXVArzSfoKjoN-TAHxxmnQFYvmffhFaqnncBgy",
]
laura=dict(pal="v0",slug="estetica-laura-bardolino",name="Estetica Laura",comune="Bardolino",zona="Centro",
 address_short="Via Palestro 15",address_full="Via Palestro 15, 37011 Bardolino (VR)",
 map_q="Via+Palestro+15,+37011+Bardolino+VR",
 tel="351 809 7016",cid="https://maps.google.com/?cid=8175647460457244655",
 rating=3.7,reviews_total=6,
 hero=photo(laura_photos[0],1600),band=photo(laura_photos[1],1600),about=photo(laura_photos[2],900),
 hero_h1="Il tuo momento<br><em>di bellezza</em>",
 hero_p="Un angolo di benessere a Bardolino, dove ceretta, unghie e trattamenti diventano un piccolo rito di coccole.",
 band_quote="La tua estetista di fiducia ti aspetta a Bardolino. Il tuo momento di relax è pronto: manca solo che tu venga a trovarci.",
 about_h2="Cura, pulizia<br>e mani esperte",
 about_p="<p>Da Estetica Laura, in Via Palestro a Bardolino, ti accogliamo in un ambiente pulito e curato dove ci si sente subito a proprio agio. Le nostre clienti apprezzano la puntualità e la cura in ogni dettaglio.</p><p>Ceretta, manicure e pedicure con semipermanente, trattamenti viso: ti seguiamo con attenzione per farti sentire al meglio.</p>",
 about_sign="coccole vere, ogni volta",
 svc_h2="I nostri servizi",svc_p="Ceretta, unghie e cura del viso, con professionalità e prodotti di qualità.",
 svcs=[("Ceretta","Epilazione con cera per gambe, viso e corpo, con mano delicata e attenzione alla pelle."),
       ("Manicure & Pedicure","Cura di mani e piedi con applicazione di smalto semipermanente, preciso e duraturo."),
       ("Ricostruzione unghie","Unghie sempre in ordine con ricostruzione e refill su misura."),
       ("Trattamenti viso","Pulizia e trattamenti idratanti personalizzati, anche per pelli sensibili."),
       ("Trattamenti corpo","Percorsi di benessere per ritrovare leggerezza e relax."),
       ("Consulenza","Consigli sinceri sul percorso più adatto a te: qui la cliente viene coccolata.")],
 hero_review=("Le ragazze sono fantastiche, il locale è molto pulito e sono molto puntuali! Servizio strepitoso!","Federica L"),
 mini_reviews=[("Servizio di ceretta fantastico!","Laura Thomas"),("Brava Sara, sempre precisa e gentile.","Simona Bonaretti")],
 hours=[(1,"Lunedì","09:00 – 19:00"),(2,"Martedì","09:00 – 19:00"),(3,"Mercoledì","09:00 – 19:00"),(4,"Giovedì","09:00 – 19:00"),(5,"Venerdì","09:00 – 20:00"),(6,"Sabato","09:00 – 19:00"),(0,"Domenica","Chiuso")],
 periods={"1":[[900,1900]],"2":[[900,1900]],"3":[[900,1900]],"4":[[900,1900]],"5":[[900,2000]],"6":[[900,1900]],"0":None},
 socials='<a href="https://www.instagram.com/esteticalaurabardolino_/" target="_blank" rel="noopener" title="Instagram">◉</a>',
 mobile_bar='<a class="mb-call" href="tel:+393518097016">☎ Chiama</a><a class="mb-alt" href="https://wa.me/393518097016" target="_blank" rel="noopener">💬 WhatsApp</a>')

antonella=dict(pal="v1",slug="estetica-antonella-bardolino",name="Estetica Antonella",comune="Bardolino",zona="Centro",
 address_short="Via G. F. Marzan 1",address_full="Via Giovanni Federico Marzan 1, 37011 Bardolino (VR)",
 map_q="Via+Giovanni+Federico+Marzan+1,+37011+Bardolino+VR",
 tel="045 621 2001",cid="https://maps.google.com/?cid=7795170496146589581",
 rating=4.4,reviews_total=10,
 hero=stock[0],band=stock[2],about=stock[3],
 hero_h1="La bellezza<br><em>su misura per te</em>",
 hero_p="A Bardolino, la professionalità e la cura di Antonella per trattamenti viso e corpo che ti fanno sentire davvero seguita.",
 band_quote="Non conta solo la location, ma la professionalità di chi ti segue. Da Estetica Antonella uscirai sempre soddisfatta.",
 about_h2="Professionalità<br>e vera competenza",
 about_p="<p>Estetica Antonella di Barcella Antonella è un punto di riferimento a Bardolino da tanti anni. Un ambiente estremamente pulito e accogliente, dove ogni cliente viene seguito con competenza e attenzione.</p><p>Chi ci sceglie apprezza soprattutto la professionalità e la sincerità dei consigli: qui la cura della persona viene prima di tutto.</p>",
 about_sign="competenza che si sente",
 svc_h2="Trattamenti viso e corpo",svc_p="Rituali di bellezza personalizzati, con mano esperta e prodotti di qualità.",
 svcs=[("Trattamenti viso","Pulizia del viso e trattamenti idratanti su misura, delicati anche sulle pelli sensibili."),
       ("Trattamenti corpo","Percorsi di benessere e cura del corpo per ritrovare tonicità e leggerezza."),
       ("Ceretta","Epilazione professionale con attenzione e delicatezza in ogni zona."),
       ("Manicure & Pedicure","Cura di mani e piedi con smalto tradizionale e semipermanente."),
       ("Sopracciglia","Definizione dello sguardo con ritocco e cura delle sopracciglia."),
       ("Consulenza","Consigli sinceri e trattamenti su misura, pensati davvero per te.")],
 hero_review=("La Signora Antonella è molto professionale, competente ed accogliente. Location estremamente pulita. Se cercate professionalità, andateci pure: resterete soddisfatti!","Fortuna Laganà"),
 mini_reviews=[("Troppo brava. Bravissima!","Dora Tommasini"),("Sempre un ottimo servizio, mi trovo benissimo.","Marianna Ragno")],
 hours=[(1,"Lunedì","Chiuso"),(2,"Martedì","09:00 – 13:00 / 15:00 – 19:00"),(3,"Mercoledì","09:00 – 13:00 / 15:00 – 19:00"),(4,"Giovedì","09:00 – 13:00 / 15:00 – 19:00"),(5,"Venerdì","09:00 – 13:00 / 15:00 – 19:00"),(6,"Sabato","Su appuntamento"),(0,"Domenica","Chiuso")],
 periods={"1":None,"2":[[900,1300],[1500,1900]],"3":[[900,1300],[1500,1900]],"4":[[900,1300],[1500,1900]],"5":[[900,1300],[1500,1900]],"6":None,"0":None},
 socials='',
 mobile_bar='<a class="mb-call" href="tel:+390456212001">☎ Chiama</a><a class="mb-alt" href="https://maps.google.com/?cid=7795170496146589581" target="_blank" rel="noopener">◍ Come arrivare</a>')

caldana_photo="AWCwydjZq7duPrhPzArOiV0yM4KxrX-lpuOkw75K5FRtLZd5Z3R81IOCwn3aZMRYuHLuiSxJVRDC1e4-I5HXUGRTILQISADdwgtKOYTBX-DIyRP9qzryL-LN6IU0AzjrNKiDhYcGQl0JMHVIDsKnY97HRpyxUVD2kabhZLmFSm80dUkNFI03BvHUcwgk4DxItVWNMDsFjFDd7Euug6UwpvutqhImujQHoZn7eUVv--RglspHrhmh48unJjSphhqqnoBEJW_I3B-OWb1NAdSN9ZaNsMnN4tb2IWqf57ENpPrQvaJIDsiIYxmyrAzWZ279fYUA1W_3Y2UpOtZELEsL62Ilzm-eDsFrE5BstJmHQtnADpHkE-CCTyf1V3ecNBQrVyTDyeDIxUmXK17nc0N6wFse-VWuRGEF6F9H51kxCTHVNKzUfA"
caldana=dict(pal="v2",slug="estetica-giuliana-caldana-calmasino",name="Estetica Giuliana Caldana",comune="Bardolino",zona="Calmasino",
 address_short="Via Chiesa 1, Calmasino",address_full="Via Chiesa 1, 37011 Calmasino di Bardolino (VR)",
 map_q="Via+Chiesa+1,+37011+Calmasino+VR",
 tel="045 626 0308",cid="https://maps.google.com/?cid=14152060109842468268",
 rating=4.6,reviews_total=11,
 hero=photo(caldana_photo,1600),band=stock[5],about=photo(caldana_photo,900),
 hero_h1="Benessere del corpo<br><em>e della mente</em>",
 hero_p="A Calmasino di Bardolino, i massaggi e i trattamenti di Giuliana per riequilibrare corpo e mente in un ambiente accogliente.",
 band_quote="Un tocco sano per il corpo e per la mente. Da Giuliana il benessere è un percorso fatto di ascolto e passione.",
 about_h2="Un tocco sano,<br>per corpo e mente",
 about_p="<p>Estetica Giuliana Caldana, a Calmasino di Bardolino, è molto più di un centro estetico: un luogo accogliente e rilassante dove ritrovare equilibrio, tra estetica, massaggi e benessere.</p><p>Giuliana trasmette con delicatezza la passione per la naturopatia e la psicosomatica, per prendersi cura della persona nella sua interezza.</p>",
 about_sign="ascolto, delicatezza, passione",
 svc_h2="Estetica &amp; benessere",svc_p="Trattamenti estetici e massaggi per riequilibrare corpo e mente.",
 svcs=[("Massaggi","Massaggi rilassanti e su misura, un tocco sano per il corpo e la mente."),
       ("Trattamenti viso","Pulizia e trattamenti personalizzati per una pelle luminosa e curata."),
       ("Trattamenti corpo","Percorsi di benessere per ritrovare leggerezza, tonicità e relax."),
       ("Naturopatia","Un approccio naturale al benessere, con ascolto e consigli su misura."),
       ("Ceretta & Estetica","I servizi estetici di sempre, con delicatezza e professionalità."),
       ("Riequilibrio","Percorsi che uniscono corpo e mente, per ritrovare il tuo equilibrio.")],
 hero_review=("Giuliana mi ha conquistata: gentile, simpatica e molto professionale. Il suo massaggio è stato un tocco sano per il mio corpo e la mia mente!","Barbara Ramos"),
 mini_reviews=[("Professionale! Trasmette con delicatezza la passione per la naturopatia. Ambiente accogliente e rilassante.","Alessandro Bianco"),("Gentile e lavora con grande professionalità.","Christiane Vollmer")],
 hours=[(1,"Lunedì","Chiuso"),(2,"Martedì","08:00 – 17:00"),(3,"Mercoledì","08:00 – 17:00"),(4,"Giovedì","08:00 – 17:00"),(5,"Venerdì","08:00 – 17:00"),(6,"Sabato","08:00 – 12:00"),(0,"Domenica","Chiuso")],
 periods={"1":None,"2":[[800,1700]],"3":[[800,1700]],"4":[[800,1700]],"5":[[800,1700]],"6":[[800,1200]],"0":None},
 socials='',
 mobile_bar='<a class="mb-call" href="tel:+390456260308">☎ Chiama</a><a class="mb-alt" href="https://maps.google.com/?cid=14152060109842468268" target="_blank" rel="noopener">◍ Come arrivare</a>')

leads=[laura,antonella,caldana]
for c in leads:
    html=build(c)
    open("/tmp/hub_1784637408/%s.html"%c["slug"],"w",encoding="utf-8").write(html)
    print("WROTE %s.html  %d bytes"%(c["slug"],len(html)))
