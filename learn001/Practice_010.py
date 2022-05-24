from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support.ui i
# from selenium.webdriver.support.ui import I
import time

image_source = r"C:\Users\Administrator\Desktop\T.html"
print(image_source)
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.get("https://m.runoob.com/try/try2.php?filename=tryhtml5_select_form")
driver.get(image_source)
year = driver.find_element(By.ID, "year")
years = driver.find_elements()
input1 = driver.find_element(By.ID, "input1")
cbs1 = driver.find_elements(By.NAME, "cb1")
rds1 = driver.find_element(By.NAME, "Fruit")
select1 = Select(year)
id1 = year.get_property("id")
print(id1)
ops = select1.options
# WebDriverWait(driver, 10).until(lambda x: x>5)
WebDriverWait(driver, 10).until(lambda x: len(Select(x.find_element(By.ID, "year")).options) > 2)
print("gogoogogogooooooooooooooooooooooooooo")
print(len(ops), type(ops))
# type1 = type(select1)
# type2 = type(input1)
# type3 = type(cbs1)
# type4 = type(rds1)
# print(type1, type2, type3, type4)
# print(input1.get_property("type"))
# print(rds1.get_property("type"))
# print(cbs1.get_property("type"))

# for cb in cbs1:
#     print(type(cb))
time.sleep(5)
driver.quit()
