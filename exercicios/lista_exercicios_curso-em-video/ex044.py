print('{:=^40}'.format(' LOJAS MAYQUIN '))
preço = float(input('Preço das compras: R$'))
print('''***FORMAS DE PAGAMENTO***
[ 1 ] - à vista: dinheiro/cheque
[ 2 ] - à vista: cartão
[ 3 ] - 2x no cartão de crédito
[ 4 ] - 3x ou mais no cartão de crédito''')
opção = int(input('Qual é a opção de pagamento? '))
if opção == 1:
    novo_preço = preço - (preço * 10 / 100)
elif opção == 2:
    novo_preço = preço - (preço * 5 / 100)
elif opção == 3:
    novo_preço = preço
    parcelas = preço / 2
    print('Sua compra será parcelada em DUAS vezes de R${:.2f} SEM JUROS!'.format(parcelas))
elif opção == 4:
    novo_preço = preço + preço * 20 / 100
    total_parcelas = int(input('Quantas parcelas? '))
    parcelas = novo_preço / total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(total_parcelas, parcelas))
else:
    novo_preço = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, novo_preço))
