from random import randint
from time import sleep
n = int(input('Quantos números quer que eu sorteie? '))
print('-' * 30)
print(f'Sorteando os {n} números: ')
c = 1
s = 0
while c <= n:
    sorteio = randint(0, 10)
    print(sorteio, end=' -> ')
    c += 1
    s += sorteio
    sleep(0.5)
print('FIM!')
print(f'A soma entre todos os valores sorteados é {s} ')
