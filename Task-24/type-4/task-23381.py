with open(r'../files/24_23381.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)-1):
    if data[i] in '02468' and data[i+1] not in '0123456789':
        ch = data[i+1]
        cnt = 3
        for j in range(i + 2, len(data)):
            if data[j] == ch:
                cnt += 1
            elif data[j] in '02468':
                ans = max(ans, cnt)
                break
            else:
                break

print(ans)
