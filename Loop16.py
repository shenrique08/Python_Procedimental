tot = 0
mais_jovem = 0
mais_velho = 0
soma_idades = 0
maior = 0
menor = 0
while True:
    print('----------', 'NOVO AMIGO', '----------')
    print('Digite "ACABOU" para interromper')
    nome = str(input('NOME: '))
    if nome == 'ACABOU':
        break
    idade = int(input('IDADE: '))
    tot += 1
    soma_idades += idade
    if tot == 1:
        mais_velho = nome
        mais_jovem = nome
        maior = idade
        menor = idade
    else:
        if idade < menor:
            menor = idade
            mais_jovem = nome
        elif idade > maior:
            maior = idade
            mais_velho = nome
media_de_idades = soma_idades / tot
print('*' * 30, 'INTERROMPIDO', '*' * 30)
print(f'Total de amigos: {tot}')
print(f'A média de idades: {media_de_idades.real}')
print(f'Seu amigo mais jovem é {mais_jovem} com {menor} anos')
print(f'Se amigo mais velho é {mais_velho} com {maior} anos')
