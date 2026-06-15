from string import printable

def convert(num, sus):
    res = ''
    while num:
        res += printable[num%sus]
        num //= sus
    return res[::-1]


ans = []
for x in range(1, 27_001):
    num = convert(3*27**9 + 2*27**6 + 27**3 - x, 27)
    if num.count('0') == 6:
        ans.append(x)

print(min(ans))