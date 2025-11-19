from string import printable as pr


def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

ans = []
for i in range(3, 4):
    num1 = 3*7**(i+1) + 13*7**(i+2) + 31*7**(3*i) + 1*7**(2*i)

    if sum(map(int, convert(num1, 7))) == 18:
        ans.append(i)


print(min(ans))

