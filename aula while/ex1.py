#Programa para exibir tabuada de um número
import sys
try:
    x = int(input('Informe o multiplicador: '))
    if x <= 0:
        sys.exit('Informe número inteiro positivo')
except ValueError:
    sys.exit('Informe multiplicador inteiro positivo')

intMultiplicando = 1
while intMultiplicando  <= 10:
        print(f'({x} x {intMultiplicando} = (intM')