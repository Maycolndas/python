reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = reais / 5.49
euro = reais / 5.94
libra = reais / 7.01
pesoa = reais / 0.0060
print('Com R${:.2f} você pode comprar US${:.2f}!\n'.format(reais, dolar))
print('Veja outros valores, caso necessite: \n')
print('R${:.2f} equivalem a {:.2f} EUROS!'.format(reais, euro))
print('R${:.2f} equivalem a {:.2f} LIBRAS!'.format(reais, libra))
print('R${:.2f} equivalem a {:.2f} PESOS ARGENTINOS!'.format(reais, pesoa))
