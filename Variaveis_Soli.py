import sqlite3

tabela1 = "Empresas"
tabela3 = "Log"

banco = sqlite3.connect('banco_de_dados.db')

cursor = banco.cursor()

usuario = ''
senha = ''
entradadi = ""
entradadf = ''
entradacnpj = []

def login():
    global usuario
    global senha
    cursor.execute(f'SELECT * FROM {tabela3}')
    TabCadastro = cursor.fetchall()[0]
    usuario = TabCadastro[1]
    senha = TabCadastro[2]


def data():
    global entradadi
    global entradadf
    cursor.execute(f'SELECT * FROM {tabela3}')
    TabCadastro = cursor.fetchall()[1]
    entradadi = TabCadastro[1]
    entradadf = TabCadastro[2]

def empresas():
    global entradacnpj
    entradacnpj = []
    cursor.execute(f'SELECT cnpj FROM {tabela1}')
    a = cursor.fetchall()

    for i in range(0,len(a)):
        ab = a[i]
        entradacnpj.append(ab[0])

