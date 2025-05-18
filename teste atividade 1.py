import sys

num = int(input('digite um número inteiro de até 4 digitos '))
unidade = num % 10 
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num// 1000) % 10

if num <= 0  > 9999:
    sys.exit('ERRO: informe número inteiro positivo de até 4 dígitos')

if num <= 9:
    print(f'soma dos algarismos: {unidade}')
if num >= 10 <= 99:
    print(f'soma dos algarismos:{dezena + unidade} ')
if num >= 100 <=999:
    print(f'soma dos algarismos:{centena + dezena + unidade}')
if num >= 1000 <= 9999:
    print(f'soma dos algarismos:{milhar + centena + dezena + unidade}')