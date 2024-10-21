import tkinter as tk

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

        botoes = [("7",0,0), ("8",0,1), ("9",0,2), ("/",0,3),
                  ("4",1,0), ("5",1,1), ("6",1,2), ("*",1,3),
                  ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
                  ("0",3,0), (".",3,1), ("=",3,2), ("+",3,3)]
        
        for botao in botoes:
            self.criar_botoes(botao[0],botao[1],botao[2])


    def criar_botoes(self, texto, linha, coluna):
        botao = tk.Button(self.frame_botoes,text=texto,font="Arial 12",width=6,height=3,command=lambda: self.apertar_botao(texto))
        botao.grid(row=linha, column=coluna)

    def apertar_botao(self,texto):
        if texto == "=":
            self.calcular()
        else:
            self.expressao += texto
            self.texto.set(self.expressao)

        
    def calcular(self):
        expressao = self.texto.get()
        resultado = eval(expressao)
        self.expressao = str(resultado)
        self.texto.set(self.expressao)

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x300")

calculadora = Calculadora(janela)

janela.mainloop()