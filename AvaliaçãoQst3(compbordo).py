horaPartida = int(input('Informe a hora da partida:'))
minutosPartida = int(input('Informe os minutos da partida:'))

horaChegada = int(input('Informe a hora da chegada:'))
minutosChegada = int(input('Informe os minutos da chegada:'))

segsPartida = (horaPartida * 3600) + (minutosPartida  * 60)

segsChegada = (horaChegada * 3600) + (minutosChegada * 60)

#Calculando tempo de viagem
tempViagem = segsChegada - segsPartida

if segsChegada > segsPartida:
    #Para casos onde o tempo de chegada é anterior à hora de partida (caso de viagens noturnas que terminam na madrugada do dia seguinte) para que não seja dado um resultado negativo, se realiza um ajuste no cálculo de 24 horas ao tempo final para considerar a mudança de dia
    tempViagem += 24 *3600
    segDescanso = float(input('Informe os segundos parados para descanso:'))

    consCombustivel = float(input('Informe os litros de combustível consumidos:'))

    precoCombustivel = float(input('Informe o preço do litro de combustível (em R$):'))

    distancia = float(input('Informe a distância percorrida (em Kms):'))

    #Calculando a velocidade média total
    velMediaTotal = distancia / (tempViagem / 3600)

    #Calculando a velocidade média em movimento
    velMediaMov = (distancia / ((tempViagem / 3600)- segDescanso)) * -1

    #Calculando o custo total da viagem
    custoViagem = consCombustivel * precoCombustivel

    #Calculando o desempenho em Km/L
    desempenhoKmL = distancia / consCombustivel

    #Calculando o desempenho em L/h
    desempenhoLh = consCombustivel / (tempViagem / 3600)

    #Calculando o desempenho em R$/Km
    desempenhoRsKm = custoViagem / distancia

    print (f'Tempo de viagem de: {tempViagem:.0f}segs.')

    print (f'Velocidade média total: {velMediaTotal:.1f}Km/h')

    print (f'Velocidade média em movimento: {velMediaMov:.1f}Km/h')

    print (f'Custo da viagem com combustível: R$ {custoViagem:.2f}.')

    print (f'Desempenho do carro: {desempenhoKmL:.2f}Km/L, {desempenhoLh:.2f}L/h, {desempenhoRsKm:.2f}R$/Km')

else:
    segDescanso = float(input('Informe os segundos parados para descanso:'))

    consCombustivel = float(input('Informe os litros de combustível consumidos:'))

    precoCombustivel = float(input('Informe o preço do litro de combustível (em R$):'))

    distancia = float(input('Informe a distância percorrida (em Kms):'))

    #Calculando a velocidade média total
    velMediaTotal = distancia / (tempViagem / 3600)

    #Calculando a velocidade média em movimento
    velMediaMov = (distancia / ((tempViagem / 3600)- segDescanso)) * -1

    #Calculando o custo total da viagem
    custoViagem = consCombustivel * precoCombustivel

    #Calculando o desempenho em Km/L
    desempenhoKmL = distancia / consCombustivel

    #Calculando o desempenho em L/h
    desempenhoLh = consCombustivel / (tempViagem / 3600)

    #Calculando o desempenho em R$/Km
    desempenhoRsKm = custoViagem / distancia

    print (f'Tempo de viagem de: {tempViagem:.0f}segs.')

    print (f'Velocidade média total: {velMediaTotal:.1f}Km/h')

    print (f'Velocidade média em movimento: {velMediaMov:.1f}Km/h')

    print (f'Custo da viagem com combustível: R$ {custoViagem:.2f}.')

    print (f'Desempenho do carro: {desempenhoKmL:.2f}Km/L, {desempenhoLh:.2f}L/h, {desempenhoRsKm:.2f}R$/Km')
