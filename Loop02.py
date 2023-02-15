from time import sleep
print('*' * 20)
print('    JOGO DO PIN')
print('*' * 20)
f = int(input('Deseja contar até quanto? '))
c = 1
while c <= f:
    if c % 4 != 0:
        print(c, end=' -> ')
        sleep(0.4)
        c += 1
    else:
        print('PIN!', end=' -> ')
        c += 1
print('FIM!')
