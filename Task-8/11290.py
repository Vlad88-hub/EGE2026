from itertools import product
from string import printable as pr

cnt = 0
for val in product(pr[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('9') == 1:
        for i in pr[:16:2]:
            val = val.replace(i, '!')
        for i in pr[1:16:2]:
            val = val.replace(i, '@')
        if '!!' not in val and '@@' not in val:
            cnt += 1
print(cnt)