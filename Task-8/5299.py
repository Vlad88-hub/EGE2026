from itertools import permutations as pr

cnt = -1
for val in set(pr('хочу_сотку')):
    val = ''.join(val)
    if val[0] not in '_у' and '_у' not in val and val[-1] != '_':
        cnt += 1
print(cnt)