from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont

from bd_geladeiras import scrape, listar_tudo, select_marca
from appWeb import Web

janela = Tk()
style = ttk.Style()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
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

        self.janela.geometry("750x800")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=800)

        self.photo = Image.open("images/magalu.png")
        self.photo = self.photo.resize((188, 55), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)

        rotulo_imagem = tk.Label(janela, image=self.photo, borderwidth=0)
        rotulo_imagem.pack()
        rotulo_imagem.place(relx=0.03, rely=0.03)

    def frames(self):
        # self.frame0 = Frame(self.janela, bg="#0477de")
        # self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="#0477de")
        self.frame1.place(relwidth=0.950, relheight=0.3, relx=0.025, rely=0.2)

    def botoes(self):
        self.btLimpar = Button(text='Limpar', background='#FFFF00', command=self.limpar_bd)
        self.btLimpar.place(relx=0.03, rely=0.12, relwidth=0.10, relheight=0.05)
        self.btCarregar= Button(text='Carregar', command=self.carregar_models)
        self.btCarregar.place(relx=0.15, rely=0.12, relwidth=0.10, relheight=0.05)
        self.btProcurar = Button(text='Buscar', command=self.procurar)
        self.btProcurar.place(relx=0.90, rely=0.134, relwidth=0.07, relheight=0.03)

    def labels(self):
        self.escolhaMarca = Label(text="Escolha a marca", background="#0086FF", foreground='white')
        self.escolhaMarca.place(relx=0.38, rely=0.10, relwidth=0.24, relheight=0.1)
        fontReal = tkFont.Font(family="Arial", size=16, weight="bold" )
        self.escolhaMarca.configure(font=fontReal)
    def dropdown(self):
        op = [
            "Consul",
            "LG",
            "Brastemp",
            "Electrolux",
            "Panasonic",
            "Todas"
        ]
        self.clicked = StringVar()
        self.clicked.set("Marcas")
        self.drop = OptionMenu(janela, self.clicked, *op)
        self.drop.pack()
        self.drop.place(relx=0.65, rely=0.13, relwidth=0.20, relheight=0.04)
        fontdrop= tkFont.Font(family="Arial", size=9, weight='bold')
        self.drop.configure(font=fontdrop)


    def dropdown_precos(self):
        op = [
            "Desc.",
            "Cres.",
            "Todas"
        ]
        self.clicked = StringVar()
        self.clicked.set("Ordem")
        self.drop_precos = OptionMenu(janela, self.clicked, *op)
        self.drop_precos.pack()
        self.drop_precos.place(relx=0.65, rely=0.13, relwidth=0.20, relheight=0.04)
        font_drop = tkFont.Font(family="Arial", size=9, weight='bold')
        self.drop.configure(font=font_drop)
    def limpar_bd(self):
        scrape()
        self.lista_models()

    def carregar_models(self):
        Web()
        self.lista_models()

    def lista(self):

        self.listaMod = ttk.Treeview(self.frame1, height=3, columns=("col1", "col2", "col3", "col4"))


        self.listaMod.heading('#0', text='ID', anchor=CENTER)
        self.listaMod.heading('#1', text='Marca', anchor=CENTER)
        self.listaMod.heading('#2', text='Modelo', anchor=CENTER)
        self.listaMod.heading('#3', text='Preço', anchor=CENTER)

        self.listaMod.column('#0', width=58, anchor=CENTER)
        self.listaMod.column('#1', width=150, anchor=CENTER)
        self.listaMod.column('#2', width=320, anchor=CENTER)
        self.listaMod.column('#3', width=120, anchor=CENTER)
        style.configure(self.listaMod.heading, font=('Arial', 'bold'))
        self.listaMod.place(relx=0.025, rely=0.080, relwidth=0.950, relheight=0.850)

        self.scrollLista = Scrollbar(self.frame1, orient='vertical')
        self.listaMod.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.952, rely=0.079, relwidth=0.02, relheight=0.84)
        self.scrollLista.config(command=self.listaMod.yview)

    def lista_models(self):
        self.listaMod.delete(*self.listaMod.get_children())
        for i in listar_tudo():
            self.listaMod.insert(parent='', index=0, values=(i[1], i[2], i[3]), text=i[0])

    def procurar(self):
        self.listaMod.delete(*self.listaMod.get_children())
        marca = self.clicked.get()
        linhas = select_marca(marca)
        if marca == 'Todas':
            for i in listar_tudo():
                self.listaMod.insert(parent='', index=0, values=(i[1], i[2], i[3]), text=i[0])
        for i in range(len(linhas)):
            self.listaMod.insert(index=i, values=[linhas[i][1], linhas[i][2], linhas[i][3]], parent='', text=[i][0])









