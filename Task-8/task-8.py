from itertools import product as pr

alph = sorted('АПРЕЛЬ')

for pos, val in enumerate(pr(alph, repeat = 6)):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in 'АЛ' and val.count('П') >= 2:
        print(pos)
        break