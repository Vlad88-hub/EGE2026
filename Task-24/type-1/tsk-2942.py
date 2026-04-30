with open(r'../files/24_2942.txt') as file:
    data = file.readline()

cnt = 0
ans = []
for i in range(len(data)-1):
    if data[i:i+2] == 'AB' or data[i:i+2] == 'AC':
        cnt += 1
        for j in range(len(data[i+1:])):
            if data[j:j+2] == 'AB' or data[j:j+2] == 'AC':
                cnt += 1
            else:
                ans.append(cnt)
                cnt = 0
                break

print(max(ans))

