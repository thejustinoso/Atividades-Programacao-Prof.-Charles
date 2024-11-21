diaInicial = int(input("Digite o dia inicial: "))
mesInicial = int(input("Digite o mês inicial: "))
diaFinal = int(input("Digite o dia final: "))
mesFinal = int(input("Digite o mês final: "))

if 1 <= diaInicial <= 31 and 1 <= diaFinal <= 31:
    print ('Data inválida.')
    SystemExit
elif 1 <= mesInicial <= 12 and 1 <= mesFinal <= 12:
    print ('Data inválida.')
    SystemExit 
# Identificando se um dos meses é de 30 dias
elif mesInicial in ['04', '06', '09', '11'] or mesFinal in ['04', '06', '09', '11']:
    a
# Identificando se um dos meses é Feveiro, mês com 28 dias
elif mesInicial == '02' or mesFinal == '02':
    a
