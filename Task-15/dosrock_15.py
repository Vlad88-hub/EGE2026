from itertools import combinations

def f(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = A1 <= x <= A2
    return P <= ((Q and not A) <= (not P))

line_A = [25, 40, 64, 115]
line_x = [26, 41, 65]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(min(ans))
print(24)