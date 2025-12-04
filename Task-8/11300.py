from itertools import *

alph = sorted('гондубш')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] != 'б' and val.count('н') == 2 and val.count('у') == 0:
        print(pos, val)
