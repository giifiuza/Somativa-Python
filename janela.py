from tkinter import ttk
from tkinter import *

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.dropdown()
        # self.botoes()
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
        self.frame0 = Frame(self.janela, bg="#ffb3b3")
        self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="#ffb3b3")
        self.frame1.place(relheight=0.20, relwidth=0.94, relx=0.03, rely=0.12)
        self.frame2 = Frame(self.janela, bg="#ffb3b3")
        self.frame2.place(relheight=0.20, relwidth=0.94, relx=0.03, rely=0.34)

    def dropdown(self):
        self.btBuscar = Button(self.frame0, text='Buscar')
        self.btBuscar.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.50)

        # label.config(text=clicked.get())

        # Dropdown menu options
        options = [
            "Brastemp",
            "Electrolux",
            "Samsung",
            "LG",
            "Consul",
        ]

        # datatype of menu text
        clicked = StringVar()

        # initial menu text
        clicked.set("Choose")

        # Create Dropdown menu
        drop = OptionMenu(self.janela, clicked, *options)
        drop.pack()

        # Create button, it will change label text
        button = Button(self.janela, text="click Me", command=self.dropdown()).pack()

        # Create Label
        label = Label(text="Choose one of them")
