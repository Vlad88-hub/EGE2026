def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res [::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 4)
    if R[:1] == '3':
        R = R.replace('3', '@')
        R = R.replace('1', '3')
        R = R.replace('@', '1')
        R = '21' + R
    else:
        R = '1' + R[1:] + '12'
    R = int(R, 4)
    if R < 598:
        ans.append(N)
print(max(ans))

