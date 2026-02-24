def f(start, end, steps = ''):
    if start == end and steps.count('A') <= 4 and steps.count('B') >= 2 and steps.count('C') == 5: return 1
    if start > end: return 0
    return f(start * 5, end, steps + 'A') + f(start * 3, end, steps + 'B') + f(start + 45, end, steps + 'C')

print(f(1, 2970, ''))