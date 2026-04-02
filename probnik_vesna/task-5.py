def convert(num, sus):
    res = ''
    while num:
        res += str(num % sus)
        num //= sus
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 4)
    if N % 4 == 0:
        R += R[:2]
    else:
        R += convert((N % 4) * 4, 4)
    R = int(R, 4)
    if R > 291:
        ans.append(R)

print(min(ans))

# data = '11234'
# print(data[:2])