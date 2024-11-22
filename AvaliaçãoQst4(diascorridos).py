diaInicial = int(input("Digite o dia inicial: "))
mesInicial = int(input("Digite o mês inicial: "))
diaFinal = int(input("Digite o dia final: "))
mesFinal = int(input("Digite o mês final: "))

if mesInicial == mesFinal:
    diasDecorridos = diaFinal - diaInicial
else:
    #O operador "in" é utilizado para verificar se um valor pertence a uma sequência.
    if mesInicial in [1, 3, 5, 7, 8, 10, 12]:
        diasDecorridos = ((mesFinal - mesInicial) * 31) - (diaFinal - diaInicial)

    elif mesInicial in [4, 6, 9, 11]:
        diasDecorridos = ((mesFinal - mesInicial) * 30) - (diaFinal - diaInicial)

    elif mesInicial == '2' or mesFinal == '2' :
        diasDecorridos = ((mesFinal - mesInicial) * 28) - (diaFinal - diaInicial)

    else:
        print ('Data inválida.')
        exit()
print(f"Quantidade de dias: {diasDecorridos}")
