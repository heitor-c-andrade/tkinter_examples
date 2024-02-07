#
# Utilização de Radio Button: As bolinhas para ticar em cima como opções
#

from tkinter import *

def imprimirEsporte() :
    ve = vesporte.get()
    if ve == "f" :
        print("Esporte Futebol")
    elif ve == "v" :
        print("Esporte Volley")       
    elif ve == "b" :
        print("Esporte Basket")
    else :
        print("Selecione um esporte")              

app = Tk()

app.title("Título")
app.geometry("500x300")

vesporte = StringVar()

lb_esportes = Label(app,text="Esportes")
lb_esportes.pack()

rb_futebol = Radiobutton(app,text="Futebol",value="f",variable=vesporte)
rb_futebol.pack()

rb_volley = Radiobutton(app,text="Volley",value="v",variable=vesporte)
rb_volley.pack()

rb_basket = Radiobutton(app,text="Basket",value="b",variable=vesporte)
rb_basket.pack()

btn_esporte = Button(app,text="Esporte Selecionado",command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()
