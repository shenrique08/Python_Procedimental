from random import randint
from time import sleep
c = 1
maiores_que_cinco = 0
divisivel_por_tres = 0
n = int(input('Quantos números vou sortear? '))
print('-' * 30)
print(f'Sorteando os {n} valores: ')
while c <= n:
    sorteio = randint(1, 10)
    print(sorteio, end=' -> ')
    sleep(0.5)
    if sorteio > 5:
        maiores_que_cinco += 1
    elif sorteio % 3 == 0:
        divisivel_por_tres += 1
    c += 1
print('FIM')
print('-' * 30)
print(f'Dos {n} números sorteados, temos {maiores_que_cinco} maiores que cinco'
      f' e {divisivel_por_tres} divisível por três.')
