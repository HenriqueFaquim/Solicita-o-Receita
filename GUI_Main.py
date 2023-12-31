import PySimpleGUI as sg
from datetime import datetime
import GUI_Tabela as GUI_Tabela
import GUI_Login as GUI_Login
import Solicitar as Solicitar
import SQLite as SQLite
import time
import GUI_Baixar

indices = [1440,1410,1380,1350,1320,1290,1]
horas = ['00:00','00:30','01:00','01:30','02:00','02:30','03:00','03:30','04:00','04:30','05:00','05:30','06:00','06:30','07:00','07:30','08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00','22:30','23:00','23:30',]
headings = ['Nome', 'CNPJ']
tab = []

sg.SetOptions(background_color='white',
            text_element_background_color='white',
            element_background_color='white',
            scrollbar_color='white',
            input_elements_background_color='#e6e6e6',
            button_color=('white','#6061EF'),
            element_text_color='black',
            text_color='black',
)

layout = [
    [sg.Image(filename='Menu.png',size=(500, 150),expand_x=True)],
    [sg.In('',font='Courier 14 italic bold',text_color='black',key='datai',size=12,readonly=True,enable_events=True), sg.CalendarButton('Data inicial',format='%d/%m/%Y',font='Courier 10 italic bold') ,sg.In('',font='Courier 14 italic bold',text_color='black',key='dataf',size=12,readonly=True,enable_events=True), sg.CalendarButton('Data Final',format='%d/%m/%Y',font='Courier 10 italic bold')],
    [sg.Text("")],
    [sg.Text('',expand_x=True),sg.Text('Agendar Horário:',font='Courier 14 italic bold',text_color='black'), sg.Spin(horas,size=14,font='Courier 14 italic bold',text_color='black',readonly=True,enable_events=True, key='hora')
],
    [sg.Text('',expand_x=True), sg.Checkbox('Solicitar agora', key='checkbox',font='Courier 14 italic bold')
],
    [sg.Button("Agendar",expand_x=True,font='Courier 12 italic bold',border_width='2'),
        
        sg.Button("Baixar Notas",font='Courier 12 italic bold',border_width='2',key='baixar'), 
        sg.Button("Configurações",font='Courier 12 italic bold',border_width='2'), 
        sg.Button("Cancelar",font='Courier 12 italic bold',border_width='2')],
]

janela = sg.Window("Solicitação Receita", layout, icon='Icone.ico')

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Configurações":
        SQLite.tabela()
        tab = SQLite.dados_tab
        tab.sort()
        GUI_Tabela.create(tab,headings)

    
    if evento == 'Agendar':
        datai = valores['datai']
        dataf = valores['dataf']
        hora = valores['hora']
        SQLite.attdata(datai,dataf) 

        if dataf == '' or datai =='':
            sg.popup("Selecione o período desejado!",text_color='black',font='Courier 12 italic bold')
        elif dataf < datai:
            sg.popup("data final menor que a inicial!",text_color='black',font='Courier 12 italic bold')
        elif valores['checkbox'] == True:
            Solicitar.func01()
        else:
            sg.popup_auto_close(f"Solicitações agendadas para {hora}",text_color='red',font='Courier 12 italic bold')
            hora_ag = str(hora[0]+hora[1])
            min_ag = str(hora[3]+hora[4])
            while True:
                agora = time.localtime()
                if str(agora[3]) == '0' and str(agora[4]) == '0':
                    hora_atual = "00" + ':' + '00'
                elif str(agora[3]) == '0':
                    hora_atual = "00" + ':' + str(agora[4])
                elif str(agora[4]) == '0':
                    hora_atual = str(agora[4]) + ':' + '00'
                else:
                    hora_atual = str(agora[3]) + ':' + str(agora[4])
                
                hora_agendada = hora_ag + ':' + min_ag
                time.sleep(10)
                if hora_atual == hora_agendada:
                    Solicitar.func01()
                    break

    if evento == "baixar":
        GUI_Baixar.Baixar()

janela.close()