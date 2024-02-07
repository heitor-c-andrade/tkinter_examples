#
#   Mostra Message Box
#

from tkinter import *
from tkinter import messagebox

def mostrarMsg(tipomsg,msg) :

    if tipomsg=="1" :
        messagebox.showinfo(title="Show Info", message=msg)
    elif tipomsg=="2" :
        messagebox.showwarning(title="Show Warning", message=msg)
    elif tipomsg=="3" :
        messagebox.showerror(title="Show Error", message=msg)

def resetTB() :
    res = messagebox.askyesno("Reset","Confirma reset do textbox ?")
    if (res==True) :
        tb_num.delete(0,END)
        tb_num.insert(0,"1")


vmsg="** Mensagem **"

app = Tk()
app.title("Título")
app.geometry("500x300")

vnum_cxtexto = StringVar()

Label(app,text="Tipo de Caixa (1,2 ou 3)").pack()

tb_num = Entry(app,textvariable=vnum_cxtexto)

vnum_cxtexto.set("1")
tb_num.pack()

btn_msg = Button(app, text="Mostrar Mensagem", command=lambda:mostrarMsg(vnum_cxtexto.get(),vmsg))
btn_msg.pack()

btn_reset = Button(app, text="Reset Textbox", command=resetTB)
btn_reset.pack()


app.mainloop()
