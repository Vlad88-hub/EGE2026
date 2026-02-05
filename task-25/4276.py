def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) >= 7:
        ct = 0
        for i in sorted(d)[::-1]:
            ct += 1
            if ct == 7:
                return i, len(d)
    return ()

cnt = 0
for n in range(400000001, 10**20):
    if F := f(n):
        cnt += 1
        print(*F)
        if cnt == 5:
            break