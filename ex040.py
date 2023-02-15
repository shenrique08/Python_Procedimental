n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2)/2
if media < 5:
    print('Tirando {} e {}, a média do aluno é de {}'.format(n1, n2, media))
    print('O aluno está REPROVADO. ')
elif media >= 7:
    print('Tirando {} e {}, a média do aluno é de {} '.format(n1, n2, media))
    print('O aluno está APROVADO. ')
else:
    print('Tirando {} e {}, a média do aluno é de {} '.format(n1, n2, media))
    print('O aluno está de RECUPERAÇÃO. ')
