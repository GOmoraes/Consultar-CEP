import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Print
import requests

# layout
sg.theme('Reddit')
Layout = [
    [sg.Text('Digite o Cep desejado')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Buscar')],
]

#janela

Janela = sg.Window('Tela de Busca',Layout)

# leitura de eventos

while True:
    Eventos, valores = Janela.read()
    if Eventos == sg.WINDOW_CLOSED:
        break
    if Eventos == 'Buscar':
        R= requests.get('http://viacep.com.br/ws/{}/json/'.format(valores['-INPUT-']))
        F = R.json()
        if 'erro' not in F:
            print ('CEP: {}'.format(F['cep']))
            print ('UF: {}'.format(F['uf']))
            print ('Localidade: {}'.format(F['localidade']))
            print ('Bairro: {}'.format(F['bairro']))
            Print (F)