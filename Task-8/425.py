from itertools import permutations as per

cnt = 0
for val in set(per('запись', r=6)):
    val = ''.join(val)
    if val[0] != 'ь' and 'аь' not in val and 'иь' not in val:
        cnt += 1
print(cnt)