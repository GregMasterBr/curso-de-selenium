from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from time import sleep

url ='https://selenium.dunossauro.live/aula_04_a.html'
navegador = Firefox()

navegador.get(url)

sleep(3)


def find_by_text(browser, tag, text):
    '''
    Encontrar o elemento com o 'texto'

    Argumentos:
        - browser - Instância do navegador em execução (Firefox, Google Chorme, Edge)
        - text -  conteúdo que deve ser encontrado na tag
        - tag - tag onde o text serpá procurado
    '''
    elementos = browser.find_elements(By.TAG_NAME,tag)

    for elemento in elementos:
        if elemento.text==text:
            return elemento
    return

def find_by_href(browser, link, tag='a'):
    '''
    Encontrar o elemento A com o 'link'

    Argumentos:
        - browser - Instância do navegador em execução (Firefox, Google Chorme, Edge)
        - link -  link que será procurado em todas as tags `A` 
        - tag - tag por default é A
    '''
    elementos = browser.find_elements(By.TAG_NAME,tag)

    for elemento in elementos:
        
        if link in elemento.get_attribute('href'):
            return elemento
    return    

elemento_ddg = find_by_text(navegador,'li','DuckDuckGo')

elemento_ddg_link = find_by_href(navegador,'ddg')

print(elemento_ddg)

print(elemento_ddg_link)