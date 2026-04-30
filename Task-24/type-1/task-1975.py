with open(r'../files/24_1975.txt') as file:
    data = file.readline()

cnt = 0
ans = []
for i in range(len(data)-1):
    cnt += 1
    if data[i:i+2] == 'PP':
        ans.append(cnt)
        cnt = 0

print(max(ans))