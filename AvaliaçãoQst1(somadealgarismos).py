numero = int(input('Digite um número de até 4 algarismos:'))
soma = 0

if numero > 0 and numero < 10:
    print (f'O número que você digitou foi o {numero}, e como ele é unitário, não pode ser somado com outros algarismos.')
    
elif numero > 9 and numero < 100:
    soma += numero % 10
    numero //= 10
    print (f'O resultado da soma dos algarismos é {soma:.0f}')

elif numero > 99 and numero < 1000:
    soma += numero % 10
    numero //= 10
    soma += numero % 10
    numero //= 10
    print (f'O resultado da soma dos algarismos é {soma:.0f}')

elif numero > 999 and numero < 10000:
    soma += numero % 10
    numero //= 10
    soma += numero % 10
    numero //= 10
    soma += numero % 10
    numero //= 10
    soma += numero % 10
    numero //= 10
    print (f'O resultado da soma dos algarismos é {soma:.0f}')

else:
    print ('Digite um valor válido')
