ans = []
for N in range(1, 100000):
    R = hex(N)[2:]
    if R.count('b') % 2 == 0:
        R = '1' + R
    else:
        R += '1'
    R = int(R, 16)
    if 10 <= R <= 99:
        ans.append(N)

print(len(set((ans))))

