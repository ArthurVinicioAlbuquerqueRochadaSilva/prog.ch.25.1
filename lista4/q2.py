import requests, sys
ano = int(input('Digite o ano desejado: '))
strURLCartola = f'https://api.cartolafc.globo.com/{ano}/atletas/mercado'
try:
    dicCartola = requests.get(strURLCartola).json()
except Exception as erro:
    sys.exit(f'ERRO: {erro}')
else:
    if strURLCartola.status_code != 200:
        sys.exit('ERRO: Na requisição')
    print(dicCartola)