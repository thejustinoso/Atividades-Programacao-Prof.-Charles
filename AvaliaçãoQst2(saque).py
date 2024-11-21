valor = float(input('Digite o valor do saque (decimal separado por ponto):'))

if valor <= 0:
    print ('Digite um valor válido.')
    SystemExit
else:
valor = float(input('Digite o valor do saque (decimal separado por ponto):'))
    # Convertendo o valor total em centavos para facilitar o cálculo
    valorCentavos = int(valor * 100)

    cedulas100 = valorCentavos // 10000
    valorCentavos %= 10000

    cedulas50 = valorCentavos // 5000
    valorCentavos %= 5000

    cedulas20 = valorCentavos // 2000
    valorCentavos %= 2000

    cedulas10 = valorCentavos // 1000
    valorCentavos %= 1000

    ceduls5 = valorCentavos // 500
    valorCentavos %= 500

    cedulas2 = valor_centavos // 200
    valor_centavos %= 200

    moedas1 = valorCentavos // 100
    valorCentavos %= 100

    moedas50 = valorCentavos // 50
    valorCentavos %= 50

    moedas25 = valorCentavos // 25
    valorCentavos %= 25

    moedas10 = valorCentavos // 10
    valorCentavos %= 10

    moedas05 = valorCentavos // 5
    valorCentavos %= 5

    moedas01 = valorCentavos // 1

    print("=== SEU SAQUE ===:")
    print("Cédulas:")
    print(f"R$ 100,00: {cedulas100}")
    print(f"R$ 50,00: {cedulas50}")
    print(f"R$ 20,00: {cedulas20}")
    print(f"R$ 10,00: {cedulas10}")
    print(f"R$ 5,00: {cedulas5}")
    print(f"R$ 2,00: {cedulas2}")

    print("Moedas:")
    print(f"R$ 1,00: {moedas1}")
    print(f"R$ 0,50: {moedas50}")
    print(f"R$ 0,25: {moedas25}")
    print(f"R$ 0,10: {moedas10}")
    print(f"R$ 0,05: {moedas05}")
    print(f"R$ 0,01: {moedas01}")

    
