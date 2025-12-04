from itertools import *

cnt = 0
alph = sorted('зеркало')
for val in product(alph, repeat=6):
    val = ''.join(val)
    if 1 <= val.count('к') <= 4:
        val = val.replace('к', '')
        if len(val) == len(set(val)):
            cnt += 1

print(cnt)