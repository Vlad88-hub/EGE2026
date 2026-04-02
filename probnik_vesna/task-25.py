def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i}
            if num // i != num:
                d |= {num // i}
    for n in sorted(d):
        if n % 100 == 11 and n != 11:
            return n
    return 0

cnt = 0
for n in range(1_350_051, 10**20):
    if F := f(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break