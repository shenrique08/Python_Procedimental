from time import sleep
c = int(input('Minha contagem regressiva vai começar em: '))
m = int(input('Desejo marcar os múltiplos de: '))
while c >= 0:
    if c % m == 0:
        print('[', c, ']', end=' -> ')
        c -= 1
        sleep(0.5)
    else:
        print(c, end=' -> ')
        c -= 1
        sleep(0.5)
print('FIM')
