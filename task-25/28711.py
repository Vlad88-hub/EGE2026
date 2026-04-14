def fact(num):
    d = []
    while num % 2 == 0:
        d.append(2)
        num //= 2
    i = 3
    while i < int(num ** .5)+1:
        while num % i == 0:
            d.append(i)
            num //= i
        i += 2

    if num > 2:
        d.append(num)
    return d

cnt = 0
for n in range(2_400_001, 10**20):
    F = fact(n)
    if len(F) == 3 and sorted(F) == sorted(set(F)):
        u = [1 for i in F if '4' in str(i) or '7' in str(i)]
        if sum(u) == 3:
            cnt += 1
            print(n, max(F))
            if cnt == 5:
                break