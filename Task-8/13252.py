from itertools import permutations as per

cnt = 0
for val in set(per('кидала', r=5)):
    val = ''.join(val)
    if 'аа' not in val:
        cnt += 1
print(cnt)
