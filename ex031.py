d = float(input('Qual é a distância da sua viagem dem km? '))
n1 = d * 0.5
n2 = d * 0.45
if d > 200:
    print('Você está prestes a fazer uma viagem de {}km '.format(d))
    print('E o preço da sua passagem será de R${:.2f}'.format(n2))
else:
    print(f'Você está prestes a fazer uma viagem de {d}km ')
    print('E o preço da sua passagem será de R${:.2f}'.format(n1))
input(f'Você está prestes a fazer uma viagem de km {d}')
