#Programa palavra chave
senha = '123Mudar'
palavra = ""

while palavra != senha:
    palavra = input('Informe a palavra chave: ')
    if palavra != senha:
        print('Palavra errada')
print('Palavra chave correta')