#Programa para executar uma potenciação de 2 números inteiros utilizando apenas o operador produto (*)
#base = 2
#potencia = 10
# r = base * base * base ...........
base = int(input('Digite o valor da base: '))
potencia = int(input('Digite o valor da potência: '))
r = base ** potencia
p = base
while p < r:
    p *= base

print(p)