import sys
try:
    num = int(input('Digite um número inteiro positivo: '))
    if num <= 0:
        sys.exit('Digite um número inteiro postivo')
except ValueError:
    sys.exit('Digite valor válido')

else:
    divisor = 1
    contador = 0
    while contador <= num:
        if num % divisor == 0:
            divisor += 1
        contador += 1
    if divisor == 2:
        print('Este número é primo')
    else:
        print('Este número não é primo')