#from math import factorial
#n1 = int(input('Digite um número para o qual deseja realizar o cálculo de seu fatorial: '))
#fatorial = (factorial(n1))
#print(f'O fatorial de {n1} é {fatorial}')

n1 = int(input('Digite um número para o qual deseja realizar o cálculo de seu fatorial: '))
if n1 > 0:
    fatorial = 1
    for item in range(1, n1 + 1):
        fatorial = fatorial * item
    print(fatorial)

