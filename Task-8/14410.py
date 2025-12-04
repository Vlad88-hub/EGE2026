from itertools import *

alph = sorted('солнце')

ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] not in 'ое' and val.count('ц') == 2:
        ans.append(pos)

print(len(ans))
