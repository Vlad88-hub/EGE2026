def is_prime(num):
    if num < 2 : return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i) and i % 10 == 7:
                d |= {i}
            if is_prime(num // i) and num // i % 10 == 7:
                d |= {num // i}

    if len(d) > 1:
        F = sum(d)//len(d)
        if F % 111 == 0:
            return F
    return 0

cnt = 0
for n in range(1, 750_000)[::-1]:
    F = f(n)
    if F:
        cnt += 1
        print(n, F)
        if cnt == 5:
            break