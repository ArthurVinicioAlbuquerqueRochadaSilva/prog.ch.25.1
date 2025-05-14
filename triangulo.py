import sys

#Solicitar os 3 ângulos do triângulo
angA = int(input(' Digite o ângulo A '))
angB = int(input(' Digite o ângulo B '))
angC = int(input(' Digite o ângulo C '))

#Verificando se os ângulos são positivos
if (angA <= 0 ) or (angB <= 0) or (angC <= 0):
    sys.exit('ERRO: Um ou mais ângulos não são positivos.')

#Verificar se a soma dos ângulos é igual a 180
if angA + angB + angC != 180:
    sys.exit('ERRO: A soma dos ângulos deve ser 180')

#Classificar o triângulo com base nos ângulos
if angA == 90 or angB == 90 or angC == 90:
    print('O triângulo é retângulo.')
elif angA > 90 or angB > 90 or angC > 90:
    print('O triângulo é obtusângulo.')
else:
    print('O triângulo é Acutângulo.')
