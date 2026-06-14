def f(x):
    C = 30 <= x <= 45
    return ((x % A == 0) and C) <= (not(x % 12 == 0))

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break