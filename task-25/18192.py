def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}

    if len(d) == 3:
        return max(d)
    return 0

cnt = 0
for n in range(1_000_001, 10**20):
    if F := f(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break
