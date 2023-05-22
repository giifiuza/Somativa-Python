from selenium import webdriver
from selenium.webdriver.common.by import By
# from bd_fogao import inserir_models


class Web:
    def __init__(self):
        self.site = {
            'site': 'https://www.magazineluiza.com.br/busca/geladeira/?filters=brand---$marca$',
            'modelo': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[$modelo$]/a/div[3]/h2',
            'precos': '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[$preco$]/a/div[3]/div/div/p[2]',
        }

        self.driver = webdriver.Chrome()
        self.driver.minimize_window()
        self.getDados()

    def getDados(self):

        marcas = ['consul', 'lg', 'brastemp', 'panasonic', 'electrolux']