def f(A):

    for x in range(0, 1000):
        B = 70 <= x <= 90
        F = (x % A == 0) or (B <= (x % 22 != 0))
        if not F:
            return False
    return True


for A in range(1, 1000):
    if f(A):
        print(A)