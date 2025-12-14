from itertools import product as pr

cnt = 0
for val in pr('01', repeat=16):
    val = ''.join(val)
    if val.count('1') % 3 == 0 and val[0] != '0':
        cnt += 1
print(cnt)