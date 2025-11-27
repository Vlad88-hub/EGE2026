import re


def convert(num, sys ):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2031):
    num = convert(7**170 + 7**100 - x, 7)
    n = num.count('0')
    ans.append([n, x])

print(max(ans))



