ans = []
for N in range(1, 100000):
    R = bin(N + 2)[2:]
    R += str(R.count('1') % 2)
    R += str(R.count('1') % 2)
    R = int(R, 2)
    if R < 61:
        ans.append(N)
print(max(ans))

