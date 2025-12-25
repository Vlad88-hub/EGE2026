from itertools import product, permutations, repeat

def f(x, y, z, w):
    return (x or y) and not (y == z) and not w

for i in product((0, 1), repeat=4):
    tadle = [
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3], 1, 1, 0)
    ]
    if len(set(tadle)) == len(tadle):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in tadle] == [1, 1, 1]:
                print(*p, sep='')