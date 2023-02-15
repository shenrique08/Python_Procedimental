from time import sleep
c = 0
while True:
    print('=' * 30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('=' * 30)
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
        sleep(0.3)
print('PROGRAMA TABUADA ENCERRADO')
