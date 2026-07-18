# -*- coding: utf-8 -*-
import re
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def ph(ref): return "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference=%s&key=%s"%(ref,KEY)
def rev_section(cards):
    return '<div class="rv-grid">\n      %s\n    </div>\n  </div>\n</section>'%("\n".join(cards))

# ===== BEAUTY QUEEN (lesya / variante 2) =====
BQ=["AWCwydh9oMG2z171SuH2IA2YtjD0n4Q7UCbtriFweKA81hWYbo353RoXReIR6GkCHirTinmfjfiVBaUkP2gq65dmrjBirdrU1OVIPUm3uPd1W8vaBhjaCYwc0laEFNDhI9wkaRx9k5Bvd2bFkuSqYtdawfTirJlcd_znqiEaVtn-YFuXmH53uw8f-GVNB3pU7twNt7zATvUDqtnSVVtMqdNBxcPyq4vPvM4mkqj-JzUesweUKd0dHKYjU9AspLunU2epR2PyBItEemJRnb4gWiJi931koDLB07H8pYokkqo4xNh5qMlu9DHfR2kja5DD8_3sRyoXPcb8mBXkTcSjDGCPYG3UkbvMoIKZOyEY8VIO5sp7fXe6o_Q6g12o3NRM7DK2Se1EMSgifNm4KzILcREZeMkii9YwQHjAVCB-Fk7LoyI",
"AWCwydhpHtt2yMkOAdKq2sb3LiQm3HbSym8AMyt2b1MY3GjM-cWpYgsxpHVK7W7BJSP2sa4WjvNtHyDZuYB1Aa0I2mXTpM3q2qxEdKfpmspRuMU2d853sU1UkNgXuuONN4MO1E4JKp0CCpwUYnYB44SdEMQeGLgibfqNSdBhYu0aSMcD_SdZXLQp9ul43OMPCydhN1DzZSXR5JMiyOXUhYtzF_k8fl_Cc1B4c938IYvRZLChzWKkvfa49gdLl46z_B365XIPQPohuWl0Ok6RsgFDibQjobWkEEjFty0d-ezxd3Cm31CYT9n5BlmaHdZCU9YA0Ko603LiPyxKo_8KETJ-uOdduv_rpukIWsJR0YFiTM75fYCdvIuPfgWbu-radVnNvbfnr07lMScUMSIzeOGds0xBvPdgsEqLvWOR3C6-GFmpikg",
"AWCwydjSNQlrR8-1Ge00piS5NpNVAnPeOPMWUa42BZ0UVzXexyYTAzmQ2j6B3YYq-I_xlb_2gMRgWveJ8z7wNOg3D2qGhZpoATcpPnV95IqlQEbhkmTdLIDL33MvmkjolJX_ZJckX30bLS4J1JyJNvnFDy4delS2qG8BEc_tKeXAMXYs9J-DCA8YPj3QM7roCL-QJu1bbUQJ-1My4BYQwI-LwT2b18VMOKq3Qv4Mm7yKPcbIj5ID8oq6AbX0em8_NTUPZvJVcufNbcI-RtA1SvaKsheuvyHZGW5d72HMURhkJNbXzTNBfSzdp9SQhNWx-XzFC8eIjrLui-YFZrxvlqFDpzw1-c1PHfWhUAcWo10rzsurxR4jALBCSAeKjkm-YfEK8A71XQ0vttlF2ztiEuUVEdK9849nttfAhCCCNgVrMRypP7fN",
"AWCwydg58tSbz1i3Pvc-dvvSZPudUPIdevv5Go94QjATzLe-ghBxyB1ZisWJhTgNPlCrAkysvjmIbAbVz9EbZNJVbpP_6FvZGfvt_Je4m3e7XQlmNTkEt25TZKmHanU1Doc5AxrScqB8EqPId_C71_GepJkssT8sQ_F32mFt2XqJQx0G8F_k43tDgjEw5o26T0uhLEfW00P_k30f7bPRzRGXjOtn9kWH4u-4Mf2_y8MF5bhCxKAGyKqzwa7nKbVCh7aLsk8COIHp2WSiGbTP8YtuSEJ-rKIZuBgWNAV6ECFB3XxaqJc3GSMlrix3yr8Oq-_mC4OQwIx_i8dskPfpbFNYgs3JUIyqKUzrDYYd3QGbGdaIvY4OGExr-s84dgu9xokDnA-tKa0D6eAG2ll3n5bmXWCmt_ggjLEsSNyepzh2JRM",
"AWCwydhmT-kGzC8-o17G_JoPEPK5OsJIzOFO8d_irt1U4OA1ayHyhzBLELmT35yn1uXplEtaTgWRI_1I8nLqtZiHNWiO89WfIFI9nNQDcqcalbr-WWMNRqI_fWvd4Y_nhV3D_vmUr5OfLhBkmb9-HeIOJb0sSdIo0_lgaBR6t3HVOCZ0Fn_OxKlYE-0bkDuL0LwBqfvK52m6JA2MOwtWkMvEUT6_MWxFhVzef5I4mfL2WCtc61yE7Xc9aDw2PDfQOYtMuCmrAMR4g6z1GuKQ-9X5Jgt9tLHAw_58NfA51FrqRG67fCefPvujz83p5gob8fiQhwN3rrgrJBVecssBww6RTZ0LMlo8XJbY699GVRGrxnJDYEb_uZ6-_FW4YKhVvwJe0layGhz-FSaKQzbX1OYPuvTuNe8xrw6G9y530Edj530",
"AWCwydizdZAZmlE2LHZ_tljrfcWbng5i32WxupDnOo0Uz-PN3ZK1rOPszIOTXkIwhX7R-Sd77JyzOKqKv5OoMreHjcc2216SKqbPMiNrV4ONBsLVpgpTWkE60t5e19e3Turg3qaVpM_GBcahR7tXb_6mU99B8N4Sli5_ggQubFTmqzp5MZK7HfCA_TdOwczk4dPwUMZQ3OxQk3_BnaDAfomZhTMY-oC8QibM5usNpaSrSNRowX7T18cBhsPXKIETO_99pucDN4zRc0pYIPTnDA5gXeHAmsO73pjDaCSLSWqYfGktSvon02jdda9rolKOPFgpnbg-T8qsJqO4FcuQEruCdL6Q5XghImjkYNmwTaOOB1-V-dILMbh_xZGo2e0UYEtUqeArzdO6qP9gpy1Wm6j8RSDZIv14zmiI91vsQmcffvTl1FyS"]
bq=open("estetiste-lesya-flagship.html",encoding="utf-8").read()
bq=bq.replace('<a href="#top" class="brand">Beauty Luce</a>','<a href="#top" class="brand">Beauty Queen</a>')
bq=bq.replace('Studio Beauty Luce','Beauty Queen').replace('Beauty Luce','Beauty Queen')
# images
bq=bq.replace('https://images.pexels.com/photos/3997391/pexels-photo-3997391.jpeg?auto=compress&cs=tinysrgb&w=1000',ph(BQ[1]))
bq=bq.replace('https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BQ[0]))
bq=bq.replace('https://images.pexels.com/photos/3757952/pexels-photo-3757952.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BQ[2]))
bq=bq.replace('https://images.pexels.com/photos/3865711/pexels-photo-3865711.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BQ[3]))
bq=bq.replace('https://images.pexels.com/photos/6663368/pexels-photo-6663368.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BQ[4]))
bq=bq.replace('https://images.pexels.com/photos/3997379/pexels-photo-3997379.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BQ[5]))
bq=bq.replace('https://images.pexels.com/photos/3985338/pexels-photo-3985338.jpeg?auto=compress&cs=tinysrgb&w=800',ph(BQ[0]))
bq=bq.replace('https://images.pexels.com/photos/3985360/pexels-photo-3985360.jpeg?auto=compress&cs=tinysrgb&w=1000',ph(BQ[4]))
bq=bq.replace('https://images.pexels.com/photos/6663571/pexels-photo-6663571.jpeg?auto=compress&cs=tinysrgb&w=1600',ph(BQ[3]))
# kick + hero p
bq=bq.replace('<span class="kick">Estetica &amp; benessere · Verona</span>','<span class="kick">Centro estetico · Affi</span>')
bq=bq.replace('Trattamenti viso e corpo con prodotti naturali, epilazione e unghie. Un piccolo studio dove ti senti a casa.','Trattamenti estetici viso e corpo, unghie ed epilazione in un centro accogliente al Parco Commerciale di Affi.')
# hours list
bq=re.sub(r'<ul class="hours-list">.*?</ul>',
 '<ul class="hours-list">\n        <li><span>Lun – Sab · mattino</span><span>9:30 – 12:30</span></li>\n        <li><span>Lun – Sab · pomeriggio</span><span>15:00 – 19:00</span></li>\n        <li><span>Domenica</span><span>Chiuso</span></li>\n      </ul>', bq, flags=re.S)
# reviews (1 reale)
bq=bq.replace('<div class="sec-h"><span class="kick">Recensioni</span><h2>Le parole delle clienti</h2></div>','<div class="sec-h"><span class="kick">Recensioni</span><h2>4,6★ su Google</h2></div>')
bq=re.sub(r'<div class="rv-grid">.*?</section>', rev_section([
 '<div class="rv"><div class="st">★★★★★</div><p>"Semplicemente fantastico."</p><b>Annalisa Traverso</b></div>']), bq, flags=re.S)
# contatti / phone / cta
bq=bq.replace('tel:+390450000000','tel:+390457235994').replace('045 000 0000','045 723 5994')
bq=bq.replace('<a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>','<a href="https://maps.google.com/?cid=7585048331859768540" target="_blank" rel="noopener" class="btn btn-glass">Come arrivare</a>')
bq=bq.replace('Chiamaci o scrivici su WhatsApp: ti aspettiamo nel nostro studio.','Chiamaci per fissare il tuo appuntamento: ti aspettiamo nel nostro centro.')
bq=bq.replace('info@beautyluce.it','')
bq=bq.replace('<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390457235994">045 723 5994</a><br><a href="mailto:"></a></p></div>',
 '<div><h4>Contatti</h4><p><a href="https://maps.google.com/?cid=7585048331859768540" target="_blank" rel="noopener">Via Giovanni Pascoli 329, Parco Commerciale Affi (VR)</a><br><a href="tel:+390457235994">045 723 5994</a></p></div>')
bq=bq.replace('<div><h4>Orari</h4><p>Mar–Ven 9:00–19:00<br>Sab 9:00–17:00</p></div>','<div><h4>Orari</h4><p>Lun–Sab 9:30–12:30 / 15:00–19:00<br>Domenica chiuso</p></div>')
bq=bq.replace('Estetica e benessere naturale a Verona.','Centro estetico ad Affi (VR).')
# title/meta
bq=bq.replace('<title>Beauty Queen — Estetica &amp; benessere naturale a Verona</title>','<title>Beauty Queen — Centro estetico ad Affi | Prenota</title>')
bq=bq.replace('content="Beauty Queen a Verona: trattamenti viso e corpo naturali, epilazione, unghie e benessere. 4,8★ su 140 recensioni. Prenota il tuo appuntamento."','content="Beauty Queen ad Affi (VR): trattamenti estetici viso e corpo, unghie ed epilazione al Parco Commerciale. 4,6★ su Google. Prenota il tuo appuntamento."')
bq=bq.replace('a Verona','ad Affi').replace('di Verona','di Affi').replace('— Verona','— Affi').replace('Verona','Affi')
open("beauty-queen-affi.html","w",encoding="utf-8").write(bq)
print("BQ",len(bq))

# ===== BEAUTY CONCEPT (spamagic / variante 3) =====
BC=["AWCwydj4THCqqI9lfUXOTKM5Y4QkERQhQKo9eQekO5zrlTFFYQhIlcR4XrHepdk_lpOkITBIB-Y1SGO7S2BitXSnY1vVUaAFQhI5MzakEqMqUvOLJtbSng7BmvsaX8x1k0-v39_PqDKWDnoqTJV70iPOKbejGhd6poxwbTqEI00uxz26Fqqq0WvgO7qpPYVJuYbg0K4sY_FKQj7zuU11KEXp2Z_BgteGLTOwri1VwCuidSHXHYhvQhrOPWW1kW--LupwteGqECnqVlwLqG2KWFTNLlyAER335k4gj_AtIzHWhqCrFCexLofdlX8cYIa4u7Gb9cbD4fZVN_QP4FCk91JCj_GFDz82qU0iEhuZco9HYAGAnWk0V5jtOtE0g1MltvCsW0JZ7vwVGLw2fAC4VCshfXuJmMKUl5GUuR5SQLxHiBI0Aw",
"AWCwydgn-_C8h_lusRTatZttzeGVcO0onv_Q-kYgRvAho7VOI50WN5CQz1AQ-2S_vjH1PqbOJ75DBUFv4RE-gD5jzq01GgYCJkrHAcYUgJEsqqoo4bDN84o0UGI-1T-bLAhQTMheodzvK4kyaAyU0u_y-0lnmDfYVPH2-w25LTHpGH-YHqgShE3EUMhS0pby0JMvSxuzOCUsozZ33DCHmRxlmlLiK2wdoHiYdtM8z6L0mO7W1_bXhTMDqIN7zAmznXqxQ_WMpvpO4EpJEpbe9T1XqZL43WgHzXnABrOLAOB1ONz8XW5hUnwE6GyZr-kg6BNpfl0JDD8HFGj5ySKYbq6dpy2b_lHDsb2FVhsuW1THvv8DrdJCJK6K2okleUDBBdXnw8YfUW30i9o5Le9smBgHJEtmELJ2AiffoWdTSjiWV61XjQ",
"AWCwydiiKi48dMmJu_vSWNV_IzVr5eKAafA3tomr4Kcy-074SYODne9qsM5OfuCVA8USUgHpCV-tFfe-56OIDKyHOwpVd_jyIB6QJHAS1d7APPFS7vn0wLJVby9DcZcCo9jUhw4R1-M9A3yfwa_PirrNvbHJ3LdW7zdFM2ZUNtHj5Yeu4Nl0wnwOK5xaKfemjSGP63vkkN9DEUCJ_HJTjz7a_PH0DEPFwlGHj1N1hlj6EL7PFM6vnB7eAvaT5BhslZs_KYT8Ovq4hN98-syc4sYLOI3PiUz5yZYspJ81nqS5YUoUd5yh8sSwTSy3BZkmn--3ojxDSdXUeWsNrnHeVt5niz7LkyEL34EOurCfaJM_TZVnkpil8ynT6fuRsVmCeOAu61bDTL5Z4xgcRCd_Rbhy4sdsG7Txgzy8L5SEbSeHR6Q"]
bc=open("estetiste-spamagic-flagship.html",encoding="utf-8").read()
bc=bc.replace('<a href="#top" class="brand">Centro Estetico <b>Iris</b></a>','<a href="#top" class="brand">Beauty <b>Concept</b></a>')
bc=bc.replace('Centro Estetico Iris','Beauty Concept Affi')
bc=bc.replace('https://images.pexels.com/photos/3997385/pexels-photo-3997385.jpeg?auto=compress&cs=tinysrgb&w=1600',ph(BC[0]))
bc=bc.replace('https://images.pexels.com/photos/3762879/pexels-photo-3762879.jpeg?auto=compress&cs=tinysrgb&w=1000',ph(BC[1]))
bc=bc.replace('https://images.pexels.com/photos/3985329/pexels-photo-3985329.jpeg?auto=compress&cs=tinysrgb&w=1600',ph(BC[2]))
bc=bc.replace('Trattamenti viso e corpo, unghie, epilazione e make-up. Un centro estetico dove prenderti cura di te con stile.','Parrucchieri ed estetica in un unico spazio: capelli, unghie, extension ciglia e make-up al Grand\'Affi.')
bc=bc.replace('Il tuo angolo di bellezza a Verona','Parrucchieri ed estetica ad Affi')
bc=bc.replace('Al Beauty Concept Affi uniamo competenza, prodotti di qualità e tanta cura per farti sentire bella e a tuo agio, ad ogni visita.','Da Beauty Concept uniamo competenza, prodotti di qualità e tanta cura per farti sentire bella: dal taglio al trattamento viso.')
bc=bc.replace('<div class="serv-c"><div class="ic">💄</div><h3>Make-up</h3><p>Trucco per cerimonie, eventi e tutti i giorni.</p></div>','<div class="serv-c"><div class="ic">💄</div><h3>Make-up &amp; PMU</h3><p>Trucco per eventi e trucco semipermanente.</p></div>')
bc=bc.replace('<div class="serv-c"><div class="ic">✨</div><h3>Pacchetti sposa</h3><p>Percorsi dedicati per il tuo giorno speciale.</p></div>','<div class="serv-c"><div class="ic">💇</div><h3>Capelli</h3><p>Taglio, piega e colore nel salone hair al primo piano.</p></div>')
bc=bc.replace('<div class="sec-h"><span class="script">Recensioni</span><h2>Cosa dicono le clienti</h2></div>','<div class="sec-h"><span class="script">Recensioni</span><h2>4★ su 119 recensioni Google</h2></div>')
bc=re.sub(r'<div class="rv-grid">.*?</section>', rev_section([
 '<div class="rv"><div class="st">★★★★★</div><p>"Veramente gentili e professionali, complimenti a tutte! Sono entrata con un colore orribile e sono uscita con i capelli trasformati."</p><b>Paola Righetti</b></div>']), bc, flags=re.S)
bc=bc.replace('tel:+390450000000','tel:+390457238309').replace('045 000 0000','045 723 8309')
bc=bc.replace('<a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>','<a href="https://www.facebook.com/beautyconceptaffi/" target="_blank" rel="noopener" class="btn btn-glass">Facebook</a>')
bc=bc.replace('Chiamaci o scrivici su WhatsApp: fissiamo insieme il tuo appuntamento.','Chiamaci o scrivici sui social: fissiamo insieme il tuo appuntamento.')
bc=bc.replace('info@centroiris.it','')
bc=bc.replace('Il tuo angolo di bellezza e benessere a Verona.',"Parrucchieri &amp; estetica al Grand'Affi (VR).")
bc=bc.replace('<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390457238309">045 723 8309</a><br><a href="mailto:"></a></p></div>',
 '<div><h4>Contatti</h4><p><a href="https://maps.google.com/?cid=2369544215639656625" target="_blank" rel="noopener">Localita Canove 1, Grand\'Affi (VR)</a><br><a href="tel:+390457238309">045 723 8309</a><br><a href="https://www.facebook.com/beautyconceptaffi/" target="_blank" rel="noopener">facebook.com/beautyconceptaffi</a></p></div>')
bc=bc.replace('<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>','<div><h4>Orari</h4><p>Tutti i giorni 9:00–21:00</p></div>')
bc=bc.replace('<title>Beauty Concept Affi — Beauty &amp; Spa a Verona | Prenota</title>','<title>Beauty Concept Affi — Parrucchieri &amp; Estetica | Prenota</title>')
bc=bc.replace('content="Beauty Concept Affi a Verona: trattamenti viso, corpo, epilazione, unghie e make-up. 4,9★ su 175 recensioni. Prenota il tuo appuntamento di bellezza."','content="Beauty Concept ad Affi (VR): parrucchieri, estetica, unghie, extension ciglia e trucco semipermanente. 4★ su 119 recensioni al Grand\'Affi."')
bc=bc.replace('a Verona','ad Affi').replace('di Verona','di Affi').replace('— Verona','— Affi').replace('Verona','Affi')
open("beauty-concept-affi.html","w",encoding="utf-8").write(bc)
print("BC",len(bc))
