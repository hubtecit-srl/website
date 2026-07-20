src=open('dentisti-dentique-flagship.html',encoding='utf-8').read()
CID="https://maps.google.com/?cid=10604484846312157914"
R=[
('<title>Clinica Dentale Aurora — Dentista a Verona | Prenota</title>','<title>Studio Dentistico Dr. Giuseppe Scala — Dentista a Affi</title>'),
('<meta name="description" content="Clinica Dentale Aurora a Verona: prevenzione, implantologia, ortodonzia e sbiancamento. 4,8★ su 190 recensioni. Prenota il tuo appuntamento.">','<meta name="description" content="Studio dentistico del Dr. Giuseppe Scala a Affi (VR): igiene, prevenzione e cure dentali per adulti e bambini. Via Napoleone 8. Prenota una visita.">'),
('<a href="#top" class="brand"><span class="mk">🦷</span> Aurora</a>','<a href="#top" class="brand"><span class="mk">🦷</span> Dr. Scala</a>'),
('<span class="kick">Clinica dentale · Verona</span>','<span class="kick">Studio dentistico · Affi</span>'),
('<p>Alla Clinica Aurora uniamo prevenzione, tecnologia e un tocco umano. Cure delicate per adulti e bambini, in un ambiente sereno.</p>','<p>Nello studio del Dr. Giuseppe Scala ad Affi trovi prevenzione, cure attente e un rapporto di fiducia, per adulti e bambini, in un ambiente sereno.</p>'),
('''    <div class="stat"><div class="n">15+</div><p>Anni di esperienza</p></div>
    <div class="stat"><div class="n">8K+</div><p>Pazienti trattati</p></div>
    <div class="stat"><div class="n">4,8★</div><p>190 recensioni</p></div>
    <div class="stat"><div class="n">6</div><p>Specialisti</p></div>''','''    <div class="stat"><div class="n">Affi</div><p>Via Napoleone 8</p></div>
    <div class="stat"><div class="n">Lun–Ven</div><p>Su appuntamento</p></div>
    <div class="stat"><div class="n">🦷</div><p>Cure per tutta la famiglia</p></div>
    <div class="stat"><div class="n">✓</div><p>Prima visita conoscitiva</p></div>'''),
('''      <h2>Una clinica dove sentirti a tuo agio</h2>
      <p>Da anni ci prendiamo cura del sorriso delle famiglie di Verona. Il nostro approccio unisce competenza clinica e ascolto, per farti vivere ogni visita con serenità.</p>
      <ul class="about-list">
        <li><span class="ck">✓</span> Prima visita e preventivo gratuiti</li>
        <li><span class="ck">✓</span> Tecnologia digitale e cure poco invasive</li>
        <li><span class="ck">✓</span> Finanziamenti a tasso zero</li>
      </ul>''','''      <h2>Uno studio dove sentirti a tuo agio</h2>
      <p>Da anni il Dr. Giuseppe Scala si prende cura del sorriso dei pazienti di Affi e dintorni, unendo competenza clinica e ascolto per farti vivere ogni visita con serenità.</p>
      <ul class="about-list">
        <li><span class="ck">✓</span> Prima visita conoscitiva su appuntamento</li>
        <li><span class="ck">✓</span> Attenzione alla prevenzione</li>
        <li><span class="ck">✓</span> Cure per adulti e bambini</li>
      </ul>'''),
('<details class="faq-item"><summary>Come prenoto un appuntamento?</summary><div class="a">Puoi chiamarci, scriverci su WhatsApp o inviarci una mail: ti richiamiamo noi.</div></details>','<details class="faq-item"><summary>Come prenoto un appuntamento?</summary><div class="a">Puoi chiamare lo studio allo 045 723 5188 negli orari di apertura: fisseremo insieme l\'appuntamento.</div></details>'),
('''<section class="reviews">
  <div class="wrap">
    <div class="sec-h"><span class="kick">Recensioni</span><h2>La voce dei nostri pazienti</h2></div>
    <div class="rv-grid">
      <div class="rv"><div class="st">★★★★★</div><p>"Personale gentilissimo e cure indolori. Finalmente un dentista di fiducia."</p><b>Marta G.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Clinica moderna e accogliente, i miei figli non hanno più paura!"</p><b>Davide L.</b></div>
      <div class="rv"><div class="st">★★★★★</div><p>"Preventivo chiaro e lavoro perfetto sull'impianto. Consigliata."</p><b>Elena S.</b></div>
    </div>
  </div>
</section>

''',''),
('''    <h2>Prenota il tuo appuntamento</h2>
    <p>Chiamaci o scrivici su WhatsApp: troviamo insieme l'orario più comodo. Prima visita gratuita.</p>
    <div class="btns">
      <a href="tel:+390450000000" class="btn btn-white">📞 045 000 0000</a>
      <a href="https://wa.me/390450000000" class="btn btn-y">WhatsApp</a>
    </div>''','''    <h2>Prenota il tuo appuntamento</h2>
    <p>Chiama lo studio negli orari di apertura: troviamo insieme l'orario più comodo per te.</p>
    <div class="btns">
      <a href="tel:+390457235188" class="btn btn-white">📞 045 723 5188</a>
      <a href="CIDPLACEHOLDER" target="_blank" rel="noopener" class="btn btn-y">📍 Via Napoleone 8, Affi</a>
    </div>'''),
('''      <div><div class="brand" style="color:#fff">🦷 Clinica Aurora</div><p>Cure dentali per tutta la famiglia, a Verona.</p></div>
      <div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@clinicaaurora.it">info@clinicaaurora.it</a></p></div>
      <div><h4>Orari</h4><p>Lun–Ven 9:00–19:00<br>Sab 9:00–13:00</p></div>''','''      <div><div class="brand" style="color:#fff">🦷 Studio Dr. Scala</div><p>Studio dentistico a Affi (VR).</p></div>
      <div><h4>Contatti</h4><p>Via Napoleone 8<br>37010 Affi (VR)<br><a href="tel:+390457235188">045 723 5188</a></p></div>
      <div><h4>Orari</h4><p>Lun–Gio 9:00–12:30 · 14:00–19:00<br>Ven 9:00–13:00<br>Sab–Dom chiuso</p></div>'''),
('<div class="foot-bot"><span>© Clinica Dentale Aurora — Verona</span><span>Sito realizzato da HubTec</span></div>','<div class="foot-bot"><span>© Studio Dentistico Dr. Giuseppe Scala — Affi</span><span>Sito realizzato da HubTec</span></div>'),
('  <a href="tel:+390450000000" class="call">Chiama</a>','  <a href="tel:+390457235188" class="call">Chiama</a>'),
]
miss=0
for o,n in R:
    if o not in src:
        miss+=1; print("MISS:",repr(o[:60]))
    src=src.replace(o,n)
src=src.replace("CIDPLACEHOLDER",CID)
open('studio-scala-affi.html','w',encoding='utf-8').write(src)
print("misses",miss,"len",len(src))
print("leftover Aurora:",src.count('Aurora'),"Esempio:",src.count('Esempio'),"000 0000:",src.count('000 0000'),"reviews sec:",src.count('class="reviews"'))
