print('=' * 30)
print('    10 TERMOS DE UMA P.A    ')
print('=' * 30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU!')
