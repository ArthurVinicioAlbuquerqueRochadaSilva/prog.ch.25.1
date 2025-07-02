import sys

PALAVRA_CHAVE = 'Flamengo'.lower()
print(' JOGO DA FORCA ')
try:
    letra = input('Digite uma letra: ')
except ValueError:
    sys.exit('ERRO: Tente Novamente')
except Exception as e:
    sys.exit('ERRO:{e} Tente Novamente')
else:
    if len(letra) == 0:
        sys.exit('ERRO: Digite uma letra ')
    tentativas = 6
    
    while letra != PALAVRA_CHAVE:
        tentativas -= 1
        print(f'ERRO: Você tem {tentativas} tentativas, tente novamente:' )
        

        break        
    

           