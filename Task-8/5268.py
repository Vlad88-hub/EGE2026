from itertools import permutations

cnt = 0
for val in set(permutations('амфибрахий')):
    val = ''.join(val)
    if val.count('иифаа') >= 1 or val.count('аафии') >=1:
        cnt += 1
print(cnt)