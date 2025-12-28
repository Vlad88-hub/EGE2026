with open(r'.\files\24_865.txt') as file:
    data = file.readline()

test = 'ABAAACABFCCCDADFF'

cnt = 0
ans = 0
for i in data:
    if i not in 'CF':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)