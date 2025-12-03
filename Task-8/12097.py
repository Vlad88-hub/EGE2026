from itertools import *

alph = sorted('гирлянда')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val.count('д') == 3 and val[0] != 'я' and pos % 2 == 0:
        print(pos, val)