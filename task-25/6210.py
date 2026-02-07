from fnmatch import fnmatch

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 30:
        return sum(d)
    return 0

for n in range(202 - 202 % 53, 10**7, 53):
    if F := f(n) and fnmatch(str(n), '*2?2*') and str(n) == str(n)[::-1]:
        print(n, f(n))