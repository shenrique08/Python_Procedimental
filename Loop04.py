c = 1
s = 0
media = 0
tot = int(input('Quantos números deseja informar? '))

print('Início')
while c <= tot:
    n = int(input(f'Digite o {c}° valor: '))
    c += 1
    s += n
print('FIM')
print(f'A soma dos números que você digitou é {s} ')
media = s / 4
print(f'A média da soma dos números é {media} ')
