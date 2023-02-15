from random import randint
tot = 1
soma = 0
maior = 0
menor = 0
cinco = 0
while True:
    n = randint(1, 10)
    print('*' * 20)
    print(f'O {tot}° valor sorteado foi o [{n}] ')
    resposta = str(input('Quer continuar? [S/N] '))
    if n == 5:
        cinco += 1
    if tot == 1:
        maior = n
        menor = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    if resposta == 'N' or resposta == 'n':
        break
    tot += 1
    soma += n
print('==========', 'RESULTADO', '==========')
print(f'Ao todo, foram sorteados {tot} valores. ')
print(f'A soma de todos os números sorteados foi {soma}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
print(f'O valor 5 só foi sorteado {cinco} vezes.')
