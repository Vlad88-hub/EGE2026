def DEL(n, m):
    return n % m == 0

def f(x):
    return DEL(x, 17) <= ((x not in range(80, 101)) or (A < x + 30))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)