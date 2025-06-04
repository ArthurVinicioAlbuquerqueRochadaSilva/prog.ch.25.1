
num = int(input('Informe valor inicial da PA: '))
razao = int(input('Informe o valor da razão da PA: '))
nelementos = int(input('Informe a quantidade de elementos da PA: '))
if razao > 0:
    print('Esta PA é crescente')
elif razao < 0:
    print('Está PA é decrescente')
elif razao == 0:
    print('Está PA é constante')


somaPA = num
print(f'Termos da PA = {num} ')
for pa in range(num, nelementos + 1):
    somaPA = somaPA + razao
    print(f'Termos da PA = {somaPA}')
print(f'Soma dos elementos = {(nelementos / 2) * (num + somaPA)}')    
print('FIM')
   
    



