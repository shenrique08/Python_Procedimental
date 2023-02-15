from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 1 e 10. Tente advinhar!')
print('Será que você consegue advinhar qual foi? ')
computador = randint(1, 10)
jogador = int(input('Qual é o seu palpite? '))
c = 1
while jogador != computador:
    if jogador > computador:
        print('Menos... Tente novamente!')
        jogador = int(input('Qual é o seu palpite? '))
    elif jogador < computador:
        print('Mais... Tente novamente!')
        jogador = int(input('Qual é o seu palpite? '))
    else:
        break
    c += 1
print(f'Acertou com {c} tentativas. Parabéns! ')
