def f(x):
    return (x % 21 == 0) <= ((not (x % A == 0)) <= (not (x % 77 == 0)))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break