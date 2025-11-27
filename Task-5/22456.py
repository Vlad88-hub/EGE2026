ans = []
for N in range(1, 100000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '11' + R[2:] + '1'
    elif R.count('1') > R.count('0'):
        R += '0'
    else:
        R += '0'
    R = int(R, 2)
    if R > 271:
        ans.append(N)
print(min(ans))
