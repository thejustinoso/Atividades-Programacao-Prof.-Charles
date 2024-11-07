base = float(input('Informe a medida da base:'))
altura = float(input('Informe a medida da altura:'))

if base <= 0:
    print('A base não pode ser igual a zero ou negativa')

elif altura <= 0:
    print('A altura não pode ser igual a zero ou negativa')

elif base == altura:
    print ('O quadrilátero é um Quadrado.')

else:
    print ('O quadrilátero é um Retângulo.')
