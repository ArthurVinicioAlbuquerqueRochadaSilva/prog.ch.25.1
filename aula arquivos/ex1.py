
from operator import truediv
import os
strDir = os.path.dirname(__file__)
try: 
    arqLeitura = open(f'{strDir}\\carta.txt','r', encoding = 'utf-8')
except FileNotFoundError:
    print('ERRO: Arquivo não encontrado')
except Exception as erro:
    print('ERRO: {erro}')
else:
     #readlines é para listas , o read é conteúdo todo, readline vai parágrafo por parágrafo
    
    while True:
        strConteudo = arqLeitura.readline()
        if not strConteudo : break
        print('-'* 50)
        print(strConteudo.strip())
    arqLeitura.close()