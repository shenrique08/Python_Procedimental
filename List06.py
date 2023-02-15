from random import randint
from time import sleep
chave = tot = 0
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for c in range(0, len(valores)):
    print(f'{valores[c]}', end=' -> ', )
    sleep(0.5)
print('FIM')
chave = int(input('\nEstá procurando por qual valor? '))
for c in range(0, len(valores)):
    if valores[c] == chave:
        print(f'Achado na posição {c}')
        tot += 1
    sleep(0.5)
print(f'O valor {chave} foi achado {tot} vezes')
