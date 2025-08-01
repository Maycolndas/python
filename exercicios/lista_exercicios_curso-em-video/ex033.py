a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a == b or a == c or a == c:
    print("Foram digitados números iguais. Sendo assim, não posso definir quem é maior e menor!")
else:
    #Testando quem é o menor valor
    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c
    #Testando quem é o maior
    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c
    print("O menor valor digitado foi {}!".format(menor))
    print("O maior valor digitado foi {}!".format(maior))
