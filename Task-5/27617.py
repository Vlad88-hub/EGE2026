ans_min = []
ans_max =[]

for N in range(0, 100000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin((N % 3)* 3)[2:]
    R = int(R, 2)
    if R < 130:
        ans_min.append([R, N])
    else:
        ans_max.append([R, N])

min_ans = max(ans_min)
max_ans = min(ans_max)
if 130 - min_ans[0] < max_ans[0] - 130:
    print(min_ans[1])
else:
    print(max_ans[1])