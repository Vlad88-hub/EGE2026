def f(start, end, cnt):
    if start in (18, 38): cnt += 1
    if start == end and cnt >= 1: return 1
    if start < end: return 0
    return f(start - 3, end, cnt) + f(start - 5, end, cnt) + f(start // 3, end, cnt)

print(f(80, 3, 0))