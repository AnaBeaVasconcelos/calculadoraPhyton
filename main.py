from tkinter import *
from tkinter import ttk

cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#eceff1"
cor5 = "#ffab40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x320")
janela.configure(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg = cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

b_1 = Button(frame_corpo, text="1", width=5, height=2, bg=cor4, fg=cor5)

janela.mainloop()