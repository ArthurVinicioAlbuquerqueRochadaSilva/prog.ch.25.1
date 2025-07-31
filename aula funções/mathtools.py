def mdc(v1: int, v2: int)-> int:
    if not isinstance(v1, int):
        raise Exception ('\nERRO: o argumento \'v1\' tem que ser inteiro')
    if not isinstance(v2, int):
        raise Exception ('Valor 2 tem que ser inteiro')
    if v1 <= 0:
        raise Exception ('\nERRO: O arumento \'v1\' tem que ser inteiro positivo')
    if v2 <= 0:
        raise Exception ('Valor 2 tem que ser inteiro positivo')    
    vaux1 = v1
    vaux2 = v2
    while vaux2 != 0:
         vaux1, vaux2 = vaux2, vaux1 % vaux2 
        
    return (f'{v1} e {v2} = {vaux1}')

def fibonacci(quantidade):
    intNumeroAtual   = 1
    intProximoNumero = 1
    print(f'{intNumeroAtual}, {intProximoNumero}, ', end = '')

    for _ in range(3, quantidade + 1):
      
      intNumeroAtual, intProximoNumero = intProximoNumero, intProximoNumero + intNumeroAtual
      print(f'{intProximoNumero}, ', end = '')
      
    return('\n')
#def divisores_primo(intvalor):


