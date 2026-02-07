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

    if num > 2:
        d += [num]
    return d

cnt = 0
for n in range(7_305_679, 10**20):
    F = fact(n)
    if len(F) == 4:
        if str(sum(F)) == str(sum(F))[::-1]:
            cnt += 1
            print(n, sum(F))
            if cnt == 5:
                break