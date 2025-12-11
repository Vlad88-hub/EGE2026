from itertools import *

cnt = 0
for val in set(permutations('амфибрахий')):
    val = ''.join(val)
    if val[4] == 'б' and val[5] == 'р':
        cnt += 1
print(cnt)