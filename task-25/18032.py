def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    S = 0
    for n in d:
        S += n
    if S % 100 == 23:
        return S
    return 0

for n in range(1000, 10000):
    if F := f(n):
        print(n, F)