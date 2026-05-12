with open(r'../files/24_15339.txt') as file:
    data = file.readline()

ans = cnt = 0
for i in range(0, len(data), 2):
    if data[i] in '6789' and data[i+1] in 'ABC':
        cnt += 2
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print(ans)