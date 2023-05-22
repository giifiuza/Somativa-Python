from selenium import webdriver
from selenium.webdriver.common.by import By
from bd_geladeiras import inserir_modelos


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

        for marca in marcas:
            site = self.site['site'].replace("$marca$", marca)
            self.driver.get(site)
            for i in range(1, 11):
                nome = self.driver.find_element(By.XPATH, self.site['modelo'].replace("$modelo$", str(i))).text
                preco = self.driver.find_element(By.XPATH, self.site['precos'].replace('$preco$', str(i))).text
                print(nome)
                preco_split = preco.split("R$")
                preco = preco_split[1].split(" ")
                preco[1] = "R$" + preco[1]
                preco_final = preco[1]
                print(preco_final)
                inserir_modelos(marca.capitalize(), nome, preco_final)