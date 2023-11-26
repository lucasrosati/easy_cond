import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class CobrancaTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()

        self.browser.get('https://appeasycond.azurewebsites.net/menu/')
        time.sleep(3)
                 
        go_to_billing_list_button = self.browser.find_element(By.XPATH, '//a[@href="/lista_cobrancas/"]/button')
        go_to_billing_list_button.click()
        time.sleep(2)
          
        return_menu_button = self.browser.find_element(By.XPATH, '//div[@class="return-button"]/a[text()="Retornar ao Menu"]')
        return_menu_button.click()
        time.sleep(2)
        
        go_to_add_billing = self.browser.find_element(By.XPATH, '//a[@href="/adicionar_cobranca/"]/button')
        go_to_add_billing.click()

    def test_adicionar_cobranca(self):
        # Obtenha o identificador da janela atual
        main_window = self.browser.current_window_handle

        # Execute o código para adicionar uma cobrança aqui
        data_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "id_data")))
        tipo_conta_select = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "id_tipo_conta")))
        valor_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "id_valor")))
        boleto_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "id_boleto")))

        # Preencha os campos do formulário mais rapidamente
        self.preencher_data_com_mouse(data_input, "25/11/2023")
        self.preencher_lentamente(tipo_conta_select, 'Área Comum')
        self.preencher_lentamente(valor_input, "200")
        self.preencher_lentamente(boleto_input, "https://upload.wikimedia.org/wikipedia/commons/c/c7/BoletoBancario.png")

        # Agora, clique no botão de submit
        submit_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()

        # Aguarde uma mensagem de sucesso (altere o XPATH conforme necessário)
        try:
            success_message = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Cobrança adicionada com sucesso!")]')))
            self.assertEqual(success_message.text, 'Cobrança adicionada com sucesso!')
            print("Mensagem de sucesso encontrada:", success_message.text)
        except Exception as e:
            print("Erro ao encontrar mensagem de sucesso:", e)

        # Agora, retorne ao menu
        self.browser.switch_to.window(main_window)
        return_menu_button = self.browser.find_element(By.XPATH, '//div[@class="return-button"]/a[text()="Retornar ao Menu"]')
        return_menu_button.click()
        time.sleep(2)

        # Abra a lista de cobranças
        go_to_billing_list_button = self.browser.find_element(By.XPATH, '//a[@href="/lista_cobrancas/"]/button')
        go_to_billing_list_button.click()
        time.sleep(2)

        # Agora, abra o boleto da última cobrança adicionada
        lista_cobrancas = self.browser.find_elements(By.XPATH, '//table/tbody/tr')
        if lista_cobrancas:
            ultima_cobranca = lista_cobrancas[-1]
            link_boleto = ultima_cobranca.find_element(By.XPATH, 'td[4]/a')
            link_boleto.click()

            # Aguarde tempo suficiente para visualizar o boleto
            time.sleep(5)

            # Retorne à página anterior
            self.browser.execute_script("window.history.go(-1)")
            time.sleep(2)

            # Retorne ao menu
            return_menu_button_cobranca = self.browser.find_element(By.XPATH, '//div[@class="return-button"]/a[text()="Retornar ao Menu"]')
            return_menu_button_cobranca.click()
            time.sleep(2)

        # Agora, alterne para a janela principal
        self.browser.switch_to.window(main_window)

    def preencher_lentamente(self, elemento, texto):
        for char in texto:
            time.sleep(0.1)
            elemento.send_keys(char)

    def preencher_data_com_mouse(self, elemento, data):
        ActionChains(self.browser)\
            .move_to_element(elemento)\
            .click()\
            .send_keys(data)\
            .perform()

    def tearDown(self):
        # Volte ao menu no final do teste
        return_menu_button_final = self.browser.find_element(By.XPATH, '//div[@class="return-button"]/a[text()="Retornar ao Menu"]')
        return_menu_button_final.click()
        time.sleep(2)

        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
