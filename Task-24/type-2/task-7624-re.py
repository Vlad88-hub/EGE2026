from re import *

with open(r'../files/24_7624.txt') as file:
    data = file.readline()

pattern = r'[XYZ]*([XYZ][^XYZ]+)+[XYZ]?'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))