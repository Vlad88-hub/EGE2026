def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 1:
        return min(d) + max(d)
    return 0

cnt = 0
for n in range(800_001, 10**20):
    F = f(n)
    if F % 10 == 4 and F:
        print(n, F)
        cnt += 1
        if cnt == 5:
            break