from itertools import permutations as per

graph = 'ad de eg gc cf fa ab be bf'.split()
matrix = '37 367 125 56 34 247 1260'.split()

print(*range(1, 8))
for i in per('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(66)