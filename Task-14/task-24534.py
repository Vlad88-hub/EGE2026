def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 11501):
    num = convert(7**270 + 7**170 + 7**70 - x, 7)
    ans.append([num.count('0'), x])

print(max(ans)[1])