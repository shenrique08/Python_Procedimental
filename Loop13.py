idade = 0
soma = 0
while idade != 999:
    idade = int(input('Digite a sua idade: '))
    if idade != 999:
        soma += idade
print('DONE')
print(f'A soma de todas as idades é {soma}')
