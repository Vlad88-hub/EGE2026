from string import printable
from itertools import product

cnt = 0
for val in product(printable[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        cnt_ch = 0
        for i in val:
            if i in printable[:25:2]:
                cnt_ch += 1
        cnt_15 = 0
        for i in val:
            if int(i, 25) > 15:
                cnt_15 += 1
        if cnt_ch >= 1 and cnt_15 > 2:
            cnt += 1

print(cnt)
