from  itertools import *

# product - возвращает все возможные расстановки символов с повторентем длины repeat
alph_1 = '012'
res = product(alph_1, repeat=8)
print(*res)
for val in product(alph_1, repeat=2):
    val = ''.join(val)
    print(val)

# permutations - все возможные перестановки символов
alph_2 = 'sd'
for val in permutations(alph_2):
     val = ''.join(val)
     print(val)

# enumerate - нумерация символов
alph_3 = 'aswx'
res = enumerate(alph_3, start=1)
print(*res)

# sorted - расставляет алфавит в нужном порядке
