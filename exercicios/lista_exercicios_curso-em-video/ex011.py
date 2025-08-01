largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura * largura
tinta = area / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área total é de {:.3f}m²!'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.3f}L de tinta!'.format(tinta))
