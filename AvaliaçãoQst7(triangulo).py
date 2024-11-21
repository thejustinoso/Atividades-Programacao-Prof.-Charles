import math

ladoA = int(input('Insira o valor do Lado A:'))
ladoB = int(input('Insira o valor do Lado B:'))
ladoC = int(input('Insira o valor do Lado C:'))

if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
    
    # Cálculo dos ângulos gerado por IA visto que eu não sei bem como usar essa biblioteca.
    angulo1 = math.degrees(math.acos((ladoB**2 + ladoC**2 - ladoA**2) / (2 * ladoB * ladoC)))
    angulo2 = math.degrees(math.acos((ladoA**2 + ladoC**2 - ladoB**2) / (2 * ladoA * ladoC)))
    angulo3 = 180 - angulo1 - angulo2
  
    if ladoA == ladoB == ladoC:
        tipoLados = "Equilátero"
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        tipoLados = "Isósceles"
    else:
        tipoLados = "Escaleno"
      
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        tipoAngulos = "Agudo"
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        tipoAngulos = "Retângulo"
    else:
        tipoAngulos = "Obtuso"

    print(f"O triângulo é {tipoLados} e {tipoAngulos}.")
else:
    print("Não é possível formar um triângulo com esses lados.")
