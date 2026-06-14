def convert(num, sus):
    res = ''
    while num:
        res += str(num % sus)
        num //= sus
    return res[::-1]

ans = []
for x in range(1, 5556):
    num = convert(5**150 + 5**135 - x, 5)
    if num.count('4') == 134:
        ans.append(x)

print(max(ans))