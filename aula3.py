
from selenium.webdriver import Firefox
from time import sleep

url ='https://curso-python-selenium.netlify.app/aula_03.html'
navegador = Firefox()

navegador.get(url)

sleep(3)

tag_p = navegador.find_element_by_tag_name('p')
tag_a = navegador.find_element_by_tag_name('a')

for click in range(10):
    tag_p_todos = navegador.find_elements_by_tag_name('p')

    tag_a.click()
    print(f'Valor de P é {tag_p_todos[-1].text} -> valor do click {click}')

print(f'texto da tag A: {tag_a.text}')
print(f'texto da tag P: {tag_p.text}')

sleep(3)
navegador.quit()
