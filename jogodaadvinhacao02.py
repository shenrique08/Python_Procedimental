from random import randint

print('=' * 40)
print('     JODO DA ADVINHAÇÃO 2.0 TURBO')
print('=' * 40)
valor_aleatorio = randint(1, 10)
print('Pensei em um número entre 1 e 10. Tente advinhar! ')
tentativas = 1
total = 3
acertou = False
nome = str(input('Primeiro, digite seu nome: '))
while not acertou:
    print(f'    TENTATIVAS {tentativas}/3')
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == valor_aleatorio:
        acertou = True
        print(f'Parabéns, {nome}! Você acertou em {tentativas} tentativas! ')
        print(f'Realmente eu tinha pensado no número {valor_aleatorio}. Você é um gênio! ')
    elif tentativas < total:
        if jogador < valor_aleatorio:
            print('Tente um valor MAIOR! ')
        elif jogador > valor_aleatorio:
            print('Tente um valor MENOR! ')
    else:
        print(f'As suas chances acabaram, {nome}! Tente da proxima vez.')
        break
    tentativas += 1
print('=' * 15, 'FIM', '=' * 15)
