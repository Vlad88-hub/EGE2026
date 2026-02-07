def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 1:
        M = sum(d)
        if is_prime(M % 100000):
            return M
    return 0

cnt = 0
for n in range(1273548, 10**20):
    if F := f(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break