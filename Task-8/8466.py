from itertools import product
from string import printable as pr

cnt = 0
for val in product(pr[:7], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val[-1] in '456':
        for i in pr[:7:2]:
            val = val.replace(i, '!')
        for i in pr[1:7:2]:
            val = val.replace(i, '@')
        if val.count('!') == val.count('@'):
            cnt += 1
print(cnt)