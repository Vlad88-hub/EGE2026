with open(r'../files/24_2942.txt') as file:
    data = file.readline()

data = data.replace('AB', '*')
data = data.replace('AC', '*')

cnt = 0
ans = []
for i in range(len(data)):
    if data[i] == '*':
        cnt += 1
        for j in range(len(data[i+1:])):
            if data[j] == '*':
                cnt += 1
            else:
                ans.append(cnt)
                cnt = 0
                break

print(max(ans))