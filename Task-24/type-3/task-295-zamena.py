with open(r'../files/24-295.txt') as file:
    data = file.readline()

dat = '**DE***DE***DDD*****DE***DEDEEDEDEDE'
data = data.replace('DE', 'D E')
data = data.split()

ans = 0
print(data)
for i in range(len(data) - 240):
    # print(''.join(data[i:i + 241]))
    ans = max(ans, len(''.join(data[i:i + 241])))

print(ans)