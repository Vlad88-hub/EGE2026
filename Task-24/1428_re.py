from re import *

with open(r'.\files\24_1428.txt') as file:
    data = file.readline()


ans = 0
pattern = r'(^|(?<=(XY|XZ))).+?($|(?=(XY|XZ)))'
for match in finditer(pattern, data):
    cnt = match.groups().count('XY') + match.groups().count('XZ')
    ans = max(ans, len(match.group()) + 2 if cnt == 2 else 1)

print(ans)

