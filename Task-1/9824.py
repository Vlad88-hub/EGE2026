from itertools import permutations as per

graph = 'ab bc ce eg gd df fa ac de'.split()
matrix = '346 45 16 125 247 137 56'.split()

print(*range(1, 8))
for i in per('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)