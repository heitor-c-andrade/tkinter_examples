#
#   Monta uma tabela com Conteúdo / TreeView
#

from tkinter import *
from tkinter import ttk

def semComando():
    print("")

app = Tk()
app.title("Título")
app.geometry("600x300")

listaNomes =[['0','Nome 0','1234'],['1','Nome 1','4321'],['2','Nome 2','5678']]

tv = ttk.Treeview(app,columns=('id','nome','fone'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)
tv.heading('id',text='ID')
tv.heading('nome',text='NOME')
tv.heading('fone',text='FONE')
tv.pack()

for (i,n,f) in listaNomes :
    tv.insert("","end",values=(i,n,f))

app.mainloop()
