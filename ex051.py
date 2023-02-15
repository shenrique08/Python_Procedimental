print('=' * 30)
print('    10 TERMOS DE UMA P.A.')
print('=' * 30)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n10 = n1 + (11 - 1) * razao
for c in range(n1, n10, razao):
    print(c, end=' -> ')
print('FIM')
