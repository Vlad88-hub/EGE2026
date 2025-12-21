from itertools import permutations as per

graph = 'ce eg gf fa ac cd dh he ab bf'.split()
matrix = '68 47 45  237 368 15 248 157'.split()

print(*range(1, 9))
for i in per('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(18)