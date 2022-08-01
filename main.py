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

frame_tela = Frame(janela, width=360, height=90, bg = cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=360, height=370, bg = cor4)
frame_corpo.grid(row=1, column=0)

b_1 = Button(frame_corpo, text="C", width=12, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=6, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=166, y=0)

b_3 = Button(frame_corpo, text="/", width=6, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=264, y=0)

b_4 = Button(frame_corpo, text="7", width=6, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=57)

b_5 = Button(frame_corpo, text="8", width=5, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=98, y=57)

b_6 = Button(frame_corpo, text="9", width=5, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=180, y=57)

b_7 = Button(frame_corpo, text="*", width=6, height=3, bg=cor5, fg=cor2 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=264, y=57)

b_8 = Button(frame_corpo, text="4", width=6, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=134)

b_9 = Button(frame_corpo, text="5", width=5, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=98, y=134)

b_10 = Button(frame_corpo, text="6", width=5, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=180, y=134)

b_11 = Button(frame_corpo, text="-", width=6, height=3, bg=cor5, fg=cor2 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=264, y=134)

b_12 = Button(frame_corpo, text="1", width=6, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=210)

b_13 = Button(frame_corpo, text="2", width=5, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=98, y=210)

b_14 = Button(frame_corpo, text="3", width=5, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=180, y=210)

b_15 = Button(frame_corpo, text="+", width=6, height=3, bg=cor5, fg=cor2 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=264, y=210)

b_16 = Button(frame_corpo, text="0", width=12, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=300)

b_17 = Button(frame_corpo, text=".", width=6, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=166, y=300)

b_18 = Button(frame_corpo, text="=", width=6, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=264, y=300)


janela.mainloop()