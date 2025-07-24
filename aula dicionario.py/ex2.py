import requests, sys, json
try:
    reqHTTP = requests.get('https://api.cartolafc.globo.com/atletas/mercado')
except Exception as erro:
    sys.exit(f'{erro}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('ERRO: Na requisição')
    
    dictCartola = reqHTTP.json()
    #print(dictCartola)