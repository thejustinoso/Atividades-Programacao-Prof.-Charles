#Este código recebeu contribuição de IA para uso das bibliotecas.

from datetime import datetime
from dateutil.relativedelta import relativedelta # type: ignore

sexo = ('Informe seu sexo (M ou F):').strip().lower()
nascimento = ('Informe sua data de nascimento no formato DD/MM/AAAA:').strip()
inicioContribuicao = ('Informe a data em que você começou a contribuir com a previdência no formato DD/MM/AAAA:').strip()

#Convertendo as datas para objetos datetime
nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
inicioContribuicao = datetime.strptime(inicioContribuicao, "%d/%m/%Y")
hoje = datetime.today()

#Calculando a idade atual
idadeAtual = relativedelta(hoje, nascimento)

#Calculando o tempo de contribuição
tempoContribuicao = relativedelta(hoje, inicioContribuicao)

if sexo == 'M':
    idadeAposentadoria = 65
    tempoContribuicaoNecessario = 35

elif sexo == 'F':
    idadeAposentadoria = 62
    tempoContribuicaoNecessario = 30

else:
    print ('Sexo inválido.')
    exit()
    
#Calculando as datas de aposentadoria
dataAposentadoriaIdade = nascimento + relativedelta(years=idadeAposentadoria)
dataAposentadoriaContribuicao = inicioContribuicao + relativedelta(years=tempoContribuicaoNecessario)

#Verificando se atende ao tempo mínimo de contribuição
tempoMinimoContribuicao = 15

if tempoContribuicao.years < tempoMinimoContribuicao:
    print("Você ainda não atingiu o tempo mínimo de contribuição de 15 anos.")

else:
    #Determinar a primeira data de aposentadoria válida
    if dataAposentadoriaIdade > dataAposentadoriaContribuicao:
        aposentadoria = dataAposentadoriaIdade
    else:
        aposentadoria = dataAposentadoriaContribuicao
    print(f"Você poderá se aposentar em: {aposentadoria.strftime('%d/%m/%Y')}")
