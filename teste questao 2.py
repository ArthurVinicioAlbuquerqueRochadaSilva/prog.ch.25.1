print('Saque de caixa eletrônico')

valor = int(input(' Valor do saque:R$'))
total = valor
ced = 100
totced = valor / ced
if total >= 100:
    print(f'Total de cédulas: {totced}')