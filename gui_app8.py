#
#  Abre Campo com Opções para Escolher => OptionMenu
#

from tkinter import *

def imprimirEsporte() :
    ve = vesporte.get()
    if ve == "Futebol" :
        print("Esporte Futebol")
    elif ve == "Volley" :
        print("Esporte Volley")       
    elif ve == "Basket" :
        print("Esporte Basket")
    else :
        print("Selecione um esporte")              

app = Tk()

app.title("Título")
app.geometry("500x300")

listaEsportes = ["Futebol","Volley","Basket"]

vesporte = StringVar()
vesporte.set(listaEsportes[0]) # Esporte Padrão

lb_esportes = Label(app,text="Esportes")
lb_esportes.pack()

op_esportes = OptionMenu(app,vesporte,*listaEsportes)
op_esportes.pack()

btn_esporte = Button(app,text="Esporte Selecionado",command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()
