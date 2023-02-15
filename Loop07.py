c = 1
meninas = 0
meninos = 0
while c <= 5:
    sx = str(input('Qual é o sexo? [F/M] '))
    if sx == 'm' or sx == 'M':
        meninos += 1
    elif sx == 'f' or sx == 'F':
        meninas += 1
    c += 1
print(f'O total de meninas é {meninas}')
print(f'O total de meninas é {meninos}')
