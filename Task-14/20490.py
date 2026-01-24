def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2006):
    num = convert(4**163*5 + 12**62 - x, 5)
    if num.count('1') < num.count('4'):
        ans.append(x)
print(max(ans))