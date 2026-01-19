def DEL(n, m):
    return n % m == 0

def f(x):
    return DEL(x, A) or (DEL(x, 23) <= (x not in range(50, 71)))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break