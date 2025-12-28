from re import *
with open(r'.\files\24_1874.txt') as file:
    data = file.readline()

pattern = r'(?<=QW).+?(?=QW)'
matcher = [match.group() for match in finditer(pattern, data)]

print(len(max(matcher, key=len)))