with open(r'.\files\24_21421.txt') as file:
    data = file.readline()

alph = '0123456789AB'
alph_chet = '02468A'
ans = 0
for i in range(len(data)):
    if data[i] in alph and data[i] != '0':
        cnt = 1
        for j in range(i + 1, len(data)):
            if data[j] in alph:
                cnt += 1
                if data[j] in alph_chet:
                    ans = max(ans, cnt)
            else:
                break
print(ans)