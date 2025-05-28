#Programa para executar um produto de 2 números inteios positivos utilizando apenas o operador soma
# x = 80
# y = 6 
# p = y + y + y (80 vezes)
import sys

print(f'Programa para produto')

try:
    x = int(input('Informe valor de x: '))
    y = int(input('Informe o valor de y: '))
    p = 0
    contador = 0
    while contador <= :
        p += y
        contador += 1


    print({x} '')

except ValueError:
    sys.exit('Não foi informado um valor inteiro válido')

except Exception as e:
    sys.exit(f'ERRO:{e}')
else:
    if x <= 0:
        sys.exit('Informe valor positivo')
    if y <= 0:
        sys.exit('Informe valor válido')