dia = int(input('Quantos dias ficou com o carro ?'))
km = float(input('Quantos KMS rodados '))
d = dia * 60
k = km * 0.15
print('{} dias deram {} reais '.format(dia, d))
print('{} KMS rodados deram, {:.2f} reais'.format(km, k))