#
#   Mostra SpinBox, caixa que pode incrementar números de um em um com duas flexinhas do lado
#

from tkinter import *

def impVal():
    print("Valor: "+str(sb_valores.get()))


app = Tk()
app.title("Título")
app.geometry("500x300")

#sb_valores = Spinbox(app,from_=0,to=10)
sb_valores = Spinbox(app,values=(0,1,2,4,5))
sb_valores.pack()

btn_valor = Button(app,text="Imprimir Valor",command=impVal)
btn_valor.pack()


app.mainloop()
