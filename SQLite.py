import sqlite3

banco = sqlite3.connect('banco_de_dados.db')

cursor = banco.cursor()

tabela1 = "Empresas"
tabela2 = "Cadastro"
login = "69696411987"
senha = "8001DI"
dados_tab =[]

    #Criação das Tabelas ##
#cursor.execute('CREATE TABLE Log (id int, cpf text, senha text)')
#cursor.execute('CREATE TABLE Cadastro (cpf text, senha text)')

    ## comando padrão para inserir valores ##
#cursor.execute('INSERT INTO Log VALUES("02","01/04/2023", "30/04/2023")')
#cursor.execute('INSERT INTO Cadastro VALUES("69696411987", "8001DI")')



def tabela():
    global dados_tab
    global cursor
    cursor.execute("SELECT * FROM Empresas")
    a = cursor.fetchall()
    for i in range(0,len(a)):
        a[i]=list(a[i])
    dados_tab = a


def add(empresa,cnpj):
    global cursor
    global banco
    cursor.execute(f'INSERT INTO Empresas VALUES("{empresa}", "{cnpj}")')
    banco.commit() 


def remove(empresa):
    global cursor
    global banco
    cursor.executescript(f'DELETE FROM Empresas WHERE Nome = "{empresa}"')
    banco.commit() 

def attlog(login,senha):
    global cursor
    global banco
    cursor.executescript(f'UPDATE Log SET cpf = "{login}", senha ="{senha}"  WHERE id = 01;')
    banco.commit() 

def attdata(datai,dataf):
    global cursor
    global banco
    cursor.executescript(f'UPDATE Log SET cpf = "{datai}", senha ="{dataf}"  WHERE id = 02;')
    banco.commit() 