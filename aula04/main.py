from selenium.webdriver import Firefox
from urllib.parse import urlparse

url ='https://selenium.dunossauro.live/aula_04.html'
navegador = Firefox()

navegador.get(url)

url_parseada= urlparse(navegador.current_url)

print(url_parseada)
print(navegador.title)

#navegador.refresh()
