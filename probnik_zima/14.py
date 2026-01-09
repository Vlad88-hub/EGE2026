def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(10, 70001):
    num = convert(5**2025 + 5**400 - x, 5)
    if num.count('4') >= 1:
        ans.append([num.count('4'), x])

print(max(ans)[0])
for i in ans:
    if i[0] == 399:
        print(i[1])


