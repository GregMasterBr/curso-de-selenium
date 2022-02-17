from selenium.webdriver import Firefox
from time import sleep

url ='https://curso-python-selenium.netlify.app/exercicio_01.html'
navegador = Firefox()

navegador.get(url)

sleep(3)

tag_h1 = navegador.find_element_by_tag_name('h1')
tag_p_todos = navegador.find_elements_by_tag_name('p')
itens_p = {}

for p in tag_p_todos:
    itens_p[p.get_attribute("atributo")] = p.text
    #print(f'Valor de P é {p.text}')
    print(f'Valor de P é {p.text}')


objeto = {tag_h1.text:itens_p}

print(f'{objeto}')

sleep(10)
navegador.quit()