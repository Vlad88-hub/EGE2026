def f(start, end, steps = []):
    if start == end and ((24 in steps and [25,26,27,28,29,30,31,32] not in start) or (25 in steps and [24,26,27,28,29,30,31,32] not in start) or (26 in steps and [24,25,27,28,29,30,31,32] not in start) or (27 in steps and [24,25,26,28,29,30,31,32] not in start) or (28 in steps and [24,25,26,27,29,30,31,32] not in start) or (29 in steps and [24,26,27,28,25,30,31,32] not in start) or (30 in steps and [24,26,27,28,29,25,31,32] not in start) or (31 in steps and [24,26,27,28,29,30,25,32] not in start) or (32 in steps and [24,26,27,28,29,30,31,25] not in start)): return 1
    if start > end: return 0
    return f(start + 1, end, steps + [start + 1]) + f(start + 2, end, steps + [start + 1]) + f(start + 4, end, steps + [start + 1]) + f(start + 8, end, steps + [start + 1])

print(f(16, 48))