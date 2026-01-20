def f(x, y):
    return (2 * x + y != 150) or (x not in range(50, 71)) or (A > y)

for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)