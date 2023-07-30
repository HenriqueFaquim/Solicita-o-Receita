from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Variaveis_Soli
import os,shutil



def func_Baixar(pastinha):
    
    num_emp = 0
    dir = r"C:\temp\\"
    try:
        print(os.listdir(pastinha))
    except:
        
        os.makedirs(pastinha)
    try:
        print(os.listdir(dir))
    except:
        
        os.makedirs(dir)


    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": f"{dir}", # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    Variaveis_Soli.empresas()
    Variaveis_Soli.nome_empresas()
    Variaveis_Soli.login()
    usuario = Variaveis_Soli.usuario
    senha = Variaveis_Soli.senha
    entradacnpj = Variaveis_Soli.entradacnpj
    entradanome = Variaveis_Soli.entradanome
    #s=Service(ChromeDriverManager().install())    
    #navegador = webdriver.Chrome(service=s) 
    navegador = webdriver.Chrome(chrome_options=options)
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

    #### looping
    for item in entradacnpj:
        nome = str(entradanome[num_emp])
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
        time.sleep(2)

        try:
            arquivos = list(navegador.find_element(By.CLASS_NAME, 'x-grid-row').find_elements(By.XPATH, '//img[@data-qtip=\"<b>Download disponível</b>. Por favor clique na imagem para fazer o download.\"]'))
            arquivos[1].click()
            time.sleep(2)
        except:
            time.sleep(1)

        for file_name in os.listdir(dir):
            old_name = dir + file_name
            new_name = dir + 'Destinadas - ' + nome + ' ' + file_name
            os.rename(old_name,new_name)
        
        for file in os.listdir(dir):
            try:
                print(os.listdir(pastinha + f'/{nome}'))
            except:
                os.makedirs(pastinha + f'/{nome}')
            
            souce = dir + file
            shutil.move(souce, pastinha + f'/{nome}')

        time.sleep(2)
        try:
            arquivos[0].click()
            time.sleep(2)
        except:
            time.sleep(1)

        for file_name in os.listdir(dir):
                old_name = dir + file_name
                new_name = dir + 'Emitidas - ' + nome + ' ' + file_name
                os.rename(old_name,new_name)

        for file in os.listdir(dir):
                souce = dir + file
                shutil.move(souce, pastinha + f'\{nome}')
        num_emp = num_emp + 1

        time.sleep(1)

    time.sleep(2)
    navegador.quit()

def func01():
    Variaveis_Soli.data()
    Variaveis_Soli.login()
    Variaveis_Soli.empresas()

    usuario = Variaveis_Soli.usuario
    senha = Variaveis_Soli.senha
    entradadi = Variaveis_Soli.entradadi
    entradadf = Variaveis_Soli.entradadf
    entradacnpj = Variaveis_Soli.entradacnpj
    #s=Service(ChromeDriverManager().install())    
    #navegador = webdriver.Chrome(service=s) 
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


