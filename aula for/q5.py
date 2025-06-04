num = int(input('Informe valor inicial da PA: '))
razao = int(input('Informe o valor da razão da PA: '))
nelementos = int(input('Informe a quantidade de elementos da PA: '))

for pa in range(1, nelementos):
    print(f'{num + razao}')
print('FIM')