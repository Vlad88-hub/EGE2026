from re import *

with open(r'.\files\24_19967.txt') as file:
    data = file.readline()

pattern = r'AFD([1-9][0-9]*|0)([+\*]([1-9][0-9]*|0))+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))