src=open('parrucchieri-rhazor-flagship.html',encoding='utf-8').read()
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
REF="AWCwydhZRYdDIapa2niqelBmQ3e_bIKJnngneKP10TWJ8XVBDhqwMrEb45o_qhkv3B9bdMY9IAzD9IwIcdjbCdhwY71WlwabZlCsFAowj6Xh4hOTa2o03TRyxy87n6D8jy7Gdc2lkLu1I_nRHh_R5CKMJrihufGTsm7jN1TheERjz28mXgcWvBVIvP9MhMtG5fBzrnK3J6dgUPSP46ewAjkyTi9Ri7KUrCZqGik0VxKRjhRxWDhaixF4ivTXMz_yYAGgllg4TfHxTISnfhxEj5KbsbmQMDEouiAdIxgzjFKlzF8tq-BOiWBESndcD1xaRp_igTrB95StvnnfMcC-zvLoaKqlgXHC-GSagK3_D6zh6mHf8tOj2aO0N1uimaRw3HYARxg-Mz-3-koTguNzbyBZrt_zaE9WcZ2ULYRox1jM72lTP__LcxE9zNpZspkP9w"
P12=f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={REF}&key={KEY}"
P8=f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={REF}&key={KEY}"
CID="https://maps.google.com/?cid=5989232254377922410"
R=[
('<title>Barberia Rasoio — Barbiere a Verona | Prenota</title>','<title>Hair Studio — Parrucchiere a Affi | Silvia De Beni</title>'),
('<meta name="description" content="Barberia Rasoio, barbiere a Verona: taglio uomo, rasatura tradizionale, barba e styling. 4,9★ su 200 recensioni. Prenota il tuo appuntamento.">','<meta name="description" content="Hair Studio di Silvia De Beni, parrucchiere a Affi (VR): taglio, piega, colore e trattamenti. 4,7★ su 13 recensioni. Vieni a trovarci.">'),
('<a href="#top" class="brand">Barberia <b>Rasoio</b></a>','<a href="#top" class="brand">Hair <b>Studio</b></a>'),
('''    <span class="kick">Barbiere · Verona</span>
    <h1>Il miglior <span>barbiere</span> della città</h1>
    <p>Taglio uomo, barba e rasatura tradizionale con panno caldo. Stile, precisione e un'esperienza da veri intenditori.</p>
    <div class="hero-cta">
      <a href="#prenota" class="btn btn-gold">Prenota ora</a>
      <a href="#servizi" class="btn btn-ghost">Listino prezzi</a>
    </div>''','''    <span class="kick">Parrucchiere · Affi</span>
    <h1>Il tuo <span>hair studio</span> ad Affi</h1>
    <p>Taglio, piega, colore e trattamenti su misura. La cura dei capelli con la professionalità e la passione di Silvia.</p>
    <div class="hero-cta">
      <a href="#prenota" class="btn btn-gold">Contattaci</a>
      <a href="#servizi" class="btn btn-ghost">I servizi</a>
    </div>'''),
('''    <div class="c"><div><h4>Chiamaci</h4><p><a href="tel:+390450000000">045 000 0000</a></p></div></div>
    <div class="c"><div><h4>Dove siamo</h4><p>Via Esempio 12, Verona</p></div></div>
    <div class="c"><div><h4>Orari</h4><p>Mar–Sab 9:00–19:00</p></div></div>''','''    <div class="c"><div><h4>Orari</h4><p>Lun–Sab 8:30–18:00</p></div></div>
    <div class="c"><div><h4>Dove siamo</h4><p>Via Elena da Persico 8, Affi</p></div></div>
    <div class="c"><div><h4>Su appuntamento</h4><p>Ti aspettiamo in salone</p></div></div>'''),
('''      <div class="serv-c"><div><h3>Taglio uomo</h3><small>Taglio e styling</small></div><span class="dots"></span><span class="price">20€</span></div>
      <div class="serv-c"><div><h3>Taglio &amp; barba</h3><small>Taglio completo + barba</small></div><span class="dots"></span><span class="price">30€</span></div>
      <div class="serv-c"><div><h3>Rasatura tradizionale</h3><small>Rasoio e panno caldo</small></div><span class="dots"></span><span class="price">18€</span></div>
      <div class="serv-c"><div><h3>Sistemazione barba</h3><small>Rifinitura e cura</small></div><span class="dots"></span><span class="price">15€</span></div>
      <div class="serv-c"><div><h3>Taglio bambino</h3><small>Fino a 12 anni</small></div><span class="dots"></span><span class="price">14€</span></div>
      <div class="serv-c"><div><h3>Trattamento capelli</h3><small>Cura e styling</small></div><span class="dots"></span><span class="price">20€</span></div>''','''      <div class="serv-c"><div><h3>Taglio &amp; piega</h3><small>Taglio donna e styling</small></div><span class="dots"></span><span class="price">su richiesta</span></div>
      <div class="serv-c"><div><h3>Colore</h3><small>Colorazione e ritocco</small></div><span class="dots"></span><span class="price">su richiesta</span></div>
      <div class="serv-c"><div><h3>Méches &amp; balayage</h3><small>Schiariture e riflessi</small></div><span class="dots"></span><span class="price">su richiesta</span></div>
      <div class="serv-c"><div><h3>Piega &amp; styling</h3><small>Messa in piega</small></div><span class="dots"></span><span class="price">su richiesta</span></div>
      <div class="serv-c"><div><h3>Trattamenti capelli</h3><small>Cura e ricostruzione</small></div><span class="dots"></span><span class="price">su richiesta</span></div>
      <div class="serv-c"><div><h3>Acconciature</h3><small>Cerimonie ed eventi</small></div><span class="dots"></span><span class="price">su richiesta</span></div>'''),
('<div class="about-img" role="img" aria-label="La barberia"></div>','<div class="about-img" role="img" aria-label="Hair Studio Affi" style="background-image:url('+P12+')"></div>'),
('''      <h2>Un'esperienza da vero barbiere</h2>
      <p>Da Barberia Rasoio ogni cliente è unico. Mani esperte, strumenti di qualità e la tradizione del barbiere di una volta, in un ambiente curato e maschile.</p>
      <ul class="about-list">
        <li><span class="ck">✦</span> Barbieri esperti e appassionati</li>
        <li><span class="ck">✦</span> Rasatura tradizionale con panno caldo</li>
        <li><span class="ck">✦</span> Prodotti professionali per capelli e barba</li>
      </ul>''','''      <h2>La cura dei capelli, da Silvia</h2>
      <p>Da Hair Studio ad Affi, Silvia De Beni si prende cura dei tuoi capelli da anni: ascolto, tecnica e prodotti professionali per un risultato naturale che dura nel tempo.</p>
      <ul class="about-list">
        <li><span class="ck">✦</span> Parrucchiera esperta e appassionata</li>
        <li><span class="ck">✦</span> Consulenza personalizzata su taglio e colore</li>
        <li><span class="ck">✦</span> Prodotti professionali per la cura del capello</li>
      </ul>'''),
('<div class="sec-h"><span class="kick">Galleria</span><h2>I nostri tagli</h2></div>','<div class="sec-h"><span class="kick">Galleria</span><h2>Il nostro salone</h2></div>'),
('''      <img src="https://images.pexels.com/photos/1570806/pexels-photo-1570806.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Taglio 1">
      <img src="https://images.pexels.com/photos/1805600/pexels-photo-1805600.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Taglio 2">
      <img src="https://images.pexels.com/photos/2521617/pexels-photo-2521617.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Taglio 3">
      <img src="https://images.pexels.com/photos/3998429/pexels-photo-3998429.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Taglio 4">''',f'''      <img src="{P8}" alt="Hair Studio Affi">
      <img src="https://images.pexels.com/photos/3993449/pexels-photo-3993449.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Salone">
      <img src="https://images.pexels.com/photos/3757952/pexels-photo-3757952.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Cura dei capelli">
      <img src="https://images.pexels.com/photos/3865711/pexels-photo-3865711.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Dettaglio">'''),
('<div class="sec-h"><span class="kick">Recensioni</span><h2>I nostri clienti</h2></div>','<div class="sec-h"><span class="kick">Recensioni</span><h2>Le nostre clienti</h2></div>'),
('''      <div class="rv"><div class="st">★★★★★</div><p>"Miglior barbiere di Verona. Taglio sempre perfetto e ambiente top."</p><b>Luca M.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"La rasatura col panno caldo è un'altra cosa. Bravissimi e simpatici."</p><b>Andrea P.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Professionali, veloci e curati. Ci porto anche mio figlio."</p><b>Stefano R.</b></div>''','''      <div class="rv"><div class="st">★★★★★</div><p>"Rimasta molto soddisfatta: ha capito perfettamente le mie esigenze, ascoltandomi e consigliandomi in modo professionale."</p><b>Arrietty S.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Da tanti anni è la mia parrucchiera. Molto professionale, cura dei capelli e buoni prodotti. Ambiente rilassante."</p><b>Raffaella B.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Silvia è bravissima nel suo lavoro: una piega che tiene anche dopo giorni. Molto professionale."</p><b>Cliente Google</b></div>'''),
('''    <h2>Prenota il tuo taglio</h2>
    <p>Chiamaci o scrivici su WhatsApp: ti aspettiamo in poltrona.</p>
    <div class="btns">
      <a href="tel:+390450000000" class="btn btn-gold">📞 045 000 0000</a>
      <a href="https://wa.me/390450000000" class="btn btn-ghost">WhatsApp</a>
    </div>''',f'''    <h2>Vieni a trovarci</h2>
    <p>Passa in salone ad Affi per il tuo appuntamento: ti aspettiamo.</p>
    <div class="btns">
      <a href="{CID}" target="_blank" rel="noopener" class="btn btn-gold">📍 Via Elena da Persico 8, Affi</a>
      <a href="#servizi" class="btn btn-ghost">I servizi</a>
    </div>'''),
('''      <div><div class="brand">Barberia <b style="color:var(--gold)">Rasoio</b></div><p>Barbiere tradizionale nel cuore di Verona.</p></div>
      <div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@barberiarasoio.it">info@barberiarasoio.it</a></p></div>
      <div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>''',f'''      <div><div class="brand">Hair <b style="color:var(--gold)">Studio</b></div><p>Parrucchiere ad Affi, nel cuore del paese.</p></div>
      <div><h4>Contatti</h4><p>Via Elena da Persico 8<br>37010 Affi (VR)<br><a href="{CID}" target="_blank" rel="noopener">Apri su Google Maps</a></p></div>
      <div><h4>Orari</h4><p>Lun–Sab 8:30–18:00<br>Domenica chiuso</p></div>'''),
('<div class="foot-bot"><span>© Barberia Rasoio — Verona</span><span>Sito realizzato da HubTec</span></div>','<div class="foot-bot"><span>© Hair Studio — Affi</span><span>Sito realizzato da HubTec</span></div>'),
('''  <a href="tel:+390450000000" class="call">Chiama</a>
  <a href="#prenota" class="book">Prenota</a>''',f'''  <a href="{CID}" target="_blank" rel="noopener" class="call">Mappa</a>
  <a href="#prenota" class="book">Contatti</a>'''),
]
miss=0
for o,n in R:
    if o not in src:
        miss+=1; print("MISS:",o[:70])
    src=src.replace(o,n)
open('hair-studio-affi.html','w',encoding='utf-8').write(src)
print("misses",miss,"len",len(src))
print("leftover Barberia:",src.count('Barberia'),"Rasoio:",src.count('Rasoio'),"Esempio:",src.count('Esempio'),"000 0000:",src.count('000 0000'))
