from itertools import product
from string import printable

cnt = 0
for val in product(printable[:13], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') >= 2:
        for i in printable[10:13]:
            val = val.replace(i, '*')
        if val.count('*') == 2 and '**' in val:
            cnt += 1

print(cnt)


#################################################################

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for N in range(int('100000', 13), int('cccccc', 13) + 1):
    R = convert(N, 13)
    if R.count('0') >= 2:
        for i in printable[10:13]:
            R = R.replace(i, '!')
        if R.count('!') == 2 and '!!' in R:
            cnt += 1