soma = 0
cont = 0
for c in range (1, 7):
    numero = int(input('Digite o {}º valor: '.format(c)))
    if numero % 2 == 0:
        cont += 1
        soma += numero
print('Você informou {} números PARES e a soma deles é igual a {}!'.format(cont, soma))
