def f(start, end):
    if start == end: return 1
    if start > end: return 0
    if start == 6: return f(start + 2, end) + f(start + 5, end)
    return f(start + 2, end) + f(start + 5, end) + f(start**2, end)


print(f(4, 36))


###########################################################

def f(start, end, steps=''):
    if start == end and steps[-1] == 'C': return 0
    if start == end: return 1
    if start > end: return 0
    return f(start + 2, end, steps + 'A') + f(start + 5, end,steps + 'B') + f(start**2, end, steps + 'C')


print(f(4, 36))