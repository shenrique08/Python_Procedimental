s = 0
resposta = 'S'
while resposta == 'S' or resposta == 's':
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] '))
    s += n
print(f'A soma dos valores digitados vale {s}')
