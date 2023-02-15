c = 1
maior = 0
menor = 0
while c <= 4:
    n = int(input('Digite um número: '))
    if c == 1:
        maior = n
        menor = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    c += 1
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
