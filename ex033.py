n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
if n1 < n2 and n1 < n3:
    print('O menor valor digitado foi {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor valor digitado foi {}'.format(n2))
if n3 < n2 and n3 < n1:
    print('O menor valor digitado foi {}'.format(n3))
