with open(r'.\files\24_25361.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)):
    if data[i] in '02468':
        cnt = 0
        cnt_F = 0
        for j in range(i + 1, len(data)):
            cnt += 1
            if data[j] == 'F':
                cnt_F += 1
                if cnt_F == 77:
                    ans = max(ans, cnt)
                    break
            if data[j] in '02468':
                if cnt_F == 76:
                    ans = max(ans, cnt + 1)
                break

print(ans)
