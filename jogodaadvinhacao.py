from random import randint

print('-' * 30)
print('     JODO DA ADVINHAÇÃO')
print('-' * 30)
valor_aleatorio = randint(1, 10)
print('Pensei em um número entre 1 e 10. Tente advinhar! ')
nome = str(input('Primeiro, digite seu nome: '))
jogador = int(input('Digite um número entre 1 a 10 em que acha que pensei: '))
while True:
    if jogador < valor_aleatorio:
        jogador = int(input(f'O valor {jogador} é menor do que o valor que eu pensei. Tente novamente! '))
    elif jogador > valor_aleatorio:
        jogador = int(input(f'O valor {jogador} é maior do que o valor que eu pensei. Tente novamente! '))
    else:
        break
print(f'Parabéns, {nome}! Você acertou! ')
print(f'Realmente eu tinha pensado no número {valor_aleatorio}. Você é um gênio! ')
