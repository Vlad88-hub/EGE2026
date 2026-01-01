from re import *

with open(r'.\files\24_1273.txt') as file:
    data = file.readline()
pattern = r'(^|(?<=(XYZ))).+?($|(?=(XYZ)))'
ans = 0
for match in finditer(pattern, data):
    res = match.group()
    if match.groups().count('XYZ') == 2:
        ans = max(ans, len(res) + 4)
    elif match.groups().count('XYZ') == 1:
        ans = max(ans, len(res) + 2)


print(ans)