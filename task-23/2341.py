def f(start, cnt):
    if cnt == 8 and start in range(1000, 1025): return {start}
    if cnt == 8 and start not in range(1000, 1025): return set()
    return f(start + 1, cnt + 1)| f(start + 5, cnt + 1) | f(start * 3, cnt + 1)

print(len(f(1, 0)))
