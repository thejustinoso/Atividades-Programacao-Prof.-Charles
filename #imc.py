#calculo de imc

peso = float(input('Informe seu peso em quilos:'))
altura = float(input('Informe sua altura em metros:'))

imc = peso / altura **2

print (f'Seu IMC é de {imc:.2f}')
