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
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}

    if len(d) >= 4:
        M = sorted(d)[0] + sorted(d)[1] + sorted(d)[-1] + sorted(d)[-2]
        if M % 114 == 39:
            return M
    return 0

cnt = 0
for i in range(456_790, 10**20):
    F =f(i)
    if F:
        cnt += 1
        print(i, F)
        if cnt == 5:
            break