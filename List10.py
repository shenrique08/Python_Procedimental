from random import randint
from time import sleep
valores = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('SORTEANDO OS VALORES')
print(f'{valores}', end=' ')
print('FIM')
sleep(0.4)
print('=' * 40)
print('    Analisando os valores sorteados')
print('=' * 40)
sleep(0.4)
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O maior valor ocorreu nas posições/na posição {valores.index(max(valores))}')
print(f'O maior valor apareceu {valores.count(max(valores))} vez/vezes')
sleep(0.4)
print('=' * 40)
