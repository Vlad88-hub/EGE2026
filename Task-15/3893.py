def f(x):
    return (A % 25 == 0) and (((x % 24 == 0) and (x % 75 == 0)) <= (x % A == 0))

cnt = 0
for A in range(-999, 1000):
    if A != 0:
        if all(f(x) for x in range(-999, 1000)):
            cnt += 1

print(cnt)