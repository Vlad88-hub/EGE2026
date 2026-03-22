from itertools import permutations

cnt = 0
for val in permutations('АБИКОЛУН'):
    val = ''.join(val)
    for i in 'АИОУ':
        val = val.replace(i, '!')
    for i in 'БКЛН':
        val = val.replace(i, '@')
    if '!!' not in val and '@@' not in val:
        cnt += 1

print(cnt)