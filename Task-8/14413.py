from itertools import permutations as per

cnt = 0
for val in set(per('сортировка')):
    val = ''.join(val)
    for i in 'оиа':
        val = val.replace(i, '!')
    for i in 'срткв':
        val = val.replace(i, '@')
    if val.count('!!!') == 0 and val.count('@@@') == 0:
        cnt += 1
print(cnt)