def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        new_R = 0
        for i in R:
            new_R += int(i)
        new_R *= 3
        new_R = convert(new_R, 3)
        R += new_R
    R = int(R, 3)
    if R % 2 != 0 and R > 208:
        ans.append(R)
print(min(ans))
