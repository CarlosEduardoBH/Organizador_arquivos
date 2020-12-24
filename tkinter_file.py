from tkinter import *
import tkinter
from tkinter import ttk
from executeMove import files
import os


# recebe retorno da função do executor

def imprimir():
    txt.delete(0.0, END)

    sentence = files()
    txt.insert(END, str(sentence))


menu_inicial = Tk()
menu_inicial.title('Organizador de Arquivos')
menu_inicial.geometry("500x500+500+250")
menu_inicial.configure(background='#1e3743')

Frame()

#Frame 
# frame1 Top
frame1 = Frame(menu_inicial,
               bd=4, bg='#dfe3ee',
               highlightbackground='#759fe6',
               highlightthickness=2)

frame1.place(relx= 0.01, rely=0.01, relwidth=0.98, relheight=0.45)

#frame2 Botton
frame2 = Frame(menu_inicial,
               bd=4, bg='#dfe3ee',
               highlightbackground='#759fe6', 
               highlightthickness=2)

frame2.place(relx= 0.01, rely=0.47, relwidth=0.98, relheight=0.55)

# Buttons
btn_executar = Button(menu_inicial,
                      text="Executar", 
                      bg='#107db2', 
                      fg='white', bd=2, 
                      font= ('Arial', 10, 'bold'), 
                      command= imprimir)

btn_sair = Button(menu_inicial, 
                  text="Sair", 
                  bg='#107db2', 
                  fg='white', 
                  bd=2, 
                  font= ('Arial', 10, 'bold'), 
                  command= menu_inicial.quit)


btn_executar.place(relx =0.27, rely = 0.35, relwidth=0.2)
btn_sair.place(relx =0.53, rely = 0.35, relwidth=0.2)


# Label
label1 = Label(frame1,
             text = "Organizador de Arquivos",
             font = "Arial 20 bold",
             fg="#107db2",
             bg='#dfe3ee')

label2 = Label(frame2,
             text = "PRINT",
             font = "Arial 16 bold",
             fg="#107db2",
             bg='#dfe3ee')
             
label3 = Label(frame1,
               text="Pasta Atual ", 
               font = "Arial 14 bold", 
               bg='#dfe3ee')

label4 = Label(frame1, 
                text= (os.getcwd().upper()), 
                font = "Arial 10 bold", 
                relief="sunken",
                bd=3)


label1.pack()
label2.pack()
label3.pack()
label4.pack()


#ScrolList
scrolList = Scrollbar(frame2, orient='vertical')
scrolList.pack(side=RIGHT, fill="y")

# label Print Text
ent = Entry(frame2)
txt = Text(frame2, 
            width=25, 
            height=10, 
            wrap=WORD, 
            yscrollcommand=scrolList.set, 
            font= ('calibri', 14))

txt.place(relx =0.005, rely = 0.09, relwidth=0.98, relheight=0.90)

scrolList.config()

menu_inicial.mainloop()