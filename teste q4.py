try:
    a = float(input('Informe valor de A:'))
    b = float(input('Informe valor de B:'))
    c = float(input('Informe valor de C:'))
except ValueError:
    print('ERRO: Digite apenas números')

delta = b**2 - 4 * a * c
if delta > 0:
    x1 = (-b +  delta**(1/2)) / (2 * a)
    x2 = (-b -  delta**(1/2)) / (2 * a)
    print(f'A equação tem duas raízes distintas:')
    print(f'Raiz 1:{x1}')
    print(f'Raiz 2:{x2}')

elif delta == 0:
    x = (-b**2 + delta**(1/2)) / (2 * a)
    print(f'A equação possui uma raiz dupla')
    print(f'Raiz:{x}')

else:
    print(f'A equação não possui raiz')
