from itertools import permutations as per

cnt = 0
for val in set(per('росомаха')):
    val = ''.join(val)
    for i in 'оа':
        val = val.replace(i, '!')
    for i in 'рсмх':
        val = val.replace(i, '@')
    if '@@' not in val and '!!' not in val:
        cnt += 1
print(cnt)
