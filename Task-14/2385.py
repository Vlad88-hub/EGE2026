def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

num = 16**820 - 2**761 +14

print(convert(num, 4).count('0'))