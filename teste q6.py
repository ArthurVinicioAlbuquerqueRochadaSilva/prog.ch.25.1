import math

a = int(input('Digite o lado A: '))
b = int(input('Digite o lado B: '))
c = int(input('Digite o lado C: '))

if a + b > c and b + c > a and a + c > b:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um Triângulo')


if a == b == c:
    print('Classificação do triângulo(Lados) = Equilátero ')
elif (a == b) or (a == c) or (b == c):
    print('Classificação do triângulo(Lados) = Isósceles ')
else:
    print('Classificação do triângulo(Lados) = Escaleno ')

angA = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
angB = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
angC = 180 - angA - angB

if (angA == 90) or (angB == 90) or (angC == 90):
    print('Classificação do Triângulo(ângulo) = Retângulo.')
elif (angA > 90) or (angB > 90) or (angC > 90):
    print('Classificação do Triângulo(ângulo) = Obtusângulo.')
else:
    print('Classificação do Triângulo(ângulo) = Acutângulo.')
