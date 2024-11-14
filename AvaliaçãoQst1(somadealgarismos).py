numero = int(input('Digite um número de até 4 algarismos:'))

if 0 <= numero <= 9999:
    soma = 0
    #Abaixo está um loop para somar cada algarismo extraido da operação "numero % 10" e remove o último algarismo do número com "numero //= 10"
    while numero > 0:
        #Abaixo o operador "+=" atribuir o valor da operação de resto da divisão por 10 da variável numero ("numero % 10") a varável "soma"
        soma += numero % 10
        numero //= 10
    print (f'O resultado da soma dos algarismos é {soma}')

else:
    print ('Digite um valor válido')
