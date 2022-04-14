import requests
from requests.api import options

Cep = input ('Digite o CEP que deseja consultar:\n')

if len(Cep) != 8:
    print('Esse CEP parece estar errado.')
    main()
R= requests.get('http://viacep.com.br/ws/{}/json/'.format(Cep))

F = R.json()
if 'erro' not in F:
    print ('CEP: {}'.format(F['cep']))
    print ('UF: {}'.format(F['uf']))
    print ('Localidade: {}'.format(F['localidade']))
    print ('Bairro: {}'.format(F['bairro']))
    exit()
else:
    option = int(input('{} CEP não encontrado, tente novamente! \n1. Tentar novamente \n2. Sair \n'))
    if option == 1:
        main()
    else:
        print ('Volte Logo')
        __name__ =='__stop__'

CEP = (F['cep'])
