c = 1
maior = 0
menor = 0
mais_velha = 0
mais_jovem = 0
n = int(input('Quantas pessoas quer cadastrar? '))
while c <= n:
    print('=' * 20)
    print(f'{c}ª PESSOA')
    print('=' * 20)
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    if c == 1:
        maior = idade
        menor = idade
        mais_velha = nome
        mais_jovem = nome
    else:
        if idade < menor:
            menor = idade
            mais_jovem = nome
        elif idade > maior:
            maior = idade
            mais_velha = nome
    c += 1
print('=' *20)
print('=' *20)
print(f'A pessoa mais jovem é {mais_jovem} com {menor} anos')
print(f'A pessoa mais velha é {mais_velha} com {maior} anos ')
