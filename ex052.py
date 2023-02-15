from time import sleep
soma_divisivel = 0

n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print(f'[{c}]', end=' -> ')
        soma_divisivel += 1
        sleep(0.3)
    else:
        print(f'{c}', end=' -> ')
        sleep(0.3)
print('FIM')
if soma_divisivel <= 2:
    print(f'\nO número {n} foi divisível {soma_divisivel} vezes')
    print('Por isso ele É PRIMO!')
else:
    print(f'O número {n} foi divisível {soma_divisivel} vezes')
    print('Por isso ele não é primo')
