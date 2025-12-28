from string import *

with open(r'.\files\24_4602.txt') as file:
    data = file.readline()


vowels = 'EYUIOA'
combinations = []
for i in ascii_uppercase:
    for j in vowels:
        if i not in vowels:
            combinations.append(i + j)

print(combinations)

ans = 0
for i in range(len(data) - 1):
    if data[i] + data[i + 1] in combinations:
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] + data[j + 1] in combinations:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)