print('=' * 40)
print('          ESCOLA GIROQUETELIUM')
print('=' * 40)
notas = list()
c = 1
for c in range(1, 5):
    notas.append(float(input(f'Digite a nota do {c}º aluno: ')))
    c += 1
print('=' * 40)
media = sum(notas) / len(notas)
print(f'   A média de nota da turma vale {media:.2f}')
print('=' * 40)
print('FIM')
