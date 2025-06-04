num = int(input('Informe valor inicial da PA: '))
razao = int(input('Informe o valor da razão da PA: '))
nelementos = int(input('Informe a quantidade de elementos da PA: '))
contador = 0
while contador <= nelementos:
     num += razao
     contador += 1
print (num)