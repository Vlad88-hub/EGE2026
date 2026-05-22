def f(num):
    d = set()
    for i in range(1, int(num**.5) +1):
        if num % i == 0:
            d |= {i, num//i}
    if len(d) == 4:
        return d
    return set()

for n in range(178965, 178983):
    F = f(n)
    if F:
        print(sorted(F, reverse=True))

