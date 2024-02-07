#
# Monta TreeView com possibilidade de Inserir, Deletar e Obter Dados
#

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def inserir():
    if vid.get()=="" or vnome=="" or vfone=="" :
        messagebox.showinfo(title="ERRO",message="Digite todos os dados")
        return
    tv.insert("","end",values=(vid.get(),vnome.get(),vfone.get()))
    vid.delete(0,END)
    vnome.delete(0,END) 
    vfone.delete(0,END)
    vid.focus()


def deletar():
    try:
        itemSelecionado=tv.selection()
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title="ERRO",message="Selecione um elemento a ser deletado")   

def obter():
    try:
        itemSelecionado=tv.selection()[0]
        valores=tv.item(itemSelecionado,"values")
        print("Id......:"+valores[0])
        print("Nome....:"+valores[1])
        print("Telefone:"+valores[2])

    except:
        messagebox.showinfo(title="ERRO",message="Selecione um elemento a ser mostrado")      


app = Tk()
app.title("Título")
app.geometry("600x300")

lbid = Label(app,text='ID') #,anchor=W)
vid = Entry(app)

lnome = Label(app,text='NOME') # ,anchor=W)
vnome = Entry(app)

lfone = Label(app,text='FONE') # ,anchor=W)
vfone = Entry(app)


tv = ttk.Treeview(app,columns=('id','nome','fone'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)
tv.heading('id',text='ID')
tv.heading('nome',text='NOME')
tv.heading('fone',text='FONE')

bt_inserir = Button(app,text="Inserir",command=inserir)
bt_deletar = Button(app,text="Deletar",command=deletar)
bt_obter = Button(app,text="Obter",command=obter)

lbid.grid(column=0,row=0,stick="w")
vid.grid(column=0,row=1)

lnome.grid(column=1,row=0,stick="w")
vnome.grid(column=1,row=1)

lfone.grid(column=2,row=0,stick="w")
vfone.grid(column=2,row=1)

tv.grid(column=0,row=3,columnspan=3,pady=5)

bt_inserir.grid(column=0,row=4)
bt_deletar.grid(column=1,row=4)
bt_obter.grid(column=2,row=4)

app.mainloop()
