from time import sleep

elementos = int(input('Quantos elementos quer exibir? '))
c = 3
n1 = 0
n2 = 1
print(n1, end=' ')
sleep(0.4)
print(n2, end=' ')
sleep(0.4)
for c in range(0, elementos):
    # ou "while c <= elementos:"
    n3 = n1 + n2
    print(n3, end=' ')
    sleep(0.4)
    n1 = n2
    n2 = n3
print('FIM')
