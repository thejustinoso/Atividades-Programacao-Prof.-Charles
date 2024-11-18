horaPartida = str(input('Informe a hora da partida:'))
minutosPartida = str(input('Informe os minutos da partida:'))

horaChegada = str(input('Informe a hora da chegada:'))
minutosChegada = str(input('Informe os minutos da chegada:'))

#Abaixo uso a ferramenta "split()" que permite dividir uma string em substrings para poder trabalhar com os dados separados de horas e minutos.
hsPartida, mnsPartida = horaPartida.split(":")
hsChegada, mnsChegada = horaChegada.split(":")

partidaHs = float(hsPartida)
partidaMns = float(mnsPartida)
chegadaHs = float(hsChegada)
chegadaMns = float(mnsChegada)


segsPartida = (partidaHs * 3600) + (partidaMns * 60)

segsChegada = (chegadaHs * 3600) + (chegadaMns * 60)

#Calculando tempo de viagem
tempViagem = segsChegada - segsPartida
        
segDescanso = float(input('Informe os segundos parados para descanso:'))

consCombustivel = float(input('Informe os litros de combustível consumidos:'))

precoCombustivel = float(input('Informe o preço do litro de combustível (em R$):'))

distancia = float(input('Informe a distância percorrida (em Kms):'))

#Calculando a velocidade média total
velMediaTotal = distancia / (tempViagem / 3600)

#Calculando a velocidade média em movimento
velMediaMov = (distancia / 1000) / (tempViagem  - segDescanso)

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
