with open(r'.\files\26_16390.txt') as file:
    S, N = file.readline().split()
    gifts = [int(i) for i in file]

gifts = sorted(gifts)
S_new = S

ans = []
for i in range(1, int(N)):
    cnt = 0
    last_gift = 0
    for gift in gifts[i:]:
        if int(S_new) - gift >= 0:
            cnt += 1
            S_new = int(S) - gift
            last_gift = gift
    S_new = S
    ans.append([cnt, last_gift])

max_ans = max(ans)[0]
max_cnt_ans = 0
for i in ans:
    if i[0] == max_ans:
        max_cnt_ans = max(i[1], max_cnt_ans)


print(max_cnt_ans, max_ans)