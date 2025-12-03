from itertools import *

alph = sorted('теория')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[:1] != 'р' and val[:1] != 'т' and val[:1] != 'я' and val.count('и') >= 2 and pos % 2 != 0:
        print(pos, val)
