def f(x):
    return (abs(A) % 25 == 0) and (((abs(x) % 24 == 0) and (abs(x) % 75 == 0)) <= (abs(x) % A == 0))

cnt = 0
for A in range(-999, 1000):
    if all(f(x) for x in range(-999, 1000)):
        cnt += 1