from selenium.webdriver import Firefox
from time import sleep

url ='https://curso-python-selenium.netlify.app/exercicio_02.html'
navegador = Firefox()
navegador.get(url)
sleep(3)

tag_a = navegador.find_element_by_tag_name('a')
numero_esperado = navegador.find_elements_by_tag_name('p')[1].text
numero_esperado = numero_esperado.split()[-1]

while(True):
    tag_a.click()
    sleep(1)
    numero_sorteado = navegador.find_elements_by_tag_name('p')[-1].text

    if int(numero_esperado)==int(numero_sorteado):
        break

sleep(3)
navegador.quit()