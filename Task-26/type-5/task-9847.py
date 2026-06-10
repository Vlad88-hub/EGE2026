with open(r'../files/26_9847.txt') as file:
    N = file.readline()
    pos = [list(map(int, i.split())) for i in file]

new_pos = []
for p1, p2 in pos:
    # print(p1, p2)
    for i in range(p1, p2):
        # print(i)
        new_pos.append(i)

new_pos = sorted(new_pos)
shop = [0] * 1440
# print(new_pos)

ans = []
cnt = 1
for i1, i2 in zip(new_pos, new_pos[1:]):
    if i2 == i1:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 1
max_ans = max(ans)

print(sum(i == max_ans for i in ans), max_ans)



