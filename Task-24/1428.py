with open(r'.\files\24_1428.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in range(len(data) - 1):
    if data[i:i + 2] not in 'XY XZ':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(ans)