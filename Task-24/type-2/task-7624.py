with open(r'../files/24_7624.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in range(len(data)-1):
    if data[i:i+2] not in ['XY', 'YX', 'XZ', 'ZX', 'XX', 'YZ', 'ZY', 'ZZ', 'YY']:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

print(ans + 1)