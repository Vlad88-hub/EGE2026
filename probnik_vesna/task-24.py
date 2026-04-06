from re import *

with open(r'.\files\24 (1).txt') as file:
    data = file.readline()

data = data.split('Z')

ans = 100000000000
for i in range(len(data) - 268):
    ans = min(ans, len('Z'.join(data[i:i+269])) + 2)

print(ans)

#########################################################

# pattern = r'(Z[^Z]*){270}'
# matches = [match.group() for match in finditer(pattern, data)]
#
# print(len(min(matches, key=len)))