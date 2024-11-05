#calculo de imc

peso = float(input('Informe seu peso em quilos:'))
altura = float(input('Informe sua altura em metros:'))

imc = peso / altura **2

print (f'Seu IMC é de {imc:.2f}')

if imc < 17:
  print ('Você está abaixo do peso')
elif 17 <= imc < 25:
  print ('Você está no peso ideal')
elif 25 <= imc < 30:
  print ('Você está com sobrepeso')
elif 30 <= imc < 35:
  print ('Você está com obesidade grau 1')
elif 35 <= imc < 40:
  print ('Você está com obesidade grau 2')
else:
  print ('Você está com obesidade grau 3')
