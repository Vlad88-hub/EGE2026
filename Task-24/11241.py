from re import *

with open(r'.\files\24_11241.txt') as file:
    data = file.readline()

pattern = r'[^ABCD]+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))