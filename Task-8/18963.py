from itertools import *

alph = sorted('котбус')

cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    if val[0] != 'о' and val[0] != 'у' and 'кот' in val:
        cnt += 1
print(cnt)