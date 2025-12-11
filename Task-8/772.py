from itertools import permutations as per

cnt = 0
for val in set(per('пробник')):
    val = ''.join(val)
    if val[0] not in 'ои' and val[-1] not in 'ои' and 'ои' not in val and 'ио' not  in val:
        cnt += 1
print(cnt)

