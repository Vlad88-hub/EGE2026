from itertools import product

cnt = 0
for val in product('ABCDEF', repeat=6):
    val = ''.join(val)
    if val[0] not in 'AE' and val[-1] not in 'AE':
        cnt += 1
print(cnt)