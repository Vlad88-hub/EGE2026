from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 10: return 1
    return (n + 3) * f(n - 3)

for i in range(10, 247_564):
    f(i)

print((f(247_563)/519-477*f(247_560))/f(247_557))