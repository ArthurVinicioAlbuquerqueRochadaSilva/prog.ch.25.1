import sys
try:
    num = int(input('Digite inteiro positivo de até 4 dígitos: '))
    num_str = str(num)
except ValueError:
    sys.exit('ERRO: Informe valor válido')
except Exception as e:
    sys.exit(f'ERRO: {e}')
else:
    if num % 1111 == 0:
        sys.exit('ERRO: Número não pode ter algarismos iguais')

    if num <= 0:
        sys.exit('ERRO: Informe valor positivo')
    digitos = 0
    while digitos < len(num_str):
        digitos += 1
        if digitos > 4:
            sys.exit('ERRO: Informe um número inteiro positivo de até 4 dígitos')
            break
        elif digitos == 4:
            crescente = sorted(num_str)
            print(crescente)
            decrescente = sorted(num_str,reverse=True)
            print(crescente)
            print(decrescente)
    maior = int(''.join(sorted(str(crescente))))
    print(maior)    
    iteracao = 0
    for _ in range(0, 8):
        x = maior - menor
        iteracao += 1