# -*- coding: utf-8 -*-
import re, json, urllib.parse, os
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

# ========== LEAD A: Art Hair Katia -> revival ==========
A=["AWCwydiSUOzCHG0N1Lwx7ImEoUkH8Q5R3NUKRyf3pzqp29YhU7y_q5GhtYheMMTfW9qH5vYBQUt-dHtmsVuUq4qhQQtfbVOKFPQjyC0K2HzxMe6XLXklEG6QLY3CTmFEvbTTPdDT7hpPGzFRAg0fyEhY5mfQ_oM3QLR02cvUv2s1N8XMhyUkATGfb4f7XxVBGEmBRgNxBBepFKNJKjT1f8p6O3T5pK8tSBLWoNJlY3YTIKS6X2yrNTXDfplVKybvmbmfjniBpZ-RnNbF-FVLAuPxDSWTrosC0BVPgRLdvAF3W8yoBCYAyF2h9C_bWkpidCWflQrljaPLjB_IrUynJoI6cyWIeilPkGWBxBjsLOQ0GNbwxOXE84Rs4dmWtms6QOECtSS_l29kxFaSFU99uaxFigZBq1ViH3ChXs_oOb_Ms58Z-Tfp",
"AWCwydgkEX4ZjvxVFpE7X4WHB8_pqev2RHkISMukSr769g7VBFE4_uuESBxoy0MIpuvhHW359yDC45J7_GgWIcsx_lvsfUmLvnWArYnXL3gvvehwEvmQAKPcRWRdqzRk0BtwaQ7-Jprtra45UNRakQQGKz15SxAzgdsXucvi-yEwuuqs5ZmvYYcdaKe6-VTSge0V8m_KjxFgvqPSHJX1KnoDkcLJuWjS2l-u7GRe9tfmj6ZHJmzqfmywajw56N9CWunYRVzYErHKO9BMRvUWBb-a07GAuxFZ1wMSZLpayNBrGwOKOZb7Z5UstcSCL4BO7a_Jln8s8G33p-8P2FlYnXcehS2xAJ19jxaKe0Zow2k0LzO99gQn7o4kpFrtJ-qQeTqtP5X2y9z1Tzv0HP-J3oBFIDMDHXOlDlfmKScFcb9vkQ-SvDw",
"AWCwydh4dDMxqScfvt8R2Deh3LZ4JHL20Ohu5lbgNAlgq4j-9YQ5ZDd3IORAMhPqZS9dxI6phfUDQyaJb3xOtvQbnR5iUHMWYEE2HSE7pio1vQp7Osn3DJP5d48piQH06sbxYnu4UFgQ-UEvJM-KmE8o1SE2TiPm9tT3S6aH1PX0BhKhLeG-Qc2bmuG76nbTHr7NJUQ4HgqnbvY66U-zSnIyzgHHFMtIhvzOUyea2e1ULuM52MxLXycZwWxJv6hekUsVDwMrRjiHv_suvUCu7B9iVZkbERIUciFnqipztsKcvNvZkuwGoQd36vsH9x0k3jrWGQG8LFlPEMeBZNpj2Gg8nQfCuyY0oPum0sIy-zW5pFF_JUlwbFB9wY97NZRHIVl2-wXeOHxN47ra3MqLTSEze9tcrqEF7pbAhztewSsjOnii0_qi"]
h=open("parrucchieri-revival-flagship.html",encoding="utf-8").read()
h=R(h,'<title>Revival Hair Studio — Parrucchiere a Verona | Prenota</title>','<title>Art Hair Katia — Parrucchiere a Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Revival Hair Studio, parrucchiere a Verona: taglio, colore e styling d\'autore. Un salone dal design minimal ed elegante. 4,9★ su 180 recensioni. Prenota.">','content="Art Hair Katia, parrucchiere a Cologna Veneta (VR) in Piazza Duomo 21. Taglio, colore, trattamenti e styling. 4,3★ su 9 recensioni Google. Prenota.">')
h=R(h,"https://images.pexels.com/photos/3993462/pexels-photo-3993462.jpeg?auto=compress&cs=tinysrgb&w=1600",ph(A[0],1600))
h=R(h,"https://images.pexels.com/photos/3992874/pexels-photo-3992874.jpeg?auto=compress&cs=tinysrgb&w=1000",ph(A[1],1000))
h=R(h,"https://images.pexels.com/photos/3065209/pexels-photo-3065209.jpeg?auto=compress&cs=tinysrgb&w=800",ph(A[0],800))
h=R(h,"https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800",ph(A[1],800))
h=R(h,"https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800",ph(A[2],800))
h=R(h,"https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800",ph(A[0],800))
h=R(h,'<a href="#top" class="brand">REVIVAL</a>','<a href="#top" class="brand">Art Hair Katia</a>')
h=R(h,'<span class="kick">Hair Studio · Verona</span>','<span class="kick">Parrucchiere · Cologna Veneta</span>')
h=R(h,'<h1>Revival</h1>','<h1>Art Hair Katia</h1>')
h=R(h,'<li><span>Martedì – Venerdì</span><span>9:00 – 19:00</span></li>','<li><span>Martedì – Sabato</span><span>8:30–12:00 · 15:00–19:00</span></li>')
h=R(h,'<li><span>Sabato</span><span>9:00 – 18:00</span></li>','')
h=R(h,'<q>Un salone diverso da tutti. Eleganza, competenza e un taglio impeccabile.</q>','<q>Una certezza, sempre al top!</q>')
h=R(h,'<b>Beatrice C.</b>','<b>Alberto D. · Google</b>')
h=R(h,'<div class="c rv"><div class="st">★★★★★</div><q>"Colore perfetto e consulenza vera. Mi sento sempre valorizzata."</q><b>Elena V.</b></div>','<div class="c rv"><div class="st">★★★★★</div><q>4,3★ su 9 recensioni Google verificate.</q><b>Recensioni Google</b></div>')
h=R(h,'<div class="c rv"><div class="st">★★★★★</div><q>"Ambiente raffinato e staff attentissimo. Consigliato."</q><b>Giulia F.</b></div>','<div class="c rv"><div class="st">★★★★★</div><q>Taglio, colore e styling curati nei dettagli.</q><b>Art Hair Katia</b></div>')
h=R(h,'<div class="c rv"><div class="st">★★★★★</div><q>"Il miglior taglio che abbia mai avuto. Tornerò sicuramente."</q><b>Sofia R.</b></div>','<div class="c rv"><div class="st">★★★★★</div><q>Nel cuore di Cologna Veneta, in Piazza Duomo.</q><b>Piazza Duomo 21</b></div>')
h=R(h,'<a href="tel:+390450000000" class="btn btn-light">045 000 0000</a>','<a href="tel:+393485278553" class="btn btn-light">348 527 8553</a>')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>','<a href="https://wa.me/393485278553" class="btn btn-ghost">WhatsApp</a>')
h=R(h,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@revivalhair.it">info@revivalhair.it</a></p></div>','<div><h4>Contatti</h4><p>Piazza Duomo 21, 37044 Cologna Veneta (VR)<br><a href="tel:+393485278553">348 527 8553</a><br><a href="https://maps.google.com/?cid=7248882325913514953" target="_blank" rel="noopener">Come arrivare →</a></p></div>')
h=R(h,'<div><div class="brand" style="color:#fff;letter-spacing:.22em">REVIVAL</div><p>Hair studio d\'autore nel cuore di Verona.</p></div>','<div><div class="brand" style="color:#fff;letter-spacing:.22em">Art Hair Katia</div><p>Parrucchiere nel cuore di Cologna Veneta.</p></div>')
h=R(h,'<p>Mar–Ven 9:00–19:00<br>Sab 9:00–18:00</p>','<p>Mar–Sab 8:30–12:00 · 15:00–19:00<br>Dom e Lun chiuso</p>')
h=R(h,'<span>© Revival Hair Studio — Verona</span>','<span>© 2026 Art Hair Katia · Cologna Veneta (VR)</span>')
h=R(h,'<a href="#prenota" class="book">Prenota</a>','<a href="https://wa.me/393485278553" class="book">WhatsApp</a>')
h=h.replace('tel:+390450000000','tel:+393485278553').replace('045 000 0000','348 527 8553')
open("art-hair-katia-cologna-veneta.html","w",encoding="utf-8").write(h)
print("A: pexels_left",h.count("images.pexels.com"),"revival_left",h.count("Revival")+h.count("REVIVAL"),"verona_left",h.count("Verona")-h.count("Cologna Veneta")*0)

# ========== LEAD B: Passione Capelli -> silvia-de-guidi ==========
P=["AWCwydiquFNf3cIihdcmglPuFxT5UZjZSA4TzKCkFQWBCIT-PgB-h1XtcmAlExOWNgTwYtcG6wjCoNhB19u3SkwUdFRsPo7s3ZYb5kb9NcMpklR0eh1V4qSSjlhoI1hxOJnIEsyWOsLi33cqtr47FzzhzZcdjNPLhjkI0BJRWavfBC4lZrIy_ACqpCn9fYHjMI4pjbJrRfEnw6dDJOkBHFVsenZK0WnNgAnwSybnvm_tNeL1eheakPNqUUgDtBSIUVoabN4GYUHyOcYC0xjsg-unnv6xLmssSnLmrX_h4VkDihHsGQ1kVcjzJ7Ous4T2ZADwTcpiCPx2Jc-9PUhkAFtKpBj732syY_uBUeuJt7Q0mlzdTvsuIaYf-XLtc7MobLiFmEdLOAk2Qlo9uU5eOM_ryUwfxP4Ukwq44spAOf_QA3HXVFyk",
"AWCwydglvbp-FkGSsejXBHWrl121ohMKmsb-2j4p2gkyjficZq25XeL4XExuJcgE9AAIZ_DTDZOLkRZlaMhVRLeAYQuiUKbyXEvGO-ndndfXLIo1sJkf1yX45aevH_JX1iTbcWHdjmxtlWosf9uXHiVMfW0y9r8AbJ-BEpXmGWgwc8F1XErtlOu7ko2rLi4HcZO_9lNoHXFuUHqAhTtkCMVOrbKGItProsy2KRwt1pdTCqOPnwzBV1nPohejgfoHpnfXSZZydwK0lAR3nF8sv-Lgb3TCc7l-LIBxL_OLWwEHT_dZtSJJy1BS3sCFFjmWl-97JnLCiPIQpbPCXLVJ6CB5moiObF5DvBIa8NVvnxS6MJoBM146LT42nquAZlghqp7lyEECcdK3N3OuVsCSIuoweLsFpqMvfDezmwmtq72ruC_3G28",
"AWCwydgZ3297reyyDB87wSK2r3osNVzKSvZ7cma4MDBCsg7Malh6pgTtiJu0BW1pAxlWQxfqd5QxDncGyvL4JIdgsSqleAxA8bcd_TrtkH5rjsXwC0H-ZrvAQuC2LyQnIW41uC2O-J6Z7hqoJUM9MWFyXXQU7oRC10qrWqnS4krkYhAyusQtRjsVYU6x_qJjmlNaA_JYKWf6QJx9ZY3nPUpUTcNtl8XwhJqcdWnJEV0-Cufr-j7VNBlsf7bJeyul6iTyL7k4BNctVKly_xsef90psc3gWhSzApwUv7XgTLh9nem4FTuOhmdL4dOUldTuvX5_VnKio4ez67twMLB8U5Gjme1BcLv8xTReyZKjhQzcYzkvw-jvSn4gSUJhVAYIgze-IW5gdFHqpDwuDkFGd0wjKIRcJfrXq1C-bGerTSoimjg",
"AWCwydi9DVCoo7qHoVLc0FfKjC0UndCgBW8mv6C3SCfFDqKoXUvnt24Z2MQd-3lEK06vMbcstlUNHKskgprkukZFavqCswIlnQ4OsfMfTRH7qQmqXQgvgEpTTPtUotx8SImV3h_qP7jwF_gmrc4fHTsLXkw6wpvVKuaxDZdZt7Xh3QUraImbXgkMhIOV5bw8bRiwyJ5XSvI3-tgzdv5mdCu8cyiX4YsXkMYwo-jf5N_ygOpDify8pwFOBMX1aJ-pt6_mIQ7LU88TivI1ASHExflE-EkZGQecu8ZVAeaYT74nwVTEwL7DCgOpf1rurxDQyMX1A93bzw4fIXJkSZm5uHTgdMBu8rL9xOjS-6ZAvi9tCA5xAahuHrdjJo_N_VctTHvfaLXA2JDxJyoh5fJyd_R08cfVO4eJtDD3fZvpegByT-fmkro4",
"AWCwydjr3lPPuajfm3xLsB4pGiOdaEd9BA1ok9FVFDwKCmA6C86hMcP6eKKNHvkbj-rk3VcTOIWlva_puZPjuJXngOC8lUbLW-TtUKy_wsosZl72Sxe2Rk62BwHUe1PKczSjPLWrCFVTWVxA_PKdugmXjHK6quWImRxg9qMtm8oV_yg_ttr42sOpwo5jh0U0bK4rQ08BpUa2AvrTjugi57HKu7cw2Bdbn7SOf1lwuip_ZA402xQO3-ikqt0o6mW1ySJYcxj6vqxjaI9Mwbd_9_Ba_NFLhobZPHOitDNKL5-GZ0LDxh34KiKzeNi8H7qCaBGxulQaU1XFKl8JCdsHuItGtLxia3nDbvgmikdAHDJ7EenJZApQxjVCzRSgyjBoGxzvDNJp_Mw1ZerM2kFgTWfB2wdYWwvkzhEJUSJrTBLUrHcvMg",
"AWCwydgy3ljbY9GZxutZ2fTr0R2SLzcTBO9Ngri05j4L8ILa09w5T2XzIebObAp3_RILX9yBHOedXMBD1bUT5peoW6S5iP4Gwn7ghAQWd8B8uP7wbmuBJUvDWg01ybAzh0z66fuvBL_881KVSbESppsdOJoDyAgb2ow6An7pPLxn4jar3GRvPThEwaqSWRDFA2oHvq41iTEjJSlAMeyFknoruesTtqRRlma_i6IvwwUlYRKtpnt9QE6egjvouR5KHsk7ETR0I48D7Qpqd_fp8ct7mrD7M4XMXn0_VRGQC4ACR8yplnhQtyXOHB-ceGcCagsE7v5kI9iCbHMy_cj6HIdKSsnmEBCgSLXbRMHtczs_V79idEnLt1M40v-R1-8AZyjWctE51Q-5cl98M5uC9PloKOYkUnKdRZt8yxxIj1_qKiZ_iF5i"]
h=open("silvia-de-guidi-capelli-verona.html",encoding="utf-8").read()
cnt=[0]
def sub(m):
    i=cnt[0]; cnt[0]+=1; return "photo_reference="+P[i if i<len(P) else -1]
h=re.sub(r'photo_reference=[^&]+', sub, h)
h=R(h,'<title>Silvia De Guidi Capelli — Parrucchiere a Verona (Golosine)</title>','<title>Passione Capelli di Ilenia — Parrucchiere a Cologna Veneta (VR)</title>')
h=R(h,'content="Silvia De Guidi Capelli, parrucchiere a Verona in Via Golosine 117. Taglio, colore, acconciature sposa e trattamenti. 4,9★ su 71 recensioni. Prenota.">','content="Passione Capelli di Ilenia, parrucchiere a Cologna Veneta (VR) in Via Bernardino Anti 10. Taglio, colore, trattamenti e acconciature. 4,7★ su 11 recensioni Google. Prenota.">')
h=R(h,'<a href="#" class="brand"><span class="mk"></span>SILVIA DE GUIDI</a>','<a href="#" class="brand"><span class="mk"></span>PASSIONE CAPELLI</a>')
h=R(h,'<b>#01</b> Parrucchiere · Verona Golosine','<b>#01</b> Parrucchiere · Cologna Veneta')
h=R(h,'<h1 class="display">Silvia<br>De Guidi</h1>','<h1 class="display">Passione<br>Capelli</h1>')
h=R(h,'<small>4,9 / 5 · 71 recensioni Google</small>','<small>4,7 / 5 · 11 recensioni Google</small>')
h=R(h,'<p>4,9 stelle su 71 recensioni Google verificate.</p>','<p>4,7 stelle su 11 recensioni Google verificate.</p>')
# reviews cell 1 (Veronica -> Giulia)
h=R(h,'“Mi sono affidata a Silvia per l\'acconciatura del mio matrimonio. Gentilezza e simpatia infinita, mi ha fatto sentire una vera principessa. Non finirò mai di ringraziarvi.”','“Sempre una garanzia di successo. Molto empatica, capisce sempre quello che vuoi senza dirglielo apertamente!”')
h=R(h,'https://lh3.googleusercontent.com/a/ACg8ocKYZPC0FPjNxUab_ETwBd7kApfKgRmGFmITmWnEOMvhFEO5qQ=s128-c0x00000000-cc-rp-mo','https://lh3.googleusercontent.com/a/ACg8ocJpqQdGVMDlGYDLccFhzpWG0ptyA1HwJtpcBWGJc5HxzBfJiA=s128-c0x00000000-cc-rp-mo-ba3')
h=R(h,'alt="Veronica"><div><b>Veronica Giberti</b><span>un anno fa</span>','alt="Giulia"><div><b>Giulia Boschetto</b><span>4 anni fa</span>')
# cell 2 (Manuel -> Elena)
h=R(h,'“Puntuale, competente e veloce. Ho portato anche i miei figli: felicissimi, soprattutto il più grande che si sente super figo dopo il nuovo taglio. Bravissime ragazze!”','“Taglio perfetto! Sono molto soddisfatta, soprattutto per come ha tagliato i capelli a mio figlio.”')
h=R(h,'https://lh3.googleusercontent.com/a-/ALV-UjXDqjipjbXDEVfR6Ex17SsDv0OkSOvQBDhTJX94eqyjVUXW-XsywA=s128-c0x00000000-cc-rp-mo-ba3','https://lh3.googleusercontent.com/a-/ALV-UjWDMyYJLo0QdJYzsnylfOj102Kj5qCv2-_rtyvIsoZMTi4469Ntdw=s128-c0x00000000-cc-rp-mo-ba4')
h=R(h,'alt="Manuel"><div><b>Manuel Nardo</b><span>3 anni fa</span>','alt="Elena"><div><b>Elena Pegoraro</b><span>4 anni fa</span>')
# cell 3 (Jessica -> Anna)
h=R(h,'“Negozio accogliente, professionale e disponibile. Ho fatto il colore e sono uscita perfetta. Ottimo rapporto qualità-prezzo. Consigliatissima!”','“Ti accolgono subito con il sorriso, mettendoti a tuo agio. Sono bravissime e ti tolgono ogni dubbio: sicuramente ci tornerò.”')
h=R(h,'https://lh3.googleusercontent.com/a/ACg8ocLOGzP9U04fQ6GRRAbhOV40jVUffHXYEKyHKz2YWv7XwIcA2A=s128-c0x00000000-cc-rp-mo','https://lh3.googleusercontent.com/a/ACg8ocKttDNRYaZoMg23rcmwbjdXb4So93SBlISfGOtgN8BwrwcaaA=s128-c0x00000000-cc-rp-mo')
h=R(h,'alt="Jessica"><div><b>Jessica Marconcini</b><span>recensione Google</span>','alt="Anna"><div><b>Anna Vottarghi</b><span>un anno fa</span>')
# hours
h=R(h,'<li data-day="1"><span class="d">Lunedì</span><span>08:30 – 15:00</span></li>','<li data-day="1"><span class="d">Lunedì</span><span>Chiuso</span></li>')
h=R(h,'<li data-day="2"><span class="d">Martedì</span><span>09:00 – 18:00</span></li>','<li data-day="2"><span class="d">Martedì</span><span>08:00–12:00 · 14:00–17:00</span></li>')
h=R(h,'<li data-day="3"><span class="d">Mercoledì</span><span>09:00 – 18:00</span></li>','<li data-day="3"><span class="d">Mercoledì</span><span>14:00 – 20:00</span></li>')
h=R(h,'<li data-day="4"><span class="d">Giovedì</span><span>12:00 – 21:00</span></li>','<li data-day="4"><span class="d">Giovedì</span><span>08:00–12:00 · 14:00–17:00</span></li>')
h=R(h,'<li data-day="5"><span class="d">Venerdì</span><span>09:00 – 18:00</span></li>','<li data-day="5"><span class="d">Venerdì</span><span>08:00–12:00 · 14:00–19:00</span></li>')
h=R(h,'<li data-day="6"><span class="d">Sabato</span><span>08:00 – 16:00</span></li>','<li data-day="6"><span class="d">Sabato</span><span>08:00 – 16:00</span></li>')
h=R(h,'const periods={1:[830,1500],2:[900,1800],3:[900,1800],4:[1200,2100],5:[900,1800],6:[800,1600],0:null};','const periods={1:null,2:[800,1700],3:[1400,2000],4:[800,1700],5:[800,1900],6:[800,1600],0:null};')
# contatti
h=R(h,'<p style="margin-bottom:8px"><a href="tel:+393335037075">333 503 7075</a></p>','<p style="margin-bottom:8px"><a href="tel:+393889844635">388 984 4635</a></p>')
h=R(h,'<p style="margin-bottom:8px"><a href="mailto:deguidisilvia@gmail.com">deguidisilvia@gmail.com</a></p>','')
h=R(h,'<p><a href="https://maps.google.com/?cid=3290711706439048689" target="_blank" rel="noopener">Via Golosine 117, 37136 Verona →</a></p>','<p><a href="https://maps.google.com/?cid=2910958458943210008" target="_blank" rel="noopener">Via Bernardino Anti 10, 37044 Cologna Veneta →</a></p>')
h=R(h,'<p>Parrucchiere unisex a Verona, zona Golosine. Taglio, colore, acconciature sposa e trattamenti con prodotti di qualità.</p>','<p>Parrucchiere a Cologna Veneta (VR). Taglio, colore, trattamenti e acconciature con prodotti di qualità, in un ambiente accogliente.</p>')
h=R(h,'<span>© 2026 Silvia De Guidi Capelli · Verona</span>','<span>© 2026 Passione Capelli di Ilenia · Cologna Veneta (VR)</span>')
# mobile bar bk -> whatsapp
h=R(h,'<a href="tel:+393335037075" class="bk">Prenota</a>','<a href="https://wa.me/393889844635" class="bk">WhatsApp</a>')
h=h.replace('tel:+393335037075','tel:+393889844635').replace('333 503 7075','388 984 4635')
open("passione-capelli-cologna-veneta.html","w",encoding="utf-8").write(h)
print("B: photos_set",cnt[0],"golosine_left",h.count("Golosine"),"silvia_left",h.count("Silvia")+h.count("De Guidi"),"333_left",h.count("333 503"))

print("WARN:",WARN)
