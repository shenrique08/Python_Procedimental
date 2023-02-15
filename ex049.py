from time import sleep
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} X {c} = {n * c}')
    sleep(0.3)
print('FIM')
