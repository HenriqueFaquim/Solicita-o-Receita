from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Variaveis_Soli


def func01():
    Variaveis_Soli.data()
    Variaveis_Soli.login()
    Variaveis_Soli.empresas()

    usuario = Variaveis_Soli.usuario
    senha = Variaveis_Soli.senha
    entradadi = Variaveis_Soli.entradadi
    entradadf = Variaveis_Soli.entradadf
    entradacnpj = Variaveis_Soli.entradacnpj
    navegador = webdriver.Chrome() 
    navegador.maximize_window()
    navegador.get('https://receita.pr.gov.br/login')
    navegador.implicitly_wait(30)
    navegador.set_page_load_timeout(50)
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="cpfusuario"]').send_keys(usuario)
    time.sleep(1)
    navegador.find_element(By.XPATH, '/html/body/div[2]/form[1]/div[3]/div/input').send_keys(senha)
    time.sleep(1)
    navegador.find_element(By.XPATH, '/html/body/div[2]/form[1]/div[4]/button').click()
    time.sleep(3)
    navegador.get('http://www.dfeportal.fazenda.pr.gov.br/dfe-portal/manterDownloadDFe.do')
    navegador.implicitly_wait(30)
    navegador.set_page_load_timeout(50)
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1030"]').clear()
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1030"]').send_keys(entradadi)
    time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1032"]').clear()
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1032"]').send_keys(entradadf)
    time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1022"]').clear()
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1022"]').send_keys("00:00:00")
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1022"]').send_keys(Keys.ENTER)
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1022"]').send_keys(Keys.ENTER)

    time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1023"]').clear()
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1023"]').send_keys("23:59:59")
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1023"]').send_keys(Keys.ENTER)
    navegador.find_element(By.XPATH, '//*[@id="ext-gen1023"]').send_keys(Keys.ENTER)
    time.sleep(1)

    #### looping

    for item in entradacnpj:
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="ext-gen1081"]').clear()
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="ext-gen1081"]').send_keys(item)
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="ext-gen1081"]').send_keys(Keys.ENTER)
        time.sleep(0.2)
        navegador.find_element(By.XPATH, '//*[@id="ext-gen1081"]').send_keys(Keys.ENTER)
        time.sleep(0.2)
        navegador.find_element(By.XPATH, '//*[@id="ext-gen1081"]').send_keys(Keys.ENTER)
        time.sleep(0.2)
        navegador.find_element(By.XPATH, '//*[@id="ext-gen1081"]').send_keys(Keys.ENTER)
        try:
            navegador.find_element(By.XPATH, '//*[@id="ext-gen1112"]').click()
            navegador.find_element(By.XPATH, '//*[@id="ext-gen1112"]').click()
            navegador.find_element(By.XPATH, '//*[@id="ext-gen1112"]').click()
            navegador.find_element(By.XPATH, '//*[@id="ext-gen1112"]').click()
            time.sleep(1)
            navegador.find_element(By.XPATH, '//*[@id="ucs20_BtnAgendar-btnInnerEl"]').click()
            try:
                time.sleep(1)
                navegador.find_element(By.XPATH, '//*[@id="ext-gen1116"]').click()
                navegador.find_element(By.XPATH, '//*[@id="ext-gen1116"]').click()
                navegador.find_element(By.XPATH, '//*[@id="ext-gen1116"]').click()
                navegador.find_element(By.XPATH, '//*[@id="ext-gen1116"]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '//*[@id="ucs20_BtnAgendar-btnInnerEl"]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '//*[@id="ext-gen1081"]').clear()
            except:
                time.sleep(1)
                navegador.find_element(By.XPATH, '//*[@id="button-1009-btnInnerEl"]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '//*[@id="ext-gen1081"]').clear()
        except:
            time.sleep(1)
            navegador.find_element(By.XPATH, '//*[@id="button-1009-btnInnerEl"]').click()
                
        
### looping
    time.sleep(2)
    navegador.quit()

 
if __name__ == '__main__':
    func01()
