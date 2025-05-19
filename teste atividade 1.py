import sys

num = int(input('Digite um número inteiro de até 4 digitos:'))

unidade = num % 10 
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num// 1000) % 10

if num <= 0:
    sys.exit('ERRO: Informe número inteiro positivo de até 4 digitos')
elif num > 9999:
     print(f'ERRO: Informe número inteiro positivo de até 4 dígitos')

if num <= 9999:
    print(f'Soma dos algarismos: {milhar + centena + dezena + unidade}')
elif num <= 999:
    print(f'Soma dos algarismos: {centena + dezena + unidade}')
elif num <= 99:
    print(f'Soma dos algarismos: {dezena + unidade}')
elif num <= 9:
    print(f'Soma dos algarismos: {unidade}')

