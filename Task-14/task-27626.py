def convert(num, sus):
    res = ''
    while num:
        res += str(num % sus)
        num //= sus
    return res[::-1]

cnt_0 = []
for x in range(1, 2031):
    num = convert(6**2030 + 6**100 - x, 6)
    cnt_0.append(num.count('0'))

print(min(cnt_0))