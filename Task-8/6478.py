from itertools import *

alph = sorted('моль')

cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != 'ь' and 'оь' not in val and 'ьь' not in val:
        cnt += 1
print(cnt)
