from itertools import product

cnt = 0
for val in product('0123456', repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        u = [1 for i in val if int(i) in range(3, 6)]
        if '11' not in val and '22' not in val and '00' not in val and '33' not in val and '44' not in val and '55' not in val and '66' not in val and sum(u) == 2:
            cnt += 1

print(cnt)
