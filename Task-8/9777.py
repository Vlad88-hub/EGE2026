from itertools import *

alph = sorted('компьютер')

for pos, val in enumerate(product(alph, repeat=5), start=1 ):
    val = ''.join(val)
    if pos % 2 != 0 and val[:1] != 'ь' and val.count('к') == 2:
        print(pos, val)

