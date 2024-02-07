#
#   Posicionamento da Tela em forma de Grid
#


from tkinter import *
from tkinter import ttk


app = Tk()
app.title("Título")
app.geometry("500x300")

lb_canal = Label(app,text="Titulo")
lb_nome = Label(app,text="Digite seu Nome")
lb_idade = Label(app,text="Informe sua Idade")

et_nome = Entry(app)
et_idade = Entry(app)

btn = Button(app,text="Youtube")

lb_canal.grid(column=0,row=0,columnspan=2,pady=15)

lb_nome.grid(column=0,row=1,sticky="w") # n, s, e, w
et_nome.grid(column=0,row=2,padx=5)

lb_idade.grid(column=1,row=1,sticky="w") # n, s, e, w
et_idade.grid(column=1,row=2,padx=5)

app.mainloop()
