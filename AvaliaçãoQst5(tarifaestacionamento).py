minutos = int(input("Digite os minutos em que  carro ficou estacionado: "))
horas = minutos / 60

valor = 0

# Calculando o valor para cada faixa de tempo
if horas <= 2:
    valor = horas * 8

elif horas > 2 and horas < 4:
    valor = 2 * 8 + (horas - 2) * 5

elif horas > 4 and horas < 12:
    valor = 2 * 8 + 2 * 5 + (horas - 4) * 3

else:
    valor = 30

print(f"O valor a ser pago é de R$ {valor:.2f}")