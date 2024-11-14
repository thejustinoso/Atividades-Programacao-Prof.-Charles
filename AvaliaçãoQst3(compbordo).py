#computador de bordo

horaPartida = str(input('Informe a hora da partida (ex: HH:MM):'))

horaChegada = str(input('Informe a hora da chegada (ex: HH:MM):'))

#Abaixo uso a ferramenta "split()" que permite dividir uma string em substrings para poder trabalhar com os dados separados de horas e minutos.
hsPartida, mnsPartida = horaPartida.split(":")
hsChegada, mnsChegada = horaChegada.split(":")

partidaHs = float(hsPartida)
partidaMns = float(mnsPartida)
chegadaHs = float(hsChegada)
chegadaMns = float(mnsChegada)


segsPartida = (partidaHs * 3600) + (partidaMns * 60)

segsChegada = (chegadaHs * 3600) + (chegadaMns * 60)

tempViagem = segsChegada - segsPartida
        
segDescanso = float(input('Informe os segundos parados para descanso:'))

consCombustivel = float(input('Informe os litros de combustível consumidos:'))

precoCombustivel = float(input('Informe o preço do litro de combustível (em R$):'))

distancia = float(input('Informe a distância percorrida (em Kms):'))

velMediaTotal = distancia / tempViagem

velMediaMov = distancia / (tempViagem - segDescanso)

custoViagem = consCombustivel * precoCombustivel

desempenhoKmL = distancia / consCombustivel

desempenhoLh = consCombustivel / tempViagem

desempenhoRsKm = custoViagem / distancia

print (f'Tempo de viagem de: {tempViagem:.2f} segs.')

print (f'Velocidade média total: {velMediaTotal:.2f} Km/h')

print (f'Velocidade média em movimento: {velMediaMov:.2f} Km/h')

print (f'Custo da viagem com combustível: R$ {custoViagem:.2f}.')

print (f'Desempenho do carro: {desempenhoKmL:.2f} Km/L, {desempenhoLh:.2f}L/h, {desempenhoRsKm:.2f}R$/Km')
