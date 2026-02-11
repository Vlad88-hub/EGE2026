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
    Fa = fact(n)
    F = ''
    ans = []
    for i in Fa:
        F += str(i) + '0'
    F = F.split('0')
    for i in set(Fa):
        if F.count(str(i)) == 5:
            ans += [i]
    if ans:
        print(n, min(ans))
        cnt += 1
        if cnt == 5:
            break
    

