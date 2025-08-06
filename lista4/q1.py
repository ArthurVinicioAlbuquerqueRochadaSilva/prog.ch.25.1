import os, sys
from datetime import datetime

strDir = os.path.dirname(__file__)
try: 
    arqLeitura = open(f'{strDir}\\cotacao_dolar.csv','r', encoding = 'utf-8')
except FileNotFoundError:
    print('ERRO: Arquivo não encontrado')
except Exception as erro:
    print('ERRO: {erro}')
else:
    lstCabecalho = arqLeitura.readline().strip().split(';')
    lstLinha = list()
    lstAux = list()
    lstCotacoes = list()
    while True:
        strLinha = arqLeitura.read().strip()
        if not strLinha: break
        
        lstAux = strLinha.split(';')

        try:
            lstAux.append(strLinha)
            compra = float(lstAux[0].replace(',', '.'))
            venda = float(lstAux[1].replace(',', '.'))
            data = datetime.strptime(lstAux[2], '%d/%m/%Y').date()
            
            lstCotacoes.append([compra, venda, data])
        except Exception as e:
            sys.exit(f'ERRO: {e}')

arqLeitura.close()

if lstCotacoes:
    print("\n--- Cotações do Dolar processadas --- ")
    for cotacao in lstCotacoes:
        print(f"Compra: {cotacao[0]: .3f} | Data: {cotacao[2].strftime('%d/%m/%Y')}")
    
    