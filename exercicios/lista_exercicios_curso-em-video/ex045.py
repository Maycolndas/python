from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) #FAZ O COMPUTADOR PENSAR
print('''Suas opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
jogador = int(input('Qual a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA \nJogue novamente!!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-=-'*10)
    print('Computador jogou {}!'.format(itens[computador]))
    print('Jogador jogou {}!'.format(itens[jogador]))
    print('-=-'*10)
    if computador == 0: #COMPUTADOR JOGOU PEDRA
        if jogador == 0:
            print('EMPATE!!')
        elif jogador == 1:
            print('JOGADOR GANHA!!')
        elif jogador == 2:
            print('COMPUTADOR GANHA!!')
        else:
            print('JOGADA INVÁLIDA!!')
    elif computador == 1:  #COMPUTADOR JOGOU PAPEL
        if jogador == 0:
            print('COMPUTADOR GANHA!!')
        elif jogador == 1:
            print('EMPATE!!')
        elif jogador == 2:
            print('JOGADOR GANHA!!')
        else:
            print('JOGADA INVÁLIDA!!')
    elif computador == 2:  #COMPUTADOR JOGOU TESOURA
        if jogador == 0:
            print('JOGADOR GANHA!!')
        elif jogador == 1:
            print('COMPUTADOR GANHA!!')
        elif jogador == 2:
            print('EMPATEE!!')
        else:
            print('JOGADA INVÁLIDA!!')
