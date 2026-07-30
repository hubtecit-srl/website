# -*- coding: utf-8 -*-
import re

# ============ LEAD 1: Estetica Nynfea (template estetica-anna-verona.html) ============
src = open('estetica-anna-verona.html', encoding='utf-8').read()
h = src

refs = [
"AWCwydjVcxWtFrx1qSMzE1zlhNEEHax6zud343rnlnXB_PkwGBls2Uwvvbm-9l8NLn8TrUTSPMD1eTSzfHCTA-0bZVe8jF_aa-ob4aft4_sqfMyoB7FDXrh__bLQuIUfI0oEg0XgIooNrp3Pdz7Q2HNouq-GklMdz_E38uDJQckgO8M2m803G5htreIVli1z_-CYGhaqauROEpblDcTLezyHcJnh8EXXEUAB0BwlJrpmKI9ANpjYlCtbe9S_YqfpzXTHhkbNvhRx7OvWRmlfVtnRT9Vqn0b6tvs18jhwwYEHg-jbQJFr9s5w8qt1rUk1ZHAuCuoaAs39CNzAPt8RmpEKedfwndnceAOsQ0jSOtbbwMOKvb1fJMU8X8MoYqYG-VhDVeLab8f4QgjvCfaYH0ez49CgDlcaMjQ5XqM-eHDKPBCbsA",
"AWCwydislqaFRBeZ5tjW3D0dLQm0o7KN1BTNi1dDPCYAEQbdqsmWxtR7Qi8s3QjV9MQLI-ByZPEDQ2bi91suj311J82p6LmCcyFfipJaP1SMYi8mMnMRaZN9WC2Ru28NJoit3QqxVWRj0zYUJbdgjmr7VQFjOqA85Sn5oNCi82gOpws78cGdjcKJF9WqHu27FZr-xRK766xcIk02yDo6LwgWZxm1jrdVIvyCVgVt2LeKixKGbP6ul0oTAfBMuxJnOFCOaCFDHDJgeb7gM2993Jh5FY1zvpZ8pazG1AyRKR2oMegut7eRmy2qXYIiZ8o6emD7saohxZ244zTaQ_VarykQDfxe5igkO2lL7eIVFo51qxhie3OIVyMfa-ret6iT_TwOSWONLs0A-YMxdXxNGTbhbTIA5R0v4TMZTuqnSJt1Xtw",
"AWCwydiTdawQs0-UQ19p3OYwUaS70y0SpE7g5Z7arQO_K4Un_DDRqvVHWrLGVZZZ-_gA37A0KN9OvBDdrDA0t1lCKRdVyTmQfim8ZrJgtg9VJO2d4ix6_0WXxMCMw1y1RrhgJGKylMNrLcIJ8hfT6HGpNU_7x1d8LZLql0NSuXs5Tskj15YLRx-Kn24JuqKJBpniL7k5U4ylBiUGpJU03Jj1kR9qJorakBF_S1Hz--HM5gUdv5sWq34sWU8Kn5x2jYn9FkCVCxfAjV7uUETW5UqC8Pwq1l3_AF8y6fRFhWA_pP6oMzVJ6Zp5-8o7cqoRyhT_fck1LD51sle4jkzkfwfY4D05OTbUhAvZ99FD8mskkLNR6W2G928vumcRuelNN0SW0r4RoLjuPhSkrhDcxRrNd6OEOfHNETmB1d-7QO8S13H_2d2X",
]
cnt = {'i':0}
def repl_ref(m):
    r = refs[cnt['i'] % 3]; cnt['i'] += 1
    return 'photo_reference=' + r + '&'
h = re.sub(r'photo_reference=[^&]+&', repl_ref, h)

R = [
('<title>Estetica Anna — Centro estetico a Verona</title>',
 '<title>Estetica Nynfea — Centro estetico a Colognola ai Colli</title>'),
('<meta name="description" content="Estetica Anna, centro estetico a Verona in Via Ghetto 63B. Trattamenti viso, corpo, sopracciglia e abbronzatura con prodotti naturali. 4,9★ su 109 recensioni.">',
 '<meta name="description" content="Estetica Nynfea di Sabrina Zanini, centro estetico a Colognola ai Colli in Piazza Donatore 1. Trattamenti viso, corpo, sopracciglia e abbronzatura. 5,0★ su Google.">'),
('045 862 1514','340 670 7816'),
('+390458621514','+393406707816'),
('ESTETICA ANNA VERONA','ESTETICA NYNFEA COLOGNOLA'),
('Estetica Anna','Estetica Nynfea'),
('Centro estetico · Verona','Centro estetico · Colognola ai Colli'),
('Un angolo di benessere in Via Ghetto, dove prendersi cura di sé diventa un piccolo rito di coccole.',
 'Un angolo di benessere in Piazza Donatore, a Colognola ai Colli, dove prendersi cura di sé diventa un piccolo rito di coccole.'),
('<div class="c">4,9<small>★ 109 REC.</small></div>',
 '<div class="c">5,0<small>★ 9 REC.</small></div>'),
('<h2>Un ambiente accogliente e curato, dove Anna e Maria mettono passione, gentilezza e prodotti naturali in ogni gesto.</h2>',
 '<h2>Un ambiente accogliente e curato, dove Sabrina mette passione, gentilezza e attenzione in ogni gesto.</h2>'),
('<h2>Bellezza autentica,<br>con cura naturale</h2>',
 '<h2>Bellezza autentica,<br>con cura e passione</h2>'),
('Anna e Maria ti accolgono sempre con un sorriso e tanta competenza.',
 'Sabrina ti accoglie sempre con un sorriso e tanta competenza.'),
('<p>Utilizziamo prodotti di origine naturale, delicati anche sulle pelli più sensibili, e ti consigliamo con sincerità il percorso più adatto a te.</p>',
 '<p>Ogni trattamento è pensato su misura per te, con attenzione e delicatezza, per farti sentire subito a tuo agio.</p>'),
('<p>Lampada solare professionale Ergoline per un colorito sano e uniforme tutto l\'anno.</p>',
 '<p>Un colorito sano e uniforme tutto l\'anno, in tutta sicurezza.</p>'),
# review main blockquote + author
('Trattamento viso purificante e idratante, poi una maschera per borse e occhiaie. Tutti prodotti naturali, si sente la differenza sulla pelle sensibile. Anna ti fa sentire a tuo agio: consiglio a tutti!',
 'Luogo molto carino, titolare gentile e disponibile. Professionalità e simpatia ad ogni visita: consiglio!'),
('https://lh3.googleusercontent.com/a-/ALV-UjVJN_yK6gvCMXEIgctNxEtCPSJdUPO1sgeQqBx10D0E9P6EmhQ=s128-c0x00000000-cc-rp-mo',
 'https://lh3.googleusercontent.com/a-/ALV-UjUl_PyhRfoMUGtUOLQeOLoV-l1X7tek9dLNzm1lNZtb8_j4XOXI=s128-c0x00000000-cc-rp-mo'),
('<b>Vittoria Toffalini</b>','<b>Elena Luperini</b>'),
('“Bravissima e super precisa! Prezzi molto onesti, sincera nei consigli e ti mette a tuo agio. Ambiente super accogliente: ci si sente a casa!”',
 '“Gentilissima e bravissima... consiglio!”'),
('<b>Stefania Morabito</b>','<b>Francesca Fra</b>'),
('“Centro estetico eccellente: gentilezza e professionalità di alto livello. Personale sempre accogliente. Ottima la lampada solare Ergoline!”',
 '“Professionalità e simpatia!”'),
('<b>Davide Moletta</b>','<b>Monica Bertoldi</b>'),
('Tutte le 109 recensioni su Google','Tutte le 9 recensioni su Google'),
('4526940053737465846','7576507479791775756'),
('Via Ghetto 63 B, 37137 Verona (VR)','Piazza Donatore 1, 37030 Colognola ai Colli (VR)'),
('Via Ghetto 63B, 37137 Verona','Piazza Donatore 1, 37030 Colognola ai Colli'),
('https://www.google.com/maps?q=Via+Ghetto+63B,+37137+Verona&output=embed',
 'https://www.google.com/maps?q=Piazza+Donatore+1,+37030+Colognola+ai+Colli&output=embed'),
('const periods={1:[900,1830],2:[900,1830],3:[900,1830],4:[900,1830],5:[900,1830],6:null,0:null};',
 'const periods={1:null,2:[830,1900],3:[830,1900],4:[830,1900],5:[830,1900],6:[900,1700],0:null};'),
]
for a,b in R:
    assert a in h, 'NYNFEA MISS: '+a[:60]
    h = h.replace(a,b)

# hours list
hours_new = '''<ul class="hours-list" id="hoursList">
          <li data-day="1"><span class="d">Lunedì</span><span>Chiuso</span></li>
          <li data-day="2"><span class="d">Martedì</span><span>08:30–12:30 · 14:30–19:00</span></li>
          <li data-day="3"><span class="d">Mercoledì</span><span>08:30–12:30 · 14:30–19:00</span></li>
          <li data-day="4"><span class="d">Giovedì</span><span>08:30–12:30 · 14:30–19:00</span></li>
          <li data-day="5"><span class="d">Venerdì</span><span>08:30–12:30 · 14:30–19:00</span></li>
          <li data-day="6"><span class="d">Sabato</span><span>09:00–17:00</span></li>
          <li data-day="0"><span class="d">Domenica</span><span>Chiuso</span></li>
        </ul>'''
h = re.sub(r'<ul class="hours-list" id="hoursList">.*?</ul>', lambda m: hours_new, h, flags=re.S)

open('estetica-nynfea-colognola-ai-colli.html','w',encoding='utf-8').write(h)
print('WROTE estetica-nynfea-colognola-ai-colli.html', len(h))
