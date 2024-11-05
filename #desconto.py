preco = float(input('Qual o valor do produto?'))
desconto = float(input('Qual o percentual de desconto?'))

valor_final = preco * desconto / 100

print (f'O valor final do produto é de R${valor_final:.2f}.')
