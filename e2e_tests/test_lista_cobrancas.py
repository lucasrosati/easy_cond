import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ListaCobrancasTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_acesso_lista_cobrancas(self):
        url = "https://appeasycond.azurewebsites.net/lista_cobrancas/"  # Substitua pela URL correta

        self.browser.get(url)

        # Aguarde até que a tabela de cobranças seja carregada (usando time.sleep)
        time.sleep(3)

        # Verifique se o título da página é "Lista de Cobranças"
        titulo = self.browser.find_element(By.CSS_SELECTOR, 'h2').text
        self.assertEqual(titulo, 'Lista de Cobranças')

        # Verifique se há pelo menos uma linha na tabela
        linhas_tabela = self.browser.find_elements(By.CSS_SELECTOR, 'table tbody tr')
        self.assertGreater(len(linhas_tabela), 0)

        # Clique no link "Ver Boleto" da primeira linha (se existir)
        if len(linhas_tabela) > 0:
            link_boleto = linhas_tabela[0].find_element(By.XPATH, 'td[4]/a')
            link_boleto.click()

            # Aguarde até que o link do boleto seja carregado (usando time.sleep)
            time.sleep(5)

            # Volte para a página anterior
            self.browser.back()

        # Clique no link "Retornar ao Menu"
        link_retorno = self.browser.find_element(By.XPATH, '//div[@class="return-button"]/a')
        link_retorno.click()

        # Aguarde até que o link de retorno seja carregado (usando time.sleep)
        time.sleep(5)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
