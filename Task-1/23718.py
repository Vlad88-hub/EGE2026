from itertools import permutations

graph = 'ОТ ТЛ ЛЕ ЕВ ВЛ ВУ УЯ ЯМ МК КО КТ'.split()
matrix = '25 159 78 67 126 457 346 39 28'.split()

print(*range(1, 10))
for i in permutations('ТЛЕВУЯМКО'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)