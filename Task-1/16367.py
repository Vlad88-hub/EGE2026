from itertools import permutations as per

graph = 'ag gb be ef fd dc ca ba fc'.split()
matrix = '246 16 57 15 347 127 356'.split()

print(*range(1, 8))
for i in per('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)