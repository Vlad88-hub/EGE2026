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
for n in range(6_086_056, 10**20):
    F = fact(n)
    if len(F) == 2 and all(str(i).count('6') == 1 for i in F):
        cnt += 1
        print(n, max(F))
        if cnt == 5:
            break
