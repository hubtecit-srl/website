# -*- coding: utf-8 -*-
def rep(html, old, new, label, n=1):
    if old not in html:
        print(f"  !! MISS [{label}]")
    return html.replace(old, new, n) if n else html.replace(old,new)

# da Gioia photo refs
G1="AWCwydhX-GLay7RT6z88XTfs3R2Jx0GxYVW_Fn9qwGr2UYeXhF1YEIBhzxaDE-ICIDBBrX0itMCtdh-vKuXbApPZ7RnI6MfNGgsOKEkzEt0yLiN2nZ_dgmwJVp2kuiNy0AIPIE57dH4kZtzpRPs1SnpuyVMIH53yS3Qd5Y3R6MBHdVeqSMknYFxwZ4-OVMLEFei_ouIV3SBKJTAu-hkrieXVF-ZL1wDJfkNVltcUU2SOzLRIAu3YS9mApqdirjvP3jXnPGHrzhLcV3oHniEARjdWsqVVuEurJS__naPMtT9ZKDy2aTV835OsnvmgqSRldlf2eyEtWSkbl3FBxig4vSKOHsVPFnvopEBP3RIAA1I0-4-DT6uvyhHg0bRw29P7uDT7H5giUqihQDvZUf5H_CatstiNp071B8rbEr_c_lbxa9eEfA"
G2="AWCwydhyKyiNXi5DSggc8LfIuiZXHLcBhymCBJ_AuKY0oEUn8iBr-SPcFwtw_UqBPOagymmQcBTRSU5Ky5IpQjH8u-Ql8Vu5sVGz0AA9gsBjYMOLNhIM0AHo5N7fP8rk4DalfPdBtoOnx5lQoCOMqYW5EW_XKWjtIXp_01LOM_r7jriyIuEgTxyQ608d_2dhB7DDDdCzR0fEo9hTIh_mbnvyXdNHHDaq0dVFNsJQcBBzDbnBSTd9s_KwdERM3jnALUVUrLHblnFjNfuKsURDaNgscbsjUiiktQ_rkywLK5oeiypUnKvomcBcIG2xecVFAMvL8bxyKK20Pv7y-CVBsaI3_nlV1jH8HNpzlln5cinNXASpSdUGMMHzR7S30lcX7L1Yw2gGyVCzttd5aI4HR1JywnkqC1bp9SsdS4YNnS6YMzfy9g"
G3="AWCwydggxsN6Ta4pGrYAd9gee3XW7U_InprH-sngdpaZJzPRjTk-fMbGHEKa2FUIphDH1Ov3tbeU47BTauQhsrxGDy1Z36-w0VvhDtlioACRmtHd8dJUMk9XIVUs25Ud_-rt2RwClIFXz0uqJx9MovzpO1YGe7Thkj6czBVKKob93WiPlL7t3pFpZ9jcS7nhY0Xyr-ZIMrF4koUXMh7zExBTn8yfQ_t3mCqt6BA5oAPgLii2pe6Rx9T8RS2RL7q3sN-dnZhDRPc_NL3EJzw9_LgAC3rVURcMKSFCAXrrOZ8uLMkgq5-VOOpRe64NLH-9kpzTSg__ogSGfMNZ12Fb24fNsF7e2xIKTz3HrnTj-KKicY4pDIDAeoeymdqgvuyljQ2eYzzJi4uPB-5XZPH1gYQUMscKB26AK64afRRGV5tfMTTTG29a"
G4="AWCwydgNA8XYlFVHwpSoxzr-4mOwnGeZSkVl5mlQFuI6_Z07LIwZfscI4PrNwU30RDOB8imQmrAKUyQdtvtx_DRZ_zePEpZWySlkA2y0yKNd0v0zii1v-qnu2zCqZNrRPQJ2pGf8xS67b7HlB-GDn25dvNaCj2hxfwcRfhHUX_HU1ujOsut3FbfdFJPWFEVzjMnyBMr7ugS-c7FB5wrdTLoUB8KqgeLSXb4cQ-YiyGBE0fi1mued_iGx9SasDySRMSMwxFKk_OI-dfshpOZ8inV9wyBQTl6mOuyGrgpniuxTXJlrnjeTvfdgqPdOaFD1UsCZPe9T01nq5MHDCBC4giibIbWYW4bK8dxDIX8A77x1U30GxNsrQx8sSmYdDruR-3ZeKEX6h3iLCjeGXXqGa3J8r_mPJFeIs3IlmrpXqGjKKqPU79k1"
G5="AWCwydiu0sRa7BBA9SA9o2eM_BiB3lyglnmZDj5jDk3vLp1Yq04MfSBgtxk91nSsJRvgwVW2dpVxAJZ80I2cmD8fwLk3n2f2XQ5i_W2CPEVOH_9JUmyvgYIZcICjeq9KdYt_InXVTBp64FRA-8ro8ti19qWUpPv0dXX1Ll7aTbfJxpSCpkSL8PcAElqsODDyw8EYckJVMRgOPPvotMp8Une8OmqABzGNQnBdaXsZqkaxN-0Ec-T3owg6sR0-bvA_fEiD-sanlZNCTsZF-OOwGhah3P_t0ug938KXdPw3In3CvuNcCNV8jFeSmRLA6Pk59xdYammyOMhDeZlNwOqcRSfICb1GLaITRHs2pYM9BmCmnkndZ_CwNb8fXQC--HMrNMM_Og72uq8c1vKBCzBb9b4UGP3TTC50llF7n5LSHyLeJysdTbNWSKfV9TOdmGPFsQTu"
G6="AWCwydj_fDRlCBngxDDoWewxHDkH9bijOFclK5r4WFmbqxNaJZzvAca-J_MuOlPb4HH0RUaeP1tWxGofZtb1fMUNOyA2uW-LKAwLQlm9obrbN9xi04RoBwvaqbymyuYnJQeAmIl8UmUYZVOrnAvIsuu2f76R8GXz3ZMyh2Df8hDfZh6ZP2uee53utFlEjn1r14SJRhMx4IPTIjhV6tdAbycPRT0O2ecGodq1uUDpGgWLLVllKvEeMjHtYFf0KodJif_ZNoziwM_PRSL5Bduqw4LqElJR8akqHEt4SCubII4t_hYHltruyd-DGigeqjgxD2vSd7bvm_FNse8BO8N2ROrUZKGdZS0QH4echnQ7S9blNg9IXfD1hKjVnO_NvVCuEeOJ1jZMPX2dwUQ_vvTaZR-uzTf74wAZnxbndHAczmW-m-xgKm0"
# Il Vicoletto template refs
T_HERO="AWCwydj7Gd6EFqrUq_ItFG2C03TCmKOi-tks7gmjMdHn6JJZdk7g4GN3yb-bCgFPLFNIJYypYKAh8DGWK_mwWzv28MLU-irU0jzpvZ1hVqnfgIwkY0SPPZUP-BEBKJMWYQXZ3JpMrHhoxOHAInF2ETyDOYw2qNZUtJwkhi0lepRf2Pout6EvvjyZENQhx9TF76LBtbAV7i9q3Fj2IuYdI6JiICqQlswvnwJ2vAT2JoBfS0oU545CxLkCmvlpFiC55Zcq1AaNG50MbP-Y6o11j_d7OeYw0sAtSKIpyIZyO9H7TyEoaQ39V23983sZ8ZsOkLCdx_Itj6dNqXXcukLWliMdruuM48yjW4jSosJLywyzsICR6X1nFyq3itTgAejvJEqrSez5-zFoB-hKhdplSvl8E23fNzRyoiiBz5I7RhqQQjI"
T_ABOUT="AWCwydhYTIodB_ZJzUCwvuj4XwZMJSWokBaRc9eq3cAadxc1PkZcDPTD9rFH1TdRt0DoLwYQudBcn_SqqVHfsvgD07FTfr3wwQJigG0AMOIZ_OJhQ7-BWpA0G9t1gq7vsJZ8MSL8PiC-XKNm8ii6MeHI26xvWWbmEYqoTOdfCYFcMNY7QMorcsPxFjrbit3J1N9s36tchDvfxcGhcjzsVjJ3txfZxP7CHNB-3T5_gXTQDYAES656qDoo7SYYhzjgxilRjH-jcXG2SRpVBzDJYuIajU0ZM_N1LPVq8zCGLxc6YqEf0ehUMlF3cgWqnQpFcn07kfuuy6NZQfhOSKy1IIMigD1m35ZItEy3lgo8kY7LRjxY7wM1CWmWNtJLQxBZvWsbKyCMs8qlB9eG2hyNcflJ4x5305aziWZjypLnSEKpRd5HsxpsaEA86cVMSlrJG1Sj"
T_G1="AWCwydhlFPh5C29OiUFseKMZ50DXdw1troEKOdJ_CQ2-33bxhCqBwC7tfWX4iAa-xdq48zoy1TUcJwjdkcmfs-fkoiTdjUTLnHHX4BriJD-9Fb6WnR3t7prP95Se7EIyhqZENBC80Xgk7OID9z8Z8z6O3qQPy79VGvi7QFuylG2nATSx_v5SUapaFhO0DMa2kgM0HVuKWSG0g4m5jz5VzF3MeJNByVc5Fz_q8XPgsly6E1_QO_wt60gMZUvNSaIDUTqtc2DI2upWEXTqF663uRAxy8zWuPyW8Sz-APJ2ZzCfwPMUCsctkWrch23tpXHBaLwIRf4PGDlbhXdQOxnI9_AfmyFVUeaJV0hmjBwGIiujvIRyyvZmL-gbLZTQNdGLAeWts8cJGaxB4_g4D9uJzW9BbqPR73LnlFoXCz7z8WFU8SLWhETCDRHi-95_2PxHlD7d"
T_G2="AWCwydjXPmFoUapcS3L4lN9SFvOTa1yQeGHMhjj625E-Ixom9pCZlAu_oAmTLd5Q9B94Nk17-FIl-da8UPAAcFYKr6YV37iIAA6JsD-b9u3YxDrMsAWEq_9xoiXxl6Qwt8olY3GVaOLhapQLt3J1F_iDhGvQl3vucFd6cX96aGk76LQ6m1-Xja_rWqd4A2y-yAC8hSukxQNY9yEjAjBpcddO0tbwlKvXf3ZMd1XGa8uxrMhu4VrOwWrQdXObVNrQIRDgFWBI7ZiV9CldORnUx7JBoEQOs6EQiVKYtRnvO5FpeKe2gDd5g7umpA5TckglhPCqaPoZ45c6z2pD9VjfnXTJ6FDGGXMBcjC0Ucr7Yh3fZb3uL_aKmhxEbC7XNrQes2BbpfXrrUWrOul1VMA8ci1cXKakembDyKWniCDOBmJBLNQhRC--gFaSQhJn6sTFFA"
T_G3="AWCwydgsMwKBs4LdDTdO0SDZCuOukYQqAtlIFJGTbiQf6a3SZQ4gZfyz7XvERoItNfDTGqaKt5pqA6aaJLIMrcLRmODrozN2Hd8quDfXD87Z_aKgsY2xQti-niRa7YbrJxWJKTE80a0CxmdybIEt6z062XZuEx2jEo6YGsBE9DuepZnBN1OUXK9EC-S1_rW0PWaPJ3QV9gtn4wawOntu0I8kjgho5bIu6zVdqDZYQP3P5GgqbCsoZPdWWQXA9PGbk1sOlxt62xxFMs8jtkcAP28IK2zl3oXFhtoh2nvvYWZlTcYnHwXWl6h-XYl1I-shqTQ9eh6W2K6umlgd_YqjjXv6aHTSZV9QBp_-b9B0ZnZY73BX0PulXcz5djg7Ygt3XIeg_qFtQ0LTn35scsYv0FVtiz6Rvh6SEliMIItZYUwmNUEzEfirPjoBDzRL1NXqGQ"
T_G4="AWCwydhEfWweL8OJWvl3D6xAGrj2IQ6a_LFD-Ioplyr99AxF1b2nfCYHHb8JIogcPbdwcNsVuKpAnIQMAhcy_PyW8gsTTllxEcyXwL4__lhwgFm6x46QqJN5jMBnb_Q8_oNDs60CxFOjGrb88eCVrhd0MTxxtoBXuXIaS3MC5KZ75-4JbWrsb9j8iFp0Z-OVdKqvH_PSgO5ky27sZwqdBcLTqxjjmSuj-bzR-UZiP476y-2ZfS55mFVSonIA7RSJdZSozo86fffiwtsdtsk0ORLMAHAUNlTdrb0cJyouBetkHygBQ9sneJz_lgUZSGZH2YQXsbO9ewg7k-UMHEF7cn1dTKOCxCHzbrr0fC2YtAf8bGD1cmC9dzhBXMx-bsWGZ53mMp_n-iipw2feJb2_7d_thntLKD-TL5XjXh5RqYwG8lSgXwhAIOGrbbWg8VpEgJQi"
T_G6="AWCwydhlvN44ifgUDzkvwylKs-DflYhyJzjuC7cROI3nua2H97RZtNSc9PDbDYEni72o-tub0y2C6dkumg7Hsgboj601304ytvfZXbOT8ft4eeI8GRMtADowHRBfv-C_LETjyhor43CQiv9UDlsm7GE3xx_INUyQZ3PudYtAT3siZXYQNP8I7nTW_mDuSp5P1qNb8cnJoUSkgEMKuT9mYRXwFKTU5AYSHB5h1Zv-H9zRm5XKKFzYSmko-hLIjMw_TBTO3Tk33KGhnRE97mUPvWCY8DZ2rqxNKUi_ATe0YAI2gHtr0CLf3MBfUn2C6qfTdrKYOBi2b3o_u0eCcV_8pq03CxdzAHpVLfxr93n3jv7VxKsZrlHf2XE3ZssIvqZe3vb_xUgb2hglEKNZ5B2xW4JMmAvQehHa8lb51Y22AeRB0gBj1jb_"

d=open("il-vicoletto-trattoria-verona.html",encoding="utf-8").read()
# photos (replace refs)
d=rep(d,T_HERO,G1,"hero-bg")
d=rep(d,T_ABOUT,G2,"about-img")
d=rep(d,T_G1,G3,"gal1")
d=rep(d,T_G2,G4,"gal2")
d=rep(d,T_G3,G5,"gal3+5",n=0)  # appears twice
d=rep(d,T_G4,G6,"gal4-wide")
d=rep(d,T_G6,G3,"gal6")
# title/meta
d=rep(d,"<title>Il Vicoletto Trattoria — Cucina tradizionale veronese | Verona</title>","<title>da Gioia — Trattoria ad Asparetto di Cerea (VR) | Prenota</title>","t")
d=rep(d,'content="Il Vicoletto Trattoria, cucina tradizionale veronese nel centro di Verona. Bigoli all\'anatra, pastissada de caval, fegato alla veneta. 4,8★ su 1.842 recensioni. Prenota un tavolo.">','content="da Gioia, trattoria ad Asparetto di Cerea (VR). Cucina casalinga, risotto alla veneta, carne e pesce, pinsa. Clima familiare. 4,8 stelle su Google. Prenota un tavolo.">',"d")
# kicker/hero
d=rep(d,'<div class="kicker">Trattoria · Verona centro</div>','<div class="kicker">Trattoria · Asparetto di Cerea</div>',"kick")
d=rep(d,"<h1>La cucina veronese,<br><em>come una volta</em></h1>","<h1>La trattoria di casa,<br><em>ad Asparetto</em></h1>","h1")
d=rep(d,'<p class="sub">Nel cuore del centro storico, tra vicoli e pietra viva. Piatti della tradizione, materie prime scelte, accoglienza sincera.</p>','<p class="sub">Da Ilaria e Mirko, ad Asparetto di Cerea. Cucina casalinga e genuina, piatti abbondanti e un\'accoglienza che ti fa sentire di famiglia.</p>',"sub")
d=rep(d,"<div>1.842 recensioni Google</div>","<div>87 recensioni Google</div>","meta-rev")
d=rep(d,"<div>Via Santa Maria in Chiavica 5</div>","<div>Via Belle Arti 19, Asparetto</div>","meta-addr")
# about
d=rep(d,"<h2>Un vicolo, una tavola, una tradizione</h2>","<h2>Una scoperta che diventa casa</h2>","abh2")
d=rep(d,"<p>Il Vicoletto è un tempio della cucina tradizionale veronese, quella vera. Un locale intimo ed elegante, curato nei dettagli, dove ogni piatto racconta il territorio.</p>","<p>da Gioia è una trattoria dal clima familiare, dove si torna sempre volentieri. Piatti genuini e abbondanti, dalla carne al pesce, dai risotti agli hamburger: è sempre tutto perfetto.</p>","abp1")
d=rep(d,"<p>Materie prime di altissima qualità, lavorate con maestria e passione: dai bigoli all'anatra alla pastissada de caval, ogni portata è una carezza per il palato. In sala, un servizio attento, gentile e preciso che mette l'ospite al centro.</p>","<p>Il risotto alla veneta è da far invidia ai ristoranti stellati e i dolci sono top. In sala Ilaria e Mirko: due persone splendide, gentili, sempre con il sorriso, che ti trattano come uno di famiglia.</p>","abp2")
d=rep(d,"<div class=\"sign\">— dove si mangia bene e ci si sente a casa</div>","<div class=\"sign\">— dove mangi bene e ti senti in famiglia</div>","sign")
# menu 6 dishes
d=rep(d,'<div class="dish"><div class="r"><h4>Prosciutto & antipasti veronesi</h4><span class="tag">Antipasti</span></div><p>Salumi selezionati e sfizi del territorio per iniziare come si deve.</p></div>','<div class="dish"><div class="r"><h4>Antipasti della casa</h4><span class="tag">Antipasti</span></div><p>Sfizi e salumi genuini per iniziare, con la cura di sempre.</p></div>',"d1")
d=rep(d,'<div class="dish"><div class="r"><h4>Bigoli al sugo d\'anatra</h4><span class="tag">Primi</span></div><p>Il nostro piatto simbolo: pasta fresca e ragù d\'anatra, un classico intramontabile.</p></div>','<div class="dish"><div class="r"><h4>Risotto alla veneta</h4><span class="tag">Primi</span></div><p>Il nostro cavallo di battaglia: mantecato a regola d\'arte, da provare assolutamente.</p></div>',"d2")
d=rep(d,'<div class="dish"><div class="r"><h4>Gnocchi con pastissada de caval</h4><span class="tag">Primi</span></div><p>Gnocchi fatti in casa con l\'iconico stracotto veronese, sapore autentico.</p></div>','<div class="dish"><div class="r"><h4>Pinsa &amp; primi di casa</h4><span class="tag">Primi</span></div><p>Pinsa leggera e primi della tradizione, con ingredienti selezionati.</p></div>',"d3")
d=rep(d,'<div class="dish"><div class="r"><h4>Fegato alla veneta</h4><span class="tag">Secondi</span></div><p>Ricetta della tradizione, morbido e profumato, servito con cura.</p></div>','<div class="dish"><div class="r"><h4>Guancia di vitello brasata</h4><span class="tag">Secondi</span></div><p>Speciale: morbidissima e saporita, cotta lentamente.</p></div>',"d4")
d=rep(d,'<div class="dish"><div class="r"><h4>Secondi di carne del territorio</h4><span class="tag">Secondi</span></div><p>Carni selezionate cucinate secondo le ricette di casa.</p></div>','<div class="dish"><div class="r"><h4>Carne, pesce &amp; hamburger</h4><span class="tag">Secondi</span></div><p>Piatti abbondanti: dalla carne al pesce fino agli hamburger, sempre perfetti.</p></div>',"d5")
d=rep(d,'<div class="dish"><div class="r"><h4>Dolci della casa</h4><span class="tag">Dessert</span></div><p>Piccola pasticceria e dolci al cucchiaio per chiudere in dolcezza.</p></div>','<div class="dish"><div class="r"><h4>Dolci della casa</h4><span class="tag">Dessert</span></div><p>I nostri dolci sono top: il modo giusto per chiudere la serata.</p></div>',"d6")
# reviews
d=rep(d,"<h2>4,8 su 1.842 recensioni</h2>","<h2>4,8 su Google — 87 recensioni</h2>","rvh")
d=rep(d,'“Il prosciutto era divino e i bigoli al sugo d\'anatra meravigliosi. I camerieri gentilissimi, il posto intimo ed elegante. Un meraviglioso posto per mangiare bene e rilassarsi.”','“Personale di sala sublime, gentile e cordiale. Cibo ottimo e super abbondante, il risotto alla veneta da far invidia ai ristoranti stellati. Una bella scoperta, torneremo!”',"rv1")
d=rep(d,'<img src="https://lh3.googleusercontent.com/a-/ALV-UjVx984yTTUmFDvbTwN5HtM4xJ_Oz9QVkZ9nVYLsbgEEGD9X0Hs=s128-c0x00000000-cc-rp-mo-ba2" alt="Genny"><div><b>Genny</b><span>un mese fa</span></div>','<img src="https://lh3.googleusercontent.com/a/ACg8ocLew5IOq66pUSprLDnCtOYTVaxBGjgng68oDSN45nb8Dgredw=s128-c0x00000000-cc-rp-mo-ba3" alt="Glenda"><div><b>Glenda A.</b><span>un mese fa</span></div>',"rv1w")
d=rep(d,'“Ottima esperienza. Abbiamo assaggiato i bigoli all\'anatra e gli gnocchi alla pastissada de caval: entrambi ottimi, la pastissada in particolare era superlativa. Personale eccezionale.”','“Ogni piatto è una bomba: carne, hamburger, pesce o risotto, è sempre tutto perfetto, porzioni abbondanti e prezzi nella media. Un plauso a Ilaria e Mirko, splendidi!”',"rv2")
d=rep(d,'<img src="https://lh3.googleusercontent.com/a-/ALV-UjVk8DCVqpxGajrVkwRCXP737IJXOVFJXTv94nYXptg1VzJfI4d_=s128-c0x00000000-cc-rp-mo-ba2" alt="Laura"><div><b>Laura Sigona</b><span>un mese fa</span></div>','<img src="https://lh3.googleusercontent.com/a-/ALV-UjVWkutShdgfBMB_dsLMvfEBjaGWIlfHfxgXjpPxvoXIEinp1IJk=s128-c0x00000000-cc-rp-mo" alt="Noemi"><div><b>Noemi A.</b><span>11 mesi fa</span></div>',"rv2w")
d=rep(d,'“Locale ben curato, frequentato da molti turisti che il personale gestisce con velocità e gentilezza. Buoni i piatti, attenti alla tradizione locale. Consigliato.”','“Una meravigliosa sorpresa! Gestori simpatici e cordiali, coccolano i clienti con ottimi piatti genuini e succulenti. I dolci sono top! Consigliatissimo.”',"rv3")
d=rep(d,'<img src="https://lh3.googleusercontent.com/a-/ALV-UjV_EJ2HB5iDRiE7G-eNfGQuPthTwBjS890TBz6hnvCujZFJH9Y=s128-c0x00000000-cc-rp-mo-ba5" alt="Enzo"><div><b>Enzo Valentini</b><span>2 mesi fa</span></div>','<img src="https://lh3.googleusercontent.com/a/ACg8ocK8ieCV94PTnLf6JNdRA6by2tOUATOozWrTh0-ETkA9OJl00g=s128-c0x00000000-cc-rp-mo-ba2" alt="Orietta"><div><b>Orietta D.</b><span>9 mesi fa</span></div>',"rv3w")
d=rep(d,"Leggi tutte le 1.842 recensioni su Google →","Leggi tutte le 87 recensioni su Google →","rvfoot")
# hours list
d=rep(d,'<li data-day="1"><span class="d">Lunedì</span><span>12:00–14:30 · 19:00–22:30</span></li>','<li data-day="1"><span class="d">Lunedì</span><span>Chiuso</span></li>',"hl1")
d=rep(d,'<li data-day="2"><span class="d">Martedì</span><span>12:00–14:30 · 19:00–22:30</span></li>','<li data-day="2"><span class="d">Martedì</span><span>Chiuso</span></li>',"hl2")
d=rep(d,'<li data-day="3"><span class="d">Mercoledì</span><span>12:00–14:30 · 19:00–22:30</span></li>','<li data-day="3"><span class="d">Mercoledì</span><span>19:30–22:00</span></li>',"hl3")
d=rep(d,'<li data-day="4"><span class="d">Giovedì</span><span>12:00–14:30 · 19:00–22:30</span></li>','<li data-day="4"><span class="d">Giovedì</span><span>19:30–22:00</span></li>',"hl4")
d=rep(d,'<li data-day="5"><span class="d">Venerdì</span><span>12:00–14:30 · 19:00–23:00</span></li>','<li data-day="5"><span class="d">Venerdì</span><span>19:30–22:00</span></li>',"hl5")
d=rep(d,'<li data-day="6"><span class="d">Sabato</span><span>12:00–15:00 · 19:00–23:00</span></li>','<li data-day="6"><span class="d">Sabato</span><span>19:30–22:00</span></li>',"hl6")
d=rep(d,'<li data-day="0"><span class="d">Domenica</span><span>12:00–15:00 · 19:00–22:30</span></li>','<li data-day="0"><span class="d">Domenica</span><span>12:00–15:00 · 19:30–22:00</span></li>',"hl0")
# JS periods
d=rep(d,"const periods={0:[[1200,1500],[1900,2230]],1:[[1200,1430],[1900,2230]],2:[[1200,1430],[1900,2230]],3:[[1200,1430],[1900,2230]],4:[[1200,1430],[1900,2230]],5:[[1200,1430],[1900,2300]],6:[[1200,1500],[1900,2300]]};","const periods={0:[[1200,1500],[1930,2200]],1:[],2:[],3:[[1930,2200]],4:[[1930,2200]],5:[[1930,2200]],6:[[1930,2200]]};","periods")
# address / map
d=rep(d,"Via Santa Maria in Chiavica 5, 37121 Verona","Via Belle Arti 19, 37053 Asparetto di Cerea (VR)","addr-info")
d=rep(d,"Via+Santa+Maria+in+Chiavica+5,+37121+Verona","Via+Belle+Arti+19,+37053+Asparetto+Cerea+VR","map")
# facebook -> whatsapp (no FB found for da Gioia)
d=rep(d,'<a href="https://www.facebook.com/profile.php?id=100078507787681" target="_blank" rel="noopener" class="btn btn-out">Facebook</a>','<a href="https://wa.me/393509947932" target="_blank" rel="noopener" class="btn btn-out">WhatsApp</a>',"fb-btn")
d=rep(d,'<a href="https://www.facebook.com/profile.php?id=100078507787681" target="_blank" rel="noopener" title="Facebook">f</a>','<a href="https://wa.me/393509947932" target="_blank" rel="noopener" title="WhatsApp">w</a>',"fb-foot")
# footer text
d=rep(d,"Trattoria · Cucina tradizionale veronese","Trattoria · Cucina casalinga ad Asparetto di Cerea","foot-line")
d=rep(d,"© 2026 Il Vicoletto Trattoria · Via Santa Maria in Chiavica 5, Verona · P.IVA da inserire","© 2026 da Gioia Trattoria · Via Belle Arti 19, Asparetto di Cerea (VR)","foot-copy")
# brand + phone + cid global
d=d.replace("Il Vicoletto","da Gioia")
d=d.replace("tel:+390458769827","tel:+393509947932").replace("045 876 9827","350 994 7932")
d=d.replace("8374942607263514723","14045401954028729376")
open("da-gioia-trattoria-cerea.html","w",encoding="utf-8").write(d)
print("da-gioia-trattoria-cerea.html",len(d))
print("DONE dagioia")
