with open(r'../files/24_9791.txt') as file:
    data = file.readline().lower()

ans = 0
cnt = 0
for i in range(len(data)):
    if data[i] in '123456789abcdef':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print(ans)