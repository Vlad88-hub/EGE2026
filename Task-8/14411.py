from itertools import *

alph = sorted('сублимаця')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[-1] != 'я':
        for i in 'уиая':
            val = val.replace(i, '!')
        if val.count('!') == 2:
            print(pos)

