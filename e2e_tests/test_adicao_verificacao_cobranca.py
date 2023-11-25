import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime


class ListaCobrancasTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_acesso_lista_cobrancas(self):
        url = "https://appeasycond.azurewebsites.net/menu/"  
        self.browser.get(url)
        time.sleep(3)

        titulo = self.browser.find_element(By.CSS_SELECTOR, 'h2').text

        adicionar_cobranca_button = self.browser.find_element(By.XPATH, '//a[@href="/adicionar_cobranca/"]/button')
        adicionar_cobranca_button.click()
        
        
        data_input = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(By.ID, "id_data"))
        tipo_conta_input = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(By.ID, "id_tipo_conta"))
        valor_input = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(By.ID, "id_valor"))
        boleto_input = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(By.ID, "id_boleto"))
        
        
        data_formatada = datetime.strptime('25/11/2023', '%d/%m/%Y').strftime('%Y-%m-%d')
        data_input.send_keys(data_formatada)
        data_input(data_formatada)
        
                
        # data = '15/11/2023'
        # tipo_conta = 'Área Comum'
        # valor = '200'
        #boleto = 



    #     if len(linhas_tabela) > 0:
    #         link_boleto = linhas_tabela[0].find_element(By.XPATH, 'td[4]/a')
    #         link_boleto.click()

    #         time.sleep(5)

    #         self.browser.back()

    #     link_retorno = self.browser.find_element(By.XPATH, '//div[@class="return-button"]/a')
    #     link_retorno.click()

    #     time.sleep(5)

    # def tearDown(self):
    #     self.browser.quit()

if __name__ == '__main__':
    unittest.main()
