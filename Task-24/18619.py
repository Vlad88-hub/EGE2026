from re import *

with open(r'.\files\24_18619.txt') as file:
    data = file.readline()

pattern = r'[B][1-9]+([-\*][1-9]+)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))