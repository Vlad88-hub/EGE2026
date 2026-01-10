from itertools import permutations

cnt_5 = 0
for val in permutations('0123456789abcdef', r=5):
    val = ''.join(val)
    if int(val[0], 16) > int(val[1], 16) > int(val[2], 16) > int(val[3], 16) > int(val[4], 16):
        cnt_5 += 1

cnt_3 = 0
for val in permutations('0123456789abcdef', r=3):
    val = ''.join(val)
    if int(val[0], 16) > int(val[1], 16) > int(val[2], 16):
        cnt_3 += 1
print(cnt_3 + cnt_5)