from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Variaveis_Soli
import os,shutil



def func_Baixar(pastinha):
    nome = "AAAAA"
    file = "novo.txt"
    dir = r"C:\temp\\"
    try:
        print(os.listdir(dir))
    except:
        os.makedirs(dir)

    print(pastinha)
    print(dir)
    try:
        print(os.listdir(pastinha + f'/{nome}'))
    except:
        os.makedirs(pastinha + f'/{nome}')
    souce = dir + file
    shutil.move(souce, pastinha + f'/{nome}')