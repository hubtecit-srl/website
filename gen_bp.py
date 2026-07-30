# -*- coding: utf-8 -*-
h = open('estetiste-beautispa-flagship.html', encoding='utf-8').read()

R = [
('<title>Bellessere Spa — Centro estetico &amp; SPA a Verona | Prenota</title>',
 '<title>Beauty Point — Centro estetico a Colognola ai Colli</title>'),
('<meta name="description" content="Bellessere Spa a Verona: trattamenti viso, massaggi, corpo e percorsi benessere. 4,9★ su 160 recensioni. Prenota il tuo momento di relax.">',
 '<meta name="description" content="Beauty Point a Colognola ai Colli (Via Strà 70): trattamenti viso, massaggi, corpo e benessere. Recensioni 5★ su Google. Prenota il tuo momento di relax.">'),
('Centro estetico &amp; Spa · Verona','Centro estetico · Colognola ai Colli'),
('in un\'oasi di relax nel cuore di Verona.','in un\'oasi di relax a Colognola ai Colli.'),
# reviews
('"Un\'oasi di pace. Massaggio fantastico e personale attentissimo."','"Personale gentilissimo, super disponibili. 5 stelline meritatissime."'),
('<b>Valentina R.</b>','<b>Martina Lombardo</b>'),
('"Trattamento viso eccezionale, pelle rinata. Tornerò di sicuro."','"Una certezza! Personale preparato e attento alle esigenze di ogni cliente. Atmosfera rilassante, ti senti coccolata."'),
('<b>Chiara D.</b>','<b>Laura Guarinoni</b>'),
('"Ambiente curato e rilassante, professioniste vere. Consigliato!"','"Personale molto gentile e preparato, offre un ottimo servizio."'),
('<b>Federica M.</b>','<b>Marica Brentonego</b>'),
# CTA
('📞 045 000 0000','📞 366 377 0444'),
('tel:+390450000000','tel:+393663770444'),
('https://wa.me/390450000000','https://wa.me/393663770444'),
# footer contacts block
('<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+393663770444">045 000 0000</a><br><a href="mailto:info@bellesserespa.it">info@bellesserespa.it</a></p></div>',
 '<div><h4>Contatti</h4><p><a href="https://maps.google.com/?cid=2066421032683320857" target="_blank" rel="noopener">Via Strà 70, 37030 Colognola ai Colli (VR)</a><br><a href="tel:+393663770444">366 377 0444</a></p></div>'),
('<p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p>',
 '<p>Mar 11:00–20:00 · Mer–Ven 9:00–18:00<br>Sab 9:00–14:00 · Lun e Dom chiuso</p>'),
('Bellessere Spa','Beauty Point'),
]
for a,b in R:
    assert a in h, 'BP MISS: '+a[:70]
    h = h.replace(a,b)
# any remaining display "045 000 0000"
h = h.replace('045 000 0000','366 377 0444')
# remaining Verona -> Colognola ai Colli
h = h.replace('Verona','Colognola ai Colli')

open('beauty-point-colognola-ai-colli.html','w',encoding='utf-8').write(h)
print('WROTE beauty-point-colognola-ai-colli.html', len(h))
# sanity: no leftovers
for bad in ['bellesserespa','Via Esempio','045 000 0000','390450000000','Bellessere']:
    print(bad, '->', h.count(bad))
