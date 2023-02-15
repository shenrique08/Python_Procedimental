s = float(input('Qual é o valor do seu salário em R$? '))
a1 = s * 1.1
a2 = s * 1.15
if s <= 1250:
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f} agora. '.format(s, a2))
else:
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f} aogra '.format(s, a1))
