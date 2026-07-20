src=open('estetiste-lesya-flagship.html',encoding='utf-8').read()
CID="https://maps.google.com/?cid=7990009959645563564"
R=[
('<title>Studio Beauty Luce — Estetica &amp; benessere naturale a Verona</title>','<title>Beautyandsun di Lia Adami — Centro estetico a Affi</title>'),
('<meta name="description" content="Studio Beauty Luce a Verona: trattamenti viso e corpo naturali, epilazione, unghie e benessere. 4,8★ su 140 recensioni. Prenota il tuo appuntamento.">','<meta name="description" content="Beautyandsun di Lia Adami, centro estetico a Affi (VR): trattamenti viso e corpo, epilazione, unghie e benessere. Vieni a trovarci.">'),
('<a href="#top" class="brand">Beauty Luce</a>','<a href="#top" class="brand">Beautyandsun</a>'),
('<span class="kick">Estetica &amp; benessere · Verona</span>','<span class="kick">Estetica &amp; benessere · Affi</span>'),
('<p>Trattamenti viso e corpo con prodotti naturali, epilazione e unghie. Un piccolo studio dove ti senti a casa.</p>','<p>Trattamenti viso e corpo, epilazione e unghie in un ambiente accogliente ad Affi. La cura di sé, su misura, con Lia.</p>'),
('''      <ul class="hours-list">
        <li><span>Lunedì</span><span>Chiuso</span></li>
        <li><span>Martedì – Venerdì</span><span>9:00 – 19:00</span></li>
        <li><span>Sabato</span><span>9:00 – 17:00</span></li>
        <li><span>Domenica</span><span>Chiuso</span></li>
      </ul>''','''      <ul class="hours-list">
        <li><span>Lunedì – Venerdì</span><span>9:00 – 18:00</span></li>
        <li><span>Sabato</span><span>Chiuso</span></li>
        <li><span>Domenica</span><span>Chiuso</span></li>
      </ul>'''),
('''<section class="reviews">
  <div class="wrap">
    <div class="sec-h"><span class="kick">Recensioni</span><h2>Le parole delle clienti</h2></div>
    <div class="rv-grid">
      <div class="rv"><div class="st">★★★★★</div><p>"Mani d'oro e prodotti naturali. La mia pelle non è mai stata così bene."</p><b>Alice T.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Ambiente accogliente e cura dei dettagli. Mi sento sempre coccolata."</p><b>Roberta C.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Professionale e gentile. Consiglio a tutte lo studio Beauty Luce!"</p><b>Silvia N.</b></div>
    </div>
  </div>
</section>

''',''),
('''    <h2>Prenota il tuo momento di cura</h2>
    <p>Chiamaci o scrivici su WhatsApp: ti aspettiamo nel nostro studio.</p>
    <div class="btns">
      <a href="tel:+390450000000" class="btn btn-light">📞 045 000 0000</a>
      <a href="https://wa.me/390450000000" class="btn btn-glass">WhatsApp</a>
    </div>''','''    <h2>Vieni a trovarci</h2>
    <p>Passa nel nostro studio ad Affi per il tuo momento di cura: ti aspettiamo.</p>
    <div class="btns">
      <a href="CIDPLACEHOLDER" target="_blank" rel="noopener" class="btn btn-light">📍 Via G. Pascoli 35, Affi</a>
      <a href="#orari" class="btn btn-glass">Orari</a>
    </div>'''),
('''      <div><div class="brand" style="color:#fff">Beauty Luce</div><p>Estetica e benessere naturale a Verona.</p></div>
      <div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@beautyluce.it">info@beautyluce.it</a></p></div>
      <div><h4>Orari</h4><p>Mar–Ven 9:00–19:00<br>Sab 9:00–17:00</p></div>''','''      <div><div class="brand" style="color:#fff">Beautyandsun</div><p>Centro estetico a Affi (VR).</p></div>
      <div><h4>Contatti</h4><p>Via Giovanni Pascoli 35<br>37010 Affi (VR)<br><a href="CIDPLACEHOLDER" target="_blank" rel="noopener">Apri su Google Maps</a></p></div>
      <div><h4>Orari</h4><p>Lun–Ven 9:00–18:00<br>Sab–Dom chiuso</p></div>'''),
('<div class="foot-bot"><span>© Studio Beauty Luce — Verona</span><span>Sito realizzato da HubTec</span></div>','<div class="foot-bot"><span>© Beautyandsun di Lia Adami — Affi</span><span>Sito realizzato da HubTec</span></div>'),
('''  <a href="tel:+390450000000" class="call">Chiama</a>
  <a href="#prenota" class="book">Prenota</a>''','''  <a href="CIDPLACEHOLDER" target="_blank" rel="noopener" class="call">Mappa</a>
  <a href="#prenota" class="book">Contatti</a>'''),
]
miss=0
for o,n in R:
    if o not in src:
        miss+=1; print("MISS:",repr(o[:60]))
    src=src.replace(o,n)
src=src.replace("CIDPLACEHOLDER",CID)
open('beautyandsun-affi.html','w',encoding='utf-8').write(src)
print("misses",miss,"len",len(src))
print("leftover Beauty Luce:",src.count('Beauty Luce'),"Esempio:",src.count('Esempio'),"000 0000:",src.count('000 0000'),"reviews sec:",src.count('class="reviews"'))
