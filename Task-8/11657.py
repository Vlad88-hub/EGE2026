from itertools import permutations

cnt = 0
for val in permutations('0124567', r=6):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0246':
            val = val.replace(i, '@')

        if val.count('@@') >= 1:
            cnt += 1
print(cnt)