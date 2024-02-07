#
# Não está funcionando direito...
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


vnome = Label(app,text="Nome")
vnome.grid(row=0,column=1 )

vfone = Label(app,text="Telefone")
vnome.grid(row=1,column=1 )

vemail = Label(app,text="E-Mail")
vnome.grid(row=2,column= 1)

vobs = Label(app,text="OBS")
vnome.grid(row=3,column=1 )


Button(app,text="Imprimir",command=impDados).place(x=10,y=270,width=100,height=20)


app.mainloop()
