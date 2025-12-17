# перебор
with open(r'.\files\24_1273.txt') as files:
    data = files.readline()


cnt = 2
ans = 0
for i in range(len(data) - 2):
    if data[i:i + 3] != 'XYZ':
        cnt += 1
    else:
        ans = max(ans , cnt)
        cnt = 2
ans = max(ans, cnt)
print(ans)

