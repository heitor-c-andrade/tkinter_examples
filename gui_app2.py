#
# Monta um Formulário
#

from tkinter import *

def impDados() :

    print("Nome.....: %s" % vnome.get())
    print("Telefone.: %s" % vfone.get())
    print("E-Mail...: %s" % vemail.get())
    print("OBS......: %s" % vobs.get("1.0",END))   

app = Tk()

app.title("Título")
app.geometry("500x300")
app.configure(background="#dde")

Label(app,text="Nome",bg="#dde",fg="#009",anchor=W).place(x=10,y=10,width=100,height=20)
vnome = Entry(app)
vnome.place(x=10,y=30,width=200,height=20)

Label(app,text="Telefone",bg="#dde",fg="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vfone = Entry(app)
vfone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-Mail",bg="#dde",fg="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vemail = Entry(app)
vemail.place(x=10,y=130,width=300,height=20)

Label(app,text="OBS",bg="#dde",fg="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vobs = Text(app)
vobs.place(x=10,y=180,width=300,height=80)

Button(app,text="Imprimir",command=impDados).place(x=10,y=270,width=100,height=20)


app.mainloop()
