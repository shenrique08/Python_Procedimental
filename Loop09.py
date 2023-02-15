c = 1
somaF_acima_do_peso = 0
somaM_acima_do_peso = 0
pessoas = int(input('Quantas pessoas vamos cadastrar? '))
peso_referencia = int(input('Qual é o peso de referência (Kg) ? '))
while c <= pessoas:
    print('-' * 20)
    print(f'Pessoa {c} de {pessoas}')
    peso = float(input('Peso (Kg): '))
    sexo = str(input('Sexo: [F/M] '))
    c += 1
    if peso_referencia < peso and sexo == 'F' or sexo == 'f':
        print('=====', 'PESO ACIMA DO LIMITE', '====')
        somaF_acima_do_peso += 1
    elif peso_referencia < peso and sexo == 'M' or sexo == 'm':
        print('=====', 'PESO ACIMA DO LIMITE', '====')
        somaM_acima_do_peso += 1
    else:
        print('====', 'PESO DENTRO DO LIMITE', '====')
print('-----', 'RESULTADO', '-----')
print(f'Ao todo, temos {somaF_acima_do_peso} mulheres e {somaM_acima_do_peso} homens acima do peso de referência. ')
