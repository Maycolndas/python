peso = float(input('Informe o seu peso: (Kg) '))
altura = float(input('Informe a sua altura: (m)'))
imc = peso / (altura * altura)
print('O IMC da pessoa com {:.2f}m de altura e pesando {:.2f}kg é de {:.1f}.'.format(altura, peso, imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc < 25:
    print('Você está no PESO IDEAL!! Parabénsss!!')
elif imc < 30:
    print('Você está com SOBREPESO. Cuidado!')
elif imc < 40:
    print('Você está com OBESIDADE! Procure um médico agora.')
else:
    print('Você está com OBESIDADE MÓRBIDA!! GOD HELP US!')
