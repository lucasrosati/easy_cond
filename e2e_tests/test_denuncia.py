import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class DenunciaTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_denuncia(self):
        self.browser.get("https://appeasycond.azurewebsites.net/denuncia/")

       
        local_input = Select(self.browser.find_element(By.NAME, "local"))
        tipo_infracao_input = Select(self.browser.find_element(By.ID, 'tipo_infracao'))
        unidade_input =  Select(self.browser.find_element(By.ID, 'unidade'))

        
        local_input.select_by_value("espaco_gourmet")
        time.sleep(1)
        tipo_infracao_input.select_by_value("barulho_excessivo")
        time.sleep(1)
        unidade_input.select_by_value("202")
        time.sleep(1)

        
        comentario_input = self.browser.find_element(By.NAME, "comentario")
        comentario = "barulho em excesso! malucos!! "
        for char in comentario:
            comentario_input.send_keys(char)
            time.sleep(0.2)  

        
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

        
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "notification")))

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
