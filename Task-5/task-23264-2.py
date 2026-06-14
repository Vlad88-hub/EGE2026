def convert(num, sus):
    res = ''
    while num:
        res += str(num % sus)
        num //= sus
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert((N % 3) * 5, 3)

    R = int(R, 3)
    if R > 150:
        ans.append(R)

print(min(ans))







# data = '1234'
# print(data[-2:])