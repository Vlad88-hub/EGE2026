cnt_chet = 0
for N in range(2, 100000):
    R = bin(N)[2:]
    for i in range(1, len(R), 2):
        if R[i] == '1':
            cnt_chet += 1
