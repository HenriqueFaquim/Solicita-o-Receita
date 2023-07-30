import PySimpleGUI as sg
import SQLite

def create(tab, headings):
    tab.sort()
    contact_information_window_layout = [
    [sg.Text("Empresas Cadastradas",expand_x=True, justification='center',  font='Courier 27 italic bold underline',text_color='#4c5e91')],
    
    [sg.Table(values=tab,
            headings=headings,
            num_rows=10,
            auto_size_columns=False,
            col_widths=[35,20],
            enable_events=True, 
            key='_filestable_',
            expand_x=True, 
            justification='center',
            font='Courier 12 italic bold',
            text_color='black')],

    [sg.Text("Nome",font='Courier 12 italic bold',text_color='#4c5e91'), 
        sg.In(key='nome',font='Courier 12 italic bold',text_color='white'),
        sg.Text("CNPJ",font='Courier 12 italic bold',text_color='#4c5e91'), 
        sg.In(key='cnpj',font='Courier 12 italic bold',text_color='white'), 
        sg.Button("Adicionar",font='Courier 12 italic bold',border_width='2',expand_x=True)],

    [sg.Text("Empresa",font='Courier 12 italic bold',text_color='#4c5e91'), 
        sg.In(expand_x=True,key='apagar',font='Courier 12 italic bold',text_color='white'),
        sg.Button("Deletar",font='Courier 12 italic bold',border_width='2')],
    
    [sg.Text("")],

    [sg.Button("Cancelar",font='Courier 12 italic bold',border_width='2')],
    ]

    contact_information_window = sg.Window("Empresas Cadastradas", 
    contact_information_window_layout, modal=True)

    while True:
        event, values = contact_information_window.read()
        if event == "Cancelar" or event == sg.WIN_CLOSED:
            break

        if event == "Adicionar":
            temp = values['cnpj']
            if temp.isnumeric() == False:
                sg.popup("Digite apenas numeros no CNPJ",text_color='black',font='Courier 12 italic bold')
            elif len(temp) != 14:
                sg.popup("CNPJ inválido",text_color='black',font='Courier 12 italic bold')
            else:

                nome = str(values['nome'])                
                cnpj = str(values['cnpj'][0]) + str(values['cnpj'][1]) + '.' + str(values['cnpj'][2])+ str(values['cnpj'][3])+ str(values['cnpj'][4])+ '.' + str(values['cnpj'][5]) + str(values['cnpj'][6]) + str(values['cnpj'][7]) + '/' + str(values['cnpj'][8])+ str(values['cnpj'][9])+ str(values['cnpj'][10])+ str(values['cnpj'][11]) + '-' + str(values['cnpj'][12]) + str(values['cnpj'][13])
                SQLite.add(nome,cnpj)
                SQLite.tabela()
                tab = SQLite.dados_tab
                contact_information_window['_filestable_'].update(tab)
                contact_information_window['nome'].Update('')
                contact_information_window['cnpj'].Update('')
                
                sg.popup('EMPRESA SALVA !',text_color='black',font='Courier 12 italic bold')

        if event == "Deletar":
            SQLite.tabela()
            tab = SQLite.dados_tab
            delemp = str(values['apagar'])
            if delemp not in str(tab):
                sg.popup("NOME INVALIDO!",text_color='black',font='Courier 12 italic bold')
            else:
                SQLite.remove(delemp)
                contact_information_window['apagar'].Update('')
                SQLite.tabela()
                tab = SQLite.dados_tab
                contact_information_window['_filestable_'].update(tab)
                sg.popup("EMPRESA REMOVIDA !",text_color='black',font='Courier 12 italic bold')



    contact_information_window.close()

