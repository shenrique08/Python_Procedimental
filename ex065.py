resposta = 0
c = 1
maior = 0
menor = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] '))
    soma += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    if resposta in 'Nn':
        break
    c += 1
media = soma / c
print(f'Ao todo, você digitou {c} números e a média entre eles é {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
