def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(1, int(num**.5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i) and num // i != num:
                d |= {num // i}

    if len(d) > 1:
        S = sum(d)
        if S % 17 == 0:
            return S
    return 0

cnt = 0
for n in range(250001, 10**20):
    if F :=f(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break
