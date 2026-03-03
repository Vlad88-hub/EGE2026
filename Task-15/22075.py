def dig(x, y):
    if str(x)[0] == str(y)[0]:
        return True
    return False

def f(x):
    return (not dig(x, 28) and dig(x, 47)) <= (x > A - 20)

for A in range(1, 1000)[::-1]:
    if all(f(n) for n in range(1, 1000)):
        print(A)
        break