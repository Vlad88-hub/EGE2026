from itertools import product

cnt = 0
for val in product('0123456', repeat=5):
    val = ''.join(val)

    if val[0] != '0' and val.count('6') == 1:
        for i in '0123456':
            val = val.replace(i+i, '*')
        if '*' not in val:
            cnt += 1



print(cnt)
