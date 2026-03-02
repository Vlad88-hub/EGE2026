from itertools import  combinations

def f(x):
    C = 47 <= x <= 115
    B = 24 <= x <= 90
    A = A1 <= x <= A2
    return C <= ((not A and B) <= (not C))


line_a = [24, 47, 90, 115]
line_x = [25, 48, 91]


ans = []
for A1, A2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)

print(min(ans))