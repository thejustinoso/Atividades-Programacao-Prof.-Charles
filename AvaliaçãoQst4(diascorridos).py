diaInicial = int(input("Digite o dia inicial: "))
mesInicial = int(input("Digite o mês inicial: "))
diaFinal = int(input("Digite o dia final: "))
mesFinal = int(input("Digite o mês final: "))

if mesInicial == mesFinal:
    diasDecorridos = diaFinal - diaInicial
else:
    if mesInicial == 1 or mesInicial == 3 or mesInicial == 5 or mesInicial == 7 or mesInicial == 8 or mesInicial == 10 or mesInicial == 12:
        diasDecorridos = ((mesFinal - mesInicial) * 31) - (diaFinal - diaInicial)

    elif mesInicial == 4 or mesInicial == 6 or mesInicial == 9 or mesInicial == 11:
        diasDecorridos = ((mesFinal - mesInicial) * 30) - (diaFinal - diaInicial)

    elif mesInicial == 2 or mesFinal == 2 :
        diasDecorridos = ((mesFinal - mesInicial) * 28) - (diaFinal - diaInicial)

    else:
        print ('Data inválida.')
        exit()
print(f"Quantidade de dias: {diasDecorridos}")
