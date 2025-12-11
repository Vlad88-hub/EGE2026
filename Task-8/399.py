from itertools import permutations as per

cnt = 0
for val in set(per('ворота', r=6)):
    val = ''.join(val)
    for i in 'оа':
        val = val.replace(i, '!')
    if "!!" not in val:
        cnt += 1
print(cnt)