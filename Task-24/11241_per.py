with open(r'.\files\24_11241.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in data:
    if i not in 'ABCD':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print(ans)