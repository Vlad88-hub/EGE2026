from itertools import permutations as per

graph = 'аб бг ги ие ед дв ва бв гж жд иж'.split()
matrix = '267 157 468 356 248 134 12 35'.split()

print(*range(1, 9))
for i in per('абвгдеиж'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(39)