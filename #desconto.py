preco = float(input('Qual o valor do produto?'))
desconto = float(input('Qual o percentual de desconto (digite em decimais)?'))

valor_final = preco + desconto

print (f'O valor final do produto é de R${valor_final:.2f}.')