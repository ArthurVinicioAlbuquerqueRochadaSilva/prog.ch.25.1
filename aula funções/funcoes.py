from logging import exception


def mediaIFRN(nota1: int, nota2: int)-> int:
    
    if not isinstance (nota1, int):
        raise Exception ('Nota1 tem que ser inteiro')
    if not isinstance (nota2, int):
        raise Exception ('Nota2 tem que ser inteiro') 


    if nota1 < 0 or nota1 > 100:
        raise Exception ('Nota1 deve ser entre 0 e 100')
    if nota2 < 0 or nota2 > 100:
        raise Exception ('Nota2 deve ser entre 0 e 100')
    
    media = (nota1 * 2 + nota2 * 3 )/ 5
    
    return int(round(media, 0))

def situacaoFinal(media : int)-> str:
    
    if media >= 60: 
        print('Aprovado')
    elif media >= 20:
        print('Prova final')
    else:
        print('Reprovado') 