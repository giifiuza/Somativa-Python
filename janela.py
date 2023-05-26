from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bd_geladeiras import scrape, listar_tudo, select_marca, listar_precoCresc, preco_LG, preco_Elec, preco_Pana, preco_Brast, preco_Consu
from appWeb import Web

janela = Tk()
style = ttk.Style()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.botoes()
        self.dropdown()
        # self.dropdown_precos()
        self.labels()
        self.frames()
        self.lista()
        self.lista_models()
        self.grafic()
        janela.mainloop()

    def tela(self):
        self.janela.title("GELADEIRAS 2023")
        self.janela.configure(background="#0086FF")

        self.janela.geometry("750x800")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=700)

        self.photo = Image.open("images/magalu.png")
        self.photo = self.photo.resize((188, 55), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)

        rotulo_imagem = tk.Label(janela, image=self.photo, borderwidth=0)
        rotulo_imagem.pack()
        rotulo_imagem.place(relx=0.03, rely=0.03)

    def frames(self):
        self.frame1 = Frame(self.janela, bg="#0477de")
        self.frame1.place(relwidth=0.950, relheight=0.3, relx=0.025, rely=0.20)

    def botoes(self):
        self.btLimpar = Button(text='Limpar', background='#FFFF00', command=self.limpar_bd)
        self.btLimpar.place(relx=0.03, rely=0.12, relwidth=0.10, relheight=0.05)
        self.btCarregar= Button(text='Carregar', command=self.carregar_models)
        self.btCarregar.place(relx=0.15, rely=0.12, relwidth=0.10, relheight=0.05)
        self.btProcurar = Button(text='Buscar', command=self.procurar)
        self.btProcurar.place(relx=0.90, rely=0.134, relwidth=0.07, relheight=0.03)
        # self.btPreco = Button(text='Procurar', command=self.ordem_preco)
        # self.btPreco.place(relx=0.90, rely=0.195, relwidth=0.07, relheight=0.03)

    def labels(self):
        self.escolhaMarca = Label(text="Escolha a marca", background="#0086FF", foreground='white')
        self.escolhaMarca.place(relx=0.38, rely=0.10, relwidth=0.24, relheight=0.1)
        fontReal = tkFont.Font(family="Arial", size=16, weight="bold" )
        self.escolhaMarca.configure(font=fontReal)
        # self.escolhaOrdem = Label(text="Ordem", background="#0086FF", foreground='white')
        # self.escolhaOrdem.place(relx=0.465, rely=0.18, relwidth=0.18, relheight=0.07)
        # fontReal = tkFont.Font(family="Arial", size=16, weight="bold")
        # self.escolhaOrdem.configure(font=fontReal)
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

    # def dropdown_precos(self):
    #     op = [
    #         "Desc.",
    #         "Cres.",
    #         "Todas"
    #     ]
    #     self.clickedd = StringVar()
    #     self.clickedd.set("Preço")
    #     self.drop_precos = OptionMenu(janela, self.clickedd, *op)
    #     self.drop_precos.pack()
    #     self.drop_precos.place(relx=0.65, rely=0.19, relwidth=0.20, relheight=0.04)
    #     font_drop = tkFont.Font(family="Arial", size=9, weight='bold')
    #     self.drop_precos.configure(font=font_drop)
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

    # def ordem_preco(self):
    #     self.listaMod.delete(*self.listaMod.get_children())
    #     ordem = self.clicked.get()
    #     if ordem == 'Cres.':
    #         listar_precoCresc()
    #         self.lista_models()

    def grafic(self):

        self.figura = plt.Figure(figsize=(10, 5), dpi=60)
        self.grafic = self.figura.add_subplot(111)
        self.canva = FigureCanvasTkAgg(self.figura)
        self.tkwid = self.canva.get_tk_widget()
        self.tkwid.place(relx=0.1, rely=0.53)
        self.grafic.set_ylabel('Preços')
        self.grafic.set_xlabel('Marcas')
        self.grafic.set_title('Comparação preços entre cada marca')

        marcas = ['LG', 'Consul', 'Panasonic', 'Electrolux', 'Brastemp']
        precolg = []
        precocon = []
        precopana = []
        precoele = []
        precobras = []

        '''For para pegar preço de cada marca e colocar em uma lista para fazer uma média'''
        for x in preco_LG():
            for i in x:
                precolg.append(float(i[2:].replace(".", "").replace(",", ".")))

        precoLG = (sum(precolg)/len(precolg))
        print(f'{precoLG:,.2f}')

        for x in preco_Pana():
            for i in x:
                precopana.append(float(i[2:].replace(".", "").replace(",", ".")))

        precoPana = (sum(precopana)/len(precopana))
        print(f'{precoPana:,.2f}')

        for x in preco_Consu():
            for i in x:
                precocon.append(float(i[2:].replace(".", "").replace(",", ".")))

        precoCons = (sum(precocon)/len(precocon))
        print(f'{precoCons:,.2f}')

        for x in preco_Brast():
            for i in x:
                precobras.append(float(i[2:].replace(".", "").replace(",", ".")))

        precoBras = (sum(precobras)/len(precobras))
        print(f'{precoBras:,.2f}')

        for x in preco_Elec():
            for i in x:
                precoele.append(float(i[2:].replace(".", "").replace(",", ".")))

        precoElec = (sum(precoele)/len(precoele))
        print(f'{precoElec:,.2f}')

        medias = [precoLG, precoCons, precoPana, precoElec, precoBras]
        colors = ['orange','orange','orange','orange','orange']

        self.grafic.bar(marcas, medias, color=colors)










