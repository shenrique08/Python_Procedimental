nome_mais_velho = 0
idade_mais_velho = 0
mulheres_menos_de_20 = 0
c = 0
soma_idade = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    if sexo == 'M':
        if c == 1:
            idade_mais_velho = idade
            nome_mais_velho = nome
        else:
            if idade > idade_mais_velho:
                idade_mais_velho = idade
                nome_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres_menos_de_20 += 1
    soma_idade += idade
media = soma_idade / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}')
print(f'Ao todo são {mulheres_menos_de_20} com menos de 20 anos')
