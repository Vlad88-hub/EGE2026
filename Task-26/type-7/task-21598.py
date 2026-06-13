with open(r'../files/26_21598.txt') as file:
    N = int(file.readline())
    workers = [list(map(int, i.split())) for i in file]


# workers = [[10, 1070], [230, 1070], [240, 1070], [1070, 1400], [1071, 1400]]
timeline = [0] * 1440
for w1, w2 in workers:
    for i in range(w1, w2):
        timeline[i] += 1


timeline_immutable = []
cnt = 1
last_change = []
for i in range(1, len(timeline) - 1):
    if timeline[i] == timeline[i+1]:
        cnt += 1
    else:
        timeline_immutable.append(cnt)
        last_change.append(i+1)
        cnt = 1
timeline_immutable.append(cnt)

# print(timeline)
print(max(timeline_immutable), last_change[-2])


##########################################

timeline = [0] * (1440 + 1)
for w1, w2 in workers:
    for i in range(w1, w2 + 1):
        timeline[i] += 1

cnt = 0
ans_1 = []
ans_2 = 0
for i in range(1,1440):
    if timeline[i-1] == timeline[i] == timeline[i+1] != 0:
        cnt += 1
    elif timeline[i] != timeline[i+1]:
        ans_1.append(i)
        cnt = 0
    ans_2 = max(cnt, ans_2)

print(ans_1[-2], ans_2)
# print(timeline)
