somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('=' * 5, end=' ')
    print('{}ª PESSOA'.format(p), end=' ')
    print('=' * 5)
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.2f} anos!'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}!'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos!'.format(totalmulher20))
