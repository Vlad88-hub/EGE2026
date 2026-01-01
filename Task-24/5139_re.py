from re import finditer
from string import *
with open(r'.\files\24_5139.txt') as file:
    data = file.readline()

vow = 'AEU'
con = 'BCDF'
pattern = fr'([{con}][{vow}][{con}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 3)