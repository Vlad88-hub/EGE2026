def f(x):
    return ((405 % x == 0) <= (81 % x == 0)) or (A - x > 162)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)