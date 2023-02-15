r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos acima podem formar um triângulo. ')
    if r1 == r2 == r3:
        print('Os segmento acima formam um triângulo EQUILÁTERO. ')
    elif r1 != r2 != r3 != r1:
        print('Os segmentos acima formam um triângulo ESCALENO. ')
    else:
        print('Os segmentos acima formam um triângulo ISÓCELES. ')
else:
    print('Os segmentos acima NÃO PODEM formar um triãngulo. ')
