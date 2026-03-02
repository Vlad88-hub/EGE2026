def f(x, y, s):
    if x + y >= 259: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x+ 1,y, s - 1),
        f(x, y + 1, s-1),
        f(x * 2, y , s-1),
        f(x, y * 2, s-1),
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19', [y for y in range(1, 242) if f(17, y, 2)]) # 61
print('20', [y for y in range(1, 242) if f(17, y, 3) and not f(17, y, 1)]) # 112, 120
print('21', [y for y in range(1, 242) if f(17, y, 4) and not f(17, y, 2)]) # 111, 119