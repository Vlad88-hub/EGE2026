from itertools import permutations as per

graph = 'аб бв вд де ек кг гв ве ва ге'.split()
matrix = '24 146 56 1267 36 23457 46'.split()

print(*range(1, 8))
for i in per('абвгдек'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(30)