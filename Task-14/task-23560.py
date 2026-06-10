def convert(num, sus):
    res = ''
    while num:
        res+= str(num % sus)
        num //= sus
    return res[::-1]

ans = []
for x in range(1, 2401)[::-1]:
    num = convert(7*9**210 + 6*9**110 - x, 9)
    if num.count('0') == 100:
        print(x)
        break
