print('=' * 40)
print('           LOJAS KASPANOTEL')
print('=' * 40)
total_da_compra = 0
mais_de_1000 = 0
mais_barato = 0
nome_mais_barato = 0
c = 1
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    total_da_compra += preco
    if c == 1:
        mais_barato = preco
        nome_mais_barato = produto
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome_mais_barato = produto
    if preco > 1000:
        mais_de_1000 += 1
    if resposta not in 'SsNn':
        print('Dados inválidos. Por favor, tente novamente.')
        produto = str(input('Nome do Produto: '))
        preco = int(input('Preço: '))
        resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
    c += 1
print('============', 'FIM DO PROGRAMA', '===========')
print(f'O total da compra foi de R${total_da_compra}')
print(f'Temos {mais_de_1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R${mais_barato}')
