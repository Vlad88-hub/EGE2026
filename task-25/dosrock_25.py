def is_prime(num):
    if num < 2: return False
    for i in range(2, (num ** .5) + 1):
        if num % i == 0:
            return False
    return True

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

    if num > 2:
        d += [num]

    return d

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(set(d)) > 1:
        M = min(d) + max(d)
        if M % 10 == 4:
            return M
    return 0

cnt = 0
for n in range(800_001, 10**20):
    if F := f(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break

print([(800004, 400004),
(800009, 114294),
(800013, 266674),
(800024, 400014),
(800033, 61554)])