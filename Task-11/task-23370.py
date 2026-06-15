from math import log2, ceil

for L in range(1, 10**10):
    N = 27
    i = ceil(log2(N))
    I = ceil(L*i/8)
    if I * 7_564_230 > 32*2**20:
        print(L)
        break   
