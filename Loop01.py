from time import sleep
c = int(input('Em qual número começa a contagem? '))
t = int(input('Em qual número termina a contagem? '))
i = int(input('Qual vai ser o incremento? '))

while c <= t:
    print(c, end=' -> ')
    sleep(0.5)
    c += i
print('FIM')
