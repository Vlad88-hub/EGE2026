from sys import setrecursionlimit

def F(n):
    if n < 3: return 3
    return F(n - 2) +2 * n + 5

setrecursionlimit(1600)
print(F(3027) - F(3023))