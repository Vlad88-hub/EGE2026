from re import *

with open(r'.\files\24_1273.txt') as file:
    data = file.readline()
pattern = r'(?<=XYZ).+?(?=XYZ)'
matcher = [match.group() for match in finditer(pattern, data)]
print(len(max(matcher, key=len)) + 4)