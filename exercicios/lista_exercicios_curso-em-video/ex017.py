'''cat = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = (cat**2 + adj**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}!'.format(hip))'''

from math import hypot
cat = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cat, adj)
print('A hipotenusa vai medir {:.2f}!'.format(hip))
