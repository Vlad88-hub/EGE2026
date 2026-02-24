def f(start, end, cnt):
    if start % 2 != 0:
        cnt += 1
        if cnt <= 4: return 0
    if start == end: return 1
    if start > end: return 0
    return f(start + 2 , end, cnt) + f(start + 3, end, cnt) + f(start * 2 + 1, end, cnt)

print(f(1, 625, 0))