#Programa para executar um produto de 2 números inteios positivos utilizando apenas o operador soma
# x = 80
# y = 6 
# p = y + y + y (80 vezes)
import sys

print(f'Programa para produto')

try:
    x = int(input('Informe valor de x: '))
    y = int(input('Informe o valor de y: '))

    produto = 0
    contador = 0
    while contador < x:
        produto += y
        contador += 1

    print(f'{x} x {y} = {produto}' )

except ValueError:
    sys.exit('INforme valor válido')