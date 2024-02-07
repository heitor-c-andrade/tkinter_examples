#
# Caixa de opções Combobox, parecido com OptionMenu
#

from tkinter import *
from tkinter import ttk

def imprimirEsporte():
    ve = cb_esportes.get()
    print("Esporte "+ve)

app = Tk()
app.title("Título")
app.geometry("500x300")

listEsportes = ["Futebol","Volley","Basket"]

lb_esportes = Label(app,text="Esportes")
lb_esportes.pack()

cb_esportes = ttk.Combobox(app,values=listEsportes)
cb_esportes.set("Futebol")
cb_esportes.pack()

btn_esportes = Button(app,text="Esporte Selecionado",command=imprimirEsporte)
btn_esportes.pack()

app.mainloop()
