print('=' * 40)
print('         CADASTRO DE CLIENTES')
print('=' * 40)
mais_de_18 = 0
totH = 0
mulher_menos_de_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    print('=' * 40)
    continuar = str(input('Quer continuar? [S/N] '))
    if sexo == 'M':
        totH += 1
    elif idade < 20 and sexo == 'F':
        mulher_menos_de_20 += 1
    if idade > 18:
        mais_de_18 += 1
    elif sexo not in 'FM':
        print('Sexo inválido.')
        sexo = str(input('Sexo: [M/F] ')).upper()
    elif continuar not in 'SsNn':
        print('Resposta inválida')
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'O total de pessoas com mais de 18 anos é {mais_de_18}')
print(f'Ao todo, temos {totH} homens cadastrados ')
print(f'E temos {mulher_menos_de_20} mulheres com menos de 20 anos ')
