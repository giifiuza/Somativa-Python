from selenium import webdriver
from selenium.webdriver.common.by import By


class Web:
    def __init__(self):
        self.site = {
            'site': 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=smartphone&_sacat=0',

            'modelo': '/html/body/div[5]/div[4]/div[2]/div[1]/div[2]/ul/li[3]/div/div[2]/a/div/span/span',
            'precos': ''
        }

        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.minimize_window()
        self.getDados()

    def getDados(self):
        self.driver.get(self.site['site'])
        phone = self.driver.find_element(By.XPATH, self.site['modelo']).text
        print(phone)
