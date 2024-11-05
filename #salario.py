salarioBase = float(input('Informe seu salário base:'))
totalVendas = float(input('Informe o valor total de suas vendas:'))
percentualComissao = float(input('Informe o percentual da sua comissão (em decimais):'))

# Calculando o valor da comissão
comissao = totalVendas * percentualComissao

# Calculando o salário total
salarioTotal = salarioBase + comissao

print (f'O salário total que lhe deve ser pago é de R${salarioTotal:.2f}.')
