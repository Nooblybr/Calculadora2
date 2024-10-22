import tkinter as tk
from math import sqrt
import re

class Calculadora:
    def __init__(self,janela):
        self.frame_visor = tk.Frame(janela) #Criando o frame do visor onde o resultado aparece
        self.frame_visor.pack()

                                #Configurando o campo onde resultado aparece
        self.texto=tk.StringVar()
        self.expressao = ""
        self.visor = tk.Entry(self.frame_visor,width=15,textvariable=self.texto,font="Arial 20")
        self.visor.pack()

        #Criando o frame dos botões:
        self.frame_botoes = tk.Frame(janela)
        self.frame_botoes.pack()

        botoes = [("%",0,0), ("√",0,1), ("(",0,2), (")",0,3),
                  ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
                  ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
                  ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
                  ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
                  ("C",5,0)]
        
        for botao in botoes:
            self.criar_botoes(botao[0],botao[1],botao[2])


    def criar_botoes(self, texto, linha, coluna):
        botao = tk.Button(self.frame_botoes,text=texto,font="Arial 12",width=7,height=3,command=lambda: self.apertar_botao(texto))
        botao.grid(row=linha, column=coluna)

    def apertar_botao(self,texto):
        if texto == "=":
            self.calcular()
        elif texto == "√":
            self.raiz_quadrada()
        elif texto == "C":
            self.limpar_visor()
        elif texto == "%":
            self.porcentagem()
        else:
            self.expressao += texto
            self.texto.set(self.expressao)

        
    def calcular(self):
        expressao = self.texto.get()
        resultado = eval(expressao,)
        self.expressao = str(resultado)
        self.texto.set(self.expressao)

    def raiz_quadrada(self):
        expressao = self.expressao
        try:
            resultado = sqrt(eval(expressao))
            self.expressao = str(resultado)
            self.texto.set(self.expressao)
        except:
            self.texto.set("ERRO")
            self.expressao = ""

    def porcentagem(self):

        expressao = str(self.texto.get())
        er = r"([/*\-+])([0-9]+)$"     # Separa o sinal operador e o último número em 2 grupos separados
        match = re.search(er,expressao)
        sinal = match.group(1)
        parte1 = re.sub(er,"",expressao)
        parte1 = eval(str(parte1))
        parte2 = float(match.group(2))/100
        parte2 = parte2 * parte1

        expressao = str(parte1) + str(sinal) + str(parte2)


        resultado = eval(expressao)

        self.expressao = str(resultado)
        self.texto.set(str(resultado))



    def limpar_visor(self):
        self.expressao=""
        self.texto.set(self.expressao)

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x445")

calculadora = Calculadora(janela)

janela.mainloop()