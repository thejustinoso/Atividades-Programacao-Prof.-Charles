numero = str(input('Digite um número de até 4 algarismos:'))

if numero > 0 and numero < 10:
    print (f'O número que você digitou foi o {numero}, e como ele é unitário, não pode ser somado com outros algarismos.')
    
elif numero > 9 and numero < 100:
    soma = int(algarismos[0]) + int(algarismos[1])
    print (f'A soma dos algarismos é: {soma}')

elif numero > 99 and numero < 1000:
    soma = int(algarismos[0]) + int(algarismos[1]) + int(algarismos[2])
    print (f'A soma dos algarismos é: {soma}')

elif numero > 999 and numero < 10000:
    soma = int(algarismos[0]) + int(algarismos[1]) + int(algarismos[3]) + int(algarismos[4])
    print (f'A soma dos algarismos é: {soma}')

else:
    print ('Digite um valor válido')