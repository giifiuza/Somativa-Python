from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont
from bd_geladeiras import inserir_modelos, scrape, listar_tudo

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        # self.frames()

        # self.dropdown()
        self.botoes()
        self.dropdown()
        self.labels()
        self.frames()
        self.lista()
        self.lista_models()
        # self.grafic()
        janela.mainloop()

    def tela(self):
        self.janela.title("GELADEIRAS 2023")
        self.janela.configure(background="#0086FF")

        self.janela.geometry("700x800")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=800)

        self.photo = Image.open("images/magalu.png")
        self.photo = self.photo.resize((188, 55), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)

        rotulo_imagem = tk.Label(janela, image=self.photo, borderwidth=0)
        rotulo_imagem.pack()
        rotulo_imagem.place(relx=0.03, rely=0.03)

    def frames(self):
        self.frame0 = Frame(self.janela, bg="#7390c9")
        self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="#ffb3b3")
        self.frame1.place(relwidth=0.950, relheight=0.3, relx=0.025, rely=0.2)

    def botoes(self):
        self.btLimpar = Button(text='Limpar', background='#FFFF00', command=self.limpar_bd)
        self.btLimpar.place(relx=0.09, rely=0.12, relwidth=0.10, relheight=0.05)

    def labels(self):
        self.escolhaMarca = Label(text="Escolha a marca", background="#0086FF", foreground='white')
        self.escolhaMarca.place(relx=0.42, rely=0.10, relwidth=0.24, relheight=0.1)
        fontReal = tkFont.Font(family="Arial", size=16, weight="bold", )
        self.escolhaMarca.configure(font=fontReal)
    def dropdown(self):
        clicked = StringVar()
        self.drop = OptionMenu(janela, clicked, "Consul", "LG", "Brastemp", "Electrolux", "Panasonic" )
        self.drop.pack()
        self.drop.place(relx=0.70, rely=0.13, relwidth=0.20, relheight=0.04)
        fontdrop= tkFont.Font(family="Arial", size=9)
        self.drop.configure(font=fontdrop)

    def limpar_bd(self):
        scrape()

    def lista(self):
        self.listaMod = ttk.Treeview(self.frame1, height=3, columns=("col1", "col2", "col3", "col4"))

        self.listaMod.heading('#0', text='ID')
        self.listaMod.heading('#1', text='Marca')
        self.listaMod.heading('#2', text='Modelo')
        self.listaMod.heading('#3', text='Preço')

        self.listaMod.column('#0', width=50)
        self.listaMod.column('#1', width=195)
        self.listaMod.column('#2', width=270)
        self.listaMod.column('#3', width=100)

        self.listaMod.place(relx=0.025, rely=0.080, relwidth=0.950, relheight=0.850)

        self.scrollLista = Scrollbar(self.frame1, orient='vertical')
        self.listaMod.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.952, rely=0.079, relwidth=0.02, relheight=0.84)

    def lista_models(self):
        self.listaMod.delete(*self.listaMod.get_children())
        for i in listar_tudo():
            self.listaMod.insert(parent='', index=0, values=i)



