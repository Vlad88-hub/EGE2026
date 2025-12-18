from itertools import permutations as per

graph = 'af fe ec cg gd db ba fb ed'.split()
matrix = '256 134 267 27 16 135 34'.split()

print(*range(1, 8))
for i in per('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)