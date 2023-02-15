c = 1
sp = 0
si = 0
while c <= 5:
    n = int(input(f'Digite o {c}° valor: '))
    c += 1
    if n % 2 == 0:
        sp += n
    elif n % 2 != 0:
        si += n
print('-' * 27)
print(f'A soma dos pares vale {sp}')
print(f'A soma dos ímpares vale {si}')
