sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [M/F]: ')).upper().strip()
print(f'Sexo {sexo} cadastrado com sucesso. ')
