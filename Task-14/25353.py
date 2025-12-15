from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 27001):
    num = 3*27**9 + 2*27**6 + 27**3 - x
    num = convert(num, 27)
    if num.count('0') == 6:
        ans.append(x)
print(min(ans))