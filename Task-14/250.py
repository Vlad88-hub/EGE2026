from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 40):
    R = convert(N, 2)
    if R[-4:] == '1011':
        ans.append(N)
print(max(ans))

