from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados são {valores}')
print(f'A soma entre eles vale: {sum(valores)}')
media = sum(valores) / len(valores)
print(f'A média entre eles é {media:2f}')
