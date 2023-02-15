from random import randint
valores = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]

print(f'Os valores sorteados foram {valores}')
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
print(f'A soma dos valores sorteados foi {sum(valores)}')
media = sum(valores) / len(valores)
print(f'A média dos valores sorteados foi {media}')
