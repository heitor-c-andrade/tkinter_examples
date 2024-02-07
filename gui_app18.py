#
#   Listbox, caixa para inserir vários dados
#


from tkinter import *

def imprimirEsporte():
    print("Esporte: "+str(lb_esportes.get(ACTIVE)))

def addEsporte():
    lb_esportes.insert(END,vnovoesporte.get())


app = Tk()
app.title("Título")
app.geometry("500x300")

listaEsportes = ["Futebol","Volley","Basket"]
lb_esportes = Listbox(app)

for esporte in listaEsportes:
    lb_esportes.insert(END,esporte)
lb_esportes.pack()

btn_esporte = Button(app,text="Imprimir Esporte",command=imprimirEsporte)
btn_esporte.pack()

vnovoesporte = Entry(app)
vnovoesporte.pack()

btn_novoesporte = Button(app,text="Adicionar Novo Esporte",command=addEsporte)
btn_novoesporte.pack()

app.mainloop()
