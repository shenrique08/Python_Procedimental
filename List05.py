from random import randint
from time import sleep
print('======= VOU SORTEAR 5 NÚMEROS =======')
valores = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('Valores sorteados: ')
for i in valores:
    print(valores.index(i), ':', end='')
    print(f'[{i}]', end=' ')
    sleep(0.5)
print('FIM')
