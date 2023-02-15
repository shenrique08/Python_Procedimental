from time import sleep
n = int(input('Digite um número para verificar se é primo: '))
c = 1
soma_divisivel = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'[{c}]', end=' -> ')
        soma_divisivel += 1
    else:
        print(c, end=' -> ')
    sleep(0.3)
    c += 1
print(f'\nO número {n} foi divisível {soma_divisivel} vezes')
if soma_divisivel == 2:
    print(f'Logo, o número {n} É PRIMO!')
else:
    print(f'Logo, o número {n} NÃO É PRIMO!')
