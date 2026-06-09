from itertools import product, repeat

cnt = 0
for val in product('0123456', repeat=5):
    val = ''.join(val)
    if val[0] in '246' and val[-1] not in '012' and val.count('4') <= 1:
        cnt +=1

print(cnt)