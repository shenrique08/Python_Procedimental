maior_peso = 0
menor_peso = 0
c = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido foi {maior_peso}kg')
print(f'O menor peso lido foi {menor_peso}kg')
