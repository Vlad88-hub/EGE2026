def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i < int(num ** .5)+1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    if len(d) == 2:
        return d
    return {}

cnt = 0
for n in range(6_086_056, 10**10):
    if F := fact(n):
        u = [str(n).count('6') == 1 for n in F]
        if sum(u) == 2:
            print(n, max(F))
            cnt +=1
            if cnt == 5:
                break