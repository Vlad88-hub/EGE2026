ans = []
for N in range(1, 100000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R1 = R.count('1')
        while R1 != 0:
            R += '1'
            R1 -= 1
    else:
        R = '1' + R +'101'
    R = int(R, 2)
    if R > 350:
        ans.append(N)
print(min(ans))