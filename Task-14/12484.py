def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(0, 10**6):
    for y in range(0, 10**6):
        num = convert(5**50 + 5**30 - 5**x - y - 5**y - x, 5)
        if num.count('0') == 10 and int(num) > -1:
            ans.append(x * y)

print(max(ans))