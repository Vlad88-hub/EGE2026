from itertools import *

alph = sorted('престол')

cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    for i in 'прстл':
        val = val.replace(i, "!")
    if pos % 2 != 0 and val[-1] != '!' and val.count('!') <= 3:
        cnt += 1
print(cnt)