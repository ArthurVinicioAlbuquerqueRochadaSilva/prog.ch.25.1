'''
   Fazer um programa que faça as seguintes operações.

   1) A partir do conteúdo do arquivo cotacao_dolar.csv gerar uma lista onde cada item
      dessa lista será uma sub-lista com os valores de cada linha do arquivo.

      a) Os valores estão separados por ";";
      b) Os dois primeiros valores são valores do tipo FLOAT;
      c) O terceiro valor é do tipo DATE;
      

   2) Gerar arquivos para cada ano. Salvar o arquivo com o mesmo nome do arquivo que 
      foi aberto na questão 1, adionando no final do nome o sufixo "_nnnn" onde "nnnn" 
      corresponde ao ano das cotações;


   3) Gerar arquivos por ano com as médias das cotações mensais. Salve os arquivos com 
      o nome "media_cotacao_nnnn.csv" onde "nnnn" corresponde ao ano. Cada linha do arquivo
      deverá ter o valor médio de compra, o valor médio de venda e o nome do mês. Separe os valores da 
      linha por ";";

      dica biblioteca statisc e datatime
'''
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
    
    


    