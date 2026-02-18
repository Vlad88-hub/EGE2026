from itertools import permutations

cnt = 0
for val in set(permutations('ДЖ*ВАСКРИПТ')):
    val = ''.join(val)
    if val.index('А') + 1 + val.index('*') + 1 + val.index('И') + 1 == 11:
        cnt += 1

print(cnt)
