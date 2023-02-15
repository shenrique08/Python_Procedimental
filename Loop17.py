totF = 0
totH = 0
tot = 0
salarioH = 0
salarioF = 0
maior_salarioH = 0
mulher_maisde1000 = 0
nome_maiorsalarioH = 0
while True:
    nome = str(input('NOME: '))
    sexo = str(input('SEXO: [M/F] '))
    salario = float(input('SALÁRIO: R$ '))
    x = str(input('Quer continuar? [S/N] '))
    print('=' * 20)
    tot += 1
    if sexo == 'M' or sexo == 'm':
        totH += 1
        salarioH += salario
        if totH == 1:
            maior_salarioH = salario
            nome_maiorsalarioH = nome
        else:
            if salario > maior_salarioH:
                maior_salarioH = salario
                nome_maiorsalarioH = nome
    elif sexo == 'F' or sexo == 'f':
        totF += 1
        if salario > 1000:
            mulher_maisde1000 += 1
    if x == 'N' or x == 'n':
        break
media_salarioH = salarioH / totH
print('=' * 10, 'RESULTADOS', '=' * 10)
print(f'Total de funcionários: {tot}')
print(f'Total de Homens: {totH}')
print(f'Total de mulheres: {totF}')
print(f'A média salarial dos Homens é de: {media_salarioH}')
print(f'Temos {mulher_maisde1000} mulheres ganhando mais de R$1000')
print(f'O maior salário entre os homens é o do {nome_maiorsalarioH} de R${maior_salarioH}')
