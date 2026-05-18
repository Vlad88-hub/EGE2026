from re import *

with open(r'../files/24_17641.txt') as file:
    data = file.readline()

dat = '123+345*32+1+0*34++832+8'

pattern = r'(([1-9][0-9]*|0)[\*\+])+([1-9][0-9]*|0)'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for match in matches:
    if eval(match) == 0:
        ans = max(ans, len(match))
    else:
        match = match.split('+')
        new_match = ''
        for m in match:
            if eval(m) == 0:
                new_match += m + '+'
            else:
                new_match = ''
            ans = max(ans, len(new_match) - 1)

print(ans)