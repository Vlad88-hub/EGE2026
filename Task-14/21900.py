def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2301):
    num = 7**350 + 7**150 - x
    num = convert(num, 7)
    if num.count('0') == 200:
        ans.append(x)
print(max(ans))
