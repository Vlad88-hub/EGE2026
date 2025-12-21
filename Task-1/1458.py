from itertools import permutations as per

graph = 'аб бе еж жд дв ва аг гв гб гд де'.split()
matrix = '256 13467 2456 237 136 1235 24'.split()

print(*range(1, 8))
for i in per('абвгдеж'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)