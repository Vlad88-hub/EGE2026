from itertools import permutations as per

graph = 'bd de ea ac cg gb gf fe fc'.split()
matrix = '26 147 456 237 37 13 245'.split()

print(*range(1, 8))
for i in per('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(39 + 21)