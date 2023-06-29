import PySimpleGUI as sg
import SQLite

def create():

    contact_information_window_layout = [
    [sg.Text("Atualizar Login",expand_x=True, justification='center',text_color='#4c5e91', font='Courier 27 italic bold underline')],
    [sg.Text("")],
    [sg.Text("Login",font='Courier 12 italic bold',text_color='#4c5e91'), sg.In(key='login', text_color='white'),sg.Text("Senha", font='Courier 12 italic bold',text_color='#4c5e91'), sg.In(key='senha', password_char='*',enable_events=True,font='Courier 12 italic bold', text_color='white')],
    [sg.Text("")],
    [sg.Button("Cancelar",font='Courier 12 italic bold',border_width='2'),sg.Button("Salvar",font='Courier 12 italic bold',border_width='2')],
    ]

    contact_information_window = sg.Window("Atualizar Login", 
    contact_information_window_layout, modal=True)

    while True:
        event, values = contact_information_window.read()
        if event == "Cancelar" or event == sg.WIN_CLOSED:
            break
        if event == 'Salvar':
            login = str(values['login'])
            senha = str(values['senha'])
            contact_information_window['login'].Update('')
            contact_information_window['senha'].Update('')
            sg.popup("LOGIN ATUALIZADO COM SUCESSO !!",text_color='black') 
            SQLite.attlog(login,senha)



    contact_information_window.close()

