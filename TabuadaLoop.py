from time import sleep
print('TABUADA')
n = int(input('NÚMERO: '))
c = 1
for c in range(1, 11):
    print(n, 'X', c, '=', n * c)
    sleep(0.4)
    c += 1
print('FIM')
