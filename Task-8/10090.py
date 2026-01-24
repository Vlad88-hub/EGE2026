from itertools import permutations

cnt = 0
for val in permutations('!!@!@!@', r=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0246':
            val = val.replace(i, '!')
        for i in '357':
            val = val.replace(i, '@')
        if '!!' not in val and '@@' not in val:
            cnt += 1
print(cnt)
