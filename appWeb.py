from selenium import webdriver
from selenium.webdriver.common.by import By


class Web:
    def __init__(self):
        self.site = {
            'site': 'https://www.magazineluiza.com.br/smart-tv/tv-e-video/s/et/elit/brand---$marca$/',
            # 'modelo': '/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[%bbb%]/a/div[3]/h2',
            'modelo': '/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[1]/a/div[3]/h2',
            'precos': '/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[$ccc$]/a/div[3]/div[2]/div/p[2]',
        }

        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.minimize_window()
        self.getDados()

    def getDados(self):

        marcas = ['samsung', 'lg', 'philco', 'philips', 'tcl']
        for i in range(5):
            print(self.site['site'].replace("$marca$", marcas[i]))

        self.driver.get(self.site['site'])

        #
        # for x in range(2, 12):
        #     print(self.driver.find_element(By.XPATH, self.site['modelo'].replace("%bbb%", f'{x}')).text)

        for model in range(1, 11):
            print(self.driver.find_element(By.XPATH, self.site['precos'].replace("$ccc$", f'{model}')).text)

        # print(self.driver.find_element(By.XPATH, self.site['modelo']).text)
