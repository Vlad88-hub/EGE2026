from functools import lru_cache

@lru_cache(None)
def F(n):
    if n >= 128: return F(n - 5) + 1092
    return 5 * G(n - 7) + 29

@lru_cache(None)
def G(n):
    if n > 303728: return n - 15
    return G(n + 8) / 2 - 109

for i in range(303728, 1, -1):
    G(i)

for i in range(1, 2049):
    F(i)



print(F(2049))