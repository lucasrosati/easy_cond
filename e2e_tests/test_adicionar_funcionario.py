import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


class addFuncionarioTeste(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def test_adicionar_funcionario(self):
        self.browser.get('https://appeasycond.azurewebsites.net/adicionar_funcionario/')
        
        
        nome_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "id_nome")))

        cargo_select_element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'id_cargo')))
        contato_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'id_contato')))
        horario_select_element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'id_horario')))


        funcionario = "Ronaldo Jacaré"
        contato = "(81) 9.8893-1255"

            
        time.sleep(1)
        for n in funcionario:
            nome_input.send_keys(n)
            time.sleep(0.2)
            
        time.sleep(1)
        ActionChains(self.browser).move_to_element(cargo_select_element).click().perform()
        Select(cargo_select_element).select_by_value('porteiro')
            
        time.sleep(1)
        
        time.sleep(1)
        for n in contato:
            contato_input.send_keys(n)
            time.sleep(0.2)
        
        time.sleep(1)
        ActionChains(self.browser).move_to_element(horario_select_element).click().perform()
        time.sleep(1)
        Select(horario_select_element).select_by_value('matutino/vespertino')
        
        
        button = WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        time.sleep(1)
        button.click()
        
        
        success_message = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'success-message')))
        self.assertEqual(success_message.text, 'Funcionário adicionado com sucesso!')


        
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
