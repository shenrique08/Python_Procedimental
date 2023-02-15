from time import sleep
n1 = int(input('Digite um número: '))
valores = [n1, n1 + 5, n1 + 10, n1 + 15, n1 + 20, n1 + 25, n1 + 30, n1 + 35, n1 + 40, n1 + 45]
for i in valores:
    print(valores.index(i), ':', end='')
    print(f'[{i}]', end=' ')
    sleep(0.5)
print('DONE')
