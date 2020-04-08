CYFRY = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-"]
from tkinter import *
class Application(Frame,):
    def __init__(app, master, color="silver"):
      super(Application, app).__init__(master, background=color)
      app.grid()
      app.create_wigets()
    def create_wigets(app):

      app.bttn = Button(app)
      app.bttn["font"] ="Terminal" , "13"
      app.bttn["background"] ="green"
      app.bttn["text"] = "Oblicz"
      app.bttn["command"] = app.licz
      app.bttn.grid(row =9 ,column =1 ,sticky =W )

      app.lbl = Label(app)
      app.lbl["background"] ="silver"
      app.lbl["font"] ="Terminal" , "13"
      app.lbl["text"] = "Wzor ogolny funkcji kwadratowej"
      app.lbl.grid(row =1 ,column =1  ,sticky =W)




      app.lbl1 = Label(app)
      app.lbl1["background"] ="silver"
      app.lbl1["font"] ="Terminal" , "13"
      app.lbl1["text"] = "ax^2 + bx + c =  0"
      app.lbl1.grid(row =2 ,column =1 ,sticky =W )

      app.lbl2 = Label(app)
      app.lbl2["font"] ="Terminal" , "13"
      app.lbl2["background"] ="silver"
      app.lbl2["text"] = "Wprowadz dane:"
      app.lbl2.grid(row =4 ,column =1 ,sticky =W )

      app.lbl3 = Label(app)
      app.lbl3["font"] ="Terminal" , "13"
      app.lbl3["background"] ="silver"
      app.lbl3["text"] = "a wynosi:"
      app.lbl3.grid(row=5 ,column =1 ,sticky =W )

      app.lbl4 = Label(app)
      app.lbl4["font"] ="Terminal" , "13"
      app.lbl4["background"] ="silver"
      app.lbl4["text"] = "b wynosi:"
      app.lbl4.grid(row =6 ,column =1 ,sticky =W )

      app.lbl5 = Label(app)
      app.lbl5["font"] ="Terminal" , "13"
      app.lbl5["background"] ="silver"
      app.lbl5["text"] = "c wynosi:"
      app.lbl5.grid(row =7 ,column =1 ,sticky =W )

      app.lbl6 = Label(app)
      app.lbl6["font"] ="Terminal" , "13"
      app.lbl6["background"] ="silver"
      app.lbl6["text"] = "   "
      app.lbl6.grid(row =8 ,column =1 ,sticky =W )

      app.lbl7 = Label(app)
      app.lbl7["font"] ="Terminal" , "13"
      app.lbl7["background"] ="silver"
      app.lbl7["text"] = "   "
      app.lbl7.grid(row =3 ,column =1 ,sticky =W )

      app.ent_a = Entry(app)
      app.ent_a["font"] ="Terminal" , "13"
      app.ent_a["background"] = "gold"
      app.ent_a.grid(row =5 ,column =1 ,sticky =E )

      app.ent_b = Entry(app)
      app.ent_b["font"] ="Terminal" , "13"
      app.ent_b["background"] = "gold"
      app.ent_b.grid(row =6 ,column =1 ,sticky =E )

      app.ent_c = Entry(app)
      app.ent_c["font"] ="Terminal" , "13"
      app.ent_c["background"] = "gold"
      app.ent_c.grid(row =7 ,column =1 ,sticky =E )

      app.lbl10 = Label(app)
      app.lbl10["text"] = " "
      app.lbl10["font"] ="Terminal" , "13"
      app.lbl10["background"] ="silver"
      app.lbl10.grid(row = 10, column = 1)

    def licz(app):


        app.deflbl = Label(app)
        app.deflbl["text"] = "Błąd! Wprowadz poprawne dane!   "
        app.deflbl["font"] ="Terminal" , "13" ,
        app.deflbl["background"] ="silver"

        app.deflb2 = Label(app)
        app.deflb2["text"] = "Używaj kropki zamiast przecinka!"
        app.deflb2["font"] ="Terminal" , "13" ,
        app.deflb2["background"] ="silver"


        a = app.ent_a.get()
        #a *= 1000
        #a = int(a)
        b = app.ent_b.get()
        #b *= 1000
        #b = int(b)
        c = app.ent_c.get()
        #c *= 1000
        #c = int(c)
        i = 0

        for item in a:
            if item == ",":
                i += 1

        for item in b:
            if item == ",":
                i += 1

        for item in c:
            if item == ",":
                i += 1
        if i > 0:
            app.deflb2["foreground"] = "red"
            app.deflb2.grid(row = 8, column = 1, sticky = W)


        i = 0
        for item in a:
            if not item in CYFRY:
                i += 1
            else:
                i += 0
        for item in b:
            if not item in CYFRY:
                i += 1
            else:
                i += 0
        for item in c:
            if not item in CYFRY:
                i += 1
            else:
                i+= 0
        if not i == 0:
            app.deflbl["foreground"] = "red"
            app.deflbl.grid(row = 8, column = 1, sticky = W)
        else:
            app.deflbl["foreground"] = "silver"
            app.deflbl.grid(row = 8, column = 1, sticky = W)


            a = app.ent_a.get()

            a = float(a)
            b = app.ent_b.get()

            b = float(b)
            c = app.ent_c.get()

            c = float(c)

            b2  = b * b
            aa = 4 * a * c
            app.delta = b2 - aa
            app.delta = float(app.delta)
            if not app.delta < 0:
                app.pierwiastek_z_delty = app.delta**0.5
                app.pierwiastek_z_delty = int(app.pierwiastek_z_delty)
      #print(a)
      #print(b)
      #print(c)
      #print(app.delta)
            app.deltalbl = Label(app)
            app.deltalbl["font"] ="Terminal" , "13"
            app.deltalbl["background"] ="silver"
            app.deltalbl["text"] = "delta:"
            app.deltalbl.grid(row = 12, column = 1, sticky = W)
            app.delta_txt = Text(app,width = 5, height = 1, wrap = WORD)
            app.delta_txt["font"] ="Terminal" , "13"
            app.delta_txt["background"] ="lime"
            app.delta_txt.grid(row  = 12, column = 1, sticky = N)
            app.delta_txt.delete(0.0, END)
            app.delta_txt.insert(0.0, app.delta)


            if app.delta < 0:
        #print("brak")

                app.lbl11 = Label(app)
                app.lbl11["font"] ="Terminal" , "13"
                app.lbl11["background"] = "silver"
                app.lbl11["text"] = " "
                app.lbl11.grid(row = 11, column = 1)

                app.wynik1 = "Delta jest ujemna, dlatego rownanie nie ma żadnego rozwiązania."
                app.wynik1_txt = Text(app, width = 40, height =2, wrap = WORD)
                app.wynik1_txt["font"] ="Terminal" , "13"
                app.wynik1_txt["background"] = "lime"
                app.wynik1_txt.grid(row = 13, column = 1, sticky  = W)
                app.wynik1_txt.delete(0.0, END)
                app.wynik1_txt.insert(0.0, app.wynik1)
                app.x1 = " ---"
                app.x2 = " ---"

##################################### 1 #######################################

                app.xlbl = Label(app)
                app.xlbl["font"] ="Terminal" , "13"
                app.xlbl["background"] ="silver"
                app.xlbl["text"] = "x1 wynosi:"
                app.xlbl.grid(row = 15, column = 1, sticky = W)

                app.delta_txt = Text(app,width = 5, height = 1, wrap = WORD)
                app.delta_txt["font"] ="Terminal" , "13"
                app.delta_txt["background"] ="aqua"
                app.delta_txt.grid(row  = 15, column = 1, sticky = N)
                app.delta_txt.delete(0.0, END)
                app.delta_txt.insert(0.0, app.x1)

                app.xlbl = Label(app)
                app.xlbl["font"] ="Terminal" , "13"
                app.xlbl["background"] ="silver"
                app.xlbl["text"] = "x2 wynosi:"
                app.xlbl.grid(row = 16, column = 1, sticky = W)

                app.delta_txt = Text(app,width = 5, height = 1, wrap = WORD)
                app.delta_txt["font"] ="Terminal" , "13"
                app.delta_txt["background"] ="aqua"
                app.delta_txt.grid(row  = 16, column = 1, sticky = N)
                app.delta_txt.delete(0.0, END)
                app.delta_txt.insert(0.0, app.x2)

                app.lbl14 = Label(app)
                app.lbl14["font"] ="Terminal" , "13"
                app.lbl14["background"] = "silver"
                app.lbl14["text"] = " "
                app.lbl14.grid(row = 17, column = 1)

###############################################################################

            if app.delta == 0:
                app.x1 = b * -1 / 2 / a
        #app.x = int(app.x)
        #print(x)

                app.lbl12 = Label(app)
                app.lbl12["font"] ="Terminal" , "13"
                app.lbl12["background"] = "silver"
                app.lbl12["text"] = " "
                app.lbl12.grid(row = 11, column = 1)

                app.wynik1 = "Delta rowna jest zeru, dlatego rownanie  ma jedno rozwiazanie."
                app.wynik1_txt = Text(app, width = 40, height =2, wrap = WORD)
                app.wynik1_txt["font"] ="Terminal" , "13"
                app.wynik1_txt["background"] = "lime"
                app.wynik1_txt.grid(row = 13, column = 1, sticky  = W)
                app.wynik1_txt.delete(0.0, END)
                app.wynik1_txt.insert(0.0, app.wynik1)

                app.xlbl = Label(app)
                app.xlbl["font"] ="Terminal" , "13"
                app.xlbl["background"] ="silver"
                app.xlbl["text"] = "x wynosi:"
                app.xlbl.grid(row = 15, column = 1, sticky = W)
                app.x2 = " ---"

#################################### 2 ########################################

                app.xlbl = Label(app)
                app.xlbl["font"] ="Terminal" , "13"
                app.xlbl["background"] ="silver"
                app.xlbl["text"] = "x1 wynosi:"
                app.xlbl.grid(row = 15, column = 1, sticky = W)

                app.delta_txt = Text(app,width = 5, height = 1, wrap = WORD)
                app.delta_txt["font"] ="Terminal" , "13"
                app.delta_txt["background"] ="aqua"
                app.delta_txt.grid(row  = 15, column = 1, sticky = N)
                app.delta_txt.delete(0.0, END)
                app.delta_txt.insert(0.0, app.x1)

                app.xlbl = Label(app)
                app.xlbl["font"] ="Terminal" , "13"
                app.xlbl["background"] ="silver"
                app.xlbl["text"] = "x2 wynosi:"
                app.xlbl.grid(row = 16, column = 1, sticky = W)

                app.delta_txt = Text(app,width = 5, height = 1, wrap = WORD)
                app.delta_txt["font"] ="Terminal" , "13"
                app.delta_txt["background"] ="aqua"
                app.delta_txt.grid(row  = 16, column = 1, sticky = N)
                app.delta_txt.delete(0.0, END)
                app.delta_txt.insert(0.0, app.x2)

                app.lbl14 = Label(app)
                app.lbl14["font"] ="Terminal" , "13"
                app.lbl14["background"] = "silver"
                app.lbl14["text"] = " "
                app.lbl14.grid(row = 17, column = 1)

###############################################################################

            if app.delta > 0:
                y1 = b * -1 - app.pierwiastek_z_delty
                app.x1 = y1 / 2 / a
        #app.x1 = int(app.x1)
        #x1 = int(x1)
                y2 = b * -1 + app.pierwiastek_z_delty
                app.x2 = y2 / 2 / a
        #app.x2 = int(app.x2)
        #x2 = int(x2)

                app.lbl13 = Label(app)
                app.lbl13["font"] ="Terminal" , "13"
                app.lbl13["background"] = "silver"
                app.lbl13["text"] = " "
                app.lbl13.grid(row = 11, column = 1)

                app.wynik1 = "Delta jest większa od zera, dlatego rownanie  ma dwa rozwiazania."
                app.wynik1_txt = Text(app, width = 40, height =2, wrap = WORD)
                app.wynik1_txt["font"] ="Terminal" , "13"
                app.wynik1_txt["background"] = "lime"
                app.wynik1_txt.grid(row = 13, column = 1, sticky  = W)
                app.wynik1_txt.delete(0.0, END)
                app.wynik1_txt.insert(0.0, app.wynik1)

#################################### 3 ########################################
                app.xlbl = Label(app)
                app.xlbl["font"] ="Terminal" , "13"
                app.xlbl["background"] ="silver"
                app.xlbl["text"] = "x1 wynosi:"
                app.xlbl.grid(row = 15, column = 1, sticky = W)

                app.delta_txt = Text(app,width = 5, height = 1, wrap = WORD)
                app.delta_txt["font"] ="Terminal" , "13"
                app.delta_txt["background"] ="aqua"
                app.delta_txt.grid(row  = 15, column = 1, sticky = N)
                app.delta_txt.delete(0.0, END)
                app.delta_txt.insert(0.0, app.x1)

                app.xlbl = Label(app)
                app.xlbl["font"] ="Terminal" , "13"
                app.xlbl["background"] ="silver"
                app.xlbl["text"] = "x2 wynosi:"
                app.xlbl.grid(row = 16, column = 1, sticky = W)

                app.delta_txt = Text(app,width = 5, height = 1, wrap = WORD)
                app.delta_txt["font"] ="Terminal" , "13"
                app.delta_txt["background"] ="aqua"
                app.delta_txt.grid(row  = 16, column = 1, sticky = N)
                app.delta_txt.delete(0.0, END)
                app.delta_txt.insert(0.0, app.x2)

                app.lbl14 = Label(app)
                app.lbl14["font"] ="Terminal" , "13"
                app.lbl14["background"] = "silver"
                app.lbl14["text"] = " "
                app.lbl14.grid(row = 17, column = 1)

###############################################################################


        #print(x1)
        #print(x2)

                app.lbl14 = Label(app)
                app.lbl14["font"] ="Terminal" , "13"
                app.lbl14["background"] = "silver"
                app.lbl14["text"] = " "
                app.lbl14.grid(row = 14, column = 1)
















    def sprawdz(app):

        app.deflbl = Label(app)
        app.deflbl["text"] = "Błąd! Wprowadz poprawne dane"
        app.deflbl["font"] ="Terminal" , "13" ,
        app.deflbl["background"] ="silver"
        app.deflbl.grid(row = 8, column = 1, sticky = W)

        a = app.ent_a.get()
        #a = int(a)
        b = app.ent_b.get()
        #b = int(b)
        c = app.ent_c.get()
        #c = int(c)
        for item in a:
            if not item in CYFRY:
                i = 1
            else:
                i = 0
        for item in b:
            if not item in CYFRY:
                i += 1
            else:
                i += 0
        for item in c:
            if not item in CYFRY:
                i += 1
            else:
                i+= 0
        if i == 0:
            app.licz
            app.deflbl["foreground"] = "silver"
        else:
            app.deflbl["foreground"] = "red"


root = Tk()
root.title("Funkcja kwadratowa")
root.geometry()
app = Application(root)

root.mainloop()





