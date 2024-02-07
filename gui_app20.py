#
# Mostra como fazer Abas
#


from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Título")
app.geometry("500x300")


nb = ttk.Notebook(app)
nb.place(x=0,y=0,width=500,height=300)

tb1 = Frame(nb)
nb.add(tb1,text="Cursos")

tb2 = Frame(nb)
nb.add(tb2,text="Canal")

lb1 = Label(tb1,text="Curso de Python")
lb1.pack()
lb2 = Label(tb1,text="Curso de ReactNative")
lb2.pack()

lb3 = Label(tb2,text="Youtube")
lb3.pack()


app.mainloop()
