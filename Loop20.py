from time import sleep
print('=' * 30)
print('        MULTI-TABUADA')
print('=' * 30)
inicial = int(input('Tabuada INICIAL: '))
final = int(input('Tabuada FINAL: '))
for x in range(inicial, final + 1):
    print('=' * 30)
    print(f'        TABUADA DE {x}')
    print('=' * 30)
    x += 1
    sleep(0.3)
    for y in range(1, 11):
        print(x - 1, ' x ', y, '=', (x - 1) * y)
        y += 1
        sleep(0.3)
print('=' * 30)
print('       FIM DO PROGRAMA')
print('=' * 30)
