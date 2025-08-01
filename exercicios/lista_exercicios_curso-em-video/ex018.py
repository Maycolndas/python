from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
print('O ângulo de {}º tem o SENO  de {:.2f}!'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {}º tem o COSSENO de {:.2f}!'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('A tangente de {} tem o valor de {:.2f}!'.format(angulo, tangente))
