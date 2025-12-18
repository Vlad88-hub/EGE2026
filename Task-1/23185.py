from  itertools import permutations as per

graph = 'ah hf fe ed dg ga gc cb bf hb'.split()
matrix = '478 38 256 15 34 37 168 127'.split()

print(*range(1, 9))
for i in per('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)