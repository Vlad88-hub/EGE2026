from itertools import product
from string import printable

cnt = 0
for val in product(printable[:13],repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') >= 2:
        for i in printable[10:13]:
            val = val.replace(i, '*')
        if val.count('*') == 2 and '**' in val:
            cnt += 1

print(cnt)