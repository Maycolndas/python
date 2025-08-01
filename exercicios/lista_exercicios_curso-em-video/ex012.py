preco = float(input('Qual o preço do produto? R$'))
desconto = preco / 100 * 5
novo = preco - desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f} agora!'.format(preco, novo))
