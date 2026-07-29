# -*- coding: utf-8 -*-
import re, json, urllib.parse, os, datetime
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
os.chdir("/tmp/hub_1785367914")
WARN=[]
def R(html, old, new, req=True):
    if old not in html:
        if req: WARN.append(old[:70])
        return html
    return html.replace(old, new)
def ph(ref,w): return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={w}&photo_reference={ref}&key={KEY}"
WA_TMPL=("Buongiorno,\n"
"Sono Laura di HubTec, azienda di Verona.\n\n"
"Ho notato che avete ottime recensioni ma nessun sito web, cosi ne ho gia preparato uno per voi, potete vederlo qui: {url}\n\n"
"Se vi piace, lo attiviamo con soli 200€.\n\n"
"In piu, se volete gestirlo in autonomia (cambiare testi, foto, orari…), possiamo aggiungere un gestionale semplice a soli 100€.\n\n"
"Chiaramente lo possiamo modificare con logo e altri minimi dettagli vostri.\n\n"
"Nessun impegno: dateci un'occhiata e fatemi sapere cosa ne pensate!\n\n"
"Laura Borin - HubTec")
def wa_link(intl,url): return "https://wa.me/"+intl+"?text="+urllib.parse.quote(WA_TMPL.format(url=url), safe='')
BASE="https://hubtecit-srl.github.io/website/"
TODAY="2026-07-30"

# ========== LEAD C: AV hair -> salonkit ==========
AV=["AWCwydhGHHf_nSPlR3hsKYylHLFwbwCCNL71rqKtadznPpzHftpaAfLtdL-Qy8ZqIIhHE8KbG5df1b0-Gz17ceYORU27wiPM5S1AzvZASdrY-lMwr4rjvQ03g8YPAmDJulOIAPLch4wAHyn7x5YqWea52JULghJXwR2hZt6H111I_DRoGt6vjg5qwnrETm19RnAck4CEQ43e64AAdSdBtaZQuDCUNkbq041-LgWDlXi1yehfA8WbHZiPC79oM2GRV7JiJJN5L6NfeVRXM9zdyi8NC9X67Qx6uDtXGm-SYoQw-5PFVyRShl1lSQbgT7wMBGBAfyGC-ErZkMMGBudT26Zl4nvAwcrl4nB-KAhkmKfeXuPSd7BW_H2eXmdUkGsZfBawhptBezKONSaZzRe9FhRuaG3jiYnKn4L-3GUqAYXCuPawTg",
"AWCwydhrH6swZ4r7OMQmP-v01PIlDf8p_zWSF6Zpba2vAiEtTLBM0H1IzbvSCxfn08qrdSiMfE64zxSvBLF1_gmQxiF5PotgRSU4dgBptoXNk6JqrRwknwpqZBTfca93wJwGJmyR__Mswt70ZpCvrqPo8QzuYR55qOKjXSMrWwL12qxE42LhTQiSOPmA0rtRPr8-q8QjYWm8Blq9Ge3W02gsK6MjvygZ9mWxPzmnEgU3WsOrU5ejWAnl0glLiXnX93qbeLxf3vYUAarvYiqB1klRgUhIS0OEJr8wdflSRhaGYB773TPq1mJTpmPTwKB36BreQCsBU0H_kTRl_nZlWWBapLw1iUXqSKdI0m9qXWNSTAF7koHsE0g4ojMBB0dcc5DPTKXaMGFtMBubA-ABuBwSv_pworDRzM0vSv6EYvticlm_UQ",
"AWCwydgJo-dv_SqYm4o3ft-ZaWbv5a-4--o6vGKOm8_JopvFZIUQ70OJmC--rzZiPKjh7465ZghQ8WCRTbd43SpK1Vdt9F4bLqYDhNRWBw5Bba5sz1ycChHwdC_IqoL9tX-bluhdAOBMfdtU_ZNfF-uok7mvhHQ_WD65deKRIqHq6UMor-pJTh9U6fWjy2-O_8b7tq-hPiDi2fbhcK3wdbg7eJV5sECIn4P5wxF_cyI8T6aazdyd4CNleWKaCS1vzkBGG4vy4dWTe9e5ZcbgW33ufqSEAgS8eIy2uqgZ3N9yvpvKeAirWg_D3ZQmQLS7fBbb-qKEwnuOkC3NX7GV4EzRRS5BiMAL1yjCsVY20vxKIuungGf1FM1Cgh8zarhuZeR7-MNgJIWHEqLqhS2qmyxhk8mfJyrO_Tvis3SoqNjn81KS3A",
"AWCwydio3JxW26eCKzt9YoOIB1We_Oz6i3SST8KcfQqgTEsh3mwfWeW5tF75MK8gw4i7b7TFeI-UZx3-OrIkTjJ6dsTXa4j4YjqMwdleNg3WSOnd_uSKTMnz_TkGJrMv3wyFVOn2PMWW2Yxo24GrimI5_hloNhwQvLu4O0_lqyUCXMd6tRI8xLDv9rO8OXi4Vw94IPt-foGdjphHCmunWgcLqIMMlFUg0Am_xs-n5127Q3WZfeas_NdgkpW-XXwfbFhjexu_HH0P37gurSQAyIWrVSqoyow6u9xQFYwdTSVKv-Qj22_r3wjI_414A5nUHI9oUN35Ubouj8oHNkg3LR9oKd3svhC5HAQoXMcAdti4V2Y1KsQOM7qWlFnEugc3c9w8PXJO0_nzFj1y3fsLtGJ9ELjHsaYc7p7Kz0BC-1JxwmbGHA",
"AWCwydh0cRM_qtYtEJG-zaRWpx-xvPzj7HdjHzFbo_z9EoQY5H_Sjq8zhHTe-bFlGPk6mxLteocgqV4DG_J8zuQ7NdGjhmrT13EM7BvIbIUxmCxKllRoBE-g3fcHZ2OUyoragOWXqa19OXz7oAptn-j17gwjMjq1gWLYRPZOG4zRjeQmqSZh28Mnx7iWZE4Jl_37r8WF9p0aY97Tyadw2R5kIsbQXv8ZSOvaDeg0wI5zwnz8h09TF9BctDW5yPJD6a1LfV6_ufet7H2d3E-CUzv1-7psPhdbWyWi9vG6y6l3p7ZZTCOsVfl6RYcV5uhumg2bKWivLr_Z8uWN0kgLXuNasHjF_jeuO-fWYaiMtmqqTIkc4RXF2_PmPX9vwROSKy5ljJgRETRINFxp5AxBTeaqGZRovh_ITC-lwL_FrHlzosEhfMTg"]
h=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
h=R(h,'<title>Salone Méta — Parrucchiere a Verona | Prenota</title>','<title>AV Hair — Parrucchiere a Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="AV Hair di Dal Lago Valentina, parrucchiere a Cologna Veneta (VR) in Via degli Alpini 5. Taglio, colore, trattamenti e acconciature. 4,8★ su 6 recensioni Google.">')
h=h.replace("https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000",ph(AV[0],1000))
h=R(h,"https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800",ph(AV[1],800))
h=R(h,"https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800",ph(AV[2],800))
h=R(h,"https://images.pexels.com/photos/3065209/pexels-photo-3065209.jpeg?auto=compress&cs=tinysrgb&w=800",ph(AV[3],800))
h=R(h,"https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800",ph(AV[4],800))
h=R(h,'<a href="#top" class="brand">Salone Méta</a>','<a href="#top" class="brand">AV Hair</a>')
h=R(h,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Cologna Veneta</span>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Taglio perfetto e colore stupendo. Mi trovo benissimo ogni volta."</p><b>Serena B.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Lavorano con tanta preparazione e passione."</p><b>Vincenzo Z. · Google</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente rilassante e staff super professionale. Consigliatissimo."</p><b>Marta L.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>4,8★ su 6 recensioni Google verificate.</p><b>Recensioni Google</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Finalmente un salone che cura davvero i capelli. Bravissimi!"</p><b>Chiara V.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>Taglio, colore e cura dei capelli nel cuore di Cologna Veneta.</p><b>AV Hair</b></div>')
h=R(h,'<a href="tel:+390450000000" class="btn btn-light">📞 045 000 0000</a>','<a href="tel:+393311459776" class="btn btn-light">📞 331 145 9776</a>')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>','<a href="https://wa.me/393311459776" class="btn btn-glass">WhatsApp</a>')
h=R(h,'<div><div class="brand" style="color:#fff">Salone Méta</div><p>Parrucchiere olistico nel cuore di Verona.</p></div>','<div><div class="brand" style="color:#fff">AV Hair</div><p>Parrucchiere nel cuore di Cologna Veneta.</p></div>')
h=R(h,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>','<div><h4>Contatti</h4><p>Via degli Alpini 5, 37044 Cologna Veneta (VR)<br><a href="tel:+393311459776">331 145 9776</a><br><a href="https://maps.google.com/?cid=17200694571118440474" target="_blank" rel="noopener">Come arrivare →</a></p></div>')
h=R(h,'<p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p>','<p>Mar–Ven 8:00–12:00 · 14:30–19:00<br>Sab 8:00–17:00 · Lun e Dom chiuso</p>')
h=R(h,'<span>© Salone Méta — Verona</span>','<span>© 2026 AV Hair di Dal Lago Valentina · Cologna Veneta (VR)</span>')
h=R(h,'<a href="#prenota" class="book">Prenota</a>','<a href="https://wa.me/393311459776" class="book">WhatsApp</a>')
h=h.replace('tel:+390450000000','tel:+393311459776').replace('045 000 0000','331 145 9776')
open("av-hair-cologna-veneta.html","w",encoding="utf-8").write(h)
print("C: pexels_left",h.count("images.pexels.com"),"meta_left",h.count("Salone Méta")+h.count("salonemeta"),"verona_left",h.count("Verona")-h.count("Cologna Veneta")*0)

# ========== LEADS metadata ==========
leads=[
 dict(name="Passione Capelli di Ilenia", file="passione-capelli-cologna-veneta.html", tel="388 984 4635", intl="393889844635", addr="Via Bernardino Anti 10", cid="2910958458943210008", tmpl="parrucchieri-silvia(v0)", cat="Parrucchieri/Estetica", rating="4,7", nrev="11"),
 dict(name="Art Hair Katia", file="art-hair-katia-cologna-veneta.html", tel="348 527 8553", intl="393485278553", addr="Piazza Duomo 21", cid="7248882325913514953", tmpl="parrucchieri-revival(v3)", cat="Parrucchieri/Estetica", rating="4,3", nrev="9"),
 dict(name="AV hair di Dal Lago Valentina", file="av-hair-cologna-veneta.html", tel="331 145 9776", intl="393311459776", addr="Via degli Alpini 5", cid="17200694571118440474", tmpl="parrucchieri-salonkit(v1)", cat="Parrucchieri/Estetica", rating="4,8", nrev="6"),
]
for L in leads:
    L["url"]=BASE+L["file"]
    L["wa"]=wa_link(L["intl"], L["url"])

# ---- whatsapp-queue.csv ----
qf="whatsapp-queue.csv"
qtxt=open(qf,encoding="utf-8").read()
existing_names=set()
for line in qtxt.splitlines():
    if ";" in line: existing_names.add(line.split(";")[0].strip())
added_q=[]
with open(qf,"a",encoding="utf-8") as f:
    if qtxt and not qtxt.endswith("\n"): f.write("\n")
    for L in leads:
        if L["name"] in existing_names:
            print("skip queue dup:",L["name"]); continue
        f.write(";".join([L["name"],L["tel"],L["wa"],L["url"],"Cologna Veneta",TODAY])+"\n")
        added_q.append(L["name"])
print("queue added:",added_q)

# ---- index.html: insert into existing Cologna 2026-07-30 parrucchieri <ul> ----
idx=open("index.html",encoding="utf-8").read()
anchor='<li><a href="./momenti-acconciature-cologna-veneta.html">Momenti Acconciature — Parrucchiere — Cologna Veneta</a></li>'
newlis="".join('\n<li><a href="./%s">%s — Parrucchiere — Cologna Veneta</a></li>'%(L["file"],L["name"]) for L in leads if './'+L["file"] not in idx)
idx=idx.replace(anchor, anchor+newlis)
open("index.html","w",encoding="utf-8").write(idx)
print("index inserted:", idx.count("art-hair-katia"),idx.count("passione-capelli-cologna"),idx.count("av-hair-cologna"))

# ---- _crm.json cache ----
crm=json.load(open("_crm.json",encoding="utf-8"))
crm_cids={x.get("cid") for x in crm}
for L in leads:
    if L["cid"] in crm_cids: print("skip crm dup:",L["name"]); continue
    crm.append(dict(name=L["name"],file=L["file"],phone=L["tel"],intl=L["intl"],comune="Cologna Veneta",
                    cid=L["cid"],tmpl=L["tmpl"],url=L["url"],wa=L["wa"],canale="whatsapp",
                    zona="Cologna Veneta",address=L["addr"]+", 37044 Cologna Veneta (VR)",
                    stato_mail="Bozza pronta",categoria=L["cat"],data=TODAY))
json.dump(crm,open("_crm.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("crm total now:",len(crm))

# save leads for CRM/Notion step
json.dump(leads,open("_cologna_leads_out.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("WARN:",WARN)
