#Programa para executar um produto de 2 números inteios positivos utilizando apenas o operador soma
# x = 80
# y = 6 
# p = y + y + y (80 vezes)

print(f'Programa para produto')

x = int(input('Informe valor de x: '))
y = int(input('Informe o valor de y: '))
p = y * x
s = 0

while s < p:
    s += y
    print("+", y)

print(s)