def is_prime(num):
    if num < 2: return True
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}

    if len(d) > 1:
        M = min(d) + max(d)
        if M % 213 == 171:
            return M
    return 0

cnt = 0
for n in range(23600001, 10**20):
    if F:=f(n):
        cnt += 1
        print(n, F)
        if cnt == 6:
            break