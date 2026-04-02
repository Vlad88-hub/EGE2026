from re import *

from probnik_vesna.task_1 import matrix

with open(r'.\files\24 (1).txt') as file:
    data = file.readline()

data = data.split('Z')

ans = 100000000000
for i in range(len(data) - 269):
    ans = min(ans, len('Z'.join(data[i:i+271])))

print(ans)

#########################################################

# pattern = r'(Z[^Z]*){270}'
# matches = [match.group() for match in finditer(pattern, data)]
#
# print(len(min(matches, key=len)))