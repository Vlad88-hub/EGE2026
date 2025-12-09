from itertools import *
from string import printable as pr

cnt = 0
for val in product(pr[:8], repeat=10):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 5:
        val = val.replace('7', '&')
        for i in pr[1:8:2]:
            val = val.replace(i , '!')
        if '&!' not in val and '!&' not in val and '&&' not in val:
            cnt += 1
print(cnt)
