from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

service = Service(executable_path = 'chromedriver.exe')

driver = webdriver.Chrome(options=options, service=service)

# Pesquissar um link -> driver.get
INITIAL_LINK = "https://pt.wikipedia.org/wiki/George_Boole"

driver.get(INITIAL_LINK)

h1 = driver.find_element(By.ID, 'firstHeading')

print(h1.text)
input('enter para finalizar\n')