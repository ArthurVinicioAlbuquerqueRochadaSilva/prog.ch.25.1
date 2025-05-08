#Programa para cálculo da média do ifrn
#As notas devem ser inteiras e entre 0 e 100 (inclusive_
#Caso a media seja igual ou superior a 60 o aluno estara aprovado; caso seja igual ou superior a 20 o aluno estara em prova final e os demais casos o aluno estara Reprovado

import sys

etapa1 = int(input("insitra a nota da etapa1:"))
if etapa1 < 0 or etapa1 > 100:
    sys.exit("ERRO: a nota deve ser positiva e menor que 100")
etapa2 = int(input("informe a nota da etapa 2: "))
if etapa2 < 0 or etapa2 > 100 :
    sys.exit("Erro nota Etapa 2 Invalida")

media = round ( (etapa1 * 2 + etapa2 * 3) /5 )
print(f"Media do aluno:{media}")

if media >= 60:
    print("Aluno Aprovado")
elif media >=20:
    print("Aluno está de Prova Final")
else:
    print("Aluno está  reprovado")


