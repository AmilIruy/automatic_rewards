import pyautogui
from time import sleep
from tkinter import *
import tkinter as tk
import ctypes
import pickle
import os


def arquivo_texto():
    os.system("Leia.txt")

def iniciar_automacao():
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

janela = Tk()
janela.title("LOCKE")
janela.geometry("700x600")
janela.resizable(False, False)
janela.config(background="#f5eff3") 

barra_lateral = tk.Frame(janela, bg="#381328")
barra_lateral.place(x=0, y=0, width=291, height=600)

barra=Menu(janela)
menuMenu=Menu(barra, tearoff=0, fg="#381328")
menuMenu.add_command(label="Leia", command=arquivo_texto)
menuMenu.add_command(label="MouseInfo", command=abrir_mouseinfo)
barra.add_cascade(label="Menu", menu=menuMenu)

janela.config(menu=barra)

myappid = "program.for.locke"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
janela.iconbitmap("imagens\iv13.5ico.ico")  

im1 = PhotoImage(file="imagens\label1.png")   
im1 = im1.subsample(1,1)   
figura1 = Label(image=im1, bg="#f5eff3") 
figura1.place(x=-5, y=-5)


Label(janela, text="Começo:", fg="#381328", bg="#f5eff3").place(x=350, y=50)
tex_1 = Entry(janela, font=("arial", 14), bd=1, width=11, justify="left")
tex_1.place(x=420, y=50)

Label(janela, text="Final:", fg="#381328", bg="#f5eff3").place(x=375, y=100)
tex_2 = Entry(janela, font=("arial", 14), bd=1, width=11, justify="left")
tex_2.place(x=420, y=100)

Label(janela, text="X:", fg="#381328", bg="#f5eff3").place(x=400, y=181)
x_1 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
x_1.place(x=420, y=180)

Label(janela, text=":Y", fg="#381328", bg="#f5eff3").place(x=572, y=181)
y_1 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
y_1.place(x=500, y=180)

Label(janela, text="X:", fg="#381328", bg="#f5eff3").place(x=400, y=221)
x_2 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
x_2.place(x=420, y=220)

Label(janela, text=":Y", fg="#381328", bg="#f5eff3").place(x=572, y=221)
y_2 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
y_2.place(x=500, y=220) 

Label(janela, text="X:", fg="#381328", bg="#f5eff3").place(x=400, y=261)
x_3 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
x_3.place(x=420, y=260)

Label(janela, text=":Y", fg="#381328", bg="#f5eff3").place(x=572, y=261)
y_3 = Entry(janela, font=("arial", 14), bd=1, width=5, justify="left")
y_3.place(x=500, y=260)

Label(janela, text="Duração", fg="#381328", bg="#f5eff3").place(x=596, y=150)
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


botao1 = Button(janela, width=10, text="Iniciar", command=iniciar_automacao, bd=0, bg="#381328", fg="white")
botao1.place(x=450, y=410)

#botao2 = Button(janela, width=5, text="Leia", command=arquivo_texto, bd=1)
#botao2.place(x=10, y=550) 

#botao3 = Button(janela, width=8, text="MouseInfo", command=abrir_mouseinfo, bd=1)
#botao3.place(x=70, y=550)

#111112

carregar_dados()

janela.mainloop()

