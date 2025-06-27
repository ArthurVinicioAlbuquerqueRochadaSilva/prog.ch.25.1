'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista apenas com os 
         números pares da lista;
'''
import sys, random

try:
    intN = int(input('Informe o valor de N: '))
    if intN < 0 or intN > 100:
        sys.exit('Informe um valor inteiro positivo')
except ValueError:
    sys.exit('/nERRO: Informe um valor inteiro válido...')
except Exception as e:
    sys.exit(f'ERRO:{e}')
else:
    #item 2
    lista = list ()
    for _ in range (intN):
        intValor = random.randint(-100, 100)
        lista.append(intValor)

    print('Lista original: ')
    print(lista)
 #item 3
    lista_pares = list ()
    for intValor in lista:
        if intValor % 2 == 0:
            lista_pares.append(intValor)
            
print("Lista apenas com os números pares:")
print(lista_pares)
        