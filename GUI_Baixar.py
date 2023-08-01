import PySimpleGUI as sg
import Solicitar

def Baixar():

    contact_information_window_layout = [
    [sg.Text("Baixar Notas",expand_x=True, justification='center',text_color='#6061EF', font='Courier 27 italic bold underline')],
    [sg.Text("")],
    [sg.Text('Diretório:',font='Courier 12 italic bold'),sg.Input(key='-USER FOLDER-', font='Courier 12 italic bold', text_color='black',readonly=True,enable_events=True), sg.FolderBrowse('Buscar',target='-USER FOLDER-',key='folder',font='Courier 12 italic bold')],
    [sg.Text("")],
    [sg.Button("Baixar",font='Courier 12 italic bold',border_width='2'),sg.Button("Voltar",font='Courier 12 italic bold',border_width='2')],
    ]

    contact_information_window = sg.Window("Atualizar Login", 
    contact_information_window_layout, modal=True, icon='Icone.ico')

    while True:
        event, values = contact_information_window.read()
        if event == "Voltar" or event == sg.WIN_CLOSED:
            break
        if event == 'Baixar':
            diretorio = values['folder']
            if diretorio == '':
                sg.popup("Selecione uma pasta de destino!",text_color='black',font='Courier 12 italic bold')
            else:
                Solicitar.func_Baixar(diretorio)



    contact_information_window.close()

