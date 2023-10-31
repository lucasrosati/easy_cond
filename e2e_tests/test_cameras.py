# import unittest
# from selenium import webdriver

# class CamerasTest(unittest.TestCase):
#     def setUp(self):
#         # Configurar o driver do Selenium (certifique-se de que o driver está no PATH)
#         self.driver = webdriver.Chrome()

#     def test_visualizar_pagina_de_cameras(self):
#         # Abra a página inicial do seu aplicativo Django
#         self.driver.get("file:///C:/Users/marce/OneDrive/Dokumenti/GitHub/easy_cond/easy_cond/cameras/templates/cameras/acesso.html")

#         # Verifique se o título da página está correto
#         self.assertIn("Câmeras de Segurança", self.driver.title)

#         camera1 = self.driver.find_element("")
#         # # Localize os elementos da página (por exemplo, botões, campos de entrada) e interaja com eles
#         # numero_input = self.driver.find_element("#id_numero")
#         # area_input = self.driver.find_element("#id_area")
#         # url_input = self.driver.find_element("#id_url")

#         # # # Preencha os campos com dados de teste
#         # # numero_input.send_keys("01")
#         # # area_input.send_keys("Área de teste")
#         # # url_input.send_keys("http://www.example.com")

#         # # # Submeta o formulário
#         # # submit_button = self.driver.find_element_by_id("submit_button")
#         # # submit_button.click()

#         # # Aguarde a página de resposta (ou elemento) carregar
#         # self.driver.implicitly_wait(10)

#         # # Verifique se a página de resposta contém uma mensagem de sucesso
#         # mensagem_sucesso = self.driver.find_element_by_id("mensagem_sucesso")
#         # self.assertIn("Registro criado com sucesso!", mensagem_sucesso.text)

#     def tearDown(self):
#         # Feche o navegador após o teste
#         self.driver.quit()



