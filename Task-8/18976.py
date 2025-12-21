from itertools import product
from string import printable as pr

cnt1 = 0
cnt = 0
for val in product(pr[:20], repeat=5):
    val = ''.join(val)

    if val[0] != '0' and int(val[-1], 20) + int(val[0], 20)== 26:
        cnt1 += 1

        for i in pr[:20:2]:
            val = val.replace(i, '!')
        for i in pr[1:20:2]:
            val = val.replace(i, '@')
        if '@@' not in val and '!!' not in val:
            cnt += 1
print(cnt)
