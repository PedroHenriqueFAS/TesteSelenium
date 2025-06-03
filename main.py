from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
path = os.getcwd() + '/chromedriver.exe'

options = webdriver.ChromeOptions()

service = Service(executable_path = path)


driver = webdriver.Chrome(options=options, service=service)

# Pesquissar um link -> driver.get
INITIAL_LINK = "https://pt.wikipedia.org/wiki/George_Boole"

driver.get(INITIAL_LINK)

h1 = driver.find_element(By.ID, 'firstHeading')

print('Assunto: ', h1.text)

texto_geral = driver.find_element(By.CSS_SELECTOR, 
                                'div[class="mw-content-container"]')
paragrafos = texto_geral.find_elements(By.TAG_NAME, 'p') # guarda uma lista de elementos paragrafos

assuntos_chave = []
for paragrafo in paragrafos: #veja se tem ancoras dentro dos paragrafos
    elementos_ancora = paragrafo.find_elements(By.TAG_NAME, 'a') #Lista de elementos ancoras
    for ancora in elementos_ancora:
        assuntos_chave.append(ancora.get_attribute('href')) #Adiciona na assuntos_chave cada ancora encontrada
        
for elemento in assuntos_chave:
    print(elemento.text)
input('enter para finalizar\n')