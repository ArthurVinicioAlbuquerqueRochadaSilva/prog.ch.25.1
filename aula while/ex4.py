#Programa palavra chave
senha = '123Mudar'
palavra = input('Informe a palavra chave: ')

while palavra != senha:
    palavra = input('Informe a palavra chave: ')
    if palavra != senha:
        print('Informe a palavra chave:')
print('Palavra chave correta')