from itertools import permutations

cnt = 0
for val in set(permutations('ДЖ*ВАСКРИПТ')):
    val = ''.join(val)
    if val.index('А') + 1 + val.index('*') + 1 + val.index('И') + 1 == 11:
        cnt += 1

print(cnt/2)

#####################################################


from itertools import permutations

cnt = 0
for val in set(permutations('ДЖАВАСКРИПТ')):
    val = ''.join(val)
    summ = 0
    for pos, buk in enumerate(val, start=1):
        if buk in 'АИ':
            summ += pos
            if summ == 11:
                cnt += 1

print(cnt)


