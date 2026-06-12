def convert(num, sus):
    res = ''
    while num:
        res += str(num % sus)
        num //= sus
    return res[::-1]

ans = []
for N in range(10, 100_000):
    R = convert(N, 3)
    if N % 4 == 0:
        R += R[-3:]
    else:
        R = '1' + R + '20'
    R = int(R, 3)
    if R > 423:
        ans.append(R)

print(min(ans))