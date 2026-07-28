# -*- coding: utf-8 -*-
from _gen_castel import build, ph, STOCK

PAL={
 0:{"teal":"#01796f","teald":"#015d55","dark":"#12312d","gold":"#b89664","cream":"#f5f2ea","soft":"#eef4f1","ov1":"rgba(18,49,45,.82)","ov2":"rgba(18,49,45,.42)","ctaov":"rgba(18,49,45,.78)","herokick":"#a9d8cf"},
 1:{"teal":"#a8657c","teald":"#8d4f66","dark":"#2c1c24","gold":"#c9a36b","cream":"#f7f1f3","soft":"#f3e9ed","ov1":"rgba(44,28,36,.82)","ov2":"rgba(44,28,36,.42)","ctaov":"rgba(44,28,36,.78)","herokick":"#e7c3d1"},
 2:{"teal":"#6d5ba3","teald":"#584a86","dark":"#241f33","gold":"#c6a15b","cream":"#f4f2f8","soft":"#eeeaf4","ov1":"rgba(36,31,51,.82)","ov2":"rgba(36,31,51,.42)","ctaov":"rgba(36,31,51,.78)","herokick":"#cabfe6"},
 3:{"teal":"#a9822f","teald":"#8a6a25","dark":"#2b2415","gold":"#d8b45a","cream":"#f8f4ea","soft":"#f2ecdd","ov1":"rgba(43,36,21,.82)","ov2":"rgba(43,36,21,.42)","ctaov":"rgba(43,36,21,.78)","herokick":"#ecd9a6"},
}

# Photo refs (owner) collected from Places details
LAB77=["AWCwydgSXMUIuhwK_vPTQes4x1b-am0RJQ7s9n3eF19Eu9oaICp_VAQqJEa7p0TFsOv8RJ1bzPfUfhjdxY5Mwx9RPTmh9heEEuv3pS4L5myWcjkk7FZSrQ7yq5_vwU59rDnq2fkx-4byQQmCoka7qt6bBwuo_ji_ge0vWjBL7U4G7cMXenCItPtHSsPNQdLAJVja_a49uC8ppZfJUbo6ZULWUrGQ6Hv3wVm_35oh727Gt9C9KQXjt02sACFZAcB0V0vdI04XYw3a_BXX0ldeiQi9OZUrivvpq2LC_thDz0U8olkhhTadXER8fCbvOZh8e6cty7Je0986t7QlucOpXiK7DzAJhgnjsj65XZNHSjCyLOhiNe7gFVU4j_L9ULhUE7htQD-rcsdfir32rglMwUw6Eod_Pfe07GnXNcjuKlKdC2ulTT3UBIoCwQDEun6_cA",
"AWCwydjByYb6_RL0vuMnPhP8zrn9WzEiTHsfNpVeItKG9ZUfDRqrgL5-x7acxvEFrUsSGu-C6OlSIZVobBNl4_d4db_Y5YTwg-TfDeL2zjihXgvwja5aEws9p_NSVnheI5W5qTb3dzY0xMhOZou6oTY-FNqklfB6UZTZubFd4eM8ob_rAfLz5RMx9JM7jeRuHKM-xjpueqzk8q-JxUJunmNBfOfljTSEB9FSSmhpfHpY6JssAuBU1eo5KZaH_Pqlbib-2ZMHudenIKa-SA7R-jpod4LaPCDRzsO3jE7aYSaZI5CvHehWwZe1AbQHSwoE64rl9r8Bn5jBUreuTFlAjxRpd8YNxRahZ9aGggohLZt6EdkfhTp1DTPqgXknpXJzRr46XBj6EYgqWNwxnRWYrfwH4bRJALxxecXBCVCkreJ12EWn6LU"]
TIME=["AWCwydgyUTMcJWZTz6XTy02qW04Dw3IuEl0EIoqcgwQphXmZWXWEHnNACDAV1gRkQleRAvtHYNd7zSglvCA6HB2ihiFWBysbmN7IfjU5Zj62nmZVElhs3AJNWP63ase9hcf77SqnVXejLtCKOh0F3tLZZbhOKT9lcPcFwXsTQvSjQ_3jyWSw4HqyQWSQcQfsYIQIioLnDVi7w_z0KiZiPQA5Nun7McuF0vmdDDiSKzvDee2Wl-bo7RuSl7mpxfNk38NXiuopAfdn6ZSgT8M3s1lSyM1EyLHz2XU0nCBPs2hiuK85BHX1AlBEvK7gn-DCXD6U1e7gfXqDtXU5sLXADjUUG70VoyzW8CcVvCZDENS_Ik0yRWGbGE3-SqdXWdt73uSqGvlRMdiyZTvJhS7YgngnPvocf3qHnaFwnCzwEZuzjJuDPSveolwDB78qMMsAP4gs",
"AWCwydh-mGY7EIam3IiEpURQjFCUyJ0kSQiGoKhnCuDqp3HicIp9MD_s2ddMO_BogVdkt18BZFI9nvCUpV-OZYXtaGPxYXHBwJ6G3xhujknCuw-OTuI5TBZ4g8JCcY_ZV5j3cUEX3pqz5qXSky1k5Qy2psFg2h_wBpCyOsNM9i_ms7bLgpVvgI9gwOKKy0lvvhMYo_UUaDYK95fCS9pedAezVr0M6-Wm8Yd3FMce9k-yBfpWiBl39ihZbbpdPMMpjq66N0hdRHQECgtjvT663-o9JL4WEPD5uku4uqzvhfF0zykFABH5jynCl48lNG3pqVH1D3ffqAE1cbsNGiFUGqdCZjhFsZafrf5rY_UsAmmNUolSRFwt_J4WKQb6621rL-a0NQlFKUC3YUBgnSxdJmRCdrFSCRqJ5Uy6rcnIzIrmSSOEjNVcNS9Fzt1ctCCXAA"]
NAILS=["AWCwydj6Rt9UEiQdqr7EWE_ukzll0D4P3Dh9l3fBy6sQV71NSp51qCkM4bf2Ugyep4npcM0AUvFe8Cn1MzSxRQ6XD2iPE4fcLs9UzyFclFbdQG2RtcxUiedbsb6VJEU0eBJxAxNvol44TeO9dE11ZVKQ3Yyr7srsq70pPtQ8ljC7Bj_iqVdCljVu8w6K6Z21Vq6Fwb-Ym-KBiOOX9DfXeqsDeJIjESgnH5AJwWIO13FWqpLwI9qYwMbsXGDagU1NBIVBRgwF2TcYopzVHwTTbrm1Rp4AzGdRTmfYX65o__nO5WglLZr2KZhXka6wXXaQo2L6n7FPp1xcWijPwrcZB5XPhDPbNBPWccBNBI1NSfOHOVhnqlyUvIxBgqBkK1jJC_bLhwWNdDT4ZnPsa7ywtaGd6SIB4Xs1X3eSwxeW5ulss2DACoBBR4ulP6w_LjBZ-ACk",
"AWCwydj4ieDWJqVU2ltas-jlxZmMHiMghmbAd4iaxYTGrWR_KTGulHHsHpmaFNmOGHs420U0qU1mwcE3FARcZslTRD5bSw2Hvkmu5v3vcwyzq4p1klI0iMVKswlyFL9B4ieHjajsVY54VZyacTKZRYclchldpHgwGQMfw6Nbf29HRUX7r5pmz5qHtxDS2T9Y2yKX7HtXE4rue_v9yvYOb1jQzfnTqbFPdW7az8iRSxXIZysnDYTgSlsGj20Uf4KigSU0OOHMhaS7NdckwbOK_u5IOMZpIyYGmMQPJC15Dhj1Ia46nPJ45UHqsOT7nuMqbBStxIDVZwzHPC7UUy0ip68thkDRkpyQGV4e20Wucfc6QVyXgy0t6Mmmfl6_u1fbTVos0SQPSwKob8X07J38DRgvt-SXqHfzbvR6LdqSoesENsscMbQFU9CPLsE8qcPYYQ"]
NICOLE=["AWCwydjEHaUCF6S3uYr9KnB3c0yORCc0infHVzimajdHcDAEuIYGWUfNqMfMisE1eoeeIPGCQrwXuxAbqOdS_XZ92f4bJyplQZ8o5BvXahptkRpnQJM5tqD_iMxJmSYNJpP1w0MJ7OUM5js9SZhIbxPPv5SALS-SRlhyxQ4QgR9yCdE7hqsEgXc_QQUHjyRrWSphfsYzgGJd0V4Ilk5pt7eKlZCrxNl2DJektbJk_WCs8DuqvAjxzYri3h-M7yUwkGsp5Z_kwal6YsJAtiMJAWlxX4q5J9mSmfWq9mHOhP_5eoy-DBhFY9PnaSEwtXhjj3DcF8pX3LUv8JsBxkND4fxhUUxhMHPKJj1eMcQyDkW0c9IpwC8PrnD-4kXpA2BELan2whAsycgVFYSvnXE2zK8Y2lSB624IyJhhYjFDOqw04l_d-b6QJ3YIAbzM4JC5RCMh",
"AWCwydgbcsvZ7A1rClYHKPa0d97Y9xuxKNwj90sjgLYzmaI4StRuFVM11A2Ph6kCsPuk4LsImwvbDQzr7ilt0UB0AqvQ5ZMiEbQWNsyJ85JBlycaqmvJ-eC1lvk23wOP4IJ8Zt8NYuxxK5jPtZV3Xe_e-77nDViowicNtNtMh3_H99qa-4YRnFQ7YJV-KPkl1qHES0YebcHfOr3FToIRuR_2Qu1Fb5ScPjKE0lxcH5hLpcWtib-pCBtCPIlPEOsamNMgbs8CyoB1ykqZve7AZYWsIPdBkHX6B2NGY1nwlQIk7Eeuw5nPs19yqbfjL-_SErFlnEFXwLG6PkB8g0suS-0wnvVDU6XGaErWTCNE8aN2g1DaJWM0VBDwxUnSLW-YUSY6IvALNUnQ50UGgJQrgB9mU508MlJpmkXhhsYxMKZRDs9JNW5HY9evFHHmgaWfVMEJ"]

LEADS=[
{
 "slug":"lab77-estetica-castel-dazzano","pal":PAL[0],
 "name":"Lab77 Estetica Avanzata","brand":"Lab77","cat":"Centro estetico",
 "metadesc":"Lab77 Estetica Avanzata a Castel d'Azzano (VR): trattamenti viso e corpo, massaggi, ricostruzione unghie, extension ciglia, epilazione laser e abbronzatura. 4,6★ su 83 recensioni.",
 "rating":"4,6","nrev":"83","phone":"045 512521","tel":"+39045512521","wa":"393486095170","email":"newlightvr@gmail.com",
 "cid":"10583207519256274924","maps_q":"Via+Marconi+77,+37060+Castel+d'Azzano+VR",
 "address":"Via Marconi 77, 37060 Castel d'Azzano (VR)",
 "hero":ph(LAB77[0]),"split":ph(LAB77[1]),"cta":STOCK[2],
 "h1":"La tua bellezza, la nostra passione","herop":"Estetica avanzata, unghie, massaggi ed epilazione laser nel cuore di Castel d'Azzano. Un team esperto guidato da Desirée.",
 "introh":"Un centro estetico all'avanguardia dal 2010","introp":"Da Lab77 ci prendiamo cura di te con trattamenti personalizzati, macchinari professionali e mani esperte.","introextra":"Manicure, pedicure, ricostruzione unghie, extension ciglia, trucco semipermanente, needling e abbronzatura.",
 "servh":"Tutti i nostri trattamenti",
 "services":[("\U0001F33F","Viso & Corpo","Pulizia, anti-age, trattamenti corpo e massaggi rilassanti."),("\U0001F485","Unghie & Ciglia","Ricostruzione unghie, manicure, pedicure ed extension ciglia."),("✨","Epilazione & Laser","Epilazione tradizionale ed epilazione laser definitiva."),("☀️","Abbronzatura","Solarium e trattamenti per un colorito sano e luminoso.")],
 "splith":"Professionalità e accoglienza, da anni","splitp":"Un ambiente curato, pulito e all'avanguardia. Le nostre clienti ci scelgono per la competenza del team e la qualità dei servizi.",
 "splitlist":["Team qualificato e sempre aggiornato","Macchinari e prodotti professionali","Consulenza personalizzata gratuita"],
 "pricing":[("Trattamento viso","da 40€",["Pulizia profonda","Trattamento personalizzato","Consulenza pelle"]),("Percorso benessere","da 70€",["Massaggio 50 min","Trattamento viso","Momento relax"]),("Unghie & Gel","da 30€",["Ricostruzione / refill","Semipermanente","Nail art"])],
 "hours":[("Lunedì","Chiuso"),("Martedì","09:00–20:00"),("Mercoledì","09:00–20:00"),("Giovedì","09:00–20:00"),("Venerdì","09:00–20:00"),("Sabato","09:00–17:00"),("Domenica","Chiuso")],
 "reviews":[("Daniela P.","Personale esperto, professionale e sempre aggiornato. Lab77 è un luogo accogliente, pulito e all'avanguardia. Complimenti a Desirée e a tutto il team!"),("Ezia S.","La titolare cordiale e professionale, circondata da uno staff consolidato. Tutte bravissime e simpatiche. Le adoro!"),("Francesca","Ottimo centro estetico con personale cordiale, preparato e competente. Prezzi molto buoni. Super consigliato!")],
},
{
 "slug":"time-di-selly-e-fede-castel-dazzano","pal":PAL[1],
 "name":"Time di Selly e Fede","brand":"Time","cat":"Parrucchiere & Centro estetico",
 "metadesc":"Time di Selly e Fede a Castel d'Azzano (VR): parrucchiere ed estetica in un unico salone. Acconciature, trattamenti viso, unghie e ceretta. 4,9★ su 68 recensioni.",
 "rating":"4,9","nrev":"68","phone":"347 196 9396","tel":"+393471969396","wa":"393471969396","email":None,
 "cid":"14219039996288196038","maps_q":"Via+Cavour+14,+37060+Castel+d'Azzano+VR",
 "address":"Via Cavour 14, 37060 Castel d'Azzano (VR)",
 "hero":ph(TIME[0]),"split":ph(TIME[1]),"cta":STOCK[3],
 "h1":"Parrucchiere ed estetica, sotto lo stesso tetto","herop":"Da Time trovi acconciature, trattamenti estetici e cura delle unghie con un team giovane, attento e professionale.",
 "introh":"Il tuo salone di fiducia a Castel d'Azzano","introp":"Un unico spazio dove prenderti cura dei tuoi capelli e della tua bellezza, con consigli su misura e tanta cordialità.","introextra":"",
 "servh":"Capelli e bellezza in un unico salone",
 "services":[("✂️","Acconciature","Tagli, piega, colore e trattamenti per capelli sani e luminosi."),("\U0001F33F","Estetica viso","Pulizia viso e trattamenti personalizzati per la tua pelle."),("\U0001F485","Manicure & Unghie","Manicure, pedicure e ricostruzione unghie."),("✨","Ceretta & Epilazione","Epilazione con cura del dettaglio e prodotti delicati.")],
 "splith":"Un team che ti fa sentire a casa","splitp":"Le nostre clienti ci descrivono come brave, gentili e solari. Ci piace mettere a proprio agio ogni persona e curare ogni dettaglio.",
 "splitlist":["Parrucchiere ed estetica insieme","Consigli personalizzati","Ottimo rapporto qualità-prezzo"],
 "pricing":[("Taglio & Piega","da 25€",["Consulenza look","Taglio","Piega"]),("Colore & Trattamento","da 45€",["Colore","Trattamento capelli","Piega"]),("Estetica & Unghie","da 20€",["Manicure / semipermanente","Ceretta","Trattamento viso"])],
 "hours":[("Lunedì","13:00–19:00"),("Martedì","10:30–19:00"),("Mercoledì","07:30–19:00"),("Giovedì","07:30–17:00"),("Venerdì","07:30–19:00"),("Sabato","07:30–17:00"),("Domenica","Chiuso")],
 "reviews":[("Daniela P.","Un ambiente molto curato e altamente professionale, le ragazze molto preparate, cordiali e simpaticissime. Qualità eccezionale."),("Chiara C.","Ambiente bello e curato, ragazze brave gentili e solari, ti fanno sentire a tuo agio! Consigliatissimo."),("Francesca G.","Sempre disponibili e super professionali, veloci ma senza tralasciare i dettagli. Fantastiche!")],
},
{
 "slug":"studio-nails-academy-castel-dazzano","pal":PAL[2],
 "name":"Studio Nails Academy","brand":"Studio Nails","cat":"Nail studio & Academy",
 "metadesc":"Studio Nails Academy a Castel d'Azzano (VR): ricostruzione unghie, manicure, pedicure, nail art e corsi professionali. Prenota il tuo appuntamento.",
 "rating":"5,0","nrev":"nuove","phone":"333 331 0986","tel":"+393333310986","wa":"393333310986","email":None,
 "cid":"4901830946432857618","maps_q":"Via+Mascagni+100,+37060+Castel+d'Azzano+VR",
 "address":"Via P. Mascagni 100, 37060 Castel d'Azzano (VR)",
 "hero":ph(NAILS[0]),"split":ph(NAILS[1]),"cta":STOCK[4],
 "h1":"Unghie perfette, in ogni dettaglio","herop":"Ricostruzione, manicure, pedicure e nail art a Castel d'Azzano. E se vuoi imparare, ci sono anche i corsi della nostra academy.",
 "introh":"Il tuo studio unghie a Castel d'Azzano","introp":"Tecnica, cura del dettaglio e prodotti professionali per unghie belle e curate. Da noi trovi anche percorsi di formazione per diventare nail artist.","introextra":"",
 "servh":"I nostri servizi",
 "services":[("\U0001F485","Ricostruzione unghie","Gel e acrilico per unghie resistenti e naturali."),("✨","Manicure","Manicure estetica e curativa con semipermanente."),("\U0001F9B6","Pedicure","Pedicure estetica per piedi curati tutto l'anno."),("\U0001F3A8","Nail art & Corsi","Decorazioni personalizzate e corsi per nail artist.")],
 "splith":"Passione per il dettaglio","splitp":"Ogni set di unghie è studiato su di te: forma, colore e finiture. Lavoriamo con prodotti professionali per un risultato che dura nel tempo.",
 "splitlist":["Prodotti professionali","Igiene e cura in ogni fase","Corsi di formazione dedicati"],
 "pricing":[("Semipermanente","da 20€",["Manicure","Applicazione","Finitura lucida"]),("Ricostruzione","da 40€",["Allungamento gel/acrilico","Forma personalizzata","Nail art base"]),("Refill","da 30€",["Ritocco","Rinforzo","Cambio colore"])],
 "hours":[("Lunedì","14:00–20:00"),("Martedì","09:00–20:00"),("Mercoledì","09:00–20:00"),("Giovedì","09:00–20:00"),("Venerdì","09:00–20:00"),("Sabato","09:00–15:00"),("Domenica","Chiuso")],
 "reviews":[],
},
{
 "slug":"nicole-falzi-beautynails-castel-dazzano","pal":PAL[3],
 "name":"Nicole Falzi BeautyNails","brand":"Nicole Falzi","cat":"Beauty & Nails",
 "metadesc":"Nicole Falzi BeautyNails a Castel d'Azzano (VR): ricostruzione unghie, manicure, pedicure, nail art e trattamenti beauty. 5,0★ su Google.",
 "rating":"5,0","nrev":"3","phone":"388 993 4600","tel":"+393889934600","wa":"393889934600","email":None,
 "cid":"13133275688994249651","maps_q":"Via+Cavour+101,+37060+Castel+d'Azzano+VR",
 "address":"Via Cavour 101, 37060 Castel d'Azzano (VR)",
 "hero":ph(NICOLE[0]),"split":ph(NICOLE[1]),"cta":STOCK[0],
 "h1":"Beauty & unghie, con cura","herop":"Ricostruzione unghie, manicure, pedicure, nail art e trattamenti beauty a Castel d'Azzano. Grande cura del dettaglio in ogni servizio.",
 "introh":"Bellezza e precisione in ogni dettaglio","introp":"Da Nicole Falzi BeautyNails ogni trattamento è pensato per farti sentire curata e a tuo agio, con attenzione ai dettagli e prodotti di qualità.","introextra":"",
 "servh":"I nostri servizi",
 "services":[("\U0001F485","Ricostruzione unghie","Unghie in gel e acrilico, resistenti e naturali."),("✨","Manicure & Pedicure","Cura completa di mani e piedi con semipermanente."),("\U0001F3A8","Nail art","Decorazioni e finiture personalizzate."),("\U0001F33F","Trattamenti beauty","Servizi estetici curati per la tua bellezza.")],
 "splith":"Professionalità e cura dei dettagli","splitp":"Le clienti apprezzano la precisione e la professionalità in ogni servizio. Un ambiente accogliente dove sentirti coccolata.",
 "splitlist":["Grande cura dei dettagli","Prodotti di qualità","Ambiente accogliente"],
 "pricing":[("Semipermanente","da 20€",["Manicure","Applicazione","Finitura"]),("Ricostruzione","da 40€",["Allungamento","Forma su misura","Nail art base"]),("Beauty","da 25€",["Trattamento viso","Ceretta","Cura mani/piedi"])],
 "hours":[("Lunedì","Su appuntamento"),("Martedì","Su appuntamento"),("Mercoledì","Su appuntamento"),("Giovedì","Su appuntamento"),("Venerdì","Su appuntamento"),("Sabato","Su appuntamento"),("Domenica","Chiuso")],
 "reviews":[("Siria B.","Bravissima e molto professionale. Grande cura dei dettagli.")],
},
]

for L in LEADS:
    out=build(L)
    fn=L["slug"]+".html"
    open(fn,"w",encoding="utf-8").write(out)
    print("WROTE",fn,len(out),"bytes")
