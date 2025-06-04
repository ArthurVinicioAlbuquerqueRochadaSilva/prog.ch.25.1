#questão do mdc euclides
import sys

try:
    num1 = int(input('Informe número inteiro positivo: '))
    num2 = int(input('Informe número inteiro positivo: '))
except ValueError:
    sys.exit('Informe valor inteiro positivo')
except Exception as e:
    sys.exit('ERRO:{e}')
else:
    if num1 <=0:
        sys.exit('Informe valor inteiro positivo')
    if num2 <=0:
        sys.exit('Informe valor inteiro positivo')
    
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

num1 // num2 = %  
