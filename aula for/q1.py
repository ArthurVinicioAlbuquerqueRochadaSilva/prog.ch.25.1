#questão do mdc euclides
import sys

try:
    a = int(input('Informe o maior número inteiro positivo: '))
    b = int(input('Informe o menor número inteiro positivo: '))
except ValueError:
    sys.exit('Informe valor inteiro positivo')
except Exception as e:
    sys.exit('ERRO:{e}')
else:
    if a <=0:
        sys.exit('Informe valor inteiro positivo')
    if b <=0:
        sys.exit('Informe valor inteiro positivo')
    if b >= a:
        sys.exit('Informe número menor que o primeiro')

resto = a % b
tentativa = 0
for mdc in range(0, a):
    resto = a % b
    if resto == 0:
        break
    resto2 = b % resto
print(resto2)

