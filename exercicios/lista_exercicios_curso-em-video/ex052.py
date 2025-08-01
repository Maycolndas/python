numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[1;34m', end=' ')
        total += 1
    else:
        print('\033[32m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, total))
if total == 2:
    print('E, por isso, ele é um número PRIMO!!')
else:
    print('E, por isso, ele NÃO é um número PRIMO!!')
