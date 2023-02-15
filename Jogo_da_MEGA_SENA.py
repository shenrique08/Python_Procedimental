from random import randint
from time import sleep
print('=' * 40)
print('           JOGO DA MEGA SENA')
print('=' * 40)
n_de_jogos = int(input('Quantos jogos deseja sortear? '))
print(f'-=-=-=-=-= SORTEANDO [{n_de_jogos}] JOGOS -=-=-=-=-=')
c = 1
for c in range(0, n_de_jogos):
    sorteio_dos_jogos = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'Jogo {c + 1}: {sorted(sorteio_dos_jogos)}')
    sleep(0.5)
print('*********** BOA SORTE! ***********')
