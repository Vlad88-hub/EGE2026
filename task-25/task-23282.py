def is_fact(num):
    if num < 2: return False
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            if is_fact(i):
                d |= {i}
            if is_fact(num//i):
                d|= {num//i}

    if len(d) > 1:
        M = max(d) + min(d)
        if str(M) == str(M)[::-1] and M > 60_000:
            return M
    return 0

cnt = 0
for n in range(5_400_001, 10**10):
    F = f(n)
    if F:
        print(n, F)
        cnt += 1
        if cnt == 5:
            break
