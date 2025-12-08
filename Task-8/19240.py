from itertools import *

alph = sorted('январь')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] != 'я' and val.count('ь') <= 1 and 'яя' not in val:
        print(pos)