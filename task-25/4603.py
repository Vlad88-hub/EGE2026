from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10**8, 141):
    if fnmatch(str(N), '1234*7') and N % 141 == 0:
        print(N, N // 141)

from itertools import product

########################################################################

for l in range(0, 4):
    for val in product("0123456789", repeat=l):
        val = int('1244' + ''.join(val) + '7')
        if val % 141:
            print(val, val // 141)
