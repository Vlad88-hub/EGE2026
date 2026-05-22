def f(x, y):
    return (x**2 <= 136) or (y < 4*x + A - 70) or (2*y > 51)

for A in range(0, 1000):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break