from itertools import permutations as per

graph = 'ab bh hf fd dc ce ea eg gc fg ah'.split()
matrix = '247 148 578 126 38 47 136 235'.split()

print(*range(1, 9))
for i in per('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)