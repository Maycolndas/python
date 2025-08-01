print("-=-" * 12)
print("Analisador de Triângulos")
print("-=-" * 12)
primeiro = float(input("Primeiro segmento: "))
segundo = float(input("Segundo segmento: "))
terceiro = float(input("Terceiro segmento: "))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print("Os segmentos acima PODEM FORMAR um triângulo.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")
