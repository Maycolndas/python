from datetime import date
ano_nasc = int(input('Informe o ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano_nasc
sexo = str(input('Qual seu sexo? [M/F] ')).upper()
if sexo == 'M':
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, hoje))
    if idade < 18:
        print('Ainda faltam {} anos para o seu alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}!'.format(ano_nasc + 18))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos!'.format(idade - 18))
        print('Seu alistamento foi em {}!'.format(ano_nasc + 18))
    else:
        print('Você tem de se alistar IMEDIATAMENTE!!')
elif sexo == 'F':
    print('Você não precisa se alistar!')
else:
    print('Opção inválida. Necessário digitar M ou F!')
