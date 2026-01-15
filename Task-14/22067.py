from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

num = convert(3*17**777 + 15*17**250 - 6*17**100 + 2, 17)

for i in pr[1:17:2]:
    num = num.replace(i, '')

print(len(set(num)))