def convert(num , sus):
    res = ''
    while num:
        res += str( num % sus)
        num //= sus
    return res[::-1]

ans = []
for N in range(2, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert((N % 3) * 3, 3)

    R = int(R, 3)
    if R <= 150:
        ans.append(N)

print(max(ans))