from itertools import product

cnt = 0
for val in product('0123456', repeat=7):
    val = ''.join(val)
    if val[0] not in '035':
        u_2 = '22' in val
        u_4 = '44' in val
        if u_2 + u_4 <= 1:
            cnt += 1

print(cnt)