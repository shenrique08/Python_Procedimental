n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
    c += 1
print(f'Você digitou {c - 1} números e a soma entre eles vale {soma}')
