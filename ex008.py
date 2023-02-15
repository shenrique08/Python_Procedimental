m = float(input('Digite uma distância em metros: '))
k = m * 0.001
h = m * 0.01
d = m * 0.1
dc = m * 10
cm = m * 100
mm = m * 1000
print('A medidade de {}m corresponde a {}km, {}hm, {:.1f}dam, {}dm, {}cm, {}mm'.format(m, k, h, d, dc, cm, mm))
