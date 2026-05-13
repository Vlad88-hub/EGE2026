def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i < int(num**.5) + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    return d

cnt = 0
for n in range(24_517_512, 10**20):
    F = fact(n)
    if len(F) == 12:
        print(n, max(F))
        cnt += 1
        if cnt == 5:
            break