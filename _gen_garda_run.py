# -*- coding: utf-8 -*-
import json, urllib.parse, os, datetime
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
BASE="https://hubtecit-srl.github.io/website/"
TODAY="2026-08-01"
WARN=[]
def R(html, old, new, req=True):
    if old not in html:
        if req: WARN.append((new[:40], old[:60]))
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

# ============ PHOTO REFS ============
E1="AWCwydh87K9Wl7PGNm4Ihb8NLO0Ui7Q6bKVfLNkUED2Xb9pymiSVaHYhifimCpqLWhNsHJtb1YybP2bv4ZEsSc_WYqIPV6lLE9aBL18T_34eRe954h4AR9R4P0P0DyhVcUaka0gkq2kDDlacDp9XQkUWcMeIx9juiIjH7v_oWHUXEeArNZc_hLpIggvgUZ9fxiCxYv0DQQabihr8CdCNgfLyQbgmnjuMdqEY0cDfic6k55LgxNCsg8gW4mhU3k0S5kDLU56IBOM4DOMgBKhOSEpTIK1AenTqNcNjS6XHn1fR3n7MDVFDGj2vw2AyKye5eoZF9LEFLaZJ4Gr6keOplGjJQMDcO68uyjN7nQk0_2xhBzG1j5Z3J29gHiFKusT9JKnWTc0N9vauB2ksCLILwNQSdkqoOuibsQ48Ft8i0oS-K_fO8TKe"
# Sara Pasquale
S1="AWCwydhaoZSlF4ByZRHu3PF8zSSPVqAYv_QRxa0aGnAe5voh_Fw0PwYpGjxc3Jlkd3V-4aCpuXb80ekpqMcy5VrYLHc7naGorNdmtVpatlgL3d6Gzn3MtgM-PU8KfFUskWsi_nJP8CzXJN4qn6UkSYm5HwmbDqCJnrIlrCHTpcM7VHu5_AsOyxFIneBklehHzvhKoPzaW4I4bUptaW2VZquWpQ4Qcr2NdpOp1AfxqMgICEWiXAKgKalc_rVr6RXgStv9a0_bWoL6K_mOc8VXLyak1Ozk3POkvyn5UFDNsz_PtQco5PejUe2bl85_Os_sDFCpUod4md-s2i3BiBw3QT-Wu9jeyg4HC-siFDIphwZUCE1ITg-vbXEel6wfaY87zK6-s_S2PM1ohlkCououcu4CUHh4fKVPbK_Vq7hfDek7EjLeHKDt"
S2="AWCwydifMPWANUw0ru_ukFRLd07lezgPRIul7B-Y77G5yEBxgMglfCqkRRe7epAk_tY7xGfCyyc80ZfKhfg29kb9nkrC2J223yhrl2g1iYkfqvwdHvp2GuFFvMIWmYIaWtvFcRAoI1_h-rIcdRgKG1KOqwEGAEdfN9Xw8zLT42LILC2fi7lNgbS4ZQJwkf9r_yZz0o6W8dkd2RYLdOeFMcOyC3LUT1YPaQubFh5F95ZcsWpgrYWEse7sLanlLvna6A2gn47yrX4sMhWsbrzqCkRrS_1a9jh99HMVRWmVvgh5Rmqz3MfI-9_y2307MX4KYBx8oB8cpOkBmkd5D7XWfGTFhnjn22Weu6Z-id6QLPZFuV0mj_jNQaUYQGGCGtDCZM70XnSgpwbZ6mHkTtBxzllqa5rvaJkrLN1ZCJRcP_YiP3Ve3Fs2"
S3="AWCwydgLt2e2vHLc_-DWlYm1LIHM34qJ2zunqare14Hsmkj4fP7joo94LJwxvJV0YOsHzU3FGtHKrpr59ZAygyJw-ddVFYTYrBF1Q80sI8k6UN11YnLY37WkU0crGnq0J2XfZvGeHf9u1rc-gC2NA2ez_OUQ8M1FScvY2i0H-sC__1heBgizjOnfUHsNnoTGGKMQZt9TuLYUcLVzMkegSwGlJXT_BQMcsYEZXhX0O9c2e_B8N_m7JBm8G6T10RrFGz_6ClERod2Ar3TlmzEeqppXQe8VRKBXORf3vv0fX6RoiiM-vNlu9tYiv2sWNbkdIh2N2G3-nZBzqJecm4Mjn8Hc5Oslh8ZVYZieM4t-IYm4dugpljJy3e9fBrPQeQatcji16j97KIJGV6sz4nxXfE5WBHpsljgZMW23aLoyW6gd-W8ceOxr"
S4="AWCwydhqH7ZyFuRdH5hJrg_-UiZu1LIykrtW7tip2fvZIWI_w_t1b3vpMVIzFw2N3LbHhsa4AnVTs4uwkVZpRU4vLhsYNKHXSPEwEbXMKgXYy8FbUW01ejSqOAtmqUqyAvBvCrr63DhfmLD1Ox_Fv0i6lzRJbOhMs8w59li8oBKZjcD6idPPycP67xv0s77WPNl6IBO6oQZ-enrxgyu6Tc4BkdBGMX9LxN_xaC9bNMP4H9uSk6AjBOoMy0YOiwFMqRdRIcV8ziV10SnKRVR9gD4TMT8auCLKVXakT1kGtiipDzJFKCnzfiDYT9uJHAfcu0iFXStE02rpUxrOY2Kd_B4XWwc5aIrVXHpSJstyVX6tiOy6wCyCkHkBVg-G7AGeQqDMkMREeMhEdTmSjpaYsUy98of2x3tCaHJOpb-R0UdRS6hONqFT7GR4OM955TorotLB"
S5="AWCwydirpE3MiV0Wx31CMIy0JNXg16pW7-Ki4VVJ-n2CsCj695aZsE29zd6DisA8woT8k5ar7XdYurMVvSb3BslAbU-w0xdV3Q2B2bDHyKAMStVoIGMBDYEKEWVs9eS3dhrJlu2Iaj7WsiOfjzi8l0j2894F3R8uGRfIDaNUiDJ2-a8xcFvKaCYlZbNZtcXjMNEFnKy8kxRbVT13lQ8k_C0ZeAHN0dM91c4xjQB7AEXeY7fGcQ2CUVkUkAiF7mGg6iaFeuQunSwYg16m6TpKaFNkkz7Dhg0k4snyBMr3u0PQ6f6QCzZ3ETQibzHrmwi9BUP8OB0UrP2DZoOim8j6EZxw3VfiUTGvZ2c29uQDL2XXks5BMcEO9jy3t-9VQYsOPruTdxJwTaoHsbq_Pup67d-E0uXy2ZARJwNQ14eci1Rnsh4jRyg4"
# Beppe
B1="AWCwydiNcefdn5uyU8RRTpSa2OcGYIHgNtHuJYM3nZE9Ee2Y4t_PNQX4Oqi9B2Dju4qPDyYAEibo5Z8rUeeH6aZUFUjkQYSs52O21WlgJms1Xa1qV8JFDd5rppAEBBd3i3bUPx-T4LHKA4tiwH54l9-YqZKJhc3ng4Sew_bEHJZR26DcFzW5eEvyt0cj4_cHFMKbQhJAPxaxHwkuH9aTuYme1XiG4DEEPBGgU--NDHQVxgrHO3AWc4VerYM9kUL6eTATF40CAUsZ1T41qAdMCj0ipzvCbx34j0fwTHSuBEaObZ0xI8ol2OiwaAJdS6G-2Ibb9_K8104814bWVK1W34l6up4VXCqEMgDulm9WQA7NzR7XfWWdn4R7hYFhJ9mKuz-FWvnJg7OYz8CgGjQYkTcwTiNt5QSBmcAkyT5McE_ttEc"
B2="AWCwydic6rfZlT1ZSFqv4pW0g40f8i7jq7u4XZpym8cZhw5r-Hk9PuXSHksZ5PqT72JRHoz5bks9Jz6fhPAt2x0c1ttOFbB0-90QSWQs4HR_gkOAYH_clVVjeWU4k_g5dy48zJGdVTDh97qpYrq9VGe5CukJ3RM5e0pONfapERBPoQm5Zxr3LwdJLZCOUVQrN8XCQoElQLoGvZ_gOjyqcgvc9PFQlOTkf7Ik--Upay95WVc5ifbRJ149-VKtCqC2BJ9-kW_080ttsDEuK7rrg5vTzKz4inu5QMY_o-uqHCoDHNOY98083HACT5KyLBHABeliOWWb-tlGnoYZhWX7dm4oMqGdx3nIH9LaRExiUIGpBzaOOgNutBmzdEQ2KGs4p4qipWJo6ssjsUzwXOHIorjJshYW1kH6xrRhYiaatH6gRt97yOE"
B3="AWCwydheE_vPCxvNDDMkGqUsolGd1m-rSXOaqn84gYiGXIXcKS-DNDbhJ5OZ_LJr54KM8NeG1f7U7JCZlMkprlunj9Nrj4RgM7wGxWOz4RSayj7NdBaa80vQEcULdmCl_O-vlp6hrPc_OBCwjTm945L-mxcD83KhYTov9ZckC3r_eW3X1F-z11J-zKWWSapoy6Isj30Zjs49N9oixqiutrDha92ZzAZuOqBP6-PQqj6uCyInPsoetmWgXEAdnVCUXs1haT9Q4vTlE-sqZQ7EyXHBeH_mU8nIOd5c2YdaKLeZDHCCxOvUqTyedDBQL-QY8YDlLEBhuAm47HfWMUF6jVxXHCdHxte8XrBA0gsuw3NpCQyO7hefp-0Beyy77_NBTRhJcGDIS1fk5QGuK5z4r8VeXdI_jXraxyAA8gfqpzf8nWHsLUcB"
B4="AWCwydjtJZ_8SCOfOJCyjbbQsogeffiXQXko8ZwiAA49NPYchLB2hVM8ITcbJa6ArcnrWOoKfOEYrCMQeRsqUCa42eowo237HsABC-WC8SkeA3TtS6WgEma-mOqF-d7LQsg5TL8DIwtRmSvKsjCyrSHtHodpO95DJpMFSarxii602JWyvmNhwLG6mzbPfxVInxIfkaIZnlhqjq1l-biC3z6GJ6-rfqIopnsrRo_N9eSvjqCiELv5ufKQ0kZxsXNECurW8sBW75sWTyIHHo45Es9RselWYsWTrweUyMob4P0BqCFVO_5hnLHqi_yQ-aIUSbJqg_YOa7vOu0kLW4DTfNXCkGsiNgX6O01Z_Nic5kz6o4xUGnmlZWTJfbIGea_ZHBoof1CijE7iKhSK-Cuqw_cwdvhIbhKPwgViX1D58AmLAEnTRMc"
B5="AWCwydjBSHR-wkeRrCwbNqSQgi7H-WeuKDgLL3WA_TInUVy4DVNEpyZNd9lRChKeOqpXS6iYlrAAAMbv-iJPWlHilJXMCIMsSbi6Ujq3zldkM4CnaobCORNNbR6eN_BNp1YWBZcrSDpW2zpC-kfEvjuknhWSQN6Yoq4jzriAwSMFk1QPpxOvG0_QygyfGL6Wrde0VC1lkUupQJnRpk8QuYuzfhxZ1NQLn0K8j3SDvasHvBN4Aol-H0vkG3aFqL1hG830Aqiq5bqWQcIa0hb074IxdbUf20LVc8RauuGxYGBe6iz8eNZ9l-puYxX_iVQVQ11VW2VE2PglU9KO5rfqDYpZmQLYXDvu5v38Re5IqsbKLc7jWDCL9w2_e46gHW5XuXUidK5G6zc7tzWYcHc_maEwr8d3BFazuhKPI9H5dCYzDIMDD2TMpZeBdd7ZK_zPpuuy"
EST_STOCK=json.load(open("stock-library.json"))["estetiste"]

results={}

# ==================== LEAD 1: EDEN -> lesya (estetiste) ====================
h=open("estetiste-lesya-flagship.html",encoding="utf-8").read()
h=R(h,'<title>Studio Beauty Luce — Estetica &amp; benessere naturale a Verona</title>','<title>Istituto di Estetica Eden — Estetista a Garda (VR)</title>')
h=R(h,'content="Studio Beauty Luce a Verona: trattamenti viso e corpo naturali, epilazione, unghie e benessere. 4,8★ su 140 recensioni. Prenota il tuo appuntamento.">','content="Istituto di Estetica Eden a Garda (VR), Via Alessandro Volta 9. Trattamenti viso e corpo, epilazione, unghie e benessere. Prenota il tuo appuntamento.">')
# photos: hero real, gallery/hours/cta stock
h=h.replace("https://images.pexels.com/photos/3997391/pexels-photo-3997391.jpeg?auto=compress&cs=tinysrgb&w=1000",ph(E1,1000))
gal_old=["https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800",
"https://images.pexels.com/photos/3757952/pexels-photo-3757952.jpeg?auto=compress&cs=tinysrgb&w=800",
"https://images.pexels.com/photos/3865711/pexels-photo-3865711.jpeg?auto=compress&cs=tinysrgb&w=800",
"https://images.pexels.com/photos/6663368/pexels-photo-6663368.jpeg?auto=compress&cs=tinysrgb&w=800",
"https://images.pexels.com/photos/3997379/pexels-photo-3997379.jpeg?auto=compress&cs=tinysrgb&w=800",
"https://images.pexels.com/photos/3985338/pexels-photo-3985338.jpeg?auto=compress&cs=tinysrgb&w=800"]
for i,o in enumerate(gal_old): h=R(h,o,EST_STOCK[i])
h=R(h,"https://images.pexels.com/photos/3985360/pexels-photo-3985360.jpeg?auto=compress&cs=tinysrgb&w=1000",EST_STOCK[6])
h=R(h,"https://images.pexels.com/photos/6663571/pexels-photo-6663571.jpeg?auto=compress&cs=tinysrgb&w=1600",EST_STOCK[7])
h=R(h,'<a href="#top" class="brand">Beauty Luce</a>','<a href="#top" class="brand">Estetica Eden</a>')
h=R(h,'<span class="kick">Estetica &amp; benessere · Verona</span>','<span class="kick">Estetica &amp; benessere · Garda</span>')
# reviews (no text reviews available -> soft/generic, no invented quotes)
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Mani d\'oro e prodotti naturali. La mia pelle non è mai stata così bene."</p><b>Alice T.</b></div>','<div class="rv"><div class="st">★★★★</div><p>Trattamenti viso e corpo, epilazione e unghie nel cuore di Garda.</p><b>Estetica Eden</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente accogliente e cura dei dettagli. Mi sento sempre coccolata."</p><b>Roberta C.</b></div>','<div class="rv"><div class="st">★★★★</div><p>Un piccolo istituto dove ti senti seguita con cura e attenzione.</p><b>Su appuntamento</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Professionale e gentile. Consiglio a tutte lo studio Beauty Luce!"</p><b>Silvia N.</b></div>','<div class="rv"><div class="st">★★★★</div><p>Prenota il tuo momento di benessere: chiamaci per informazioni e listino.</p><b>Estetica Eden · Garda</b></div>')
h=R(h,'<a href="tel:+390450000000" class="btn btn-light">\U0001F4DE 045 000 0000</a>','<a href="tel:+390457256325" class="btn btn-light">\U0001F4DE 045 725 6325</a>')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>','<a href="https://maps.google.com/?cid=13362624023508151372" target="_blank" rel="noopener" class="btn btn-glass">Come arrivare</a>')
h=R(h,'<div><div class="brand" style="color:#fff">Beauty Luce</div><p>Estetica e benessere naturale a Verona.</p></div>','<div><div class="brand" style="color:#fff">Estetica Eden</div><p>Istituto di estetica e benessere a Garda (VR).</p></div>')
h=R(h,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@beautyluce.it">info@beautyluce.it</a></p></div>','<div><h4>Contatti</h4><p>Via Alessandro Volta 9, 37016 Garda (VR)<br><a href="tel:+390457256325">045 725 6325</a><br><a href="https://maps.google.com/?cid=13362624023508151372" target="_blank" rel="noopener">Come arrivare →</a></p></div>')
h=R(h,'<span>© Studio Beauty Luce — Verona</span>','<span>© 2026 Istituto di Estetica Eden · Garda (VR)</span>')
h=R(h,'<a href="tel:+390450000000" class="call">Chiama</a>','<a href="tel:+390457256325" class="call">Chiama</a>')
h=h.replace('tel:+390450000000','tel:+390457256325').replace('045 000 0000','045 725 6325')
open("estetica-eden-garda.html","w",encoding="utf-8").write(h)
results["eden"]=dict(pexels=h.count("images.pexels.com/photos/3"),verona=h.count("Verona")-h.count("Garda (VR)")*0, beauty=h.count("Beauty Luce"))

# ==================== LEAD 2: SARA PASQUALE -> silvia (parr v0) ====================
h=open("silvia-de-guidi-capelli-verona.html",encoding="utf-8").read()
OLD_HERO="AWCwydhkn1_wypF8vun8UIeN1AiU0SdFqyqytPuy1ja3zafkjuajLieJPk4kRb_sKMfiSKi9mKxewejZOX9I3bHI4LSAqL4ozl5RG8j5y-H5eZPI2TwbFGHNvMZr2bgJ05SSL-ZN_vMohFiBfpNASTZZ7vhm-vEkiPGddE5zZjrIvtIun-_9TVYMatqeFHirkwycIYDVoW0k1Q8lF7zwyMyIxKnC6xNyfquod-ybV_mHPFWYLKxhSQiPIog2ogcl5733-TqJ9y7r1C4Xro9C2rnaSCwnV9DHdxnDWPm3vagiiR04sMB6o016T6cphseZGBjl2NxjZjFaS6gEdiKfP6J5mB-UgzuAenp72wog5V5nCrnGimW6JY6J0coubRCVWvlWmfQuJf9StjZthYWL4MAC7MAZwHZ1S1kAjGhr8m0oSFjFymWS"
OLD_FLOAT="AWCwydir9s2IqNwocQGO9_Jp7vqnBSqS246PIDVGrjVWimb2mFwsIz96SdC8zbLIblIJuq7_fb44GNLL9Bv8VewEBbTZzKPW33DCrYlUUOR4kLAoybuVKS0PmVJS71A7xsaaoRys1y4_Q3nRPVa4xHXMu3EJP6W0oiK0Q3DhizSj61JZ72x5DXCtrXvrfRSmOx7xi_e1yGwdEpVb4E9tmAEn0V4YtQs-Vepd5YTm6m1Q-GvB0ML2A5qVs5PuiuQeCgAjEuHMpBSyWItYJJ3m4kIXellgUMp_QwnNkecWNTGu1-Vp_MJkaabtYqRNC9t-K8B9q6JrSMzlx1vf2xq5QTXtbTBz4_p0r15uAge9AG4yDt3V1rD9PU9L8___2_qLTK108QCJKmfZCQQBex4LleeB6aDUg0CpeovJm9dNBdmm5zhNBg"
OLD_G1="AWCwydjC-Hz3TaJvnVIxRrdcnzwjEfAO9NikC_qjWYUMJIQXmV_GDNrG0DsPTkNCkxGNttX1FyK0hjPclyHV7G4s4N5Z5aNSAmSw7H9SQIL3JUAizAWs0_E-fzEL4huLKk_M6PWxTh4UTmF9EvZuXmsVtVQplKemoltoa0vRSRxv8HRs3uf32jTeAvFpZUjlVCzbaB_392I-JsarCBNxISTYLHn2xluVhAwUePKoFSy5Ocxh10QFm6lfC_K0560R8mFAvEzhPBx-IB25C9Jxv5QTv_WahZdqu3jSPqGcgdvxxEiSCn46EsK9oG_EWbJdD0qxcFUaZtKymc9rJ-EIaxb9B8-qCMg5eEidI8_XkhMzysDRWKH3sYx1tYS8qQHNJVGGAGmX1W6nYOIIgJJiO4HC1mPvn0lVDSgmtD5Lv5h44tYDniI"
OLD_G2="AWCwydgj-OneLyQSD5MeOTs1X0hbClM8Ok4ebzi8q9190wDB2WKK0dZxkIlXjXwwSK9TTTxT1x1tEc2rp5ngWpPCHWcBDanMlUACJolpRKXgettRkK3J1gGynPKrNWh3J0LO_tGYhLaX-eNHTVYDa4i6RUfummmswLSwoulm-TgrOxerjzMy9v5s9NsCbbpL1vbXlhm7NlYXn6sgGjAyG8Rc4q78w_enJnVccREBGaJjzQ45C0p7I-ZgguS-vfIin46rs8uIIl7b_LJPdLvObg7hMO9vEW7qcLYPk1Hbf3Mxk-xuLJlK0kWp0CLp3bkcj-_5a7QCxE41vkBgvHwBDBXcYU3CxYEUFdQMRCFVfkyt8wt_N1xyz3wXphE-CVEpdTEU1fmhrLpfXOwfRZjd0n3bQQUSWdUWqMNcFyrWvtzbJr650A"
OLD_G3="AWCwydiF60z29ik2g0FOy3kQhKcIY4xiaZ62amLr6h-wCapaxph-IBj4vZjgiIAMNs4DnGRl8SeTjussyLZ0g6kakoE3nLhZwpY1ohj2jw1x0A6zlEUBCtkurfojBKbdjoKqRN8-s0dgM2Xz1SYWD9r4p1g34JXP1srFewskQfU329hmghAcdzWBFsI3VLqzC6PErMjzQChERSsCpETgI_vNzS_VzMu7tK-eGEbs0LknHyYidZ3aicCIjYAlUWAToKbZ9HCa2ntlueLeuVZY_14D32xLpOUPem6inRx7ZTqHGOVDCeS-b1UpctpCo6nk175nkP5aKVjkHbSfI2LYNhytSh2lACUosuMC4kQUzNR4hwcJ1kPquw1jK_Ax_XzoiYuNkLIFHxk8vpkAiwIBE-sgXuPy5VfpDeKDmQpj0XnLRhkFDub3"
OLD_G4="AWCwydiILrhdR2HDtQhW4aOes4HvDVX83zdD83FK5qcobrq5T4r4phpJz_cucuNCMX8NfpiV8mFAbEcYVZiq_W77T-GJPvkzwMq1DADrui-7ywSC1sGlXhRrOre2d265In4YNgJxBDCnmbDyhyz8yymnoe6vpDHryRma27jzh13PwFje358iq3Zl_UWGBBFnkNJ8rcyJmcaqmQCN2OWjP8HiOdYC8Wl3-G5hxreV-mmk2ednGYzKjrMzzrHJRDQzA_iQAAwFKXnNpKFpDBfnXFPoJ8mKsuC7HYTO9_gWMLCh6iQF0L5ydhxxq3-bsxamEz3VtMDEG1JqahaY2IQmq__ENZYyA5qVz51tB1sBm_JxfIoDSX5aHgjuwFmcm_3geo6_mz8dVWdiWamOhkI1wupmmZ-7fs4vJq7K-82fcGQNZSM"
h=h.replace(OLD_HERO,S1).replace(OLD_FLOAT,S2).replace(OLD_G1,S3).replace(OLD_G2,S4).replace(OLD_G3,S5).replace(OLD_G4,S2)
h=R(h,'<title>Silvia De Guidi Capelli — Parrucchiere a Verona (Golosine)</title>','<title>Sara Pasquale Hair Salon — Parrucchiere a Garda (VR)</title>')
h=R(h,'content="Silvia De Guidi Capelli, parrucchiere a Verona in Via Golosine 117. Taglio, colore, acconciature sposa e trattamenti. 4,9★ su 71 recensioni. Prenota.">','content="Sara Pasquale Hair Salon, parrucchiere a Garda (VR) in Via Don C. Gnocchi 6. Taglio, colore, acconciature sposa e trattamenti. 5,0★ su 41 recensioni Google. Prenota.">')
h=R(h,'<a href="#" class="brand"><span class="mk"></span>SILVIA DE GUIDI</a>','<a href="#" class="brand"><span class="mk"></span>SARA PASQUALE</a>')
h=R(h,'<div class="tag"><b>#01</b> Parrucchiere · Verona Golosine</div>','<div class="tag"><b>#01</b> Parrucchiere · Garda (VR)</div>')
h=R(h,'<h1 class="display">Silvia<br>De Guidi</h1>','<h1 class="display">Sara<br>Pasquale</h1>')
h=R(h,'<small>4,9 / 5 · 71 recensioni Google</small>','<small>5,0 / 5 · 41 recensioni Google</small>')
h=R(h,'<p>4,9 stelle su 71 recensioni Google verificate.</p>','<p>5,0 stelle su 41 recensioni Google verificate.</p>')
# real reviews
h=R(h,'<p>“Mi sono affidata a Silvia per l\'acconciatura del mio matrimonio. Gentilezza e simpatia infinita, mi ha fatto sentire una vera principessa. Non finirò mai di ringraziarvi.”</p>','<p>“Esperienza davvero fantastica! Faccio anch’io la parrucchiera: taglio e piega bellissimi, si vede la passione e la competenza. Consiglio a chiunque cerchi professionalità e gentilezza.”</p>')
h=R(h,'<div class="who"><img src="https://lh3.googleusercontent.com/a/ACg8ocKYZPC0FPjNxUab_ETwBd7kApfKgRmGFmITmWnEOMvhFEO5qQ=s128-c0x00000000-cc-rp-mo" alt="Veronica"><div><b>Veronica Giberti</b><span>un anno fa</span></div></div>','<div class="who"><img src="https://lh3.googleusercontent.com/a/ACg8ocLq7Vtu7Cf_b7dZGBSDZU8uO0gX4BuZWWwvwHE-ejlEOqiUbA=s128-c0x00000000-cc-rp-mo" alt="Frances"><div><b>Frances</b><span>un mese fa</span></div></div>')
h=R(h,'<p>“Puntuale, competente e veloce. Ho portato anche i miei figli: felicissimi, soprattutto il più grande che si sente super figo dopo il nuovo taglio. Bravissime ragazze!”</p>','<p>“Sara è incredibilmente professionale e talentuosa. Ha ascoltato le mie richieste e trasformato la mia visione in realtà. Prodotti di altissima qualità, risultato stupendo!”</p>')
h=R(h,'<div class="who"><img src="https://lh3.googleusercontent.com/a-/ALV-UjXDqjipjbXDEVfR6Ex17SsDv0OkSOvQBDhTJX94eqyjVUXW-XsywA=s128-c0x00000000-cc-rp-mo-ba3" alt="Manuel"><div><b>Manuel Nardo</b><span>3 anni fa</span></div></div>','<div class="who"><img src="https://lh3.googleusercontent.com/a/ACg8ocLqUEs7_PMkhjZugogeslfXObFRCROz4KNyzR5qfMMYfisXEg=s128-c0x00000000-cc-rp-mo" alt="Emanuele"><div><b>Emanuele Caporale</b><span>un anno fa</span></div></div>')
h=R(h,'<p>“Negozio accogliente, professionale e disponibile. Ho fatto il colore e sono uscita perfetta. Ottimo rapporto qualità-prezzo. Consigliatissima!”</p>','<p>“Se avessi potuto ti avrei dato più stelle, te le meriti! Professionalità, disponibilità e onestà. Finalmente ti ho trovata: stiratura, colore e taglio al top. Grazie Sara!”</p>')
h=R(h,'<div class="who"><img src="https://lh3.googleusercontent.com/a/ACg8ocLOGzP9U04fQ6GRRAbhOV40jVUffHXYEKyHKz2YWv7XwIcA2A=s128-c0x00000000-cc-rp-mo" alt="Jessica"><div><b>Jessica Marconcini</b><span>recensione Google</span></div></div>','<div class="who"><img src="https://lh3.googleusercontent.com/a-/ALV-UjUFBXOg7I11og_xK9jmhXKVZh6lMZIS1yWkNTmenilP8u3ZOMZjxw=s128-c0x00000000-cc-rp-mo" alt="Carmela"><div><b>Carmela Pisu</b><span>5 mesi fa</span></div></div>')
# email line -> whatsapp
h=R(h,'<p style="margin-bottom:8px"><a href="mailto:deguidisilvia@gmail.com">deguidisilvia@gmail.com</a></p>','<p style="margin-bottom:8px"><a href="https://wa.me/393518382751" target="_blank" rel="noopener">Scrivici su WhatsApp</a></p>')
h=R(h,'<p><a href="https://maps.google.com/?cid=3290711706439048689" target="_blank" rel="noopener">Via Golosine 117, 37136 Verona →</a></p>','<p><a href="https://maps.google.com/?cid=12618135219929578395" target="_blank" rel="noopener">Via Don C. Gnocchi 6, 37016 Garda (VR) →</a></p>')
h=R(h,'<p>Parrucchiere unisex a Verona, zona Golosine. Taglio, colore, acconciature sposa e trattamenti con prodotti di qualità.</p>','<p>Parrucchiere a Garda (VR). Taglio, colore, acconciature sposa e trattamenti con prodotti di qualità.</p>')
h=R(h,'<span>© 2026 Silvia De Guidi Capelli · Verona</span>','<span>© 2026 Sara Pasquale Hair Salon · Garda (VR)</span>')
# hours list
h=R(h,'<li data-day="1"><span class="d">Lunedì</span><span>08:30 – 15:00</span></li>','<li data-day="1"><span class="d">Lunedì</span><span>09:00 – 18:00</span></li>')
h=R(h,'<li data-day="3"><span class="d">Mercoledì</span><span>09:00 – 18:00</span></li>','<li data-day="3"><span class="d">Mercoledì</span><span>Chiuso</span></li>')
h=R(h,'<li data-day="4"><span class="d">Giovedì</span><span>12:00 – 21:00</span></li>','<li data-day="4"><span class="d">Giovedì</span><span>09:00 – 18:00</span></li>')
h=R(h,'<li data-day="6"><span class="d">Sabato</span><span>08:00 – 16:00</span></li>','<li data-day="6"><span class="d">Sabato</span><span>08:00 – 12:00</span></li>')
h=R(h,'const periods={1:[830,1500],2:[900,1800],3:[900,1800],4:[1200,2100],5:[900,1800],6:[800,1600],0:null};','const periods={1:[900,1800],2:[900,1800],3:null,4:[900,1800],5:[900,1800],6:[800,1200],0:null};')
h=h.replace('tel:+393335037075','tel:+393518382751').replace('333 503 7075','351 838 2751')
open("sara-pasquale-hair-salon-garda.html","w",encoding="utf-8").write(h)
results["sara"]=dict(silvia=h.count("Silvia")+h.count("SILVIA")+h.count("De Guidi"),verona=h.count("Verona"),golosine=h.count("Golosine"))

# ==================== LEAD 3: BEPPE -> salonkit (parr v1) ====================
h=open("parrucchieri-salonkit-flagship.html",encoding="utf-8").read()
h=R(h,'<title>Salone Méta — Parrucchiere a Verona | Prenota</title>','<title>Beppe Salone di Giuseppe Pozzani — Parrucchiere a Garda (VR)</title>')
h=R(h,'content="Salone Méta, parrucchiere a Verona: taglio, colore, trattamenti e acconciature. Un approccio olistico alla bellezza. 4,9★ su 160 recensioni. Prenota.">','content="Beppe Salone di Giuseppe Pozzani, parrucchiere e barbiere a Garda (VR) in Piazzale Roma 12. Taglio uomo, barba e cura dei capelli. 4,9★ su 130 recensioni Google.">')
h=h.replace("https://images.pexels.com/photos/3993456/pexels-photo-3993456.jpeg?auto=compress&cs=tinysrgb&w=1000",ph(B1,1000))
h=R(h,"https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800",ph(B2,800))
h=R(h,"https://images.pexels.com/photos/3992855/pexels-photo-3992855.jpeg?auto=compress&cs=tinysrgb&w=800",ph(B3,800))
h=R(h,"https://images.pexels.com/photos/3065209/pexels-photo-3065209.jpeg?auto=compress&cs=tinysrgb&w=800",ph(B4,800))
h=R(h,"https://images.pexels.com/photos/3738349/pexels-photo-3738349.jpeg?auto=compress&cs=tinysrgb&w=800",ph(B5,800))
h=R(h,'<a href="#top" class="brand">Salone Méta</a>','<a href="#top" class="brand">Beppe Salone</a>')
h=R(h,'<span class="kick">Parrucchiere · Verona</span>','<span class="kick">Parrucchiere · Garda</span>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Taglio perfetto e colore stupendo. Mi trovo benissimo ogni volta."</p><b>Serena B.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Cura di ogni dettaglio, straconsiglio per un taglio da Beppe. Parcheggio comodo e taglio anche per bambini."</p><b>Gerardo L. · Google</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Ambiente rilassante e staff super professionale. Consigliatissimo."</p><b>Marta L.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"30 anni che vado da Beppe: simpatia, velocità e precisione negli appuntamenti. Grande Beppe!"</p><b>Paolo S. · Google</b></div>')
h=R(h,'<div class="rv"><div class="st">★★★★★</div><p>"Finalmente un salone che cura davvero i capelli. Bravissimi!"</p><b>Chiara V.</b></div>','<div class="rv"><div class="st">★★★★★</div><p>"Bravo, umile e onesto nei prezzi. Lo consiglio."</p><b>Cliente Google</b></div>')
h=R(h,'<a href="tel:+390450000000" class="btn btn-light">\U0001F4DE 045 000 0000</a>','<a href="tel:+390456270342" class="btn btn-light">\U0001F4DE 045 627 0342</a>')
h=R(h,'<a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>','<a href="https://maps.google.com/?cid=9788938574326369419" target="_blank" rel="noopener" class="btn btn-glass">Come arrivare</a>')
h=R(h,'<div><div class="brand" style="color:#fff">Salone Méta</div><p>Parrucchiere olistico nel cuore di Verona.</p></div>','<div><div class="brand" style="color:#fff">Beppe Salone</div><p>Parrucchiere e barbiere nel cuore di Garda (VR).</p></div>')
h=R(h,'<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@salonemeta.it">info@salonemeta.it</a></p></div>','<div><h4>Contatti</h4><p>Piazzale Roma 12, 37016 Garda (VR)<br><a href="tel:+390456270342">045 627 0342</a><br><a href="https://maps.google.com/?cid=9788938574326369419" target="_blank" rel="noopener">Come arrivare →</a></p></div>')
h=R(h,'<p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p>','<p>Mar–Sab 8:45–13:00 · 15:00–20:00<br>Lun 15:00–19:45 · Dom chiuso</p>')
h=R(h,'<span>© Salone Méta — Verona</span>','<span>© 2026 Beppe Salone di Giuseppe Pozzani · Garda (VR)</span>')
h=h.replace('tel:+390450000000','tel:+390456270342').replace('045 000 0000','045 627 0342')
open("beppe-salone-garda.html","w",encoding="utf-8").write(h)
results["beppe"]=dict(meta=h.count("Salone Méta")+h.count("salonemeta"),verona=h.count("Verona"),pexels=h.count("images.pexels.com/photos/3"))

print("RESULTS:",json.dumps(results,ensure_ascii=False))
print("WARN:",WARN)
