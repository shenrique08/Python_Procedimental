from time import sleep
inicio = int(input('INÍCIO: '))
final = int(input('FINAL: '))
passo = int(input('PASSO: '))
c = 1
if inicio < final:
    for c in range(inicio, final + 1, passo):
        print(c, end=' -> ')
        sleep(0.5)
elif inicio > final:
    for c in range(inicio, final, -passo):
        print(c, end=' -> ')
        sleep(0.5)
print('ACABOU')
