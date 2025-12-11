from itertools import *
from string import printable as pr

cnt = 0
for val in product(pr[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0369':
            val = val.replace(i, '!')
        for i in '124578ab':
            val = val.replace(i, '@')
        if '!!' not in val and '@@' not in val:
            cnt += 1
print(cnt)
