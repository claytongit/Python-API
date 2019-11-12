import requests

cep = input('Informe um CEP: ')

if len(cep) != 8:
    print('Numeros de digitos invalidos')
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

data = request.json()

if 'erro' not in data:
    print('CEP Localizado: {}'.format(data['cep']))
    print('Bairro: {}'.format(data['logradouro']))
    print('Cidade: {}'.format(data['localidade']))
    print('UF: {}'.format(data['uf']))

else:
    print('CEP invalido! {}'.format(cep))