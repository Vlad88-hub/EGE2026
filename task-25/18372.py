def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i}
            if num // i != num:
                d |= {num // i}
    A = 0
    for i in d:
         A += i
    A //= len(d)
    if A % 100 == 12:
        return A
    return 0

cnt = 0
for n in range(1, 770000)[::-1]:
    if F := f(n):
        cnt += 1
        print(n, F)
        if cnt == 5:
            break
