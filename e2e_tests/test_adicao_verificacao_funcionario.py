import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class AddFuncionarioTeste(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()

        self.browser.get('https://appeasycond.azurewebsites.net/menu/')
        time.sleep(3)
                 
        go_to_employee_list_button = self.browser.find_element(By.XPATH, '//a[@href="/lista_funcionarios/"]/button')
        go_to_employee_list_button.click()
        time.sleep(2)
          
        return_menu_button = self.browser.find_element(By.XPATH, '//div[@class="return-button"]/a[text()="Retornar ao Menu"]')
        return_menu_button.click()
        time.sleep(2)
        
        go_to_add_employee = self.browser.find_element(By.XPATH, '//a[@href="/adicionar_funcionario/"]/button')
        go_to_add_employee.click()

     

    def test_adicionar_funcionario(self):
        
        nome_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "id_nome")))
        cargo_select_element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'id_cargo')))
        contato_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'id_contato')))
        horario_select_element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'id_horario')))

        funcionario1 = "Ronaldo Jacaré"
        cargo1 = "porteiro"
        contato1 = "(81) 9.8893-1255"
        horario1 = "matutino/vespertino"

        for n in funcionario1:
            nome_input.send_keys(n)
            time.sleep(0.2)
        self.assertEqual(funcionario1, 'Ronaldo Jacaré')

        ActionChains(self.browser).move_to_element(cargo_select_element).click().perform()
        Select(cargo_select_element).select_by_value('porteiro')
        self.assertEqual(cargo1, 'porteiro')
       
        for n in contato1:
            contato_input.send_keys(n)
            time.sleep(0.2)
        
        ActionChains(self.browser).move_to_element(horario_select_element).click().perform()
        time.sleep(1)
        Select(horario_select_element).select_by_value('matutino/vespertino')
        self.assertEqual(horario1, 'matutino/vespertino')
        
        button = WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        button.click()
        
        success_message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Funcionário adicionado com sucesso!")]')))
        self.assertEqual(success_message.text, 'Funcionário adicionado com sucesso!')
        time.sleep(1)
        
        return_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="return-button"]/a')))
        return_button.click()
        
        time.sleep(2)
        
        lista_funcionarios_xpath = '//a[contains(@href, "/lista_funcionarios/")]/button'
        lista_funcionarios = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, lista_funcionarios_xpath)))
        lista_funcionarios.click()
        
        time.sleep(3)
        
        return_menu_button = self.browser.find_element(By.XPATH, '//div[@class="return-button"]/a[text()="Retornar ao Menu"]')
        return_menu_button.click()
        time.sleep(2)
            

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
