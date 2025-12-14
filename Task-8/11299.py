from itertools import product as pr

alph = sorted('бмюрн')

for pos, val in enumerate(pr(alph, repeat=6), start=1):
    val = '0'.join(val)
    if pos % 2 != 0 and val[0] != 'м' and val.count('ю') == 0 and val.count('р') >= 2:
        print(pos)