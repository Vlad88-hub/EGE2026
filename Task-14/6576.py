from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

num = 283**382 + 9**15 + 2**3
num = convert(num, 14)
B = num.count('b')
C = num.count('c')
print(B - C)