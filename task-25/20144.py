def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if num // i != num and is_prime(num // i):
                d |= {num // i}
    if len(d) > 1:
        R = max(d) - min(d)
        if R > 1000 and R % 3 == 0:
            return R
    return 0

cnt = 0
for n in range(3_333_338, 10**20):
    if F := f(n):
        print(n, F)
        cnt += 1
        if cnt == 5:
            break