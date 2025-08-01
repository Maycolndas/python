salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario / 100 * 15
novo = salario + aumento
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passará a receber o valor de R${:.2f} mensal!'.format(salario, novo))
