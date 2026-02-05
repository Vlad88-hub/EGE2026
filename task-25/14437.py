def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 0:
        M = sum(d) // len(d)
        if M % 1000 == 313:
            return M
    return 0

cnt = 0
for n in range(1, 700000)[::-1]:
    if F := f(n):
        cnt += 1
        print(n, F)
        if cnt == 7:
            break