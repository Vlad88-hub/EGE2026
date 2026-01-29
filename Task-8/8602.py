from itertools import product

alph = sorted('АКЕНС')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'СЕНЕКА':
        print(pos)