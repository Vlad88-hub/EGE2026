ans = 0
for i in 'AOBMLCNG':
    ans = max(ans, int(i, 36))

for p in range(ans + 1, 36):
    if int('BO',p) + int('OM', p) + int('BL4', p) == int('CNG', p):
        print(p)