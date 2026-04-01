from itertools import permutations as per

graph = 'BH HD DA AC CB CG GA GE EF FH'.split()
matrix = '258 17 56 68 138 347 26 145'.split()

for i in per('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

print(52)