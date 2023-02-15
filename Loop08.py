c = 1
pares = 0
impares = 0
soma_pares = 0
soma_impares = 0
while c <= 5:
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        pares += 1
        soma_pares += n
    elif n % 2 != 0:
        impares += 1
        soma_impares += n
    c += 1
print('-' * 30)
media_pares = soma_pares / pares
media_impares = soma_impares / impares
print(f'Você digitou {pares} números pares. A média é {media_pares.__int__()}')
print(f'Você digitou {impares} números ímpares. a média é {media_impares.__int__()}')
