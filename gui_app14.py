#
#   Input de senha com eco sem mostrar a digitação
#

from tkinter import *

def impSenha():
    print("Senha digitada:"+vSenha.get())

app = Tk()
app.title("Título")
app.geometry("500x300")

vSenha = StringVar()

pSenha = Entry(app,textvariable=vSenha,show="*")
pSenha.pack()

btn_mostrarSenha = Button(app,text="Imprimir Senha",command=impSenha)
btn_mostrarSenha.pack()

app.mainloop()
