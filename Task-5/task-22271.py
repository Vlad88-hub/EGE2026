def convert(num, sus):
    res = ''
    while num:
        res += str(num % sus)
        num //= sus
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 8)
    if R[0] == '5':
        R = R.replace('2', '!')
        R = R.replace('1', '2')
        R = R.replace('!', '1')
        R = '11' + R
    else:
        R = '2' + R[1:] + '10'
    R = int(R, 8)
    if R < 1354:
        ans.append(N)

print(max(ans))