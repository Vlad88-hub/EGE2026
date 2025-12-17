# перебор
with open(r'.\files\24_1205.txt') as file:
    data = file.readline()

cnt = 0
ans = 0
for i in data:
    if i not in 'GWP':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)