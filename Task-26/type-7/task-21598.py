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
last_change = 0
for i in range(len(timeline) - 1):
    if timeline[i] == timeline[i+1]:
        cnt += 1
    else:
        timeline_immutable.append(cnt)
        last_change = i
        cnt = 1
timeline_immutable.append(cnt)

# print(timeline)
print(max(timeline_immutable), last_change)
