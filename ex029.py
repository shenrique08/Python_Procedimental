v = float(input('Qual é a velocidade média atual do carro em km/h ? '))
m = (v-80) * 7
if v > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido na via, que é de 80km/h. O valor da sua multa é de '
          '{} reais '.format(m))
else:
    print('Tenha um bom dia! Dirija com segurança. ')
