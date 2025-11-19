from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49

print(set(convert(num, 16)))

