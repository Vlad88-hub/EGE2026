from itertools import permutations

cnt = 0
for val in set(permutations('кайф')):
    val = ''.join(val)
    if val[-1] != 'й' and val.count('кф') == 0:
        print(val)
        cnt += 1
print(cnt)

