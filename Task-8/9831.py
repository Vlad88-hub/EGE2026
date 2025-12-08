from itertools import *
from string import printable as pr

cnt = 0
for val in product(pr[:16], repeat=3):
    val = ''.join(val)
    if val[0] != 0 and len(set(val)) == 3:
        for i in pr[:16:2]:
            val = val.replace(i, '!')
        for i in pr[1:16:2]:
            val = val.replace(i, '@')

        if '!!' not in val and '@@' not in val:
             cnt += 1
print(cnt)