from fnmatch import fnmatch
# 100_000_000
#       1_036
def not_is_prime(num):
    if num < 2: return True
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return True
    return False

for n in range(4, 10**5):
    if not_is_prime(n):
        for i in range(int(f'1{n}036') - int(f'1{n}036') % 22768, 10**8, 22768):
            if fnmatch(str(i), f'1{n}03*6*'):
                print(i, n)

