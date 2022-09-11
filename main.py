import re
from tkinter import *
from tkinter import ttk
from turtle import color, colormode

cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#eceff1"
cor5 = "#ffab40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("360x460")
janela.configure(bg=cor1)

frame_tela = Frame(janela, width=360, height=110, bg = cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=360, height=370, bg = cor4)
frame_corpo.grid(row=1, column=0)


todos_valores = ''

def  entrar_valores(event):


    global todos_valores
    todos_valores = todos_valores + str(event)

    
    valor_texto.set(todos_valores)


def calcular():
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))

def limpar_tela():
    todos_valores=''
    valor_texto.set('')

valor_texto= StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=25, height=4, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3 , fg=cor2)
app_label.place(x=0, y=0)

b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=18, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=2, y=0)

b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=174, y=0)

b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=9, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=264, y=0)

b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=2, y=70)

b_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=88, y=70)

b_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=174, y=70)

b_7 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=9, height=3, bg=cor5, fg=cor2 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=264, y=70)

b_8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=2, y=140)

b_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=88, y=140)

b_10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=174, y=140)

b_11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=9, height=3, bg=cor5, fg=cor2 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=264, y=140)

b_12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=2, y=210)

b_13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=88, y=210)

b_14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=174, y=210)

b_15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=9, height=3, bg=cor5, fg=cor2 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=264, y=210)

b_16 = Button(frame_corpo,  command=lambda: entrar_valores('0'),text="0", width=18, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=2, y=280)

b_17 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=9, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=174, y=280)

b_18 = Button(frame_corpo, command=calcular,text="=", width=9, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=264, y=280)

janela.mainloop()