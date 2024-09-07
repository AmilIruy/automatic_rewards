import pyautogui
from time import sleep
from tkinter import *
import ctypes
import pickle
import os


def arquivo_texto():
    os.system("Leia.txt")

def iniciar_automacao():
    n1 = int(tex_1.get())
    n2 = int(tex_2.get())
    x1 = int(x_1.get())
    y1 = int(y_1.get())
    x2 = int(x_2.get())
    y2 = int(y_2.get())
    x3 = int(x_3.get())
    y3 = int(y_3.get())

    salvar_dados()

    for numero in range (n1, n2): 
        pyautogui.click(x1,y1,duration=3)
        pyautogui.typewrite(str(numero))
        pyautogui.click(x2,y2,duration=3)
        pyautogui.click(x3,y3,duration=3)

def salvar_dados():
    dados = {
        "x1": x_1.get(),
        "y1": y_1.get(),
        "x2": x_2.get(),
        "y2": y_2.get(),
        "x3": x_3.get(),
        "y3": y_3.get()
    }
    with open("dados_salvos.pkl", "wb") as arquivo:
        pickle.dump(dados, arquivo)

def carregar_dados():
    try:
        with open("dados_salvos.pkl", "rb") as arquivo:
            dados = pickle.load(arquivo)
            x_1.insert(0, dados["x1"])
            y_1.insert(0, dados["y1"])
            x_2.insert(0, dados["x2"])
            y_2.insert(0, dados["y2"])
            x_3.insert(0, dados["x3"])
            y_3.insert(0, dados["y3"])
    except FileNotFoundError:
        pass

def abrir_mouseinfo():
    pyautogui.mouseInfo()


janela = Tk()
janela.title("LOCKE")
janela.geometry("500x600")
janela.resizable(False,False)
janela.config(background="#111111")

myappid = 'program.for.locke'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
janela.iconbitmap("imagens\iv11.1ico.ico") 

im1 = PhotoImage(file="imagens\iv11.2.png")  
im1 = im1.subsample(5,5)  
figura1 = Label(image=im1,bg="#111112")
figura1.grid(row=0, column=0, padx=(130, 5), pady=(380, 10), sticky="")


Label(janela, text="Começo:").place(x=130, y=50)
tex_1 = Entry(janela, font=("arial", 14), bd=2, width=11, justify= "left")
tex_1.place(x=200, y=50)

Label(janela, text="Final:").place(x=155, y=100)
tex_2 = Entry(janela, font=("arial", 14), bd=2, width=11, justify= "left")
tex_2.place(x=200, y=100)

Label(janela, text="X:").place(x=181, y=181)
x_1 = Entry(janela, font=("arial", 14), bd=2, width=5, justify= "left")
x_1.place(x=200, y=180)

Label(janela, text=":Y").place(x=352, y=181)
y_1 = Entry(janela, font=("arial", 14), bd=2, width=5, justify= "left")
y_1.place(x=280, y=180)

Label(janela, text="X:").place(x=181, y=221)
x_2 = Entry(janela, font=("arial", 14), bd=2, width=5, justify= "left")
x_2.place(x=200, y=220)

Label(janela, text=":Y").place(x=352, y=221)
y_2 = Entry(janela, font=("arial", 14), bd=2, width=5, justify= "left")
y_2.place(x=280, y=220) 

Label(janela, text="X:").place(x=181, y=261)
x_3 = Entry(janela, font=("arial", 14), bd=2, width=5, justify= "left")
x_3.place(x=200, y=260)

Label(janela, text=":Y").place(x=352, y=261)
y_3 = Entry(janela, font=("arial", 14), bd=2, width=5, justify= "left")
y_3.place(x=280, y=260) 


botao1 = Button(janela, width=10, text="Iniciar", command=iniciar_automacao, bd=3)
botao1.place(x=230, y=310)

botao2 = Button(janela, width=5, text="Leia", command=arquivo_texto, bd=1)
botao2.place(x=10, y=550) 

botao3 = Button(janela, width=8, text="MouseInfo", command=abrir_mouseinfo, bd=1)
botao3.place(x=70, y=550)

carregar_dados()

janela.mainloop()

