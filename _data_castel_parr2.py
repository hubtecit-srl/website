# -*- coding: utf-8 -*-
from _gen_castel import build, ph, STOCK

PAL={
 0:{"teal":"#01796f","teald":"#015d55","dark":"#12312d","gold":"#b89664","cream":"#f5f2ea","soft":"#eef4f1","ov1":"rgba(18,49,45,.82)","ov2":"rgba(18,49,45,.42)","ctaov":"rgba(18,49,45,.78)","herokick":"#a9d8cf"},
 1:{"teal":"#a8657c","teald":"#8d4f66","dark":"#2c1c24","gold":"#c9a36b","cream":"#f7f1f3","soft":"#f3e9ed","ov1":"rgba(44,28,36,.82)","ov2":"rgba(44,28,36,.42)","ctaov":"rgba(44,28,36,.78)","herokick":"#e7c3d1"},
 2:{"teal":"#6d5ba3","teald":"#584a86","dark":"#241f33","gold":"#c6a15b","cream":"#f4f2f8","soft":"#eeeaf4","ov1":"rgba(36,31,51,.82)","ov2":"rgba(36,31,51,.42)","ctaov":"rgba(36,31,51,.78)","herokick":"#cabfe6"},
 3:{"teal":"#a9822f","teald":"#8a6a25","dark":"#2b2415","gold":"#d8b45a","cream":"#f8f4ea","soft":"#f2ecdd","ov1":"rgba(43,36,21,.82)","ov2":"rgba(43,36,21,.42)","ctaov":"rgba(43,36,21,.78)","herokick":"#ecd9a6"},
}

NOSE=["AWCwydjwTzuri2RkDfkekmTOpLKsvtytKOZ3KlWWX_gJVsRd26xbxDNYTOhURWarqtgq8zJq5s1aK7g_fdeyl8lBJBokLHl_aRVWmfCDrX22EzodnxBsjfEN171Rsa3a1VDgJLZSUlP8B4cd0rF7_I9tCCD8T3ZzvkxHjlfV52n4ulHzfNcQQzuTaYuv3rwNRrCgf2fP6-TsW8dj2n3fV7nzm3RlIw7FbfMOc6jLhHooUqTd_Jsl21hcKXmlGkjWKWtZ4Sr2vNaxgBr7jzyGEdSQwJV4YBliPGXHEbtqJSNGoFMIDCQNX9pjquUql8HZdwBnK93QGBd8cmfCRUk9Dfom1FQdSB8VvbV-seA9-Jw4kDBW_EEb1VR71_QtMwbvZbpII9mrG6ZLCyShftmsYAb_85OnY_IQ_o0iOybsGwqcvzU5jQE",
"AWCwydiCW6ZvRuCnlmdP8iJkYHTsgnEREC9swEQwFhnBlQdjxJo1Xj4avvXPo7suWBskpyZCqIYXMzJJTqqSeYmnja2flPthSbVA_zAe-LoJ1YjBr_JtqABjUBfInHjuZRbLRmeIcTMOKrrhcUvgaSHuka-fQ5d7WZBnrxqDtOvFfZRcZpvX4pebW7NngfLX3VBu_Yz2qMAroyyomUj1yvTUER1oLusQSrm79dE5db1rM2dmkOEO4LEUdekuwwn7bv2yDf7jzLVgxRF69cmDW12H1kRp3BUpGn6xgX6B-Voj6a3HWE6wfHtZ5He0_MMo24GvU_gIDsaSfAgfOl9rNHQ0Ey6M795t8p5zwEq_4Tpvcx-Kwrh8IwM0WZmCXJrHRF9AKIwkY-OykNdYdEnTH-EIe91OpXs2eKt_z1E27Uo1PSk"]
GIO=["AWCwydiRFdIz_Km_O5Erq5rmPiQYJ2eVe4az4GfQ_FsutoTvniDW70LYXE9eqSe557H9QRIgBGyDHWGbEUND4C0picHZIAzLVW-TZyBAtWF1iycnhfpyFJ7O8KKnMxSJUDmJ19x16tY1EL8L8yFX-f-vPdwYaDjSuLtU-Wf3f94RKBQu31r7JeS-BCvAK5HTD0p_WVRm9lgzGzrX7B0Kl0CgFTDxyspmshc6DawZVDxV6ub2XIXzNMwgkfXgcqoOqvFnYQqBmYDaFovUt-i7pT-f63HKUvq48m_L6FmsQ5W0jKIidXIGFPS1etUNZ379gRgUFJA0ZvQMO2ByHEHjcthbhUzYRwa6NZawTzJBYrY7W3uWGFS5mhGYjSUoLvsRvzBZZIsN3qVDgmSnQZpvJ9qYsbZDin6kQaa5n4sH4NFkJ8OhNA",
"AWCwydjE5fErm-oJ8TLWqvjkXNiVoODCA1f-5K_3yZdq9awkdjrzHj5IebkZDNO4iHrFOKl7IKGVTnDXZ222oVlqI0FjQ1XUV4TltzNtGBCHEWOIXd6zSF9QLh4NZzEfgU29gDKNqP1XKELA5kSWq7VI5UcGDW8Y5MWv66iFgmj07wRaMuOpzTiFXsJ877VmJLqZ9FUrASMyn4F0XQZ_UGDABbjeBq7P3vO9te2pUibZz4w3pKBSt9P4b_WOq0GiWPL3bQSCM6-KtS9Ik6uXyY40fiTDTS-WB_S6SIRmqXKLi5J4QR7LRZwX-JJg19R4-VJnds6JQ6-8NW7QZcDAvjNRjeEkMdgK-GTSxHTMHwfyjaDv_KoqQW_j0pBPXnoWsdQfglTnanUdJbUMh9Q3xtmjNMJgFvstGVQTZ9J35WiONL5PHg"]
LISA=["AWCwydiLQj_Fm14k76-4LS6LsiWxWUQsPUWvbLGjdzKoWGffVPjGfrEwrygdUTqxXQ5wnF6x7ZVM1ZxpO80J5CWjc-jm2rgpihipz_SoaxIzS2F3WfV0UujUoKLyX0UQyVEGH61k4zTtuUI_Ti-TNrI0MQiAyQr0KojBNcl26V3Rb6JEuW76TF7cC-AlZYarj2m4SdMBhtS83ld-fR67W23IXCV1fD8I_9RuIBPTqapgnALJbRZArRg9fzSO-jqBffLDDfoqKYlkd0GzzmB5E458rxy4NNOpA9ZlxIAYUKwR1BQ4mB783am1_NZ01L0nwczpQdxhaUIrku5kd-xdlX29OktPr7Bvy3O7eyUb0hipPn3ggJ_hTrzdII_YqdboOQcHqC_UedX92Se4WGR5bQ4DFBxriGhKhAyQjH_5Ukk5S0TmRn1y",
"AWCwydjs5ripjgaayNNT1DYtNig1ccZV-oTQkA11NrVS0WXmX-f5oi1TyK8EilE1201kT5S_kOlg4xSfX09BwRTlsPERT91xnRnPeQz3vtuRN8wzyz0313jkiG0gWujkT-VWg3RHmFpOKNmnNNyR59oORPMSdPkdKOPPrgApyO_rEkAko41D4nLWVy4omDV5EfGcfTQwnAoZHtklEz2yCe5BhF9He7bko2UpJ-w44JpFjqovO_xhRvxhRR0joiWM3CuR387wq46tNZt6ZaOshmD3Bt9g5rWuT3VhNgwkZNQfbecAk0YfFv2O8H8z8DpgcttBJO307L8MrVrQn6x97Jg2esUwfC8ArSUfLqZ9wsC7js30Nbfj8JqN6OeekBfLs9luuNunzvYDP5t2RpTOd_zn8LfFUK-Dsj_fgyDihLC3y3P_vEo"]
TESTA=["AWCwydgUaxeY2htBl-ONoueR5S1nun9-seyUMQ2Zww8i9ngVOQXaT1IH2uYMTF0BaeS1_-KMaNbWTq_BvL4qAUP5An_iFr_Q8LdJ3FIZersFbZnRaer9pHUOwANDMd6tl-sbzRwxob5Q9awQ7JsWIKoSmVWbNVNSbt35gcnTDAC8zDbLlbYWCEmfbresEQO-0ekJLTI1gZkVswQ7B6QH-oE8MNHmsiBhqQo2JRHJdMzVQf5EVfA6bApwrkpkbXnxkLDvqJX2h8rTIN6tPsVRLzBMHGiVRXmDKjKCOUyuIkYwSF8h3zYBq_zs8DuSdjL0XpwBEExoykkyAbCmjQwOIBL23_BpANjra8EekYrx8XUlZNlfzhtVjKqkslodFDD4zyzz09feKn58nVP2kPnlO2BJSbXoGOS1feZQcdtIVycJDtTfx0w",
"AWCwydhWpN8sVbc9KEtKQClxuAsmf24WpY-PlccJTz74tsOESv6FG1vRsUnr1R5iyMRdbMtxYWeDmJdWnbPu0vvAstqh9TWsgTBIzhnFU10XFTGZFoWDofCyeokFkrCdyb1p_MmRMlxKw_RwQcrnjuWVXrmHPGwzVUktTbWxl4wvqGHUclmH_qTxIT5_ycgM4QcdL9DNv1SnJTI0J5gN_N3nEUEy6Rin3uTkTmX8bDpXSWa15q5Eg9impDVFzffwcLEbLopzc_dNA1EP-YIiaqZ91OMss0Z6gP18cr-niC1bBnlt5nTSTS9Qd6K_-KwgWAXkXmjeM9vy_3kVw41h_KvAWHacGHHOddr25W5QYFcQna5SssQeB4IeBwgNRhYIbFL325rFbflNraME5eDZtVscyuqZ7sP6o1Xcg-a90XZ1qiBbcQ"]

LEADS=[
{
 "slug":"nose-parrucchieri-castel-dazzano","pal":PAL[0],
 "name":"NOSE' Parrucchieri","brand":"NOSE'","cat":"Parrucchiere",
 "metadesc":"NOSE' Parrucchieri a Castel d'Azzano (VR): taglio, colore, schiariture ed effetti naturali, acconciature e trattamenti. 4,8★ su 103 recensioni Google.",
 "rating":"4,8","nrev":"103","phone":"045 221 1639","tel":"+390452211639","wa":None,"email":None,
 "cid":"12211229553593254833","maps_q":"Via+Marconi+98,+37060+Castel+d'Azzano+VR",
 "address":"Via Marconi 98, 37060 Castel d'Azzano (VR)",
 "hero":ph(NOSE[0]),"split":ph(NOSE[1]),"cta":STOCK[1],
 "h1":"Il tuo look, curato nei dettagli","herop":"Taglio, colore e schiariture dall'effetto naturale a Castel d'Azzano. Un team preparato che ascolta e consiglia il meglio per i tuoi capelli.",
 "introh":"Il salone di fiducia a Castel d'Azzano","introp":"Da NOSE' Parrucchieri ci prendiamo cura di te con competenza, in particolare nella gestione del colore e delle schiariture dall'effetto naturale.","introextra":"Taglio donna e uomo, piega, colore, acconciature e trattamenti su misura.",
 "servh":"I nostri servizi",
 "services":[("✂️","Taglio & Piega","Tagli personalizzati e pieghe studiate sul tuo viso e stile."),("\U0001F3A8","Colore & Schiariture","Colore, balayage e schiariture con effetto naturale."),("\U0001F491","Acconciature","Raccolti e acconciature per cerimonie ed eventi speciali."),("✨","Trattamenti","Trattamenti ricostruttivi per capelli sani e luminosi.")],
 "splith":"Competenza e passione, dal primo taglio","splitp":"Le clienti ci scelgono per la professionalità, la cura del colore e la capacità di consigliare sempre il meglio, risolvendo anche le situazioni più difficili.",
 "splitlist":["Team preparato e sempre aggiornato","Specialisti del colore e delle schiariture","Consulenza personalizzata"],
 "pricing":[("Taglio & Piega","da 25€",["Consulenza look","Taglio","Piega"]),("Colore & Schiariture","da 45€",["Colore o balayage","Trattamento","Piega"]),("Acconciatura","da 35€",["Prova acconciatura","Styling","Finish"])],
 "hours":[("Lunedì","Chiuso"),("Martedì","Chiuso"),("Mercoledì","09:00–18:00"),("Giovedì","09:00–18:00"),("Venerdì","09:00–18:00"),("Sabato","09:00–18:00"),("Domenica","Chiuso")],
 "reviews":[("Chiara B.","Esperienza decisamente positiva, apprezzate in particolar modo le schiariture con effetto molto naturale! Il personale è sempre preparato e disponibile."),("Elena R.","Bravi bravi bravi e ancora bravi! Molto gentili, disponibili, attenti alle esigenze del cliente e capaci di consigliarti il meglio."),("Rita","Molto soddisfatta. Grande competenza e preparazione, soprattutto nella gestione del colore. Decisamente consigliato.")],
},
{
 "slug":"giorgio-laboratorio-di-stile-castel-dazzano","pal":PAL[1],
 "name":"Giorgio Laboratorio di Stile","brand":"Giorgio","cat":"Parrucchiere",
 "metadesc":"Giorgio Laboratorio di Stile a Castel d'Azzano (VR): taglio, colore, piega e trattamenti in un salone accogliente e curato. 4,7★ su 99 recensioni Google.",
 "rating":"4,7","nrev":"99","phone":"045 512677","tel":"+39045512677","wa":None,"email":None,
 "cid":"18297920119972295690","maps_q":"Via+Marconi+83,+37060+Castel+d'Azzano+VR",
 "address":"Via Marconi 83, 37060 Castel d'Azzano (VR)",
 "hero":ph(GIO[0]),"split":ph(GIO[1]),"cta":STOCK[2],
 "h1":"Un laboratorio di stile per i tuoi capelli","herop":"Taglio, colore e trattamenti con grande professionalità e passione, in un ambiente accogliente e rilassante a Castel d'Azzano.",
 "introh":"Professionalità e passione per il tuo capello","introp":"Da Giorgio Laboratorio di Stile ogni cliente riceve attenzione ai minimi dettagli, in un clima accogliente e tranquillo, affidandosi a mani esperte.","introextra":"Taglio, colore, piega, trattamenti e consulenza look personalizzata.",
 "servh":"I nostri servizi",
 "services":[("✂️","Taglio & Styling","Tagli su misura e styling curato per uomo e donna."),("\U0001F3A8","Colore","Colore, riﬂessature e trattamenti coloranti di qualità."),("✨","Trattamenti","Trattamenti ricostruttivi e di cura per capelli forti e sani."),("\U0001F4AB","Consulenza","Consulenza look personalizzata sul tuo viso e stile.")],
 "splith":"Attenti ai minimi dettagli","splitp":"Un salone dove ambiente rilassante, personale qualificato e vera passione per il mestiere fanno la differenza in ogni servizio.",
 "splitlist":["Grande professionalità e cura","Ambiente accogliente e pulito","Team cordiale e qualificato"],
 "pricing":[("Taglio & Piega","da 25€",["Consulenza look","Taglio","Piega"]),("Colore & Trattamento","da 45€",["Colore","Trattamento","Piega"]),("Percorso capello","da 55€",["Diagnosi capello","Trattamento mirato","Styling"])],
 "hours":[("Lunedì","Chiuso"),("Martedì","08:30–12:00 · 14:30–19:00"),("Mercoledì","08:30–20:00"),("Giovedì","08:30–12:00 · 14:30–20:00"),("Venerdì","08:30–18:00"),("Sabato","08:30–18:00"),("Domenica","Chiuso")],
 "reviews":[("Laura S.","Grande professionalità, attenzione al cliente e una grande passione per il proprio lavoro rendono questo salone TOP! Non ho mai avuto capelli così belli."),("Romina F.","Che dire se non il TOP... personale cordiale e qualificato, ambiente rilassante e Giorgio è un vero professionista, attento ai minimi particolari."),("Sara P.","Esperienza super positiva, clima accogliente e tranquillo. Mi sono affidata a mani esperte e sono uscita felicissima.")],
},
{
 "slug":"lisa-style-castel-dazzano","pal":PAL[2],
 "name":"Lisa Style","brand":"Lisa Style","cat":"Parrucchiere",
 "metadesc":"Lisa Style a Castel d'Azzano (VR): parrucchiera specializzata in colore e cura del capello, taglio, piega e trattamenti. 5,0★ su 25 recensioni Google.",
 "rating":"5,0","nrev":"25","phone":"340 837 3491","tel":"+393408373491","wa":"393408373491","email":None,
 "cid":"14374740748838774235","maps_q":"Via+Cecco+Angiolieri,+37060+Castel+d'Azzano+VR",
 "address":"Via Cecco Angiolieri, 37060 Castel d'Azzano (VR)",
 "hero":ph(LISA[0]),"split":ph(LISA[1]),"cta":STOCK[3],
 "h1":"Colore e cura del capello, su misura per te","herop":"Da oltre vent'anni taglio, colore e trattamenti con prodotti professionali di alta qualità, a Castel d'Azzano. Con Lisa i capelli sono in ottime mani.",
 "introh":"La tua parrucchiera di fiducia","introp":"Il punto di forza di Lisa Style sono le colorazioni: colore che non rovina il capello e lo rende morbido, con attenzione e prodotti professionali di alta qualità.","introextra":"Taglio, piega, colore, trattamenti e cura del capello per tutta la famiglia.",
 "servh":"I nostri servizi",
 "services":[("\U0001F3A8","Colore","Colorazioni che rispettano e ammorbidiscono il capello."),("✂️","Taglio & Piega","Tagli e pieghe personalizzati per ogni tipo di capello."),("✨","Trattamenti","Trattamenti professionali per capelli morbidi e sani."),("\U0001F491","Acconciature","Acconciature e styling per ogni occasione.")],
 "splith":"Una professionista di cui ci si fida","splitp":"Le clienti la seguono da oltre vent'anni: professionalità, attenzione alle esigenze e cura del capello con prodotti di alta qualità.",
 "splitlist":["Specialista delle colorazioni","Prodotti professionali di qualità","Rapporto di fiducia con le clienti"],
 "pricing":[("Taglio & Piega","da 22€",["Consulenza","Taglio","Piega"]),("Colore & Trattamento","da 40€",["Colore delicato","Trattamento","Piega"]),("Cura del capello","da 30€",["Diagnosi","Trattamento mirato","Styling"])],
 "hours":[("Lunedì","Chiuso"),("Martedì","09:00–18:00"),("Mercoledì","09:00–18:00"),("Giovedì","09:00–18:00"),("Venerdì","09:00–18:00"),("Sabato","09:00–17:00"),("Domenica","Chiuso")],
 "reviews":[("Alessandra C.","Ormai ci conosciamo da più di 20 anni e non affiderei i miei capelli (e ora anche quelli di mia figlia) a nessun altro. Una grande professionista."),("Sonia B.","Lisa è in gambissima, il suo punto di forza sono le colorazioni: non rovina i capelli e li rende morbidi."),("Rosanna M.","Professionale, attenta alle esigenze delle clienti e alla cura del capello con prodotti professionali di alta qualità.")],
},
{
 "slug":"a-testa-alta-castel-dazzano","pal":PAL[3],
 "name":"A Testa Alta di Casarotti Denise","brand":"A Testa Alta","cat":"Parrucchiere",
 "metadesc":"A Testa Alta di Casarotti Denise a Castel d'Azzano (VR): taglio, colore, consulenza look e acconciature con cura del dettaglio. 5,0★ su Google.",
 "rating":"5,0","nrev":"14","phone":"345 452 2491","tel":"+393454522491","wa":"393454522491","email":None,
 "cid":"12313372640221335360","maps_q":"Via+Vittorio+Alfieri+7c,+37060+Castel+d'Azzano+VR",
 "address":"Via Vittorio Alfieri 7c, 37060 Castel d'Azzano (VR)",
 "hero":ph(TESTA[0]),"split":ph(TESTA[1]),"cta":STOCK[4],
 "h1":"Il tuo stile, curato con il sorriso","herop":"Denise ti accoglie con professionalità e simpatia: taglio, colore e consulenza look pensati sulle tue esigenze, a Castel d'Azzano.",
 "introh":"Un salone accogliente, con cura del dettaglio","introp":"Da A Testa Alta ogni cliente viene ascoltato: dopo una consulenza si sceglie insieme la soluzione migliore di colore e taglio, sempre con il sorriso.","introextra":"Taglio donna e uomo, colore, consulenza look, piega e acconciature.",
 "servh":"I nostri servizi",
 "services":[("✂️","Taglio","Tagli personalizzati anche per chi ha pochi capelli, con cura del dettaglio."),("\U0001F3A8","Colore","Colore e consulenza per trovare la nuance giusta per te."),("\U0001F4AC","Consulenza look","Ascolto delle tue esigenze e proposta della soluzione migliore."),("\U0001F491","Acconciature","Styling e acconciature per ogni occasione.")],
 "splith":"Ti ascolta e ti mette a tuo agio","splitp":"Denise è una professionista solare e attenta: cura ogni dettaglio, ascolta le richieste e ti accoglie sempre con il sorriso.",
 "splitlist":["Grande cura del dettaglio","Consulenza personalizzata","Accoglienza calorosa e sorridente"],
 "pricing":[("Taglio & Piega","da 22€",["Consulenza look","Taglio","Piega"]),("Colore & Trattamento","da 40€",["Colore","Trattamento","Piega"]),("Consulenza & Restyling","da 30€",["Analisi viso","Proposta look","Styling"])],
 "hours":[("Lunedì","11:30–19:30"),("Martedì","08:00–17:00"),("Mercoledì","Chiuso"),("Giovedì","08:00–17:00"),("Venerdì","11:30–19:30"),("Sabato","08:00–16:00"),("Domenica","Chiuso")],
 "reviews":[("Davide C.","Denise è una ragazza solare e simpatica nonché grande professionista, attenta a curare il dettaglio e a venire incontro alle esigenze del cliente."),("Elisa P.","Molto consigliato! Denise ha ascoltato le mie richieste e dopo una consulenza abbiamo capito la soluzione migliore di colore e taglio."),("Francesca M.","Denise è molto attenta alle esigenze della cliente, le ascolta e le consiglia per ottenere il risultato voluto e molto di più.")],
},
]

for L in LEADS:
    out=build(L)
    fn=L["slug"]+".html"
    open(fn,"w",encoding="utf-8").write(out)
    print("WROTE",fn,len(out),"bytes")
