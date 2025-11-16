def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 1000000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R += convert(sum(map(int, R)), 3)
    R = int(R, 3)
    if R % 2 == 0 and R > 220:
        ans.append(R)

print(min(ans))


