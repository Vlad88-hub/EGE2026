from itertools import *

ans = []
alph = sorted('парус')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] == 'у' and 'аа' not in val:
        ans.append(pos)
print(min(ans))