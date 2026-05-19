from re import *

with open(r'../files/24_18239.txt') as file:
    data = file.readline()

dat = '123121-21112-11---23-12'
num = r'([1-9][0-9]*|0)'
pattern = fr'-?({num}-)+{num}'
matches = [match.group() for match in finditer(pattern, data)]
print(matches, len(matches))
ans = 0
for match in matches:
    len_match = len(match)
    if eval(match) > -20000:
        ans = max(ans, len(match))
    elif len_match > ans:
        for l in range(len_match):
            if match[l] == '-': continue
            for r in range(len_match - 1, l, -1):
                if match[r] =='-': continue
                new_match = match[l:r+1]
                if eval(new_match) > -20000:
                    ans = max(ans, len(new_match))

print(ans)

