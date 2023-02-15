from time import sleep
print('GERADOR DE P.A.')
print('=' * 10)
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A. '))
termo = n1
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    cont += 1
    termo += r
    sleep(0.3)
print('FIM')
