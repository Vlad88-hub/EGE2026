from re import *

with open(r'../files/24_4602.txt') as file:
    data = file.readline()

vow = 'AO'
ne_vow = 'BCD'
pattern = fr'([{ne_vow}][{vow}])+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len))//2)