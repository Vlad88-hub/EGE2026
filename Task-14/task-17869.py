from string import printable

def convert(num, sus):
    res = ''
    while num:
        res += printable[num % sus]
        num //= sus
    return res[::-1]

num = convert(3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025, 25)
print(num.count('0'))