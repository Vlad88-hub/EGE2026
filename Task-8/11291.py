from itertools import product
from string import printable as pr

cnt = 0
for val in product(pr[:6], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('2') == 1:
        for i in '04':
            val = val.replace(i, '!')
        if '!2!' not in val and '!2' not in val and '2!' not in val:
            cnt += 1
print(cnt)