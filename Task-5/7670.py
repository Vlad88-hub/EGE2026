from dataclasses import replace
from string import printable as pr

def convert(num, sys):
    res = ''
    while   num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(151, 100000):
    R = convert(N, 16)
    R = R.replace('a', '1')
    cnt = 0
    for i in R:
        if int(i, 16) % 2 == 0:
            cnt += 1
    if cnt > 2:
        R += 'b'
    else:
        R = 'f' + R
    R = int(R, 16)
    if R > 3500:
        ans.append([R, N])
print(min(ans))



