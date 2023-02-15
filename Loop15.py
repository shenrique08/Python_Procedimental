numero = 0
soma = 0
c = 0
maior = 0
while numero != 999:
    print('-' * 30)
    numero = int(input(f'{c + 1}° VALOR [Digite 999 para parar]: '))
    if numero != 999:
        soma += numero
        if c == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
    c += 1
media = soma / (c - 1)
print('=' * 30)
print(f'Ao todo, foram digitados {c - 1} valores')
print(f'A soma entre eles é {soma}')
print(f'A média entre eles é {media}')
print(f'O maior valor digitado foi {maior}')
print('=' * 30)
