from itertools import product

alph = sorted('АРГУМЕНТ')
print(''.join(alph))
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    # print(val)
    if val in ''.join(alph) and len(set(val)) == 4:
        print(pos)