def f(start, end, p1, p2):
    if start == 30: p1 = 1
    if start == 60: p2 = 1
    if start >= end: return start == end and 0 < p1 + p2 < 2
    # if start > end or 0 < p1 + p2 < 2: return 0
    return f(start + 1, end, p1, p2) + f(start * 2, end, p1, p2) + f(start * 3, end, p1, p2)



print(f(10, 70, 0, 0))