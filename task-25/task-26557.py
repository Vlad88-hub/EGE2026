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
            if is_prime(num // i) and num // i != num:
                d |= {num // i}
    if d:
        M = min(d) + max(d)
        if M % 100 == 63 and M % len(d) == 0:
            return M
    return 0

cnt = 0
for n in range(7_800_001, 10**10):
    F = f(n)
    if F:
        print(n, F)
        cnt += 1
        if cnt == 5:
            break
