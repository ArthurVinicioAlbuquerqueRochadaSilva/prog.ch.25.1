import sys

distancia = int(input('insira a distancia percorrida em km'))
if distancia <=0:
    sys.exit('informe distancia positiva')

Vo = int(input('velocidade percorrida em km/h'))
if Vo <=0:
    sys.exit('informe velocidade positiva')

acel = int(input('aceleração percorrida em m/s²'))
if acel <=0:
    sys.exit('informe aceleração positiva')

distancia *= 1000
Vo /= 3.6
delta = Vo **2 - 4*acel * distancia
if delta <0:
    sys.exit ('não é possível é possível calcular o tempo')

t = (-Vo + delta**0.5) / (2*acel)
 hora = t // 3600
 t = t % 3600
 minuto = t // 60
 segundo = t % 60
 
 print (f' tempo = {hora} : {minuto} : {segundo}')