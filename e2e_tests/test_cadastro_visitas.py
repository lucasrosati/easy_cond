import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class VisitantesTest(unittest.TestCase):
    def setUp(self):

        self.browser = webdriver.Chrome()

    def test_cadastro_visita(self):

        self.browser.get("file:///C:/Users/marce/OneDrive/Dokumenti/GitHub/easy_cond/easy_cond/visitas/templates/visitas/cadastro_visitas.html")

        nome_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "nome")))
        cpf_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "cpf")))
        visitante_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[3]/label[1]/input')))
        cadastrar_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/button')))

        usuario = "Ronaldo Jacaré"
        cpf = "128.420.034-54"

        time.sleep(1)
        for char in usuario:
            nome_input.send_keys(char)
            time.sleep(0.2)

        time.sleep(1)
        for char in cpf:
            cpf_input.send_keys(char)
            time.sleep(0.2)

        time.sleep(1)
        visitante_input.click()

        time.sleep(1)
        cadastrar_input.click()

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
