from string import printable as pr

ans = []
for x in pr[:15]:
    M = int(f'432{x}3', 15)
    N = int(f'86{x}86', 15)
    for A in range(1000000):
        if (M + A) % N == 0:
            ans.append(A)
print(min(ans))
