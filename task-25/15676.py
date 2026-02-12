from fnmatch import fnmatch
from itertools import product


# 100_000_000
#       1_036
def not_is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return True
    return False

for n in range(4, 10**4):
    if not_is_prime(n):
        for N in range(int(f'1{n}036') - int(f'1{n}036') % 22768, 10**8, 22768):
            if fnmatch(str(N), f'1{n}03*6*'):
                print(N, n)

##############################################################################################

ans = []
for l1 in range(1, 5):
    for N in range(10**(l1 - 1), 10**l1):
        if not_is_prime(N):
            for l2 in range(0, 4 - l1 + 1):
                for Z1 in product('0123456789', repeat=l2):
                    Z1 = ''.join(Z1)
                    for l3 in range(0, 4 - l1 - l2 + 1):
                        for Z2 in product('0123456789', repeat=l3):
                            Z2 = ''.join(Z2)
                            num = int(f'1{N}03{Z1}6{Z2}')
                            if num % 22786 == 0 and num < 10**8:
                                ans += [num, N]
for i in sorted(ans):
    print(*i)

