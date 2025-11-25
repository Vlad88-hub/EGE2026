from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]


for x in range(1, 3001):
    num = convert(9*11**210 + 8*11**150 - x, 11)
    if num.count('0') == 60:
        print(x)
