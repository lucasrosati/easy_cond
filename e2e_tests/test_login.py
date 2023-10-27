from selenium import webdriver


def setup(self):
    self.browser = webdriver.Chrome('e2e_tests/chromedriver.exe')
    