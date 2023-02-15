C = float(input('Valor da casa: R$'))
S = float(input('Salário do comprador: R$ '))
F = int(input('Quantos anos de financiamaneto? '))
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f} '.format(C, F, (C/F)/12))
if C/F < 0.3 * S:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO! ')
