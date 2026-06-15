from math import log2, ceil

for L in range(1, 10**10):
    N = 10+27
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 3548 > 12*2**10:
        print(L)
        break