data = 2022
nasc = int(input('Ano de nascimento: '))
if nasc > (data - 18):
    print('Você ainda não precisa se alistar, só no ano de {}, pois você ainda tem {} anos de idade: '.format(nasc + 18, data - nasc))
elif nasc < (data - 18):
    print('Você deveria ter se alistado em {}, pois você já tem {} anos de idade: '.format(nasc + 18, data - nasc))
else:
    print('Se aliste imediatamente, pois você tem {} anos de idade. '.format(data - nasc))
