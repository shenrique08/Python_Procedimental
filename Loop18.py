par = 0
impar = 0
menor_impar = 0
totvalor = 1
while True:
    valor = int(input(f'Digite o {totvalor}° valor: '))
    resposta = str(input('Quer continuar? [S/N] '))
    totvalor += 1
    if valor % 2 == 0:
        par += 1
    else:
        impar += 1
        if impar == 1:
            menor_impar = valor
        else:
            if valor < menor_impar:
                menor_impar = valor
    if resposta == 'N' or resposta == 'n':
        break
print('=' * 30)
print(f'Ao todo, você digitou {totvalor - 1} valores')
print(f'Você digitou {par} valores PARES. ')
print(f'O valor {menor_impar} foi o menor valor ÍMPAR digitado. ')
