print('-=-' * 15)
print('ANALISADOR DE TRIÂNGULO 2.0')
print('-=-' * 15)
primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if primeiro == segundo == terceiro:
        print('EQUILÁTERO!')
    elif primeiro == segundo or primeiro == terceiro or segundo == terceiro:
        print('ISÓCELES!')
    else:
        print('ESCALENO!!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!!')
