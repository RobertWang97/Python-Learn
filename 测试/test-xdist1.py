from selenium.webdriver.common.by import By
from selenium import webdriver
init_driver = webdriver.Chrome()
def test_baidu(init_driver):
    init_driver.get("https://www.baidu.com")
    init_driver.find_element(By.ID, 'xx')

    def test_baidu1(init_driver):
        init_driver.get("https://www.baidu.com")
        init_driver.find_element(By.ID, 'xx')

    def test_baidu2(init_driver):
        init_driver.get("https://www.baidu.com")
        init_driver.find_element(By.ID, 'xx')

    def test_baidu3(init_driver):
        init_driver.get("https://www.baidu.com")
        init_driver.find_element(By.ID, 'xx')