def f(x):
    return (x % A == 0) or ((x in range(50, 71)) <= (x % 16 != 0))

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
