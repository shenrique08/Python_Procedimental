p = float(input('Qual é o seu peso? (kg): '))
h = float(input('Qual é a sua altura? (m): '))
imc = p / (h ** 2)
print('Seu IMC é de {:.1f} '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal. ')
elif imc < 24.9:
    print('Você está com peso NORMAL.')
elif imc < 30.0:
    print('Cuidado, você está SOBREPESO.')
else:
    print('Cuidado, você está OBESO.')
