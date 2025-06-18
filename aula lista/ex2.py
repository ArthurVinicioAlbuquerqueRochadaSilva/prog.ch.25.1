lstNomes = list() 
'ou parenteses apenas'

while True:
    strNome = input('Digite um nome: ').strip()
    if strNome.lower() == 'fim':
        break

    if len(strNome) > 0:
        lstNomes.append(strNome)
        #append é para adicionar
lstNomes.sort()
#sort  , usa para ordenar
print(lstNomes)