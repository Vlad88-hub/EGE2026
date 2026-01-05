from itertools import product, repeat

alph = sorted('школа')
for pos, val in enumerate(product(alph, repeat=5)):
    val = ''.join(val)
    if val == 'шалаш':
        print(pos)