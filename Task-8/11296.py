from itertools import *

alph = sorted('досж')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)

    if val[0] == 'ж' and val[1] == 'с':
        print(pos, val)
