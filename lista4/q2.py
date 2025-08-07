import os, sys, json, requests
from datetime import datetime

strDirApp = os.path.dirname(__file__)
strURLCartola = 'https://api.cartolafc.globo.com/atletas/mercado'

x = input('Digite  o ano desejado para o cartola: ')
ano_int = int(x)
ano = datetime(ano_int, 1, 1)
print(f'Ano válido: {ano}')
if ano == 2025:
   dicCartola = requests.get(strURLCartola).json()
elif ano < 2021:
   sys.exit('Cartola só tem do ano 2021 até o atual')
else:
   try:
      arqCartola = open(f'strNomeArq{ano}', 'r', encoding='utf-8')    
   
   except  FileNotFoundError:
      sys.exit('ERRO: Arquivo não existe...')
   except json.JSONDecodeError:
      sys.exit('ERRO: O conteúdo do arquivo não está no formato correto...')
   except Exception as erro:
      sys.exit(f'ERRO: {erro}...')