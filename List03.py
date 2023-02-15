from time import sleep
n1 = int(input('Digite o primeiro valor: '))
valores = [n1, n1 * 2, n1 * 2**2, n1 * 2**3, n1 * 2**4, n1 * 2**5, n1 * 2**6, n1 * 2**7, n1 * 2**8, n1 * 2**9]
for i in valores:
    print(i, end=' -> ')
    sleep(0.4)
print('FIM')
