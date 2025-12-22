from itertools import permutations as per

graph = 'ac cd db bf fe ed dg ga ad'.split()
matrix = '37 57 147 37 26 57 12346'.split()

print(*range(1, 8))
for i in per('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)