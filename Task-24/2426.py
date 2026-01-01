with open(r'.\files\24_2426.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in data:
    if i not in 'ABC':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)

