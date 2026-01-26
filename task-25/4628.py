from fnmatch import  fnmatch

for N in range(124065 - 124065 % 161, 10**8, 161):
    if fnmatch(str(N), '12*4?65'):
        print(N, N // 161)

###############################################################
from itertools import product

ans = []
for V in '0123456789':
    for l in range(0, 3):
        for Z in product('012356789', repeat=l):
            val = int(f'12{''.join(Z)}4{V}65')
            if val % 161 == 0:
                ans.append([val, val // 161])
for i in sorted(ans):
    print(*i)
