from itertools import product as per
from string import printable as pr

cnt = 0
for val in per(pr[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0'and val.count('b') == 2:
        for i in pr[:12:2]:
            val = val.replace(i, '!')
        for i in pr[1:12:2]:
            val = val.replace(i, '@')
        if '!!' not in val and '@@' not in val:
            cnt += 1
print(cnt)