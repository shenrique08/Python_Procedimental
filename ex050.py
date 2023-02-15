numeros_pares = 0
soma_pares = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma_pares += n
        numeros_pares += 1
print(f'Você digitou {numeros_pares} números pares e a soma entre eles vale {soma_pares}')
