import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CamerasTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_acesso_cameras(self):
        url = "https://appeasycond.azurewebsites.net/cameras/"  

        self.browser.get(url)
        
        for i in range(1,5):
            

            elemento = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.grid-container > div:nth-child({i})')))

            elemento.click()
            
            retornar_ao_grid =  WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/button')))
            time.sleep(2)
            retornar_ao_grid.click()
            
            time.sleep(2)

        voltar_ao_menu = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/a')))
        voltar_ao_menu.click()
        time.sleep(2)
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
