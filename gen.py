# -*- coding: utf-8 -*-
import re
KEY="AIzaSyBBHDrAQlPXrn2llGekk77Fcfwu9qpm4ZU"
def ph(ref): return "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference=%s&key=%s"%(ref,KEY)

def rev_section(cards):
    body="\n".join(cards)
    return '<div class="rv-grid">\n      %s\n    </div>\n  </div>\n</section>'%body

# ---------- LOVED (beautispa / variante 1) ----------
L1="AWCwydjU7PF40lQ1S_qSE1P1yCHRIZgvb5YKsxd8HEIEbwq4jRaJ5Ygpw2LCF4p8_HYR8mIOjemPYF8SdjbNussg4Jvg2TlZvp2UISGvGcBOvrGx-xAzka0l9NkjoYbHy2US3VUtmq987xMpCCpYor9QGxZ2S-Feme76327z5An0za_bqtzE03GBLYM4TWKYMq2dtC2wAsU1t9Lb25kWx9WfNBqEa01dPa2BxSRkvT96EVlDSUtBKasB-bYllV4W55iu0LoXuQtRUS2HgWwDA9ETlEeiEu5xsbykVgngxiLFNp0VuYi5Gu6fuCp0x0nd8JICKElNMAUpIzfnprR8IMFMEyer2tTWsQ9UKiwCQ4PPpjutiEe5dbTwtkzW03gEtgRAcNOSlN03fZ4q_axS8kXuUn4IkAsrzDaedQy8uI0L5X3gWQ"
L2="AWCwydh7qo2ZHISDMXpHA4oUpp0avw37Rucbz5fiSSzL9aYqQg_I3Ee9WZxVNlmF9wDPKPdspIdw_vpPNiJ4W8BkLgKsNKv1BpSpVuKJBwE5ulL1O3uktKliMEAwdWA9one0Is3UPf0i4qhixS6M0Vqoaxt8HB0NKd163HD22yRi0aTObs_ttloJVU61Th11ZyLMFYNCjczbBZj1aF3EIIJwfrDOcCXxhl3oE_TWuZOj76VH1XjiBZNmgoGEIo8kMC6dxW3OYxOXUo6Ty0HIymFkb9_6mRVPvUKuDfIGVLMqYYHTj-2Nhssp5XCfGdZ9idqeWle1phdkRLIYnVJK2TWFf1u8AoXC5_vyRAyXNwpdgVJdA_yM2epseAzF9dvEbK3vnIUtZftx2L9H3D3qQvWvg7JQAi8D4BUJ_c-PWqrj2ANsZbne"
L3="AWCwydjedye3gTKs3s05E6VzJkgHuLyf6eXu0pZVRwBFxCU1iWKjSFIcFXTWlLADPRdxjjaf9klke8rdwXjHvBib0QOJ38sEpk9q4jXgGgtRv41-WN0Hak2JvdAVslIUBj35RLnilz8yVmLawud1hq9yLcGQkjj-BeNwzfCZr4E-jQ8uqtJVDc6yVgWrq7yQBKg6AWYdsVUTqiAtNhFF1-8fy7gtYbl6XvF_jrdu3-5BajJ3UTTTMJj_xqgetK2VCmU3c-V-F-R0OYQBg77s9R3KXRAkISDJU_cJyFNdeAiO3H4fKqWUfyla5sfUZI5lgDGbiHFcJVpjJFqOc5l0CHr_It9FjNx_1abT6vq-R_YzhfKoL4ikbN2X5czzPkBtYgb3bXXf_okhVNw0QkiKUJE9bjsseB4azrnmc7T8W_YJkioSGBE"
loved=open("estetiste-beautispa-flagship.html",encoding="utf-8").read()
loved=loved.replace('<a href="#top" class="brand">Bellessere Spa</a>','<a href="#top" class="brand">LOVED</a>')
loved=loved.replace('Bellessere Spa','LOVED Centro Estetico')
loved=loved.replace('<title>LOVED Centro Estetico — Centro estetico &amp; SPA a Affi | Prenota</title>','X')  # noop guard
loved=loved.replace('Studio Beauty Luce','LOVED')
loved=loved.replace('https://images.pexels.com/photos/3757942/pexels-photo-3757942.jpeg?auto=compress&cs=tinysrgb&w=1600',ph(L1))
loved=loved.replace('https://images.pexels.com/photos/3865676/pexels-photo-3865676.jpeg?auto=compress&cs=tinysrgb&w=1000',ph(L2))
loved=loved.replace('https://images.pexels.com/photos/3997989/pexels-photo-3997989.jpeg?auto=compress&cs=tinysrgb&w=1600',ph(L3))
loved=loved.replace('<span class="kick">Centro estetico &amp; Spa · Affi</span>','<span class="kick">Centro estetico · Affi</span>')
loved=loved.replace('Trattamenti viso e corpo, massaggi e percorsi benessere in un\'oasi di relax nel cuore di Verona.','Trattamenti viso e corpo, massaggi, epilazione e unghie in un ambiente curato e accogliente ad Affi.')
loved=loved.replace('info@bellesserespa.it','')
loved=loved.replace('tel:+390450000000','tel:+393396099603')
loved=loved.replace('045 000 0000','339 609 9603')
loved=loved.replace('https://wa.me/390450000000','https://wa.me/393396099603')
# footer contatti block
loved=loved.replace('<div><h4>Contatti</h4><p>Via Esempio 12, Verona<br><a href="tel:+393396099603">339 609 9603</a><br><a href="mailto:"></a></p></div>',
 '<div><h4>Contatti</h4><p><a href="https://maps.google.com/?cid=1067060209038639777" target="_blank" rel="noopener">Via Giovanni Pascoli 42/m, Affi (VR)</a><br><a href="tel:+393396099603">339 609 9603</a><br><a href="https://www.instagram.com/loved_diof" target="_blank" rel="noopener">@loved_diof</a></p></div>')
loved=loved.replace('<div><h4>Orari</h4><p>Mar–Sab 9:00–19:00<br>Lun e Dom chiuso</p></div>','<div><h4>Orari</h4><p>Lun–Ven 8:00–20:00<br>Sab e Dom chiuso</p></div>')
loved=loved.replace('<p>Centro estetico e spa nel cuore di Verona.</p>','<p>Estetica e benessere ad Affi (VR).</p>')
# reviews
loved=re.sub(r'<div class="rv-grid">.*?</section>', rev_section([
 '<div class="rv"><div class="st">★★★★★</div><p>"Simpatia e professionalità! Massima igiene e cura di ogni dettaglio. Antonella e Olena insuperabili!"</p><b>Irene Pitzalis</b></div>',
 '<div class="rv"><div class="st">★★★★★</div><p>"Per noi i migliori: la titolare e tutto lo staff, super professionali e competenti."</p><b>Backstage Events</b></div>']),
 loved, flags=re.S)
# mbar book -> whatsapp
loved=loved.replace('<a href="#prenota" class="book">Prenota</a>','<a href="https://wa.me/393396099603" class="book">WhatsApp</a>')
# title/meta
loved=loved.replace('<title>LOVED Centro Estetico — Centro estetico &amp; SPA a Verona | Prenota</title>','<title>LOVED Centro Estetico — Estetica &amp; benessere ad Affi | Prenota</title>')
loved=loved.replace('content="LOVED Centro Estetico a Verona: trattamenti viso, massaggi, corpo e percorsi benessere. 4,9★ su 160 recensioni. Prenota il tuo momento di relax."','content="LOVED Centro Estetico ad Affi (VR): trattamenti viso, corpo, massaggi, epilazione e unghie. 5★ su 8 recensioni. Prenota il tuo momento di relax."')
# generic Verona cleanup
loved=loved.replace('a Verona','ad Affi').replace('di Verona','di Affi').replace('— Verona','— Affi').replace('Verona','Affi')
open("loved-centro-estetico-affi.html","w",encoding="utf-8").write(loved)
print("LOVED done", len(loved))
