from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

num = 3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1

print(convert(num, 16).count('0'))
