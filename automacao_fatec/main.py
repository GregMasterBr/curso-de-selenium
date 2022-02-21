from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from time import sleep

url ='https://www.vestibularfatec.com.br/classificacao/fatec.asp'
#navegador = Firefox(executable_path=GeckoDriverManager().install())
navegador = Firefox()
navegador.get(url)

lista_fatecs = navegador.find_element(By.ID,'CodFatec')
selectFatecs = Select(lista_fatecs)
lenSelectFatecs = len(selectFatecs.options)

botao_clicar = navegador.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/form/div[2]/button')    
lista_id_fatec = [x.get_attribute("value") for x in lista_fatecs.find_elements(By.TAG_NAME,"option")]
del lista_id_fatec[0]
#print((lista_id_fatec))
#print(type(lista_id_fatec))
fatecs = {}
fatec_cursos = {}

for id_fatec in (lista_id_fatec):
    print(id_fatec)
    sleep(1)    
    selectFatecs.select_by_value(id_fatec)
    botao_clicar.submit()
    sleep(3)
    _cursos = navegador.find_element(By.ID,'CodEscolaCurso')
    lista_cursos_fatec = [x.get_attribute("value") for x in _cursos.find_elements(By.TAG_NAME,"option")]
    fatec_cursos[id_fatec] = lista_cursos_fatec[1:]
    #navegador.back()
    navegador.switch_to_default_content()


print(f'{fatec_cursos}')
sleep(3)
navegador.quit()