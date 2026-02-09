def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i < int(num ** .5) + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 1:
        d += [num]
    return d

cnt = 0
for n in range(5_000_012, 10**20, 100):
    F = fact(n)
    

