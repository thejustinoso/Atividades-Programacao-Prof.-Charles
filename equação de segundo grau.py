import sys

a = float(input('Digite um valor para a:'))
b = float(input('Digite um valor para b:'))
c = float(input('Digite um valor para c:'))

delta = b**2 - 4*a*c

if a == 0:
    sys.exit('O valor de "a" tem de ser diferente de zero para ser uma equação de segundo grau.')
else:
    if delta < 0:
        sys.exit('A equação não possui raízes reais.')
    elif delta == 0:
        x = -b / (2*a)
        print(f'A equação possui uma raiz real. x = {x:.2f}.')
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2  = (-b - delta**0.5) / (2*a)
        print(f'A equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}.')
