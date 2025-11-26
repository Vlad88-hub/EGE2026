def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 4)
    if sum(map(int, R)) % 3 == 0:
        R = R.replace('2', '!')
        R = R.replace('0', '2')
        R = R.replace('!', '0')
        R = '32' + R
    else:
        R += '33'
        R = R[:1] + '10' + R[3:]

    R = int(R, 4)
    if R > 320:
        ans.append([R, N])

mans = min(ans)[0]
for i in ans:
    if i[0] == mans:
        print(i[1])






