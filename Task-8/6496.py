from itertools import *

alph = sorted('берск')
x = 7
cnt = 0
while 5 <= x <= 7:
    for val in product(alph, repeat=x):
        val = ''.join(val)
        cnt += 1
    x -= 1
print(cnt)
