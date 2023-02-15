velocidade_maxima = float(input('Digite a velocidade máxima permitida em km/h: '))
velocidade_aferida = float(input('Digite a velocidade aferida em km/h: '))
if velocidade_aferida >= velocidade_maxima and velocidade_aferida <= (velocidade_maxima + 10):
    print('Você levou multa leve')
elif velocidade_aferida >= velocidade_maxima + 11 and velocidade_aferida <= (velocidade_maxima + 21):
    print('Você levou multa grave ')
elif velocidade_aferida > velocidade_maxima + 21:
    print('Você levou multa gravíssima ')
else:
    print('Não houve multa ')
