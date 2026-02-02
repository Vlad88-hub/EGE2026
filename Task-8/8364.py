from itertools import product

cnt = 0
cnt1 = 0
alph = sorted('крате')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'карета':
        cnt = pos
    if val == 'ракета':
        cnt1 = pos
print(cnt1 - cnt - 1)