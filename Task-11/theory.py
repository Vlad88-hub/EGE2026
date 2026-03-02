from math import log2, ceil

#
L = 101
N = 10 + 4090
i = ceil(log2(N))
I = ceil(L * i / 8)
print(I * 2048 / 1024)

# 2327
for L in range(1, 100000):
    N = 10 + 27
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 3548 * I > 12 * 2 ** 10:
        print(I)
        break

# 2395
for N in range(1, 100000):
    L = 172
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 356984 * I >= 54 * 2 ** 20:
        print(N)
        break
