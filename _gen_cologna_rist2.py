# -*- coding: utf-8 -*-
import re
WARN=[]
def R(h,old,new,req=True):
    if old not in h:
        if req: WARN.append((TAG,old[:70]))
        return h
    return h.replace(old,new)
def cyc(urls):
    i={'n':0}
    def f(_m):
        u=urls[i['n']%len(urls)]; i['n']+=1; return u
    return f
RX_PEX=re.compile(r"https://images\.pexels\.com/photos/[^'\"]+")

# fix Barbesin alt
b=open("osteria-dal-barbesin-cologna-veneta.html",encoding="utf-8").read().replace('alt="Piatto Il Vicoletto"','alt="Piatto Osteria dal Barbesin"')
open("osteria-dal-barbesin-cologna-veneta.html","w",encoding="utf-8").write(b)

LAN=["https://lh3.googleusercontent.com/place-photos/AG9NLjB9p8boRHCQlnaC6oHeqpkUETHj8payb9VAwmVizFJmqLwA1eKyp6BznFwQJU7H5do6f0pJLpyN5ez1uygJqwAgs5pC0rfz-L9eVmpImPZ1_QkdiYOEWUEBgKPPj7m7823gM0stmSYMiWHrXg=s1600-w847",
"https://lh3.googleusercontent.com/place-photos/AG9NLjBxIb9tbCDOt8KdL6T6plfyH8aBcExy1wyTbYAz2PKyX0Iw-vaQ0ZwqMFLMn1JgK_Tk-tbTVBkLp541CYxOiV4chrYS4u8gKtMy0fyaTJzy4v1MzvqqoxPF9W-_80PCk9WJhj40URY16ZIGSA=s1600-w848",
"https://lh3.googleusercontent.com/place-photos/AG9NLjDPGWD6vhjJaQBKQCY9h9Uxk6Bid-q6NJ7v5ylq0tOsYUd_FXoEzFA_d9pn25-HKWLvoLMT0sVTwfauvsmgOEwlR6YeABitduaMJQ0AAAuKCyKno5he0GFz3YjoxJlmafxL2Qhzj30n2aXzzpkabbilLA=s1600-w1200",
"https://lh3.googleusercontent.com/place-photos/AG9NLjBYo1O233qUijhKSPpf4iPpgfHBrNBRSwD-Eafmdn43J7UfhP5RUq37LGG4br_R6T9R4TNntXK0Uf0g5kJXujzpu0aunAvL9VcnajrzhoWMWpVQTI2EMQl36v2z0nZ0eGFLTC3MoUlKQiY=s1600-w1200"]
GAR=["https://lh3.googleusercontent.com/place-photos/AG9NLjC-O7KcL7r4BVnyvYt7FwMEjlh2TTT0xmo6eC06vfZp53QUHrtWY2w9g32fm0fS5zH9pvrczLzPFRXw2lhCFerOKvQcV0Nk8k-joNIFbtF8ZjGRtXNvVgMdMkkuGcqbCoqKKFuxmoJc8XNK6w=s1600-w1024",
"https://lh3.googleusercontent.com/place-photos/AG9NLjDwzInTveIO9k_j8g7de3u1aTcrFS7QxHJTxHbIqp5k1kHNuaSBOFLZtQyfzJuTNzHvqJ71SFqTS1ts_I2COjWuc7YKVF8qlp4umF1wSAKgXWe59xDNofU4wx8CVGHS0qRehdIKuLF5L9slU9jfD7dKTw=s1600-w1200",
"https://lh3.googleusercontent.com/place-photos/AG9NLjAw5gs2j1gWylnrXRSndgtLE6JTbmMSFmhkj2lI6aapBFLbjbup0ZLxDvwdQlCJUbQXUwBblNAXVVncTb5yZC1WFb4mpAnly9nf9jtTv3s4zrBB0OMHzExcxatZq0328zNwLe8_2-aW4s4bCV8=s1600-w1200",
"https://lh3.googleusercontent.com/place-photos/AG9NLjB8WWyzMmfDowEZE7F1VrLTau43BEBtGXZAuPkN24-qjBjtppUyN8g8JbHVHTUQthBLXHQjVUI_Kwhdsm3kkwgVqMzG2n522Behy_DNWPnOEFwiHcpooO-GKscD91XlKPPRM3aa_ltFTvQuU8A=s1600-w1200"]

# ================= LEAD 2: La Lanterna -> atlantic (idx1) MANUAL (landline) =================
TAG="LAN"
h=open("ristorante-atlantic-flagship.html",encoding="utf-8").read()
h=RX_PEX.sub(cyc(LAN),h)
FB="https://www.facebook.com/la.lanterna.14"
h=R(h,'<title>Bistrot Contrada — Cucina moderna a Verona | Prenota</title>','<title>Trattoria La Lanterna — Cucina casereccia a Cologna Veneta (VR) | Prenota</title>')
h=R(h,'content="Bistrot Contrada, cucina moderna nel cuore di Verona. Menù stagionale, cocktail e vini selezionati. 4,8★ su 240 recensioni. Prenota il tuo tavolo.">','content="Trattoria La Lanterna, Via Santa Giustina 25, Cologna Veneta (VR). Cucina casereccia e genuina, cibo fresco. 4,4★ su 376 recensioni Google. Prenota il tuo tavolo.">')
h=h.replace('Bistrot Contrada','Trattoria La Lanterna')
h=R(h,'<span class="kick">Cucina moderna · Verona</span>','<span class="kick">Trattoria · Cologna Veneta</span>')
h=R(h,'<h1 class="display">Sapori di stagione, nel cuore di Verona</h1>','<h1 class="display">Cucina casereccia, nel cuore di Cologna Veneta</h1>')
h=R(h,'<p class="lead">Un bistrot dove la tradizione veneta incontra la cucina contemporanea. Ingredienti locali, cantina selezionata, atmosfera informale.</p>','<p class="lead">Una trattoria di famiglia con piatti genuini e caserecci, ingredienti freschi e un\'accoglienza sincera. In Via Santa Giustina, a Cologna Veneta.</p>')
h=R(h,'<p>Trattoria La Lanterna nasce dalla passione per la materia prima del territorio. Ogni piatto racconta il Veneto con una lettura moderna, curata dallo chef e dalla sua brigata.</p>','<p>La Lanterna nasce dalla passione per la buona tavola. Piatti caserecci, materie prime fresche e ricette della tradizione veneta, come una volta.</p>')
h=R(h,'<p>Una sala accogliente, un servizio attento e una carta dei vini pensata per accompagnare ogni portata: il posto giusto per una cena tra amici o un\'occasione speciale.</p>','<p>Una sala accogliente e un servizio attento e familiare: il posto giusto per un pranzo tra amici o in famiglia.</p>')
h=R(h,'<p>Via Esempio 12<br>37121 Verona (VR)</p>','<p>Via Santa Giustina, 25<br>37044 Cologna Veneta (VR)</p>')
h=R(h,'<p>Mar–Ven 19:00–23:00<br>Sab–Dom 12:30–14:30 · 19:00–23:30<br>Lunedì chiuso</p>','<p>Lun–Ven 11:00–15:00<br>Domenica 11:00–15:00<br>Sabato chiuso</p>')
h=R(h,'<p><a href="tel:+390450000000">045 000 0000</a><br><a href="mailto:info@bistrotcontrada.it">info@bistrotcontrada.it</a></p>','<p><a href="tel:+39044285481">0442 85481</a><br><a href="'+FB+'" target="_blank" rel="noopener">Seguici su Facebook</a></p>')
# reviews
h=R(h,'<h2>4,8 su 240 recensioni</h2>','<h2>4,4 su 376 recensioni</h2>')
h=R(h,'<p>"Cena eccezionale, piatti curati e servizio impeccabile. Torneremo di sicuro."</p><b>Giulia M.</b>','<p>"Siamo stati per un compleanno in famiglia. C\'eravamo già stati e torniamo sempre volentieri."</p><b>Onorina Iscaro · Google</b>')
h=R(h,'<p>"Ambiente elegante ma informale. Il risotto all\'Amarone è da provare."</p><b>Marco T.</b>','<p>"Questi sono i posti che piacciono a me: cibo genuino e casereccio, le foto parlano da sole."</p><b>Riccardo Franco · Google</b>')
h=R(h,'<p>"Ottima carta dei vini e personale gentilissimo. Consigliatissimo."</p><b>Elena R.</b>','<p>"Tutto fresco, personale giovane e gioviale. Location perfetta per un pranzo veloce o in famiglia."</p><b>Damiano Gandini · Google</b>')
h=R(h,'<p>Siamo aperti dal martedì alla domenica. Per gruppi o eventi speciali, chiamaci: troveremo la soluzione migliore per voi.</p>','<p>Siamo aperti a pranzo, dal lunedì alla domenica (sabato chiuso). Per gruppi o occasioni speciali, chiamaci: troveremo la soluzione migliore per voi.</p>')
# footer hours
h=R(h,'<p>Mar–Ven 19–23<br>Sab–Dom 12:30–14:30 · 19–23:30<br>Lun chiuso</p>','<p>Lun–Ven 11–15<br>Domenica 11–15<br>Sabato chiuso</p>')
h=R(h,'<span>© Trattoria La Lanterna — Verona</span>','<span>© 2026 Trattoria La Lanterna · Cologna Veneta (VR)</span>')
# CTAs: manual -> no whatsapp, use Facebook
h=h.replace('<a href="https://wa.me/390450000000" class="btn btn-out">WhatsApp</a>','<a href="'+FB+'" target="_blank" rel="noopener" class="btn btn-out">Facebook</a>')
h=h.replace('<a href="https://wa.me/390450000000" class="wa">WhatsApp</a>','<a href="'+FB+'" target="_blank" rel="noopener" class="wa">Facebook</a>')
h=h.replace('Chiama 045 000 0000','Chiama 0442 85481')
h=h.replace('tel:+390450000000','tel:+39044285481')
h=h.replace('045 000 0000','0442 85481')
open("trattoria-la-lanterna-cologna-veneta.html","w",encoding="utf-8").write(h)
print("LANTERNA | pexels_left",len(RX_PEX.findall(h)),"| contrada_left",h.count("Contrada"),"| placeholder",h.count("0450000000")+h.count("045 000 0000"),"| verona_std",len(re.findall(r'Verona(?!le)',h))-h.count('Cologna'))

# ================= LEAD 3: La Gargote -> auburn (idx2) WHATSAPP (mobile) =================
TAG="GAR"
h=open("ristorante-auburn-flagship.html",encoding="utf-8").read()
h=RX_PEX.sub(cyc(GAR),h)
FB="https://www.facebook.com/La-Gargote-Paninoteca-296329040820786"
WA="https://wa.me/393332304019"
h=h.replace('Osteria del Fuoco','La Gargote')
h=R(h,'<title>La Gargote — Cucina di brace a Verona | Prenota</title>','<title>La Gargote — Paninoteca & Bar a Cologna Veneta (VR) | Ordina</title>')
h=R(h,'content="La Gargote, cucina di brace e sapori decisi a Verona. Carni, primi della tradizione, cantina locale. 4,7★ su 180 recensioni. Prenota il tuo tavolo.">','content="La Gargote, paninoteca e bar a Cologna Veneta (VR), Piazza Mazzini 5. Panini, piadine, bruschette e aperitivi. 4,5★ su 462 recensioni Google. Vieni a trovarci.">')
h=R(h,'<span class="kick">Cucina di brace · Verona</span>','<span class="kick">Paninoteca & Bar · Cologna Veneta</span>')
h=R(h,'<h1>Il gusto del fuoco</h1>','<h1>Panini, sfizi & aperitivi</h1>')
h=R(h,'<p>Carni alla brace, primi della tradizione e una cantina che racconta il territorio. Nel cuore di Verona.</p>','<p>Panini generosi, piadine, bruschette e taglieri, con un ottimo aperitivo. In Piazza Mazzini, nel cuore di Cologna Veneta.</p>')
h=R(h,'<span class="kick">Un\'esperienza unica</span>','<span class="kick">Un locale di famiglia</span>')
h=R(h,'<h2>Sapori decisi, materie prime scelte</h2>','<h2>Porzioni generose, qualità e sorriso</h2>')
h=R(h,'<p>All\'La Gargote la cucina parte dalla brace e dalla stagionalità. Piatti generosi, servizio caloroso e un ambiente rustico ed elegante insieme.</p>','<p>La Gargote è un bar e paninoteca a conduzione familiare: panini, piadine e bruschette con materie prime scelte, porzioni abbondanti e un servizio sempre gentile.</p>')
# menu rewrite: replace Primi and brace categories
h=R(h,'''      <div class="menu-cat">
        <h3>Primi</h3>
        <div class="dish"><div><h5>Pastissada de caval</h5><span>Con gnocchi fatti in casa</span></div><div class="price">15 €</div></div>
        <div class="dish"><div><h5>Tagliatelle al ragù</h5><span>Ragù lungo di manzo</span></div><div class="price">13 €</div></div>
        <div class="dish"><div><h5>Risotto all'Amarone</h5><span>Mantecato al Monte Veronese</span></div><div class="price">16 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Dalla brace</h3>
        <div class="dish"><div><h5>Costata di scottona</h5><span>Alla griglia, 500g</span></div><div class="price">28 €</div></div>
        <div class="dish"><div><h5>Grigliata mista</h5><span>Selezione di carni alla brace</span></div><div class="price">24 €</div></div>
        <div class="dish"><div><h5>Costine glassate</h5><span>Marinate e cotte lentamente</span></div><div class="price">18 €</div></div>
      </div>''','''      <div class="menu-cat">
        <h3>Panini & Piadine</h3>
        <div class="dish"><div><h5>Panino gourmet</h5><span>Pane di casa, ingredienti scelti</span></div><div class="price">8 €</div></div>
        <div class="dish"><div><h5>Piadina classica</h5><span>Crudo, squacquerone, rucola</span></div><div class="price">7 €</div></div>
        <div class="dish"><div><h5>Club sandwich</h5><span>Con patatine fritte</span></div><div class="price">9 €</div></div>
      </div>
      <div class="menu-cat">
        <h3>Bruschette & Sfizi</h3>
        <div class="dish"><div><h5>Bruschette miste</h5><span>Pane di casa, condimenti freschi</span></div><div class="price">6 €</div></div>
        <div class="dish"><div><h5>Tagliere aperitivo</h5><span>Salumi e formaggi del territorio</span></div><div class="price">12 €</div></div>
        <div class="dish"><div><h5>Patatine & sfizi</h5><span>Fritti misti da condividere</span></div><div class="price">5 €</div></div>
      </div>''')
h=R(h,'<h5>Calice Amarone</h5><span>Selezione della casa</span></div><div class="price">10 €</div></div>\n        <div class="dish"><div><h5>Sbrisolona</h5><span>Con zabaione</span></div><div class="price">7 €</div></div>','<h5>Aperol Spritz</h5><span>Il nostro aperitivo</span></div><div class="price">5 €</div></div>\n        <div class="dish"><div><h5>Dolce della casa</h5><span>Chiedi la disponibilità</span></div><div class="price">5 €</div></div>')
# address / hours / contacts
h=R(h,'<div class="addr-row"><h4>Indirizzo</h4><p>Via Esempio 12, 37121 Verona (VR)</p></div>','<div class="addr-row"><h4>Indirizzo</h4><p>Piazza Mazzini, 5, 37044 Cologna Veneta (VR)</p></div>')
h=R(h,'<div class="addr-row"><h4>Orari</h4><p>Mar–Dom 12:00–14:30 · 19:00–23:00<br>Lunedì chiuso</p></div>','<div class="addr-row"><h4>Orari</h4><p>Aperto a pranzo, aperitivo e cena<br>Consulta gli orari aggiornati su Google</p></div>')
h=R(h,'<div class="addr-row"><h4>Contatti</h4><p><a href="tel:+390450000000">045 000 0000</a> · <a href="mailto:info@osteriadelfuoco.it">info@osteriadelfuoco.it</a></p></div>','<div class="addr-row"><h4>Contatti</h4><p><a href="tel:+393332304019">333 230 4019</a> · <a href="'+FB+'" target="_blank" rel="noopener">Facebook</a></p></div>')
# reviews
h=R(h,'<h2>4,7 su 180 recensioni</h2>','<h2>4,5 su 462 recensioni</h2>')
h=R(h,'<p>"Carne alla brace strepitosa e porzioni generose. Tornerò presto!"</p><b>Andrea B.</b>','<p>"Ottima esperienza. Vasta scelta di panini, piadine e bruschette. Porzioni enormi e ottima qualità."</p><b>Noemi Tomasi · Google</b>')
h=R(h,'<p>"Atmosfera calda e piatti della tradizione fatti come si deve."</p><b>Sara P.</b>','<p>"Un bar a conduzione familiare che fa la differenza: gentilezza, disponibilità e qualità."</p><b>Gianenrico Fiumicetti · Google</b>')
h=R(h,'<p>"Ottimo rapporto qualità-prezzo, personale gentilissimo."</p><b>Luca V.</b>','<p>"Luogo curato e accogliente, servizio impeccabile. Ottimi aperitivi e pietanze."</p><b>Antonella Dal Ben · Google</b>')
h=R(h,'<p>Per gruppi, eventi o serate speciali chiamaci: ti aspettiamo attorno al fuoco.</p>','<p>Per un panino al volo, un aperitivo o una serata tra amici: ti aspettiamo in Piazza Mazzini. Scrivici su WhatsApp!</p>')
h=R(h,'<span>© La Gargote — Verona</span>','<span>© 2026 La Gargote · Cologna Veneta (VR)</span>')
h=R(h,'<p>Cucina di brace e sapori del territorio, a Verona.</p>','<p>Paninoteca e bar nel cuore di Cologna Veneta.</p>')
# footer hours
h=R(h,'<p>Mar–Dom 12–14:30<br>19–23<br>Lun chiuso</p>','<p>Aperto a pranzo,<br>aperitivo e cena<br>Orari su Google</p>')
# CTAs whatsapp valid
h=h.replace('https://wa.me/390450000000',WA)
h=h.replace('Chiama 045 000 0000','Chiama 333 230 4019')
h=h.replace('tel:+390450000000','tel:+393332304019')
h=h.replace('045 000 0000','333 230 4019')
open("la-gargote-cologna-veneta.html","w",encoding="utf-8").write(h)
print("GARGOTE | pexels_left",len(RX_PEX.findall(h)),"| fuoco_left",h.count("Fuoco")+h.count("del Fuoco"),"| brace_left",h.lower().count("brace"),"| placeholder",h.count("0450000000")+h.count("045 000 0000"))
print("WARN:",WARN)
