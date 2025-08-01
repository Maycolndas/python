casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
mes = anos * 12
prestacao = casa / mes
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}!'.format(casa, anos, prestacao))
excedente = salario * 30 / 100
if prestacao > excedente:
    print('Empréstimo NEGADO!!')
else:
    print('Empréstimo CONCEDIDO!!')
