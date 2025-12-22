from itertools import permutations as per

graph = 'ae eh hg gc cf fa ed db df bh bg'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*range(1, 9))
for i in per('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(14+17)