from time import sleep
from random import randint
computador = randint(0, 5) # FAZ O COMPUTADOR "PENSAR"
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
sleep(1)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if computador != jogador:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
else:
    print('PARABÉNS! Você coseguiu me vencer, pensei exatamente no {}!!'.format(jogador))
