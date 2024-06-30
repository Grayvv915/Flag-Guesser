import tkinter as tk
import random
from PIL import Image, ImageTk

countries_flags = {
    "Andorra":"ad.png",
    "Emiratos Árabes Unidos":"ae.png",
    "Afganistán":"af.png",
    "Antigua y Barbuda":"ag.png",
    "Albania":"al.png",
    "Armenia":"am.png",
    "Angola":"ao.png",
    "Antártica":"aq.png",
    "Argentina":"ar.png",
    "Samoa Americana":"as.png",
    "Austria":"at.png",
    "Australia":"au.png",
    "Azerbaiyán":"az.png",
    "Bosnia y Herzegovina":"ba.png",
    "Bárbados":"bb.png",
    "Bangladés":"bd.png",
    "Bélgica":"be.png",
    "Burkina Faso":"bf.png",
    "Bulgaria":"bg.png",
    "Baréin":"bh.png",
    "Burundi":"bi.png",
    "Benín":"bj.png",
    "Bermudas":"bm.png",
    "Brunéi":"bn.png",
    "Bolivia":"bo.png",
    "Brasil":"br.png",
    "Bahamas":"bs.png",
    "Bután":"bt.png",
    "Botsuana":"bw.png",
    "Bielorrusia":"by.png",
    "Belice":"bz.png",
    "Canadá":"ca.png",
    "Islas Cocos":"cc.png",
    "República Democrática del Congo":"cd.png",
    "República Centroafricana":"cf.png",
    "República del Congo":"cg.png",
    "Suiza":"ch.png",
    "Costa de Marfil":"ci.png",
    "Islas Cook":"ck.png",
    "Chile":"cl.png",
    "Camerún":"cm.png",
    "China":"cn.png",
    "Colombia":"co.png",
    "Costa Rica":"cr.png",
    "Cuba":"cu.png",
    "Cabo Verde":"cv.png",
    "Isla de Navidad":"cx.png",
    "Chipre":"cy.png",
    "República Checa":"cz.png",
    "Alemania":"de.png",
    "Yibuti":"dj.png",
    "Dinamarca":"dk.png",
    "Dominica":"dm.png",
    "República Dominicana":"do.png",
    "Algeria":"dz.png",
    "Ecuador":"ec.png",
    "Estonia":"ee.png",
    "Egipto":"eg.png",
    "Eritrea":"er.png",
    "España":"es.png",
    "Etiopía":"et.png",
    "Finlandia":"fi.png",
    "Fiyi":"fj.png",
    "Islas Malvinas":"fk.png",
    "Micronesia":"fm.png",
    "Islas Feroe":"fo.png",
    "Francia":"fr.png",
    "Gabón":"ga.png",
    "Reino Unido":"gb.png",
    "Inglaterra":"gb-eng.png",
    "Irlanda del Norte":"gb-nir.png",
    "Escocia":"gb-sct.png",
    "Gales":"gb-wls.png",
    "Grenada":"gd.png",
    "Georgia":"ge.png",
    "Guayana Francesa":"gf.png",
    "Ghana":"gh.png",
    "Gambia":"gm.png",
    "Guinea":"gn.png",
    "Guinea Ecuatorial":"gq.png",
    "Guatemala":"gt.png",
    "Guam":"gu.png",
    "Guinea-Bisáu":"gw.png",
    "Guyana":"gy.png",
    "Hong Kong":"hk.png",
    "Honduras":"hn.png",
    "Croacia":"hr.png",
    "Haití":"ht.png",
    "Hungría":"hu.png",
    "Indonesia":"id.png",
    "Irlanda":"ie.png",
    "Israel":"il.png",
    "India":"in.png",
    "Iraq":"iq.png",
    "Irán":"ir.png",
    "Islandia":"is.png",
    "Italia":"it.png",
    "Jamaica":"jm.png",
    "Jordania":"jo.png",
    "Japón":"jp.png",
    "Kenia":"ke.png",
    "Kirguistán":"kg.png",
    "Camboya":"kh.png",
    "Kiribati":"ki.png",
    "Comoras":"km.png",
    "San Cristóbal y Nieves":"kn.png",
    "Corea del Norte":"kp.png",
    "Corea del Sur":"kr.png",
    "Kuwait":"kw.png",
    "Islas Caimán":"ky.png",
    "Kazajistán":"kz.png",
    "Laos":"la.png",
    "Líbano":"lb.png",
    "Santa Lucía":"lc.png",
    "Liechtenstein":"li.png",
    "Sri Lanka":"lk.png",
    "Liberia":"lr.png",
    "Lesoto":"ls.png",
    "Lituania":"lt.png",
    "Luxemburgo":"lu.png",
    "Letonia":"lv.png",
    "Libia":"ly.png",
    "Marruecos":"ma.png",
    "Mónaco":"mc.png",
    "Moldavia":"md.png",
    "Montenegro":"me.png",
    "Madagascar":"mg.png",
    "Islas Marshall":"mh.png",
    "Macedonia del Norte":"mk.png",
    "Mali":"ml.png",
    "Myanmar":"mm.png",
    "Mongolia":"mn.png",
    "Macao":"mo.png",
    "Islas Marianas del Norte":"mp.png",
    "Martinica":"mq.png",
    "Mauritania":"mr.png",
    "Montserrat":"ms.png",
    "Malta":"mt.png",
    "Mauricio":"mu.png",
    "Maldivas":"mv.png",
    "Malawi":"mw.png",
    "México":"mx.png",
    "Malasia":"my.png",
    "Mozambique":"mz.png",
    "Namibia":"na.png",
    "Nueva Caledonia":"nc.png",
    "Níger":"ne.png",
    "Isla Norfolk":"nf.png",
    "Nigeria":"ng.png",
    "Nicaragua":"ni.png",
    "Países Bajos":"nl.png",
    "Noruega":"no.png",
    "Nepal":"np.png",
    "Nauru":"nr.png",
    "Niue":"nu.png",
    "Nueva Zelanda":"nz.png",
    "Omán":"om.png",
    "Panamá":"pa.png",
    "Perú":"pe.png",
    "Polinesia Francesa":"pf.png",
    "Papúa Nueva Guinea":"pg.png",
    "Filipinas":"ph.png",
    "Pakistán":"pk.png",
    "Polonia":"pl.png",
    "San Pedro y Miquelón":"pm.png",
    "Islas Pitcairn":"pn.png",
    "Puerto Rico":"pr.png",
    "Palestina":"ps.png",
    "Portugal":"pt.png",
    "Palaos":"pw.png",
    "Paraguay":"py.png",
    "Qatar":"qa.png",
    "Reunión":"re.png",
    "Rumanía":"ro.png",
    "Serbia":"rs.png",
    "Rusia":"ru.png",
    "Ruanda":"rw.png",
    "Arabia Saudita":"sa.png",
    "Islas Salomón":"sb.png",
    "Seychelles":"sc.png",
    "Sudán":"sd.png",
    "Suecia":"se.png",
    "Singapur":"sg.png",
    "Eslovenia":"si.png",
    "Eslovaquia":"sk.png",
    "Sierra Leona":"sl.png",
    "San Marino":"sm.png",
    "Senegal":"sn.png",
    "Somalia":"so.png",
    "Surinam":"sr.png",
    "Sudán del Sur":"ss.png",
    "Santo Tomé y Príncipe":"st.png",
    "El Salvador":"sv.png",
    "San Martín":"sx.png",
    "Siria":"sy.png",
    "Suazilandia":"sz.png",
    "Islas Turcas y Caicos":"tc.png",
    "Chad":"td.png",
    "Togo":"tg.png",
    "Tailandia":"th.png",
    "Tayikistán":"tj.png",
    "Tokelau":"tk.png",
    "Timor Oriental":"tl.png",
    "Turmekistán":"tm.png",
    "Túnez":"tn.png",
    "Tonga":"to.png",
    "Turquía":"tr.png",
    "Trinidad y Tobago":"tt.png",
    "Tuvalu":"tv.png",
    "Taiwán":"tw.png",
    "Tanzania":"tz.png",
    "Ucrania":"ua.png",
    "Uganda":"ug.png",
    "Estados Unidos":"us.png",
    "Uruguay":"uy.png",
    "Uzbekistán":"uz.png",
    "Vaticano":"va.png",
    "San Vicente y las Granadinas":"vc.png",
    "Venezuela":"ve.png",
    "Islas Vírgenes Británicas":"vg.png",
    "Islas Vírgenes de EE.UU.":"vi.png",
    "Vietnam":"vn.png",
    "Vanuatu":"vu.png",
    "Wallis y Fortuna":"wf.png",
    "Samoa":"ws.png",
    "Kosovo":"xk.png",
    "Yemen":"ye.png",
    "Sudáfrica":"za.png",
    "Zambia":"zm.png",
    "Zimbabue":"zw.png"}
countries = list(countries_flags.keys())
flags = list(countries_flags.values())

root = tk.Tk()
root.resizable(False,False)
root.attributes("-fullscreen", False)
root.overrideredirect(0)
root.iconbitmap("iconos/es.ico")
root.geometry("450x275+600+200")
root.title(string="Flag Guesser v1")

score = 0
whilepregs = 0
countriesQuestions = {}

def NextQuestion():
    global countries, whilepregs, score, countriesQuestions, country
    if whilepregs >= 10:
        root.destroy()
        root2 = tk.Tk()
        root2.resizable(False,False)
        root2.attributes("-fullscreen", False)
        root2.overrideredirect(0)
        root2.title(string="Results")
        root2.geometry("450x400+600+200")

        keys = list(countriesQuestions.keys())
        values = list(countriesQuestions.values())

        tk.Label(root2, text=f"Puntuación: {score}/10", font="Arial 20", pady=40).pack()

        # ONE
        image_path = f"banderas/{countries_flags[keys[0]]}"
        pil_image = Image.open(image_path)
        width, height = 33, 26
        pil_image = pil_image.resize((width, height), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(pil_image)
        l1i = tk.Label(root2, text=f"{keys[0]}: ", fg=values[0], image=image, compound="right")
        l1i.image = image
        l1i.place(x=10, y=100)

        # TWO
        image_path2 = f"banderas/{countries_flags[keys[1]]}"
        pil_image2 = Image.open(image_path2)
        pil_image2 = pil_image2.resize((width, height), Image.Resampling.LANCZOS)
        image2 = ImageTk.PhotoImage(pil_image2)
        l2i = tk.Label(root2, text=f"{keys[1]}: ", fg=values[1], image=image2, compound="right")
        l2i.image = image2
        l2i.place(x=10, y=140)

        # THREE
        image_path3 = f"banderas/{countries_flags[keys[2]]}"
        pil_image3 = Image.open(image_path3)
        pil_image3 = pil_image3.resize((width, height), Image.Resampling.LANCZOS)
        image3 = ImageTk.PhotoImage(pil_image3)
        l3i = tk.Label(root2, text=f"{keys[2]}: ", fg=values[2], image=image3, compound="right")
        l3i.image = image3
        l3i.place(x=10, y=180)

        # FOUR
        image_path4 = f"banderas/{countries_flags[keys[3]]}"
        pil_image4 = Image.open(image_path4)
        pil_image4 = pil_image4.resize((width, height), Image.Resampling.LANCZOS)
        image4 = ImageTk.PhotoImage(pil_image4)
        l4i = tk.Label(root2, text=f"{keys[3]}: ", fg=values[3], image=image4, compound="right")
        l4i.image = image4
        l4i.place(x=10, y=220)

        # FIVE
        image_path5 = f"banderas/{countries_flags[keys[4]]}"
        pil_image5 = Image.open(image_path5)
        pil_image5 = pil_image5.resize((width, height), Image.Resampling.LANCZOS)
        image5 = ImageTk.PhotoImage(pil_image5)
        l5i = tk.Label(root2, text=f"{keys[4]}: ", fg=values[4], image=image5, compound="right")
        l5i.image = image5
        l5i.place(x=10, y=260)

        # SIX
        image_path6 = f"banderas/{countries_flags[keys[5]]}"
        pil_image6 = Image.open(image_path6)
        pil_image6 = pil_image6.resize((width, height), Image.Resampling.LANCZOS)
        image6 = ImageTk.PhotoImage(pil_image6)
        l6i = tk.Label(root2, text=f"{keys[5]}: ", fg=values[5], image=image6, compound="right")
        l6i.image = image6
        l6i.place(x=235, y=100)

        # SEVEN
        image_path7 = f"banderas/{countries_flags[keys[6]]}"
        pil_image7 = Image.open(image_path7)
        pil_image7 = pil_image7.resize((width, height), Image.Resampling.LANCZOS)
        image7 = ImageTk.PhotoImage(pil_image7)
        l7i = tk.Label(root2, text=f"{keys[6]}: ", fg=values[6], image=image7, compound="right")
        l7i.image = image7
        l7i.place(x=235, y=140)

        # EIGHT
        image_path8 = f"banderas/{countries_flags[keys[7]]}"
        pil_image8 = Image.open(image_path8)
        pil_image8 = pil_image8.resize((width, height), Image.Resampling.LANCZOS)
        image8 = ImageTk.PhotoImage(pil_image8)
        l8i = tk.Label(root2, text=f"{keys[7]}: ", fg=values[7], image=image8, compound="right")
        l8i.image = image8
        l8i.place(x=235, y=180)

        # NINE
        image_path9 = f"banderas/{countries_flags[keys[8]]}"
        pil_image9 = Image.open(image_path9)
        pil_image9 = pil_image9.resize((width, height), Image.Resampling.LANCZOS)
        image9 = ImageTk.PhotoImage(pil_image9)
        l9i = tk.Label(root2, text=f"{keys[8]}: ", fg=values[8], image=image9, compound="right")
        l9i.image = image9
        l9i.place(x=235, y=220)

        # TEN
        image_path10 = f"banderas/{countries_flags[keys[9]]}"
        pil_image10 = Image.open(image_path10)
        pil_image10 = pil_image10.resize((width, height), Image.Resampling.LANCZOS)
        image10 = ImageTk.PhotoImage(pil_image10)
        l10i = tk.Label(root2, text=f"{keys[9]}: ", fg=values[9], image=image10, compound="right")
        l10i.image = image10
        l10i.place(x=235, y=260)

        def Close():
            root2.destroy()
        closeBtn = tk.Button(root2, text="Cerrar", height=4,width=12, command=Close)

        closeBtn.place(x=170, y=320)
    else:
        whilepregs += 1
        country = random.choice(countries)
        label.config(text=country)
        Shuffle_flags()

def BtnClick(chosen_flag):
    global score, country, countriesQuestions
    global countries, flags
    cflag = countries_flags[country]
    if chosen_flag == cflag:
        score += 1
        countriesQuestions[country] = "green"
    else:
        countriesQuestions[country] = "red"
    countries.remove(country)
    flags.remove(cflag)
    NextQuestion()

def Shuffle_flags():
    global first_btn, second_btn, third_btn, fourth_btn
    global flags, country
    cflag = countries_flags[country]
    other_flags = random.sample([flag for flag in flags if flag != cflag], k=3)
    other_flags.append(cflag)
    random.shuffle(other_flags)
    one, two, three, four = other_flags[0], other_flags[1], other_flags[2], other_flags[3]

    # ONE
    image_path = f"banderas/{one}"
    pil_image = Image.open(image_path)
    width, height = 90, 60
    pil_image = pil_image.resize((width, height), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(pil_image)
    first_btn.config(image=image, command=lambda: BtnClick(one))
    first_btn.image = image

    # TWO
    image_path2 = f"banderas/{two}"
    pil_image2 = Image.open(image_path2)
    width2, height2 = 90, 60
    pil_image2 = pil_image2.resize((width2, height2), Image.Resampling.LANCZOS)
    image2 = ImageTk.PhotoImage(pil_image2)
    second_btn.config(image=image2, command=lambda: BtnClick(two))
    second_btn.image = image2

    # THREE
    image_path3 = f"banderas/{three}"
    pil_image3 = Image.open(image_path3)
    width3, height3 = 90, 60
    pil_image3 = pil_image3.resize((width3, height3), Image.Resampling.LANCZOS)
    image3 = ImageTk.PhotoImage(pil_image3)
    third_btn.config(image=image3, command=lambda: BtnClick(three))
    third_btn.image = image3

    # FOUR
    image_path4 = f"banderas/{four}"
    pil_image4 = Image.open(image_path4)
    width4, height4 = 90, 60
    pil_image4 = pil_image4.resize((width4, height4), Image.Resampling.LANCZOS)
    image4 = ImageTk.PhotoImage(pil_image4)
    fourth_btn.config(image=image4, command=lambda: BtnClick(four))
    fourth_btn.image = image4

country = random.choice(countries)
label = tk.Label(root, font="Arial 20", pady=40)
label.pack()

first_btn = tk.Button(root, height=65, width=195, command=BtnClick)
second_btn = tk.Button(root, height=65, width=195, command=BtnClick)
third_btn = tk.Button(root, height=65, width=195, command=BtnClick)
fourth_btn = tk.Button(root, height=65, width=195, command=BtnClick)

first_btn.place(x=5, y=100)
second_btn.place(x=245, y=100)
third_btn.place(x=5, y=200)
fourth_btn.place(x=245, y=200)

NextQuestion()
root.mainloop()