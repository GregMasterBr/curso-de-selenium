from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from time import sleep

url ='https://selenium.dunossauro.live/aula_04_b.html'
navegador = Firefox()

navegador.get(url)


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

caixas_de_selecao = ['um','dois', 'tres','quatro']
for posicao in caixas_de_selecao:
    sleep(1)
    elemento_ddg = find_by_text(navegador,'div',posicao)
    elemento_ddg.click()

for posicao in caixas_de_selecao:
    sleep(1)
    navegador.back()

for posicao in caixas_de_selecao:
    sleep(1)
    navegador.forward()

print(elemento_ddg)

