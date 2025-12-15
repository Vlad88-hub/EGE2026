from itertools import product as pr

alph = sorted('гранит')

for pos, val in enumerate(pr(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] != 'а' and val[0] != 'и' and val[0] != 'г' and val.count('а') == 1:
        print(pos)