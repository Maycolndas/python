nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Quem tirou {:.1f} e {:.1f} tem a nota média de {:.1f} pontos!'.format(nota1, nota2, media))
if media < 5:
    print('Aluno \033[1;30;41mREPROVADO!!!\033[m')
elif media >= 5 and media <= 6.9:
    print('Aluno em \033[7;30;43mRECUPERAÇÃO!!\033[m Estude mais.')
else:
    print('Aluno APROVADO! \033[1;30;42mPARABÉEEEEEENS!!\033[m')
