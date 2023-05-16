from tkinter import ttk
from tkinter import *
from bd_geladeiras import inserir_modelos, scrape

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        # self.dropdown()
        self.botoes()
        self.dropdown()
        # self.labels()
        # self.inserts()
        # self.lista()
        # self.select_list()
        # self.grafic()
        janela.mainloop()

    def tela(self):
        self.janela.title("GELADEIRAS 2023")
        self.janela.configure(background="#dfe7f7")

        self.janela.geometry("700x800")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=800)


    def frames(self):
        self.frame0 = Frame(self.janela, bg="#7390c9")
        self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="#ffb3b3")
        self.frame1.place(relheight=0.20, relwidth=0.94, relx=0.03, rely=0.12)

    def botoes(self):
        pass
        # self.btListar = Button(self.frame0, text='Listar', command=inserir_modelos)
        # self.btListar.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.50)

    def dropdown(self):
        clicked = StringVar()
        self.drop = OptionMenu(janela, clicked, "Consul", "LG", "Brastemp", "Electrolux", "Panasonic" )
        self.drop.pack()
        self.drop.place(relx=0.10, rely=0.15, relwidth=0.10, relheight=0.08)


