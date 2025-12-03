from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

ans = []
for x in range(0, 101):
    num1 = 7*100**6 + 10*100**5 + x*100**4 + 0*100**3 + 1*100**2 + 2*100**1 + 3*100**0
    num2 = 1*100**5 + 11*100**4 + 10*100**3 + 6*100**2 + 4*100**1 + x*100**0
    num3 = x*100**6 + 9*100**5 + 8*100**4 + 0*100**3 + 1*100**2 + 2*100**1 + 12*100**0
    num = num1 - num2 + num3
    if num % 21 == 0:
        ans.append(x)

print(convert(max(ans), 6))

