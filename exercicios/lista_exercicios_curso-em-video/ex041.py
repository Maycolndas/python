from datetime import date
ano = int(input('Ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje - ano
print('O atleta em questão tem {} anos!'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM!')
elif idade <= 14:
    print('Classificação: INFANTIL!')
elif idade <= 19:
    print('Classificação: JUNIOR!')
elif idade <= 25:
    print('Classificação: SÊNIOR!')
else:
    print('Classificação: MASTER!!')
