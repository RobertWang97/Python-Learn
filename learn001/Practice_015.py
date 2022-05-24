from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support.ui i
# from selenium.webdriver.support.ui import I
import time, random

image_source = r"C:\Users\Administrator\Desktop\T.html"
print(image_source)
options = Options()
options.add_argument("--headless")  # => 为Chrome配置无头模式
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(1)

# driver.get("https://m.runoob.com/try/try2.php?filename=tryhtml5_select_form")
driver.get(image_source)
print("*"*100, "0000000")
x = driver.find_elements(By.ID, "year333")
y = driver.find_elements(By.ID, "year")
print(len(x),len(y) )
year = driver.find_element(By.ID, "year")
input1 = driver.find_element(By.ID, "input1")
cbs1 = driver.find_elements(By.NAME, "cb1")
rds1 = driver.find_elements(By.NAME, "Fruit")
select1 = Select(year)
id1 = year.get_property("id")
# print(id1)
print(type(cbs1[0]), type(rds1[0]))

print("*"*100, 1111111)
count = random.randint(1, 5)
i = 1
for item in rds1:
    if i == count:
        item.click()
        break
    i += 1
print("*"*100, 2222222)
value = 4
list_options = [str(i + 1) for i in range(value)]
# print(list_options)
a = random.sample(list_options, random.randint(1, len(list_options)))
s = " ".join(a)
print(s)
list_s = s.split(" ")
i = 1
print("*"*100, 333333333)
for item in cbs1:
    if str(i) in list_s:
        item.click()
    i += 1
print("*"*100, 4444444444)
# radios = rds1.find_elements(By.TAG_NAME, "input")
# radios = rds1.
# print(radios)
time.sleep(10)
driver.quit()
