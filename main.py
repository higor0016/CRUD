# importando o Tkinter
from tkinter import *
import tkinter

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# criando Janela ###############

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

################# Dividindo Janela ###############
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=400, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1,pady=0, sticky=NSEW)

################# Label Cima ###############
app_nome = Label(frame_cima, text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)


################# Configurando Frame Baixo ###############
#PARA NOME
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

#PARA EMAIL
l_email = Label(frame_baixo, text='E-mail *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

#PARA TELEFONE
l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=160)

#PARA Data de Consulta
l_data_consulta = Label(frame_baixo, text='Data de Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_data_consulta.place(x=10, y=10)
e_data_consulta = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_data_consulta.place(x=10, y=40)

#PARA Estado 
l_nome = Label(frame_baixo, text='Estado *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=10, y=40)

#PARA Sobre 
l_nome = Label(frame_baixo, text='Sobre a Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=10, y=40)

janela.mainloop()

