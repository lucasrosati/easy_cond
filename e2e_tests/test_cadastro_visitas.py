import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class VisitantesTest(unittest.TestCase):
    def setUp(self):
        # Configurar o driver do Selenium (certifique-se de que o driver está no PATH)
        self.browser = webdriver.Chrome()

    def test_cadastro_visita(self):
        # Abra a página de cadastro de visitas do seu aplicativo Django
        self.browser.get("file:///C:/Users/marce/OneDrive/Dokumenti/GitHub/easy_cond/easy_cond/visitas/templates/visitas/cadastro_visitas.html")

        nome_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "nome")))
        cpf_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "cpf")))
        visitante_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[3]/label[1]/input')))
        cadastrar_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/button')))

        usuario = "Ronaldo Jacaré"
        cpf = "128.420.034-54"

        # Aguarde 1 segundo para que o campo 'nome' seja visível
        time.sleep(1)
        nome_input.send_keys(usuario)

        # Aguarde 1 segundo para que o campo 'cpf' seja visível
        time.sleep(1)
        cpf_input.send_keys(cpf)

        # Aguarde 1 segundo para que o campo 'visitante' seja visível
        time.sleep(1)
        visitante_input.click()

        # Aguarde 1 segundo antes de clicar no botão 'cadastrar'
        time.sleep(1)
        cadastrar_input.click()

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
