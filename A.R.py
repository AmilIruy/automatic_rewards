import pyautogui
from time import sleep
from tkinter import *
import tkinter as tk
import customtkinter as ctk
import customtkinter
import ctypes
import pickle
import webbrowser
import os


user_dir = os.path.expanduser("~")
dados_salvos_path = os.path.join(user_dir, "dados_salvos.pkl")


def iniciar_automacao(): 
    janela.iconify()
    n1 = int(tex_1.get())
    n2 = int(tex_2.get())

    x1 = x_1.get()
    y1 = y_1.get()
    x2 = x_2.get()
    y2 = y_2.get()
    x3 = x_3.get()
    y3 = y_3.get()
    d1 = d_1.get()
    d2 = d_2.get()
    d3 = d_3.get()

    salvar_dados()

    for numero in range(n1, n2): 
        if x1 and y1:
            pyautogui.click(int(x1), int(y1), duration=float(d1) if d1 else 0)
        pyautogui.typewrite(str(numero))

        if x2 and y2:
            pyautogui.click(int(x2), int(y2), duration=float(d2) if d2 else 0)

        if x3 and y3:
            pyautogui.click(int(x3), int(y3), duration=float(d3) if d3 else 0)

def salvar_dados():
    dados = {
        "n1": tex_1.get(),
        "n2": tex_2.get(),
        "x1": x_1.get(),
        "y1": y_1.get(),
        "x2": x_2.get(),
        "y2": y_2.get(),
        "x3": x_3.get(),
        "y3": y_3.get(),
        "d1": d_1.get(),  
        "d2": d_2.get(), 
        "d3": d_3.get() 
    }
    with open("dados_salvos.pkl", "wb") as arquivo:
        pickle.dump(dados, arquivo)

def carregar_dados():
    try:
        with open("dados_salvos.pkl", "rb") as arquivo:
            dados = pickle.load(arquivo)
            tex_1.insert(0, dados.get("n1", ""))
            tex_2.insert(0, dados.get("n2", ""))
            x_1.insert(0, dados.get("x1", ""))  
            y_1.insert(0, dados.get("y1", ""))
            x_2.insert(0, dados.get("x2", ""))
            y_2.insert(0, dados.get("y2", ""))
            x_3.insert(0, dados.get("x3", ""))
            y_3.insert(0, dados.get("y3", ""))
            d_1.insert(0, dados.get("d1", "")) 
            d_2.insert(0, dados.get("d2", ""))  
            d_3.insert(0, dados.get("d3", ""))
    except FileNotFoundError:
        pass

def abrir_mouseinfo():
    pyautogui.mouseInfo()

def verificarnumero(char):
    return char.isdigit()

def janela_manual():
    janela2 = tk.Toplevel()
    janela2.config(background=scolor)
    janela2.iconbitmap("A.R Imagens\Logo\iv13.5ico.ico") 
    janela2.resizable(False, False)
    global imagem_janela2
    imagem_janela2 = PhotoImage(file="A.R Imagens\Manual\MANUAL_manual.png")
    label_imagem = Label(janela2, image=imagem_janela2, bg=scolor)
    label_imagem.pack(pady=20)
    botao2 = customtkinter.CTkButton(janela2, text= "MouseInfo",fg_color="yellow", border_color="#381328", hover_color="green", text_color= "black", cursor="hand2", bg_color=scolor, corner_radius= 100, width=10, height=15, command= abrir_mouseinfo)
    botao2.place(x=212, y=101)  
    janela2.mainloop()

def contato():
    webbrowser.open("https://github.com/AmilIruy")


pcolor= "#f5eff3" 
scolor= "#160810"


janela = ctk.CTk()
janela.title("A.R")
janela.resizable(False, False)
janela.config(background=pcolor) 

myappid = "program.for.locke/AmilIruy"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
janela.iconbitmap("A.R Imagens\Logo\iv13.5ico.ico")      
  
 
canvas = Canvas(janela, bd=0, highlightthickness=0, width=700, height=600)
canvas.pack()

imagem = PhotoImage(file="A.R Imagens\Logo\Barra.png")  
im1 = canvas.create_image(0, -5, anchor=NW, image=imagem)

imagem2 = PhotoImage(file="A.R Imagens\Buttons\MANUAL.png") 
im2 = canvas.create_image(65, 80, anchor=NW, image=imagem2)
botao2 = Button(janela, image=imagem2, command=janela_manual, bd=0, bg= "#160810", fg= "#160810", activebackground="#160810") 
botao2.place(x=65, y=80) 

imagem4 = PhotoImage(file="A.R Imagens\Buttons\CONTATO.png") 
im4 = canvas.create_image(65, 200, anchor=NW, image=imagem4)
botao4 = Button(janela, image=imagem4, command=contato, bd=0, bg= "#160810", fg= "#160810", activebackground="#160810") 
botao4.place(x=65, y=200) 

imagem3 = PhotoImage(file="A.R Imagens\Logo\iiiv16 1.png")  
im3 = canvas.create_image(65, 380, anchor=NW, image=imagem3)


Label(janela, text="Começo:", fg=scolor, bg=pcolor).place(x=350, y=50)
tex_1 = Entry(janela, font=("arial", 14), bd=1, width=11, justify="left")
tex_1.place(x=420, y=50)

Label(janela, text="Final:", fg=scolor, bg=pcolor).place(x=375, y=100)
tex_2 = Entry(janela, font=("arial", 14), bd=1, width=11, justify="left")
tex_2.place(x=420, y=100)

Label(janela, text="X:", fg=scolor, bg=pcolor).place(x=400, y=181)
x_1 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
x_1.place(x=420, y=180)

Label(janela, text=":Y", fg=scolor, bg=pcolor).place(x=572, y=181)
y_1 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
y_1.place(x=500, y=180)

Label(janela, text="X:", fg=scolor, bg=pcolor).place(x=400, y=221)
x_2 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
x_2.place(x=420, y=220)

Label(janela, text=":Y", fg=scolor, bg=pcolor).place(x=572, y=221)
y_2 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
y_2.place(x=500, y=220) 

Label(janela, text="X:", fg=scolor, bg=pcolor).place(x=400, y=261)
x_3 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
x_3.place(x=420, y=260)

Label(janela, text=":Y", fg=scolor, bg=pcolor).place(x=572, y=261)
y_3 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
y_3.place(x=500, y=260)

Label(janela, text="Duração", fg=scolor, bg=pcolor).place(x=596, y=150)
d_1 = Entry(janela, font=("arial", 14), bd=1, width=4, justify="left")
d_1.place(x=600, y=181)

d_2 = Entry(janela, font=("arial", 14), bd=1, width=4, justify="left")
d_2.place(x=600, y=221)

d_3 = Entry(janela, font=("arial", 14), bd=1, width=4, justify="left")
d_3.place(x=600, y=261)


validarnumero = janela.register(verificarnumero)

campos = [tex_1, tex_2, x_1, y_1, x_2, y_2, x_3, y_3, d_1, d_2, d_3]

for campo in campos:
    campo.config(validate="key", validatecommand=(validarnumero, "%S"))


botao1 = customtkinter.CTkButton(janela, text= "iniciar",fg_color="#381328", border_color="#381328", hover_color=scolor, cursor="hand2", bg_color=pcolor, corner_radius= 50, command= iniciar_automacao)
botao1.place(x=350, y=310)   


carregar_dados()

janela.mainloop()