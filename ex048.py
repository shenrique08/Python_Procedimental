soma = 0
valor = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        valor += 1
print(f'A soma de todos os {valor} valores solicitados é {soma}')
