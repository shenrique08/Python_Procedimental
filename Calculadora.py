n1 = int(input('Operando 1: '))
n2 = int(input('Operando 2: '))
opcao = 0
while opcao != 5:
    if opcao != 5:
        print('=' * 10, 'ESCOLHA UMA OPERAÇÃO', '=' * 10)
        print('[ 1 ] Adição')
        print('[ 2 ] Subtração')
        print('[ 3 ] Multiplicação')
        print('[ 4 ] Entrar com novos dados')
        print('[ 5 ] Desligar a calculadora')
        opcao = int(input('>>>> SUA OPÇÃO: '))
        if opcao == 1:
            print('-' * 20)
            print(f'Calculando {n1} + {n2} = {n1 + n2}')
            print('-' * 20)
        elif opcao == 2:
            print('-' * 20)
            print(f'Calculando {n1} - {n2} = {n1 - n2}')
            print('-' * 20)
        elif opcao == 3:
            print('-' * 20)
            print(f'Calculando {n1} * {n2} = {n1 * n2}')
            print('-' * 20)
            print('-' * 20)
        elif opcao == 4:
            print('-' * 20)
            n1 = int(input('Operando 1: '))
            n2 = int(input('Operando 2: '))
            print('-' * 20)
        elif opcao > 5 or opcao < 1:
            print('-' * 20)
            print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE! ')
            n1 = int(input('Operando 1: '))
            n2 = int(input('Operando 2: '))
print('======= CALCULADORA DESLIGADA =======')
