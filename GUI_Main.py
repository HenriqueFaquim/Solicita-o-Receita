import PySimpleGUI as sg
from datetime import datetime
import GUI_Tabela as GUI_Tabela
import GUI_Login as GUI_Login
import Solicitar as Solicitar
import SQLite as SQLite
import time


timer = 00
headings = ['Nome', 'CNPJ']
tab = []

sg.SetOptions(background_color='#e9f2f9',
            text_element_background_color='#e9f2f9',
            element_background_color='#e9f2f9',
            scrollbar_color='white',
            input_elements_background_color='#4c5e91',
            button_color=('white','#4c5e91'),
            )

layout = [
    [sg.Text("Solicitação Receita",text_color='#4c5e91',expand_x=True,justification='center', font='Courier 27 italic bold underline')],
    [sg.Text("", key="hora")],
    [sg.Text('Incluir "/" nas datas',text_color='#4c5e91',font='Courier 12 italic bold')],
    [sg.Text('DATA:',font='Courier 14 italic bold',text_color='#4c5e91',expand_x=True), sg.In(key='datai', size=14,font='Courier 14 italic bold',text_color='white') ,sg.Text('a',font='Courier 14 italic bold',text_color='#4c5e91'), sg.In(key='dataf',font='Courier 14 italic bold',size=14,text_color='white')],
    [sg.Text("")],
    [sg.Button("Agendar",expand_x=True,font='Courier 12 italic bold',border_width='2'),
        sg.Button("Salvar",font='Courier 12 italic bold',border_width='2'),
        sg.Button("Empresas",font='Courier 12 italic bold',border_width='2'), 
        sg.Button("Login",font='Courier 12 italic bold',border_width='2'),
        sg.Button("Cancelar",font='Courier 12 italic bold',border_width='2')],
]

janela = sg.Window("Solicitação Receita", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Empresas":
        SQLite.tabela()
        tab = SQLite.dados_tab
        GUI_Tabela.create(tab,headings)
    if evento == "Salvar":
        datai = str(valores['datai'])
        dataf = str(valores['dataf'])
        if datai.find("/") == 2 and dataf.find("/") == 2 and len(datai) == 10 and len(dataf) == 10:
            sg.popup(f"Data registrada: {datai} a {dataf}!!", text_color='black')
            SQLite.attdata(datai,dataf)
        else:
            sg.popup("As datas estão fora do padrão!", text_color='black')
    
    if evento == 'Agendar':
        now = datetime.now()
        timer = now.hour*60
        timer = timer + now.minute
        timer = 1440 - timer
        for i in range(1,3):
            time.sleep(1)
            print(f'passou {i} seg')
        Solicitar.func01()

    if evento == "Login":
        GUI_Login.create()
    
janela.close()