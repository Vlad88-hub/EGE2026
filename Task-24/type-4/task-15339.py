with open(r'../files/24_15339.txt') as file:
    data = file.readline()

# aaa11121a1a1a1a1aa1a1a1a1a1a1a
ans = 0
cnt = 1
for i in range(len(data)):
    if data[i] in '6789' and data[i+1] in 'ABC' or data[i] in 'ABC' and data[i+1] in '6789':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

ans = max(ans, cnt)
print(ans)