import sys

try:
   intQtNumeros = int(input('Digite a quantidade de elementos da Sequência de Fibonacci: '))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   if intQtNumeros < 2:
      sys.exit('ERRO: a Sequência de Fibonacci deve possuir pelo menos 2 números')

   intNumeroAtual   = 1
   intProximoNumero = 1
   print(f'{intNumeroAtual}, {intProximoNumero}, ', end = '')

   if intQtNumeros == 2:
      sys.exit('\n')

   for _ in range(3, intQtNumeros + 1):
      #intAuxiliar      = intProximoNumero 
      #intProximoNumero = intProximoNumero + intNumeroAtual
      #intNumeroAtual   = intAuxiliar

      intNumeroAtual, intProximoNumero = intProximoNumero, intProximoNumero + intNumeroAtual
      print(f'{intProximoNumero}, ', end = '')
      
   print('\n')