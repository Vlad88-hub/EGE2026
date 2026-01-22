def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

print(sum(map(int, convert(5*343**2031 + 4*49**2142 - 3*7**111 + 7**222, 7))))
