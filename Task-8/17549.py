from itertools import product as pr

alph = sorted('фокус')

for pos, val in enumerate(pr(alph, repeat=5), start=1):# 'ф' not in val.

    val = ''.join(val)
    if val.count('ф') == 0 and val.count('у') == 2:
        print(pos, val)





