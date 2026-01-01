with open(r'.\files\24_5139.txt') as file:
    data = file.readline()

ans = 0
vowel ='AEU'
con = 'BCDF'
for i in range(len(data) - 2):
    if data[i] in con and data[i + 1] in vowel and data[i + 2] in con:
        cnt = 1
        for j in range(i + 3, len(data) - 2, 3):
            if data[j] in con and data[j + 1] in vowel and data[j + 2] in con:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)