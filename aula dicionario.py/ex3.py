import requests, sys, json
try:
    reqHTTP = requests.get('https://viacep.com.br/ws/59031200/json')
except Exception as erro:
    sys.exit(f'{erro}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('ERRO: Na requisição')
    
    dictCEP = reqHTTP.json()
    print(dictCEP)