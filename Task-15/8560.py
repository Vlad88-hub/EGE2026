def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            for z in range(0, 1000):
                F = (2 * x + y != 136) or (z * y < 100) or (A**2 >= x + y)
                if not F:
                    return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)