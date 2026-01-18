def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (x >= 27) or (2 * x < 3 * y) or ((2 + x) * (y - 3) < A)
            if not F:
                return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)