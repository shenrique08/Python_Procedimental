print('-=' * 20)
print('Analisador da condição de existência de um triângulo. ')
print('-=' * 20)
r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos PODEM formar um triângulo. ')
else:
    print('Os segmentos acima NÃO PODEM formar um triãngulo. ')
