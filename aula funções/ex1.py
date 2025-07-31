import sys, funcoes
try:
    intE1 = int(input('Informe E1: '))
    intE2 = int(input('Informe E2: '))
except ValueError:
    sys.exit('Informe inteiro válido')
except Exception as erro:
    sys.exit('ERRO; {erro}')
else:
    try:
        mediaFinal = funcoes.mediaIFRN(intE1, intE2)
    except Exception as erro:
        print(f'ERRO: {erro}')
    else:
         print(f'Média = {mediaFinal}')
    situcao = funcoes.situacaoFinal(mediaFinal)
    print(situcao)