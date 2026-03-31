from itertools import product as pr

alph = sorted('сулак')

for x in range(1, 8):
    for pos, val in enumerate(pr(alph, repeat=x), start=1):
        val = ''.join(val)
        if val[0] == 'л' or val[0] == 'с':
            for i in 'ау':
                val = val.replace(i, '!')
            if '!!' not in val and pos == 12368 and val.count('!') <= 2:
                print(x)
