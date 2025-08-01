from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade < 21:
        total_menor += 1
    else:
        total_maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(total_maior))
print('E também tivemos {} pessoas menores de idade!'.format(total_menor))
