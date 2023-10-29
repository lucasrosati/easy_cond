from selenium import webdriver
from django.test import LiveServerTestCase 
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User 
from selenium.webdriver.common.keys import Keys 





class teste_login(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('e2e_tests/chromedriver.exe')
            
        
        self.usuario = User.objects.create_user(
            usuario='usuario_teste',
            nome_usuario='RonaldoJacaré',
            senha='12345678',
            apart='100',
            tipo_usuario='MORADOR')
        self.browser.get("http://localhost:8000/")



    def tearDown(self):
        self.browser.close()

    def teste_login_invalido(self):
        self.browser = webdriver.Chrome('e2e_tests/chromedriver.exe')
        self.browser.get('login/pagina_de_cadastro.html')
        usuario = self.browser.find_element_by_xpath(By.XPATH, '//*[@id="cadastroForm"]/div[1]')
        nome_usuario = self.browser.find_element_by_xpath(By.XPATH, '//*[@id="cadastroForm"]/div[2]')
        senha = self.browser.find_element_by_xpath_(By.XPATH, '//*[@id="cadastroForm"]/div[3]')
        apart = self.browser.find_element_by_xpath(By.XPATH, '//*[@id="cadastroForm"]/div[4]')
        tipo_usuario = self.browser.find_element_by_xpath(By.XPATH, '//*[@id="cadastroForm"]/div[5]')
        envio_dados = self.browser.find_element_by_xpath(By.XPATH, '//*[@id="cadastroForm"]/button')
        

        usuario.send_keys('usuario_teste')
        nome_usuario.send_keys('RonaldoJacaré')
        senha.send_keys('12345678')
        apart.send_keys('100')
        tipo_usuario.send_keys('MORADOR')
        envio_dados.send_keys(Keys.RETURN)


        assert 'dados incorretos' in self.browser.page_source




