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

def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) % 90 == 0:
        return True
    return False

cnt = 0
for n in range(5_200_001, 10**20):
    F = fact(n)
    if len(F) == 9 and f(n):
        print(n, max(F))
        cnt += 1
        if cnt == 5:
            break
