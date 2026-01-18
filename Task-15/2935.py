def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (2 * y + 3 * x != 135) or (y > A) or (x > A)
            if not F:
                return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)