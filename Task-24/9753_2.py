with open(r'.\files\24_9753.txt') as file:
    data = file.readline()

ans = 0
i = 0
while i < len(data):
    cnt = 0
    cnt_Y = 0
    first_Y = 0
    for j in range(i, len(data)):
        if data[j] == 'Y':
            cnt_Y += 1
        if cnt_Y == 1:
            first_Y = j
        if cnt_Y == 151:
            break
        cnt += 1
    if cnt_Y == 151:
        ans = max(ans, cnt)
        i = first_Y
        i += 1
    else:
        break

print(ans)