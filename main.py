from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
path = os.getcwd() + '/chromedriver.exe'

options = webdriver.ChromeOptions()

service = Service(executable_path = path)

driver = webdriver.Chrome(options=options, service=service)

assunto = input('Diggite o assunto que deseja pesquisar: ')

# Pesquissar um link -> driver.get
INITIAL_LINK = f"https://pt.wikipedia.org/wiki/{assunto}"

driver.get(INITIAL_LINK)

h1 = driver.find_element(By.ID, 'firstHeading')  #O find_element usamos quando ha um elemento web, logo o find_element retorna um unico elemento

print('Assunto: ', h1.text)

texto_geral = driver.find_element(By.CSS_SELECTOR, 
                                'div[class="mw-content-container"]')
paragrafos = texto_geral.find_elements(By.TAG_NAME, 'p') # guarda uma lista de elementos paragrafos

assuntos_chave = []
for paragrafo in paragrafos: #veja se tem ancoras dentro dos paragrafos
    elementos_ancora = paragrafo.find_elements(
        By.TAG_NAME, 'a') #Lista de elementos ancoras
    for ancora in elementos_ancora:
        #Adiciona na assuntos_chave(gera uma lista de links) cada ancora encontrada
        print(ancora.text)
        assuntos_chave.append([ancora.text, ancora.get_attribute('href')])
        
for elemento in assuntos_chave:
    print(elemento)
    
with open('assuntos.txt', 'w+') as file:
    file.write(f'Assunto: {h1.text}\n')
    
    for assunto in assuntos_chave:
        file.write(f"Tema: {assunto[0]} - link: {assunto[1]}\n")
        
input('enter para finalizar\n')