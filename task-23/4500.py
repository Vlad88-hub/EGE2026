def f(start, end, steps =''):
    if start == end  and 'AA' not in steps : return 1
    if start > end or start == 23: return 0
    return f(start + 1, end, steps + 'A') + f(start + 2, end, steps +'B') + f(start * 2, end, steps + 'C')

print(f(3, 11, '') * f(11, 79, ''))