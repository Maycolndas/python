velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Velocidade acima do permitido da pista! Você terá de pagar uma multa no valor de R${:.2f}, RUBENS BARRICHELLO!'.format(multa))
else:
    print('Você está dentro da velocidade permitida da pista! Siga em frente, viajante!!')
