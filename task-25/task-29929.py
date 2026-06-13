def fact(num):
    d = []
    while num % 2 == 0:
        d.append(2)
        num //= 2
    i = 3
    while i < int(num ** .5) + 1:
        while num % i == 0:
            d.append(i)
            num //= i
        i += 2
    if num > 2:
        d.append(num)

    if len(d) == len(set(d)) == 2:
        return d
    return []

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

cnt = 0
for n in range(3_700_001, 10**10):
    F = fact(n)
    if F:
        for i in range(F[0] + 1, F[1]):
            if is_prime(i):
                break
        else:
            print(n, sum(F))
            cnt += 1
            if cnt == 5:
                break
