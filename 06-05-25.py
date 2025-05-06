import sys

Vo = int(input('vel inicial:'))
if Vo <=0:
  sys.exit('informe velocidade positiva')
tempo = int(input('tempo:'))
acel = int(input('aceleração:'))

dist = Vo * tempo + ((acel * (tempo**2)) / 2)

print(f'distancia percorrida: {dist:.2f}')
