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
botao_clicar = navegador.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/form/div[2]/button')    
#lista_id_fatec = [x.get_attribute("value") for x in _cursos.find_elements(By.TAG_NAME,"option")]

selectFatecs = Select(navegador.find_element(By.ID,'CodFatec'))
print(selectFatecs)

fatecs = {}
fatec_cursos = {}

for fatec in lista_fatecs.find_elements(By.TAG_NAME,'option'):
    sleep(2)
    if fatec.get_attribute('value'):
        _fatec = fatec.text
        _id = fatec.get_attribute("value")
        #print(f'ID: {_id} - FATEC: {fatec}')
        fatecs[fatec.get_attribute("value")] = fatec.text
        fatec.click()
        botao_clicar.submit()
        sleep(3)
        _cursos = navegador.find_element(By.ID,'CodEscolaCurso')
        lista_cursos_fatec = [x.get_attribute("value") for x in _cursos.find_elements(By.TAG_NAME,"option")]
        fatec_cursos[_id] = lista_cursos_fatec[1:]
        print(fatec_cursos)
        #navegador.execute_script("window.history.go(-1)")        
        navegador.back()

print(f'{fatec_cursos}')
sleep(3)
navegador.quit()