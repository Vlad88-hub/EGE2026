from re import *

with open(r'.\files\24_4710.txt') as file:
    data = file.readline()

vow ='EYUIOA'
pattern = fr'([^{vow}][{vow}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)