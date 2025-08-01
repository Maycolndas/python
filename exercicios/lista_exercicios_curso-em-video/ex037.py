numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases abaixo para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}!'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}!'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}!'.format(numero, hex(numero)[2:]))
else:
    print('Você não digitou uma opção válida. Favor iniciar novamente e ficar atento as opções.')
