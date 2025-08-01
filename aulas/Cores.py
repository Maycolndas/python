nome = 'Maycol'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Muito prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))

'''Style
0 - NONE
1 - BOLD
4 - UNDERLINE
7 - NEGATIVE (INVERTE FUNDO E LETRA)

TEXT       BACKGROUND   COR
30         40           BRANCO          
31         41           VERMELHO
32         42           VERDE
33         43           AMARELO
34         44           AZUL
35         45           ROXO
36         46           SINGENTA
37         47           CINZA (COR PADRÃO)'''
