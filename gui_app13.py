#
# Mostra o CheckButton (caixinha quadrada), parecido com o RadioButton (caixinha redonda)
#   O CheckeButton pode ser para mais de uma opção, o RadioButton para escolher somente uma opção
#

from tkinter import *

def futebolClicado():
    print("Futebol:"+str(vFutebol.get()))

def volleyClicado():
    print("Volley:"+str(vVolley.get()))

def basketClicado():
    print("Basket:"+str(vBasket.get()))

app = Tk()
app.title("Título")
app.geometry("500x300")

vFutebol = IntVar()
vVolley = IntVar()
vBasket = IntVar()

fr_quadro1 = Frame(app,borderwidth=1,relief="solid")
# relief => flat,raised,sunken,solid
fr_quadro1.place(x=10,y=10,width=300,height=100)

cb_futebol = Checkbutton(fr_quadro1,text="Futebol",variable=vFutebol,onvalue=1,offvalue=0,command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volley = Checkbutton(fr_quadro1,text="Volley",variable=vVolley,onvalue=1,offvalue=0,command=volleyClicado)
cb_volley.pack(side=LEFT)

cb_basket = Checkbutton(fr_quadro1,text="Basket",variable=vBasket,onvalue=1,offvalue=0,command=basketClicado)
cb_basket.pack(side=LEFT)

app.mainloop()
